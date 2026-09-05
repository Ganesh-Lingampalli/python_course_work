'''n = int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=n//2) or (i+j==n-1 and i<=n//2):
            print('*',end= ' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n = int(input())
for i in range(n):
    for j in range(n):
        if (i==j and i<=n//2) or (i+j==n-1 and i<=n//2) or (j==0 and i<=n//2) or (j==n-1 and i<=n//2) or (i-j==n//2 and j<=n//2) or i+j==n+(n//2)-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

n = int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or i+j==n-1:
            print('*',end= ' ')
        else:
            print(' ',end=' ')
    print()
