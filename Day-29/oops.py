class Flipkart:
    products ={'shirts':1000,'handbag':2000,'pants':3000}
    discount = 30

    @classmethod 
    def display(cls):
        print(cls.products)


    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello{self.name}, Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% is going to provide discount")

ganesh = Flipkart()
ganesh.userinfo('ganesh',9876543210,'Hyd')
ganesh.displaydiscount()
ganesh.display()

avinash = Flipkart()
avinash.userinfo('avinash',9876543211,'Guntur')
avinash.displaydiscount()
avinash.display()

lokesh = Flipkart()
lokesh.userinfo('lokesh',9876543212,'Kadapa')
lokesh.displaydiscount()
lokesh.display()

bharath = Flipkart()
bharath.userinfo('bharath',9876543210,'Tirupati')
bharath.displaydiscount()
bharath.display()
