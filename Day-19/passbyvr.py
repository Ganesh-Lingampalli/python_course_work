#int float str list tuple set dict bool
#int float str tuple bool will affect inside and outside
#list set dict didn't affest 
def display(n):
    n+=10
    print("Inside",n)

n=10
display(n)
print("Outside: ",n) 

def display(n):
    n += 10.9
    print("Inside",n)
n=10.5
display(n)
print("Outside: ",n)

def display(n):
    n=(1,2,3)
    print("Inside",n)
n=(1,2,3,4)
display(n)
print("Outside: ",n)

def display(n):
    n.append(12)
    print("Inside",n)
n=[1,2,3,4]
display(n)
print("Outside: ",n)

def display(n):
    n.add(5)
    print("Inside",n)
n={1,2,3,4}
display(n)
print("Outside: ",n)

def display(n):
    n[5]=6
    print("Inside",n)
n={1:2,3:4}
display(n)
print("Outside: ",n)

def display(n):
    n=False
    print("Inside",n)
n=True
display(n)
print("Outside: ",n)

def display(n):
    n=(1,2,3)
    print("Inside",n)
n=(1,2,3,4)
display(n)
print("Outside: ",n
