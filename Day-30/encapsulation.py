'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []
        print(f'Hello {self.username}, Welcome to Instagram')

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._posts
    
    def display(self):
        print(self.username,self.__password,self._posts)

ganesh = Instagram('ganesh','ganesh@123')
ganesh.display()
print(ganesh.username)
print(ganesh.getpassword())
print(ganesh.accesspost)
'''

'''
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    
    def display(self):
        print(self.username,self.__password,self._posts)

ganesh = Instagram('ganesh','ganesh@123')
ganesh.display()
print(ganesh.username)
print(ganesh.getpassword())
print(ganesh.accesspost)

ganesh.username = 'lokesh'
ganesh.setpassword("lokesh@123")
ganesh.accesspost = "sunrice.png"
ganesh.accesspost = "beach.png"
ganesh.accesspost = "forest.png"

print(ganesh.username)
print(ganesh.getpassword())
print(ganesh.accesspost)

'''
class Instagram: 
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)

ganesh = Instagram("ganesh","ganesh@123")
ganesh.display()
print(ganesh.username)
print(ganesh.getpassword())
ganesh.setpassword = "gane@12345"
print(ganesh.setpassword)
ganesh.accesspost = "gane"
print(ganesh.accesspost)

