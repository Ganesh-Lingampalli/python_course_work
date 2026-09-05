Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = [1,23,4,5,6,7,]
l
[1, 23, 4, 5, 6, 7]
id(l)
1607926571200
l.append(12)
l
[1, 23, 4, 5, 6, 7, 12]
l.append(14)
l
[1, 23, 4, 5, 6, 7, 12, 14]
id(l)
1607926571200
l.insert(1,13)
l
[1, 13, 23, 4, 5, 6, 7, 12, 14]
''' extend used to adding multiple elements'''
' extend used to adding multiple elements'
l.extend(15,16,17)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.extend(15,16,17)
TypeError: list.extend() takes exactly one argument (3 given)
l.extend([15,16,17])
l
[1, 13, 23, 4, 5, 6, 7, 12, 14, 15, 16, 17]
l[3]
4
l
[1, 13, 23, 4, 5, 6, 7, 12, 14, 15, 16, 17]
l[3] = 18
l
[1, 13, 23, 18, 5, 6, 7, 12, 14, 15, 16, 17]
id(l)
1607926571200
l.pop()
17
l
[1, 13, 23, 18, 5, 6, 7, 12, 14, 15, 16]
l.pop()
16
l
[1, 13, 23, 18, 5, 6, 7, 12, 14, 15]
l.pop(1)
13
l
[1, 23, 18, 5, 6, 7, 12, 14, 15]
l.remove(6)
l
[1, 23, 18, 5, 7, 12, 14, 15]
del l[2]
l
[1, 23, 5, 7, 12, 14, 15]
id(l)
1607926571200
l.inset(3,16)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.inset(3,16)
AttributeError: 'list' object has no attribute 'inset'. Did you mean: 'insert'?
l.insert(3,16)
l
[1, 23, 5, 16, 7, 12, 14, 15]
l.clear()
l
[]
id(l)
1607926571200
l = [1, 23, 5, 16, 7, 12, 14, 15]
max(l)
23
min(l)
1
sorted(l)
[1, 5, 7, 12, 14, 15, 16, 23]
l.reverse()
l
[15, 14, 12, 7, 16, 5, 23, 1]
l.sort()
l
[1, 5, 7, 12, 14, 15, 16, 23]
l = [1,2,3]
m = [1,2,3]
n = l
n
[1, 2, 3]
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m = l.copy()
m
[1, 2, 3, 4]
m.append(5)
m
[1, 2, 3, 4, 5]
l
[1, 2, 3, 4]
l = [1, 5, 7, 12, 14, 15, 16, 23]
l.sort()
l
[1, 5, 7, 12, 14, 15, 16, 23]
l.sort(reverse=True)
l
[23, 16, 15, 14, 12, 7, 5, 1]
sum(l)
93
l==m
False
l!=m
True
all([0,'',[],(),set(),{},False])
False
all([0,'',[],(),set(),{},False])
False
all([1,'',[],(),set(),{},False])
False
KeyboardInterrupt
... any([1,'',[],(),set(),{},False])
... True
... >>> l
... [23, 16, 15, 14, 12, 7, 5, 1]
... >>> l.inder(14)
... Traceback (most recent call last):
...   File "<pyshell#69>", line 1, in <module>
...     l.inder(14)
... AttributeError: 'list' object has no attribute 'inder'. Did you mean: 'index'?
... >>> i.index(14)
... Traceback (most recent call last):
...   File "<pyshell#70>", line 1, in <module>
...     i.index(14)
... NameError: name 'i' is not defined. Did you mean: 'id'?
... >>> l.index(14)
... 3
... >>> l.index(7)
... 5
... >>> l.count(14)
... 1
... >>> l = [[1,2,3,4],[5,6,7,8]]
... >>> l
... [[1, 2, 3, 4], [5, 6, 7, 8]]
... >>> l(0)
... Traceback (most recent call last):
...   File "<pyshell#76>", line 1, in <module>
...     l(0)
... TypeError: 'list' object is not callable
... >>> l[0]
... [1, 2, 3, 4]
... >>> l[1]
... [5, 6, 7, 8]
... >>> l[0][2]
... 3
... >>> l[1][0]
... 5
... >>> l[-1][-1]
... 8
... >>> t=()
