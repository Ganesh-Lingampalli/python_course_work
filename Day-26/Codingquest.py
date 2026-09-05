'''[1]reverse a number'''
# n = int(input())
# reverse = 0
# for _ in range(n):
#     if n > 0:
#         reverse *= 10 
#         reverse += n%10
#         n = n//10
# print(reverse)

'''optimized code using while loop''' 
# n = int(input())
# reverse = 0
# while n>0:
#     reverse = reverse*10 + n%10
#     n=n//10
# print(reverse)
'''Using functions to get reverse'''
# def rev(n):
#     reverse = 0
#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10
#     return reverse
        
# print(rev(12345))
'''Optimized code Using functions to get reverse'''
# def rev(n):
#     reverse = 0
#     while n:
#         reverse = reverse * 10 + n % 10
#         n = n//10
#     return reverse
# print(rev(12345))

'''[2]palindrome num'''
# n = int (input())
# reverse =0
# org = n
# while n>0:
#     reverse = reverse*10 + n%10
#     n = n//10
# print(reverse)
# if org==reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")   
'''functins to get palindrome num'''
# def pal(n):
#     reversed =0
#     while n>0:
#         reversed = reversed*10 + n%10
#         n = n//10
#     return reversed
# num=int(input())
# print('Palindrome' if num==pal(num) else 'Not a Palindrome')

'''[3]Checking prime number'''
# n = int(input())
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             print("not a Prime Number")
#             break
#     else:
#         print("Prime Number ")
# else:
#     print("not a prime number")
'''[4]prime number in range'''
# start = int(input())
# end = int(input())
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num//+1):
#             if num%i==0:
#                 break
#         else:
#             print(num)
'''[5]find factorial of a num'''
n = int(input())
res = 1
for i in range(1,n+1):
    res *= i
print(res)

import math
print(math.factorial(n))
