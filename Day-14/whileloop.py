'''
i = 1 
while i<=10:
    print(i)
    i+= 1

i = 10
while 1>0:
    print(i)
    i -= 1
    

i = 2
while i<=100:
    print(i,end=' ')
    i += 2'''
'''
s = 'Python Programming'
i = len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
    '''
'''
s = 'Python Programming'
i = 0
while i<len(s):
    print(s[i],end='')
    i+=1
'''
'''
l = [1,0,0,0,2,3,4,5,56,12,0,12,0,13,0,0,0,16,0]
while 0 in l:
    l.remove(0)
print(l)
'''

'''
d = {}
total = 0
while True:
    prod_name = input("Name of product: ")
    if prod_name=='exit':
        break
    prod_p = int(input("Price of product: "))
    d[prod_name]= prod_p
    total += prod_p

print(d)
print(f"Total bill: {total}")
'''
i = 0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("End of loop")
