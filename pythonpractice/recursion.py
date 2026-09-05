'''
def fact(n):
    for _ in range(n):
        if n==0 or n==1:
            return 1
        return n*fact(n-1)
n= int(input())
print(fact(n))
'''

'''
def sum(n):
    for _ in range(1,n+1):
        if n==1:
            return 1
        return n+sum(n-1)
n = int(input())
print(sum(n))
'''

def nut(n):
    if n==0:
        return
    nut(n-1) 
    print(n)
n = int(input())
print(nut(n))