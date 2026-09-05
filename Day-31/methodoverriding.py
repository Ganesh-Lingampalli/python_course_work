class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to Hotstar, {self.name}")
    def login(self):
        print("you can login to Hotstar")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def playcontrollers(self):
        print("pause.resume.play")
    def history(self):
        print("you can see recent videos")
    def ads(self):
        print("Ads will run")
    def access(self):
        print("you have limited access")
    def quality(self):
        print("you don't have high quality")
    def downloads(self):
        print("you can't download high quality videos")

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f"Welcome to Premium Hotstar, {self.name}")
    
    def ads(self):
            print("Ads will not run")
    def access(self):
        print("you unlimited limited access")
    def quality(self):
        print("you can have high quality")
    def downloads(self):
        print("you can download high quality videos")

Avinash = Hotstar('Avinash')
Avinash.login()
Avinash.dashboard()
Avinash.search()
Avinash.playcontrollers()
Avinash.ads()
Avinash.access()
Avinash.quality()
Avinash.downloads()

Ganesh = PremiumHotstar('Ganesh')
Ganesh.login()
Ganesh.dashboard()
Ganesh.search()
Ganesh.playcontrollers()
Ganesh.ads()
Ganesh.access()
Ganesh.quality()
Ganesh.downloads()

