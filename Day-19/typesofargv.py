#Positional arguements
'''
def display(name,email,password):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")

display('Ganesh','ganesh@gmail.com','Gane@345')
display('Gane@345','ganesh@gmail.com','Ganesh')
display('ganesh@gmail.com','Gane@345','Ganesh')
'''
#Keyword arguements
'''
def display(name,email,password):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")

display( name='Ganesh',email='ganesh@gmail.com',password='Gane@345')
display( password= 'Gane@345',email='ganesh@gmail.com',name='Ganesh')
display( email= 'ganesh@gmail.com',password= 'Gane@345',name='Ganesh')
'''
#Default arguements
'''
def display(name,email='email@gmail.com',password=''):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")

display('Ganesh','ganesh@gmail.com','Gane@345')

def display(name,email='email@gmail.com',password=''):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")

display('Ganesh')
'''

#Variable length arguements(Positional)
'''
def display(*names):
    print(names)
display('Ganesh')
display('Ganesh','Lokesh')
display('Ganesh','Lokesh','Avinash')
display('Ganesh','Lokesh','Avinash','Bharath')
'''
#Variable length arguements(Keyword)
def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)
