Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c= 'string.py'
c.startswitch('str')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c.startswitch('str')
AttributeError: 'str' object has no attribute 'startswitch'. Did you mean: 'startswith'?
c.startswith('str')
True
c.startswith('python')
False
c.startswith('py')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'EUJCVH123'.isalpha()
False
'EUJCVH123'.isalnum()
True
'EUJCVH123'.isspace()
False
' '.isspace()
True
'EUJCVH123'.istitle()
False
'The Data Is Deleted'.istitle()
True
'var@123'.isidentifier()
False
'var_123'.isidentifier()
True
'var_123'.is identifier()
SyntaxError: invalid syntax
'var_123'.isidentifier()
True
>>> 'var_123' is identifier()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'var_123' is identifier()
NameError: name 'identifier' is not defined
>>> 'var_123' is identifier
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'var_123' is identifier
NameError: name 'identifier' is not defined
>>> '     '.isspace()
True
>>> ' ganesh    '.isspace()
False
>>> l =[]
>>> l =list()
>>> l = [1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},None,True]
>>> l
[1, 12.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, None, True]
>>> type(l)
<class 'list'>
>>> l =[1,2,3,4]
>>> m=[5,6,7,8]
>>> l+m
[1, 2, 3, 4, 5, 6, 7, 8]
>>> m*3
[5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[::3]
[1, 4]
>>> l[::1]
[1, 2, 3, 4]
>>> l[::-1]
[4, 3, 2, 1]
>>> l[::]
[1, 2, 3, 4]
>>> l[1::2]
[2, 4]
