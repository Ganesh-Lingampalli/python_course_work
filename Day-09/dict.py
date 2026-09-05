Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {'name':'ganesh','batch':63,;'course':'PFS'}
SyntaxError: invalid syntax
data = {'name':'ganesh','batch':63,'course':'PFS'}
data['name']
'ganesh'
data['batch']
63
data['course']
'PFS'
data['batch']=64
data
{'name': 'ganesh', 'batch': 64, 'course': 'PFS'}
64 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
da
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    da
NameError: name 'da' is not defined
data.get('course','key is not present')
'PFS'
data['slills']=['python','mysql','flask']
data
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask']}
data['age']= 22
data
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22}
data.update('phone':9440327952,'mail':'ganesh@gmail.com')
SyntaxError: invalid syntax
data.update('phone':9440327952,'mail':'ganesh@gmail.com')
SyntaxError: invalid syntax
data.update('phone' : 9440327952,'mail':'ganesh@gmail.com')
SyntaxError: invalid syntax
data.update({'phno':9440327952,'mail':'ganesh@gmail.com'})
data
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22, 'phno': 9440327952, 'mail': 'ganesh@gmail.com'}
data.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
data.pop('mail')
'ganesh@gmail.com'
data
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22, 'phno': 9440327952}
data.pop(age')
         
SyntaxError: unterminated string literal (detected at line 1)
data.pop('age')
         
22
data.popitem()
         
('phno', 9440327952)
data.popitem()
         
('slills', ['python', 'mysql', 'flask'])
data
         
{'name': 'ganesh', 'batch': 64, 'course': 'PFS'}
del data['course']
         
data
         
{'name': 'ganesh', 'batch': 64}
data.clear()
         
data
         
{}
data = {'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22, 'phno': 9440327952, 'mail': 'ganesh@gmail.com'}
         
data.keys()
         
dict_keys(['name', 'batch', 'course', 'slills', 'age', 'phno', 'mail'])
data.value()
         
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    data.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
data.values()
         
dict_values(['ganesh', 64, 'PFS', ['python', 'mysql', 'flask'], 22, 9440327952, 'ganesh@gmail.com'])
data.items()
         
dict_items([('name', 'ganesh'), ('batch', 64), ('course', 'PFS'), ('slills', ['python', 'mysql', 'flask']), ('age', 22), ('phno', 9440327952), ('mail', 'ganesh@gmail.com')])
sorted(data)
         
['age', 'batch', 'course', 'mail', 'name', 'phno', 'slills']
max(data)
         
'slills'
min(data)
         
'age'
data
         
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22, 'phno': 9440327952, 'mail': 'ganesh@gmail.com'}
data.get('age')
         
22
data['age']
         
22
data,setdefault('age',0)
         
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data,setdefault('age',0)
NameError: name 'setdefault' is not defined
data.setdefault('age',0)
         
22
>>> data
...          
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22, 'phno': 9440327952, 'mail': 'ganesh@gmail.com'}
>>> data.setdefault('age',0)
...          
22
>>> data
...          
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'age': 22, 'phno': 9440327952, 'mail': 'ganesh@gmail.com'}
>>> data.get('age')
...          
22
>>> data.setdefault('age',0)
...          
22
>>> len(data)
...          
7
>>> all(data)
...          
True
>>> any(data)
...          
True
>>> data.pop('age')
...          
22
>>> data.setdefault('age',0)
...          
0
>>> data
...          
{'name': 'ganesh', 'batch': 64, 'course': 'PFS', 'slills': ['python', 'mysql', 'flask'], 'phno': 9440327952, 'mail': 'ganesh@gmail.com', 'age': 0}
>>> d =dict.fromkeys(["a","b"],0)
         
d
         
{'a': 0, 'b': 0}
