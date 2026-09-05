'''
res = [i for i in range(1,11)]         #printing 1 to 10 num
print(res)

n=12
res= [i for i in range(1,n+1) if n%i==0]         #set cmprehension is just coverting [] ==> {}
print(res)                                       #factors of 12

r= [12,23,45,687,34,123,34,12,43,90]
res =[i if i%2==0 else 0 for i in r]         #printing even num and 0 in place of odd num
print(res)

r= [[12,23,45],[687,34,123],[34,12,43,90]]
res= [j for i in r for j in i if j%2==0]    #printing even num in nested list
print(res)

res = {i for i in range(1,11)}         #printing 1 to 10 num
print(res)

n=12
res= {i for i in range(1,n+1) if n%i==0}         
print(res)                                       #factors of 12

r= {12,23,45,687,34,123,34,12,43,90}
res ={i if i%2==0 else 0 for i in r}         #printing even num and 0 in place of odd num
print(res)
'''
# l = [updating for loop]
# l = [updaating for loop if cond]
# l = [upd1 if cond else upd2 for loop]
# l = [upd for loop1 for loop2]
# l = [upd for loop1 for loop2 if cond]
'''
l = [int(input(f"Enter the num - {i+1}: ")) for i in range(10)]
print(l)

m = [input(f"Enter the neme - {i+1}: ") for i in range(5)]
print(m)
'''
'''
names = {input(f"Enter the name-{i+1}: "): int(input(f"Enter the marks: ")) for i in range(5)}
print(names)
'''
res = {i : i*i for i in range(1,11)}
print(res)
