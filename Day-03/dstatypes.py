Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
count=10
count=7
count
7
type(count)
<class 'int'>
price=99.99
price
99.99
type(price)
<class 'float'>
c=3+8j
c
(3+8j)
c=4=8J
SyntaxError: cannot assign to literal
c
(3+8j)
c=4+9J
c
(4+9j)
type(c)
<class 'complex'>
s= 'codegnan'
s
'codegnan'
type(s)
<class 'str'>
d=['ganesh',12,3,'dkja']
d
['ganesh', 12, 3, 'dkja']
>>> type(d)
<class 'list'>
>>> t=()
>>> t=('ganesh',1,2,3,4,345,'eged')
>>> t
('ganesh', 1, 2, 3, 4, 345, 'eged')
>>> type(t)
<class 'tuple'>
>>> s={'ganesh','eyyfyyey',1,2,3,4,55,5.66}
>>> s
{'ganesh', 2, 1, 3, 5.66, 4, 'eyyfyyey', 55}
>>> type(s)
<class 'set'>
>>> s={}
>>> s
{}
>>> type(s)
<class 'dict'>
>>> status=none
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    status=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> status = None
>>> type(status)
<class 'NoneType'>
>>> s={1,2,3,4,}
>>> s.add(5)
>>> s
{1, 2, 3, 4, 5}
>>> s.remove(4)
>>> s
{1, 2, 3, 5}
>>> s= frozen({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s= frozen({1,2,3,4})
NameError: name 'frozen' is not defined. Did you mean: 'frozenset'?
>>> s= frozenset({1,2,34,5})
>>> s
frozenset({1, 2, 34, 5})
