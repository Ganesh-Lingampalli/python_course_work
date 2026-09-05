Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#declaring a set
s = set()
s = {1,2,3,4,324,12,9864,546}
s
{1, 2, 3, 4, 546, 324, 9864, 12}
s.add(1)
s.add(10)
s.add(12.3)
s.add(12+3j)
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,2))
s.add({1,2})
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.add({1,2})
TypeError: unhashable type: 'set'
s.add({1:2})
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add({1:2})
TypeError: unhashable type: 'dict'
s
{1, 2, 3, 4, 546, 324, (1, 2), 9864, 10, 12, 12.3, (12+3j)}
s.add(True)
s
{1, 2, 3, 4, 546, 324, (1, 2), 9864, 10, 12, 12.3, (12+3j)}
l = {1,2,3,4,5}
m = {3,5,8,9,10}
l+m
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
l*2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
l[0]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l[0]
TypeError: 'set' object is not subscriptable
l[1:2]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l[1:2]
TypeError: 'set' object is not subscriptable
2 in l
True
l.union(m)
{1, 2, 3, 4, 5, 8, 9, 10}
l | m
{1, 2, 3, 4, 5, 8, 9, 10}
# set operations
l.intersection(m)
{3, 5}
l & m
{3, 5}
l.difference(m)
{1, 2, 4}
l - m
{1, 2, 4}
l.symmetric(m)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l.symmetric(m)
AttributeError: 'set' object has no attribute 'symmetric'
l.issymmetric(m)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.issymmetric(m)
AttributeError: 'set' object has no attribute 'issymmetric'
l ^ m
{1, 2, 4, 8, 9, 10}
l.issubset(m)
False
l <= m
False
l = {1,2,3,4,5,6,7}
m = {5,6,7}
m.issubset(l)
True
m <= l
True
l.issuperset(m)
True
l >= m
True
m >= l
False
l.isdisjoint(m)
False
l = {1,2,3}
m = {4,5,6}
l.isdisjoint(m)
True
{1,2,3,4,5} <= l
False
{1,2,3,4,5} >= l
True
#set methods
a = {1,2,3,4,5}
b = {3,5,6,7,8}
len(a)
5
sum(a)
15
max(a)
5
min(a)
1
b=c
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b=c
NameError: name 'c' is not defined
c=b
c
{3, 5, 6, 7, 8}
c.add(9)
c
{3, 5, 6, 7, 8, 9}
b
{3, 5, 6, 7, 8, 9}
c = b.copy()
c
{3, 5, 6, 7, 8, 9}
c.add(10)
c
{3, 5, 6, 7, 8, 9, 10}
b
{3, 5, 6, 7, 8, 9}
a = {1,2,3,4,5,6,7}
a
{1, 2, 3, 4, 5, 6, 7}
a.add(8)
a
{1, 2, 3, 4, 5, 6, 7, 8}
a.update(1,2)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.update(1,2)
TypeError: 'int' object is not iterable
a.update({9,10})
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.pop()
1
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a.pop()
2
a
{3, 4, 5, 6, 7, 8, 9, 10}
a.pop()
3
a
{4, 5, 6, 7, 8, 9, 10}
a.pop(10)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.pop(10)
TypeError: set.pop() takes no arguments (1 given)
a.remove(10)
a
{4, 5, 6, 7, 8, 9}
a.remove(11)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.remove(11)
KeyError: 11
a.discard(11)
a
{4, 5, 6, 7, 8, 9}
a.discard(7)
a
{4, 5, 6, 8, 9}
a.update({'str',12.3,12+j})
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.update({'str',12.3,12+j})
NameError: name 'j' is not defined
a.update({'str',12.3,(12+j)})
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.update({'str',12.3,(12+j)})
NameError: name 'j' is not defined
a.update({'str',12.3,12})
a
{4, 5, 6, 8, 9, 12.3, 12, 'str'}
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
a = frozen({1,2,3,412,34,5,67,})
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a = frozen({1,2,3,412,34,5,67,})
NameError: name 'frozen' is not defined. Did you mean: 'frozenset'?
a = frozenset({1,2,3,412,34,5,67,})
a
frozenset({1, 2, 3, 34, 5, 67, 412})
a.add(10)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
d= {}
type
<class 'type'>



9
type(d)
<class 'dict'>
d = dict()
type(d)
<class 'dict'>
d = {' k1':'vi','k2':'v2','k3':'v3'}
d
{' k1': 'vi', 'k2': 'v2', 'k3': 'v3'}
id(d)
2336410982848
d['k4']= 'v4'
d
{' k1': 'vi', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d[1]= '1'
d[1.2]='1.2'
d[(3+j)]= '3+j'
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    d[(3+j)]= '3+j'
NameError: name 'j' is not defined
d={}
d[1]= 'int'
d[1.2]= 'flt'
d
{1: 'int', 1.2: 'flt'}
d[2+3j]= 'com'
d['str']='string'
d[(1,2,3,4)]= 'tuple'
d
{1: 'int', 1.2: 'flt', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d[[1,2,3]]= 'lst'
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    d[[1,2,3]]= 'lst'
TypeError: unhashable type: 'list'
d[{1,2,3}]= 'set'
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    d[{1,2,3}]= 'set'
TypeError: unhashable type: 'set'
d[{1:1}]= 'dict'
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    d[{1:1}]= 'dict'
TypeError: unhashable type: 'dict'
d={}
d[1]= 1
d[2]=1.2
d[3]=12+j
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    d[3]=12+j
NameError: name 'j' is not defined
d[3]=12+4j
d[4]='str'
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,2,3}
d[8]={1:1}
d
{1: 1, 2: 1.2, 3: (12+4j), 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}}
d[9]=True
d
{1: 1, 2: 1.2, 3: (12+4j), 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3]
>>> d[8]
{1: 1}
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,'key is not present')
'key is not present'
>>> d.get(6,'key is not present')
(1, 2, 3)
>>> d
{1: 1, 2: 1.2, 3: (12+4j), 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
>>> d
{1: 1, 2: 1.2, 3: 4, 4: 'str', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
>>> d
{1: 1, 2: 1.2, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 1.2, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]
{1, 2, 3}
>>> d
{1: 1, 2: 1.2, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 1.2, 3: 4, 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
