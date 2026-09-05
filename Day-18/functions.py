'''def display(name,email,password):
    print(f'Hello {name}')
    print(f'Your email: {email}')
    print(f'Your password: {password}')

display('Ganesh','ganeshlingampalli@gmail.com','Ganesh304')
display('Lokesh','lokeshnandyala@gmail.com','Lokesh@123')
display('Avinash','avinashpaleti@gmail.com','Avinash@123')


def isleapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')
for year in range(2001,2026):
    isleapyear(year)


def sumofdigits(n):
    sum = 0
    while n>0:
        sum += n%10
        n=n//10
    return sum
n = int(input("Enter the number: "))
print(f'sum of {n} digits is {sumofdigits(n)}')

def productofdigits(n):
    product = 1
    while n>0:
        product *= n%10
        n=n//10
    return product
n = int(input("Enter the number: "))
print(f'Product of {n} digits is {productofdigits(n)}')

def checkpassword(password):
    if len(password)>8:
        check = set()
        for char in password:
            if char.isupper():
                check.add('u')
            elif char.islower():
                check.add('l')
            elif char.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check)==4:
            return "Strong Password"
    return "Weak Password"
password = input("Enter password: ")
print(f'password is {checkpassword(password)}')
'''
def table(n):
    print(f'---------Table - {n}-----------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,21):
    table(i)
