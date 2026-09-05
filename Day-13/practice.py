'''
a = int(input())
if a >0:
    print(f'{a} is Positive.')
else:
    print(f'{a} is Negative.') 
    

a = int(input())
if a%2==0:
    print(f"{a} is even.")
else:
    print(f"{a} is odd.")
    

a = int(input())
if a%5==0:
    print(f"{a} is divisible by 5.")
else:
    print(f"{a} is not divisible by 5.")

a = int(input())
if a%3==0 and a%7==0:
    print(f"{a} is divisible by 3&7.")
else:
    print(f"{a} is not divisible by 3&7,")


a = int(input())
if a%4==0 and a%100!=0 and a%400==0:
    print(f"{a} is a leap year.")
else:
    print(f"{a} is not a leap year.")


std = input()
a = int(input())
pass_marks = int(input())
if a>pass_marks:
    print(f"{std} is pass.")
else:
    print(f"{std} is fail.")
    '''

n = int(input())
if len(n)==3:
    print(f"{n} is a 3-digit num")
else:
    print(f"{n} is not a 3-digit num")


n = input()
if n in 'aeiouAEIOU':
    print(f"{n} is vovel")
else:
    print(f"{n} is not vovel")

a = int(input())
b = int(input())
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")


a = int(input())
b = int(input())
if a<b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is greater than {b}")


n = int(input())
if n==0:
     print(f"{n} is Zero.")
else:
    print(f"{n} is not Zero.")


n = int(input())
if n%10==0:
    print(f"{n} is diisible by 10")
else:
     print(f"{n} is not divisible by 10")

age = int(input())
if age>18:
    print("eligible for vote")
else:
    print("not eligible for vote")


num = int(input())
if 1<=num<=100:
    print(f"{num} in range")
else:
    print(f"{num} not in range")


a = int(input())
b = int(input())
if a*a==b:
    print(f"{a} is square of {b}")
elif b*b==a:
    print(f"{b} is square of {a}")
else:
    print(f"not matching")
