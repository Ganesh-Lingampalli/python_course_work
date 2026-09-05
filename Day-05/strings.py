Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string operations
c = ' python programing '
len(c)
19
ord('p')
112
ord('a')
97
ord('n')
110
ord('0')
48
ord('A')
65
chr(65)
'A'
chr(66)
'B'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', ' ', ' ', 'a', 'g', 'g', 'h', 'i', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c = 'String is immutable'
c
'String is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
c = OQDUUFDSIdjjcUOC
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c = OQDUUFDSIdjjcUOC
NameError: name 'OQDUUFDSIdjjcUOC' is not defined
c = 'OQDUUFDSIdjjcUOC'
c.casefold()
'oqduufdsidjjcuoc'
c = 'String is immutable'
c.center(60,'*')
'********************String is immutable*********************'
c.center(60,'_')
'____________________String is immutable_____________________'
c.center(60,'3')
'33333333333333333333String is immutable333333333333333333333'
c,ljust(60,'!')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c,ljust(60,'!')
NameError: name 'ljust' is not defined. Did you mean: 'list'?
c.ljust(60,'!')
'String is immutable!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
c.rjust(60,'?')
'?????????????????????????????????????????String is immutable'
'12'.zfill(4)
'0012'
'12'.zfill(10)
'0000000012'
''' search & find methods '''
' search & find methods '
c.find('i')
3
c.find('S')
0
c.find('z')
-1
c.rfind('i')
10
c.rfind('s')
8
c.index('i')
3
c.rindex('i')
10
c.index('z')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c.count('i')
3
c.count('m')
2
c.count('g')
1
''' replace & modify methods'''
' replace & modify methods'
c = 'String is immutable'
c.replace('i','0')
'Str0ng 0s 0mmutable'
c.replace('String','Float')
'Float is immutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
'''splitting & joining methods'''
'splitting & joining methods'
c.split()
['String', 'is', 'immutable']
'String,is,immutable'.split()
['String,is,immutable']
'String,is,immutable'.split(',')
['String', 'is', 'immutable']
'String,is,immutable'.rsplit(',')
['String', 'is', 'immutable']
'String,is immutable'.rsplit(',')
['String', 'is immutable']
'String,is immutable'.split(',')
['String', 'is immutable']
'String is immutable'.rsplit('',1)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    'String is immutable'.rsplit('',1)
ValueError: empty separator
'String is immutable'.rsplit(' ',1)
['String is', 'immutable']
s='''
python
... programming
... language'''
>>> s
'\npython\nprogramming\nlanguage'
>>> s.splitlines()
['', 'python', 'programming', 'language']
>>> ''.join(['', 'python', 'programming', 'language'])
'pythonprogramminglanguage'
>>> ' '.join(['', 'python', 'programming', 'language'])
' python programming language'
>>> '-'.join(['', 'python', 'programming', 'language'])
'-python-programming-language'
>>> ','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> ','.join(['1','2','3'])
'1,2,3'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s = 'java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
>>> ''' whitespace & trimming '''
' whitespace & trimming '
>>> c='       hello    world       '
>>> c.strip()
'hello    world'
>>> c.lstrip()
'hello    world       '
>>> c.rstrip()
'       hello    world'
>>> text = "Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
