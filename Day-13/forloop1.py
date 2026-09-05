Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> '''
... s = 'python programming'
... for i in range(len(s)):
...     if s[i] in 'aeiouAEIOU':
...         print(i,s[i])
...         '''
... 
... '''
... l = [23,45,12,34,50,24,35,68,75,34,10]
... sum = 0
... for i in range(len(l)):
...     if l[i]%2==0:
...         sum += i
...         print(i,l[i])
... print(sum)
... '''
... 
... '''
... n = int(input("Enter the number: "))
... fact = 1
... for i in range(1,n+1):
...     fact *= i
... print(f"Factorial of {n} is {fact}")
... '''
... '''
... data = {}
... n = int(input("Enter the no of students: "))
... max_marks = 0
... for i in range(n):
...     name = input("Enter the name: ")
...     marks = int(input("Enter the marks: "))
...     if marks > max_marks:
...         max_marks = marks
...     data[name]=marks
... 
... print(data)
... print("Maximum marks: ",max_marks)
'''

data = {}
n = int(input("no of the products: "))
total = 0
for i in range(n):
    prod_name = input("Enter the name of product: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    price *= quantity
    total += price
    data[prod_name]= price
print(data)
