from abc import ABC,abstractmethod

class phonepe:
    def senderinfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("Enter the amount")
    def pin(self):
        print("you need to enter the amount")

    @abstractmethod
    def transaction(self):
        pass

class HDFC(phonepe):
    def transaction(self):
        print("payment using hdfc bank")

class SBI(phonepe):
    def transaction(self):
        print("payment using sbi bank")

class ICIC(phonepe):
    def transaction(self):
        print("payment using icic bank")

class UNION(phonepe):
    def transaction(self):
        print("payment using union bank")

ganesh = HDFC()
ganesh.senderinfo()
ganesh.amount()
ganesh.pin()
ganesh.transaction()

