Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=20
a+b
30
a-b
-10
a*b
200
a/b
0.5
9/2
4.5
a//b
0
9%2
1
2**3
8
4**2
16
a>b
False
a<b
True
a<=b
True
a>=b
False
a==b
False
a!=b
True
'''assignment operators'''
'assignment operators'
c=40
c +=10
c
50
c-=10
c *=2
c
80
c **=2
c
6400
c%=3
c
1
c/=2
c
0.5
''' relational operators '''
' relational operators '
True and True
True
n=10
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%8==0 or n%3==0
False
n
10
n<10
False
not n<5
True
''' membership operations'''
' membership operations'
#str list tuple set dict
s='codegnan'
'e' in s
True
'z' in s
False
'f' not in s
True
'o' not in s
False
l=[1,2,3,4]
4 in l
True
6 in l
False
8 not in l
True
t=(1,2,3,4)
3 in t
True
8 in t
False
3 not in t
False
4 in t
True
s={1,2,3,4,5,6,7}
4 not in s
False
3 in s
True
7 in s
True
'name' in d
True
'ganesh' in d
False
8 in d
False
'mist' in d
False
'number' not in d
False
'number' in d
True
'college' in d
True
'college' not in d
False
'mist' not in d
True
8 not in d
True
8 in d
False
'name' in d
True
'name' not in d
False
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
2540805060672
id(m)
2540805361664
''' identity operators'''
' identity operators'
l is m
False
n=l
l in n
False
id(n)
2540805060672
>>> l in n
False
>>> l is n
True
>>> ''' is  is a identity operator'''
' is  is a identity operator'
>>> l is not n
False
>>> l is not m
True
>>> s='codegnan'
>>> id(s)
2540805539504
>>> s='codegnan course'
>>> id(s)
2540805604528
>>> a=10
>>> id(a)
140733916464328
>>> a+=10
>>> a
20
>>> id(a)
140733916464648
>>> s={1,2,3,4}
>>> id(s)
2540805310272
>>> s.add(6)
>>> s
{1, 2, 3, 4, 6}
>>> id(s)
2540805310272
>>> d={'name': 'ganesh', 'number':8, 'college': 'mist'}
>>> id(d)
2540805511872
