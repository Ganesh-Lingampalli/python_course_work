num =int(input())
rev=0
for _ in range(num):
    if num >0:
        rev =rev*10 + num%10 
        num = num//10

print(rev)


