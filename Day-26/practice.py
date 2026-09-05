from datetime import date,time,datetime,timedelta

'''
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

t = time(21,22,23)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
'''
# n = datetime.now()
# print(n)
# print(n.hour)
# print(n.minute)
# print(n.second)
# print(n.day)
# print(n.month)
# print(n.year)
# print(n.weekday())
# print(n.strftime('%d-%m-%Y'))
# print(n.strftime('%d-%m-%Y %H:%M:%S'))
# print(n.strftime('%a %d %m %Y %H:%M:%S'))
# print(n.strftime('%a %d %b %Y %H:%M:%S %p'))
# print(n.strftime('%A %d %B %Y %H:%M:%S %p'))

# s = date.today()
# u = datetime.now()

# s2 = s + timedelta(days=30)
# u2 = u + timedelta(minutes=80)
# print(s,s2)
# print(u,u2)

# file = open('pfs63.txt','r')
# print(file.read())
# file.seek(0)
# print(file.readline())
# file.seek(0)
# print(file.readlines())
 
with open('pfs63.txt','r') as file:
    print(file.read())

with open('pfs63.txt','w') as file:
    print(file.write('this is ganesh..'))

with open('pfs63.txt','a') as file:
    print(file.write('I am from BCM'))

with open('pfs63.txt','a+') as file:
    print(file.write('I want to become a software engineer'))

