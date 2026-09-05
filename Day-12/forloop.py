Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#str list tuple set dict range()
'''
for var in sequence:
    print(var)
    '''

... '''
... s = 'codegnan'
... for ch in s:
...     print(ch)
...     '''
... '''
... s = 'codegnan'
... for ch in s:
...     if ch in 'aeiouAEIOU':
...         print(ch)
...         '''
... 
... '''
... l = [10,23,30,45,1,3,15,16,18,19,21]
... for i in l:
...     if i%2==0:
...         print(i,"Even")
...     else:
...         print(i,"Odd")
...         '''
... 
... '''marks = (90,20,35,46,78,92,87,48)
... for mark in marks:
...     if mark > 35:
...         print(mark,"Pass")
...     else:
...         print(mark,"Fail")
...         
... 
... followers = {'Ganesh','Avinash','Lokesh','Bharath','Srinivas'}
... for i in followers:
...     print(i) '''
... 
... bus = {'s1': 'Booked', 's2':'Available','s3':'Available','s4':'Booked','s5':'Available'}
... for seat in bus:
...     if bus.get(seat)== 'Available':
...         print(seat,bus.get(seat))
... 
