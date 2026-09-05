'''
credit_score = int(input("Credit Score: "))
income = int(input("Monthly Income: "))
liabilities = int(input("Existing Liabilities: "))
loan_status = ''
if credit_score>=750 and income>=50000 and liabilities<=20000:
    loan_status = 'Approved'
elif 650<=credit_score<=749 and income>=50000 and liabilities<=20000: 
    loan_status = 'Approved with conditions'
else:
    loan_status = 'Rejected'

print(loan_status)
'''



