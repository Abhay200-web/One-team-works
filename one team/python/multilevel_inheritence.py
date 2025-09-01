class GrandFather:
    def work(self):  #---->this is a method in parrent class
        print("Grantfather")

class Father(GrandFather):
    def teaching(self): # ----> this is a method in Father class
        print("Father")

class son(Father):
    def play(self):
        print("son")

s=son()
s.work()
s.teaching()
s.play()