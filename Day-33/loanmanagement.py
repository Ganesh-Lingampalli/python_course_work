from abc import ABC,abstractmethod

class Customer:
    def __init__(self,customer_id,name,age,email,phone,income,credit_score):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.income = income
        self.credit_score = credit_score

    def check_eligibility(self):
        if self.age < 21 or self.credit_score < 650 or self.income < 25000:
            return False
        return True

    def display_customer(self):
        print("\nCustomer details")
        print("-------------------")
        print("Customer ID: ",self.customer_id)
        print("Name: ",self.name)
        print("Phone: ",self.phone)
        print("Age: ",self.age)
        print("Income: ",self.income)
        print("Credit Score: ",self.credit_score)

ganesh = Customer(1,"ganesh","ganesh@gmail.com",9440327952,22,75000,740)
print("Eligibility: ",ganesh.check_eligibility)
ganesh.display_customer()

class Loan(ABC):

    def __init__(self,loan_id,customer,loan_amount,interest_rate,tenture):
        self.loan_id = loan_id
        self.customer = customer
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenture = tenture
        self.__balance = loan_amount
        self.__total_paid = 0
        self.repayment_history = []
        self.status = "Applied"

    @abstractmethod
    def calculate_emi(self):
        pass

    def check_loan_eligibility(self):

        if not self.customer.check_eligibility():
            self.status = "Rejected"
            return False
        return True

    def sanction_loan(self):
        if self.status == "Rejected":
            print("Loan application rejected")
            return
        if not self.check_loan_eligibility():
            print("Customer is not eligible for the loan")
            return

        self.status = "Sanctioned"
        print("\nLoan sactioned successfully")

    def repay(self,amount):
        if self.status != "Sactioned":
            print("Repayment is not allowed")
            print("Loan status",self.status)
            return
        if amount <= 0:
            print("Invalid repament amount")
            return
        if amount > self.__balance:
            print("Repayment amount is greater than outstanding balance")
            return

        self.__balance -= amount
        self.__total_paid += amount

        self.repayment_history.append(amount)

        print("\nRepayment successful")
        print("Amount paid           :",amount)
        print("Outstanding Balance   :",self.__balance)

        if self.__balance == 0:
            self.status = "Closed"
            print("Loan closed successfully")

    def get_balance(self):
        return self.__balance

    def get_loan_amount(self):
        return self.__loan_amount

    def get_total_paid(self):
        return self.__total_paid

    def display_statement(self):

        print("\n")
        print("="*40)
        print("LOAN STATEMNT")
        print("="*40)

        print("Loan ID                  :",self.loan.id)
        print("Customer Name            :",self.customer.name)
        print("Loan Amount              :",self.__loan_amount)
        print("Intrest Rate             :",self.interest_rate)
        print("Tenture                  :",self.tenture)
        print("Total Paid               :",self.__total_paid)
        print("Outstanding Balance      :",self.__balance)
        print("Loan Status              :",self.status)

        print("\nRepayment History")

        if not self.repayment_history:
            print("="*40)

        else: 
            for i in range(len(self.repayment_history)):
                print(f"Payment {i+1}         : {self.repaument_history[i]}")

        print("="*40)

    def __str__(self):

        return (
            f"Loan ID: {self.loan_id},"
            f"Customer: {self.customer.name},"
            f"Loan Amount: {self.__loan_amount},"
            f"Ountstanding: {self.__balance},"
            f"Status: {self.status}"
        )

ganesh = Customer(1,"ganesh","ganesh@gmail.com",9440327952,22,75000,740)
ganesh.display_customer()
print("Eligibility: ",ganesh.check_eligibility)



