#global variable
'''
def display(n):
    n=n+10
    print('Inside: ',n)
n= 10
display(n)
print('Outside: ',n)

def display():
    print('Inside: ',n)
n=10
display()
print('Outside: ',n)
'''
#Error inside var doesn't access outside var
'''
def display():
    n=10
    print('Inside: ',n)
display()
print('Outside: ',n)
'''

#Global var inside
'''
def display():
    global n
    n=n+10
    print('Inside: ',n)
n=10
display()
print('Outside: ',n)

def display():
    global n
    n='PFS'
    print('Updated course: ',n)
n='JFS'
display()
print('Final course: ',n)         #output= upated and final: PFS

#global and local declarations
def display():
    n='PFS'
    print('Updated course: ',n)
n='JFS'
display()
print('Final course: ',n)      #output= updated: PFS Final: JFS
'''
#Nonlocal function
'''
def display():
    n= 'JFS'
    def update():
        nonlocal n
        n='PFS'
        print("Updated Course: ",n)
    update()
    print("Final Course: ",n)         #nonlocal affect only inside function

display()
 '''   

l = [1,2,3,4,5]
max=20
sum=10
print(sum)   #built-in functions acts as a variable
