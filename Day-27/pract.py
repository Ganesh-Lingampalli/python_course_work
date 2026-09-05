# n = int(input())
# reverse =0
# for _ in range(n):
#     if n>0:
#         reverse = reverse * 10 + n%10
#         n = n//10
# print(reverse)

# n = int(input())
# reverse =0
# original = n
# for _ in range(n):
#     if n>0:
#         reverse = reverse * 10 + n%10
#         n = n//10
# if original==reverse:
#     print("palindrome")
# else:
#     print("Not a Palindrome")
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             print("not a prime num")
#     else:
#         print("prime num")
# else:
#     print("not a prime num")
n = int(input())
a = 0
b = 1
for i in range(n):
    a,b = b,a+b
    print(a,end=' ')