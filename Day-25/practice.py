# '''
# data = {
#         123456: {'pin': 1234,'balance': 5000,'history':[] },
#         234561: {'pin': 1234,'balance': 5000,'history':[] },
#         345612: {'pin': 1234,'balance': 5000,'history':[] },
#         456123: {'pin': 1234,'balance': 5000,'history':[] }
# }

# def menu():
#     print('[C]heck balance')
#     print('[D]eposit Amount')
#     print('[W]ithdraw Amount')
#     print('[V]iew transactions')
#     print('[E]xit')

# def login():
#     global acc_num
#     acc_num = int(input('Enter Account Number: '))
#     pin = int(input('Enter Pin: '))
#     if acc_num in data[acc_num]['pin']==pin:
#         print('Login Successful...')
#         return True
#     else:
#         print('Invalid Login')
#         return False 

# def checkbalance():
#     print('Balance Amount: ',data[acc_num]['balance'])

# def depositamount():
#     amount = int(input('Enter deposit amount: '))
#     data[acc_num]['balance']+=amount
#     print(f'{amount} is successfully deposited++++')
#     data[acc_num]['history'].append(f'{amount} is deposited++++++')


# def withdrawamount():
#     amount = int(input('Enter withdrawal amount: '))
#     if data[acc_num]['balance'] >= amount:
#         data[acc_num]['balance'] -= amount
#         print(f'{amount} is successfully withdraw-----')
#         data[acc_num]['history'].append(f'{amount} is withdrawed----')
#     else:
#         print('Insufficient Amount')

# def viewtransactionhistory():
#     if data[acc_num]['history']:
#         for i in data[acc_num]['history']:
#             print(i)
     
# '''

# '''
# import platform

# print(platform.system())
# print(platform.release())
# print(platform.processor())
# '''
# '''
# import math

# print(math.pi)
# print(math.e)
# print(math.sqrt(400))
# print(math.pow(3,4))
# print(math.ceil(20.999))
# print(math.ceil(20.01))
# print(math.floor(21.99))
# print(math.floor(21.01))
# print(math.fabs(24.99))
# print(math.fabs(24.01))
# print(math.factorial(6))
# print(math.gcd(131,120))
# print(math.gcd(120,240))
# print(math.gcd(12,48))
# print(math.log(8,2))
# print(math.log(24,3))
# print(math.sin(30))
# print(math.sin(60))
# print(math.sin(90))
# print(math.sin(0))
# print(math.cos(0))
# print(math.cos(30))
# print(math.cos(60))
# print(math.cos(90))
# print(math.tan(0))
# print(math.tan(30))
# print(math.tan(60))
# print(math.tan(90))
# print(math.degrees(30))
# print(math.radians(30))
# '''
# '''
# import random

# print(random.random())
# print(random.randint(1,20))
# print(random.randint(10000,99999))
# print(random.uniform(1,10))
# print(random.uniform(1000,9999))
# print(random.choice([1,2,3,4]))
# print(random.choices(['Ganesh','Srinivas','Lokesh','Avinash'],k=3))
# print(random.shuffle(['ganesh','Srinivas','Lokesh','Avinash']))
# '''
# from collections import Counter,defaultdict,deque

# l = 'python programming'

# print(Counter(l))

# d = defaultdict()
# for i in l:
#     d[i]=1
# print(d)


# m = deque([])
# m.append(10)
# m.appendleft(20)
# m.append(30)
# m.append(40)
# m.pop()
# m.popleft()
# print(m)

# from itertools import combinations,permutations

import platform

print(platform.system())