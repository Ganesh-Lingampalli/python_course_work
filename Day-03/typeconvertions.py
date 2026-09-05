Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
i=12
float(i)
12.0
complex(i)
(12+0j)
list(i)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(i)
TypeError: 'int' object is not iterable
tuple(i)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuple(i)
TypeError: 'int' object is not iterable
set(i)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    set(i)
TypeError: 'int' object is not iterable
bool(i)
True
str(i)
'12'
dict(i)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(i)
TypeError: 'int' object is not iterable
f=12.5
int(i)
12
complex(f)
(12.5+0j)
str(f)
'12.5'
list(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
bool(f)
True
c=10+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
bool(c)
True
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
l=[1,2,3,4]
int(l)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l))
SyntaxError: unmatched ')'
float(l)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex()l
SyntaxError: invalid syntax
complex(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[1, 2, 3, 4]'
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
bool(l)
True
dict(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
s='ganesh'
int(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'ganesh'
float()s
SyntaxError: invalid syntax
float(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'ganesh'
list(s)
['g', 'a', 'n', 'e', 's', 'h']
tuple(s)
('g', 'a', 'n', 'e', 's', 'h')
set(s)
{'e', 'h', 'n', 's', 'g', 'a'}
bool
<class 'bool'>

bool(s)
True
dict(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
t=(1,2,3,xx)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t=(1,2,3,xx)
NameError: name 'xx' is not defined
t=(1,2,3,'xx')
int(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
"(1, 2, 3, 'xx')"
list(t)
[1, 2, 3, 'xx']
set(t)
{1, 2, 3, 'xx'}
bool(t)
True
dict(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
s={11,2,3,'KHSD'}
int(s)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
list(s)
[11, 2, 3, 'KHSD']
tuple(s)
(11, 2, 3, 'KHSD')
set(s)
{11, 2, 3, 'KHSD'}
bool(s)
True
dict(s)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
b='true'
int(b)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: 'true'
b= True
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
str(b)
'True'
list(b)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
>>> d=(1:2,2:3,3:4)
SyntaxError: invalid syntax
>>> d=('ganesh','vikas','khdh,)
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d=('ganesh','vikas','khdh')
...    
>>> int(d)
...    
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(d)
...    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> str(d)
...    
"('ganesh', 'vikas', 'khdh')"
>>> list(d)
...    
['ganesh', 'vikas', 'khdh']
>>> tuple(d)
...    
('ganesh', 'vikas', 'khdh')
>>> set(d)
...    
{'khdh', 'ganesh', 'vikas'}
>>> bool(d)
...    
True
