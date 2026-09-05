'''Single Inheritance'''
# class whatsappv1:
#     def messaging(self):
#         print("you can massage")

# class whatsappv2(whatsappv1):
#     def calls(self):
#         print("you can do audio and video calls")

# a = whatsappv1()
# a.messaging()

# b = whatsappv2()
# b.messaging()
# b.calls()

'''Multi level Inheritance'''

# class whatsappv1:
#     def messaging(self):
#         print("you can massage")

# class whatsappv2(whatsappv1):
#     def calls(self):
#         print("you can do audio and video calls")

# class whatsappv3(whatsappv2):
#     def status(self):
#         print("you can add the status for 24 hours")

# a = whatsappv1()
# a.messaging()

# b = whatsappv2()
# b.messaging()
# b.calls()

# c = whatsappv3()
# c.messaging()
# c.calls()
# c.status()

'''Multiple Inheritance'''

# class whatsappv1:
#     def messaging(self):
#         print("you can massage")

# class whatsappv2:
#     def calls(self):
#         print("you can do audio and video calls")

# class whatsappv3(whatsappv1,whatsappv2):
#     def status(self):
#         print("you can add the status for 24 hours")

# a = whatsappv1()
# a.messaging()

# b = whatsappv2()
# b.calls()

# c = whatsappv3()
# c.messaging()
# c.calls()
# c.status()

'''hierachical Inheritance'''

# class whatsappv1:
#     def messaging(self):
#         print("you can massage")

# class whatsappv2(whatsappv1):
#     def calls(self):
#         print("you can do audio and video calls")

# class whatsappv3(whatsappv1):
#     def status(self):
#         print("you can add the status for 24 hours")

# a = whatsappv1()
# a.messaging()

# b = whatsappv2()
# b.messaging()
# b.calls()

# c = whatsappv3()
# c.messaging()
# c.status()

'''Hybrid Inheritance'''

# class whatsappv1:
#     def messaging(self):
#         print("you can massage")

# class whatsappv2:
#     def extramessage(self):
#         print("you can add emojis,stikers and gifs")

# class whatsappv3(whatsappv1,whatsappv2):
#     def calls(self):
#         print("you can do audio and video calls")

# class whatsappv4(whatsappv3):
#     def status(self):
#         print("you can add the status for 24 hours")

# a = whatsappv1()
# a.messaging()

# b = whatsappv2()
# b.extramessage()

# c = whatsappv3()
# c.messaging()
# c.extramessage()
# c.calls()

# d = whatsappv4()
# d.messaging()
# d.extramessage()
# d.calls()
# d.status()

''' same methods __status()__ super() is used '''

# class whatsappv1:
#     def status(self):
#         print("you can do audio and video calls")

# class whatsappv2(whatsappv1):
#     def status(self):
#         super().status()
#         print("you can add music and stickers")
# class whatsappv3(whatsappv2):
#     def status(self):
#         super().status()
#         print("you can like and you can add reaction")

# a = whatsappv1()
# a.status()

# b = whatsappv2()
# b.status()

# c = whatsappv3()
# c.status()

'''same method and multiple inheritance'''

class whatsappv1:
    def status(self):
        print("you can do audio and video calls")

class whatsappv2:
    def status(self):
        print("you can add music and stickers")
class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("you can like and you can add reaction")

c = whatsappv3()
c.status()