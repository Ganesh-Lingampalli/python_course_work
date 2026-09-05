n = input()
v = 0
c =0
for ch in n:
    if ch in 'aeiouAEIOU':
        v+=1
    elif ch!=" ":
        c+=1
print(f"vowels:     {v}")
print(f"consonents: {c}")

