'''
class Registration:
    def __init__(self,store_name,email,number,password):
        self.store_name = store_name
        self.email = email
        self.number = number
        self.password = password

    def register(self):
        if self.store_name and self.email and self.number and self.password:
            return "Registration Successful"
        else:
            return "Registration Failed"

n = Registration()

n.register()
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
