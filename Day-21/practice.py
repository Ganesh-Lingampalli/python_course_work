units = int(input())
senior_citizen = eval(input())
if units<=100:
    bill = units* 1.5
elif 101<=units<=200:
    bill = units* 2.5
elif 201<=units<=500:
    bill = units* 4
elif units>500:
    bill = units*6
if senior_citizen:
    bill -= bill*0.10
if units>800:
    bill += bill*0.05
print(bill)
