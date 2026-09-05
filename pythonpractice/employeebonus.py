salary = int(input("Salary: "))
rating = int(input("Performance Rating: "))
experience = int(input("Experience: "))
attendance = int(input("Attendance: "))
fb = 0
if rating==5:
    fb += salary*0.25
elif rating==4:
    fb += salary*0.15
elif rating==3:
    fb += salary*0.10
else:
    fb += salary

if experience>10:
    fb += salary*0.10
elif 5<=experience<=10:
    fb += salary*0.05
else:
    fb += 0

if attendance >= 95:
    fb += 5000
elif 85<=attendance<=94:
    fb += 2000
elif attendance<85:
    fb += 0

print(fb)

