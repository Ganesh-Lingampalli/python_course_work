Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string operations
s = 'codegnan'
s
'codegnan'
>>> s = ''
>>> s
''
>>> s = 'codegnan'
>>> s
'codegnan'
>>> 'codegnan'+'PFS'
'codegnanPFS'
>>> 'codegnan'*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> '*'*20
'********************'
>>> '*_*'*20
'*_**_**_**_**_**_**_**_**_**_**_**_**_**_**_**_**_**_**_**_*'
>>> s = 'codegnan'
>>> s[4]
'g'
>>> s[-3]
'n'
>>> s = ' gnaehs fjjsnv ganesh '
>>> s[10]
'j'
>>> s[-11]
's'
>>> s[-3]
's'
>>> names = 'ganesh lokesh avinash'
>>> s[0:5]
' gnae'
>>> #s[start:end+1:step]=>s[0:len:1]
>>> s[0:6]
' gnaeh'
>>> s[-1:-8]
''
>>> s[-1:-8:-1]
' hsenag'
>>> names[0-6]
'v'
>>> names[0:6]
'ganesh'
>>> names[::2]
'gns oehaiah'
names[::-1]
'hsaniva hsekol hsenag'
'ganesh' in names
True
'lokesh' npt in names
SyntaxError: invalid syntax
'lokesh' not in names
False
