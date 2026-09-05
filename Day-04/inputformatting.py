Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float str list tuple set
x=input()
ganesh
x
'ganesh'
name=input()
ganesh3004
name
'ganesh3004'
name=input("enter your name: ")
enter your name: ganesh33
age=input("enter age: ")
enter age: 22
age
'22'
age=int(input("enter age: "))
enter age: 22
age
22
type(age)
<class 'int'>
names=input("enter names:")
enter names: ganesh loki bahrath
names
' ganesh loki bahrath'
names.split()
['ganesh', 'loki', 'bahrath']
names=input("enter names:").split()
enter names:ganesh loki bahrath
names
['ganesh', 'loki', 'bahrath']
names=input("enter names:").split()
1 2 3 4
SyntaxError: multiple statements found while compiling a single statement
names=input("enter names: ").split()
enter names: 1 2 3 4
names
['1', '2', '3', '4']
map(int,names)
<map object at 0x000001E4770AEA70>
list(map(int,names))
[1, 2, 3, 4]
values=list(map(int,input().split()))
1 2 33 444 4 555 
values
[1, 2, 33, 444, 4, 555]
values=list(map(float,input().split()))

1 22 33 4 455
SyntaxError: invalid syntax
values=list(map(float,input().split()))
1 22 33 444
SyntaxError: multiple statements found while compiling a single statement
values=list(map(float,input().split()))
values= list(map(float,input().split()))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    values=list(map(float,input().split()))
ValueError: could not convert string to float: 'values='
values=list(map(float,input().split()))
1.2 3.4
values
[1.2, 3.4]
values=tuple(map(int,input().split()))
1 2 3 4 5 
values
(1, 2, 3, 4, 5)
values=list(map(int,input().split()))
values=tuple(map(float,input().split()))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    values=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'values=tuple(map(float,input().split()))'
values=tuple(map(float,input().split()))
12.3 33.4 
values
(12.3, 33.4)
values=set(map(int,input().split()))
1 2 4 5
values
{1, 2, 4, 5}
''' multiple values'''
' multiple values'
a,b = [1,2]
a
1
b
2
a,b = (1,2)
a
1
b
2
email,password = input("enter the email and password: ")
enter the email and password: ganesh@gmail.com ganesh304
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    email,password = input("enter the email and password: ")
ValueError: too many values to unpack (expected 2)
email,password = input("enter the email and password: ")

enter the email and password: ganesh@gmail.com 1234
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    email,password = input("enter the email and password: ")
ValueError: too many values to unpack (expected 2)
email,password = input("enter the email and password: ").split()
enter the email and password: ganesh@gmail.com 1234
email
'ganesh@gmail.com'
password
'1234'
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
>>> c
3
>>> name,marks = input().split()
ganesh 77
>>> name
'ganesh'
>>> marks
'77'
>>> int(marks)
77
>>> e= eval(input())
1
>>> e
1
>>> e= eval(input())
"ganesh"
>>> e
'ganesh'
>>> e= eval(input())
[1,2,3,4]
>>> e
[1, 2, 3, 4]
>>> e= eval(input())
(1,2,3,4,5)
>>> e
(1, 2, 3, 4, 5)
>>> e= eval(input())
{1,2,3,4,5,6}
>>> e
{1, 2, 3, 4, 5, 6}
>>> e= eval(input())
... {1:1,2:2,3:3}
SyntaxError: multiple statements found while compiling a single statement
>>> e= eval(input())
{1:1,2:2,3:3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> e= eval(input())
2
>>> e
2
