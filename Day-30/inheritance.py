'''
class WhatsappV1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - v1 {self.name}")

    def messaging(self):
        print("You can send messages")

class WhatsappV2(WhatsappV1):
    def __init__(self,name):
            self.name = name
            print(f"Welcome to the whatsapp - v2 {self.name}")
    def calls(self):
         print("You can do Audio and Video calls")

ganesh = WhatsappV1("ganesh")
ganesh.messaging()

lokesh = WhatsappV2("lokesh")
lokesh.messaging()
lokesh.calls()
'''

class Whatsappv1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the Whatsapp - v1 {self.name}")

    def messaging(self):
         print("You can send messages")

class WhatsappV2(Whatsappv1):
    def __init__(self,name):
        self.name = name
        print(f"Welcome to Whatsapp - v2 {self.name}")

    def calls(self):
        print("you can have audio and video calls")
        
        

          