'''def display(n):
    if n>10:
        return
    print(n)               #1 -10 num
    display(n+1)
display(1)
'''
'''
def display(n):
    if n>10:
        return
    display(n+1)          #10-1 num
    print(n)

display(1)
'''
'''
def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(8))                     

def displayprod(n):
    if n==1:
        return 1
    return n*displayprod(n-1)
print(displayprod(5))
'''
'''
def display(ind):
    if ind==len(s):
        return
    print(s[ind],end=' ')
    display(ind+1)
s = "Python Programming"
display(0)

def display(ind):
    if ind==len(s):
        return
    display(ind+1)
    print(s[ind],end=' ')
s = "Python Programming"
display(0)
'''
'''
def display(n):
    if n > len(s):
        return
    print(s[:n])
    display(n+1)
    
s = "Python"
display(1)
'''
'''
def display(ind,w):
    if ind > len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)
s = "Python Programming"
display(0,5)
'''
'''
def display(n):
    if n <= 0:
        return
    display(n//10)
    print(n%10)
display(987654)

def display(n):
    if n <= 0:
        return 0
    return n%10 + display(n//10)
n = 987654
print(display(n))
'''
