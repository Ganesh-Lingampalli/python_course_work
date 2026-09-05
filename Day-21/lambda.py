'''
greater = lambda a,b: a if a>b else b
print(greater(12,13))
print(greater(50,70))
print(greater(40,20))
print(greater(16,26))

wish = lambda name: f'welcome to course {name}'
print(wish('Ganesh'))
print(wish('Lokesh'))
print(wish('Avinash'))
print(wish('Bharath'))

iseven = lambda n: 'Even' if n%2==0 else 'Odd'
print(iseven(45))
print(iseven(18))
print(iseven(17))

avg = lambda a,b,c: (a+b+c)/3
print(avg(4,5,6))
print(avg(30,26,15))
'''
'''
domain = lambda mail: (mail.split('@')[-1]).split('.')[0]
print(domain('ganesh@codegnan.com'))
print(domain('ganesh@gmail.com'))
print(domain('ganesh@yahoo.com'))
print(domain('ganesh@bahuu.com'))

gst = lambda price: price + price*0.18
print(gst(1000))
print(gst(5000))
print(gst(8000))

prices = [5678,8765,5467,124,123,1600,3000]
res = list(map(lambda price: price + price*0.18 , prices))
print(res)
'''
'''
names = ['ganesh','lokesh','avinash','bharath','srinivas']
res = list(map(lambda name: name.title(),names))
print(res)

prices = [100,200,600,500,700]
res = list(map(lambda price: price - price*0.3,prices ))
print(res)

prices = [1000,200,600,500,700]                          #it prints res >500 only
res = list(filter(lambda price: price>500,prices ))      #if we use map then it give True or False
print(res)

prices = [1000,200,600,500,700]                          
res = list(filter(lambda price: price%2==0,prices ))      
print(res)

prices = [1000,200,600,500,700]                          
res = list(filter(lambda price: price%2!=0,prices ))      
print(res)

names = ['ganesh','lokesh','avinash','bharath','srinivas']
res = list(filter(lambda name: len(name)>6,names))
print(res)
'''
from functools import reduce
l = [3,4,56,7,9,20,45]
res = reduce(lambda sum,i: sum+i,l)
print(res)
