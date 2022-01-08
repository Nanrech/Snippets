class Class_with_info:
    def __init__(self, adjective, stored_int):
        self.adjective = adjective
        self.s_int = stored_int

    def bark(self):
        print('meow lmao')
    
    def sayHi(self):
        print('Hi, I have ' + str(self.s_int) + ' legs and my adjective is: ' + str(self.adjective))

Subject = Class_with_info("fresh", 4)
Friend = Class_with_info("cool", 7)
Foe = Class_with_info(".png", 4)

print(Foe.adjective)
print(Subject.s_int)
print(Foe.adjective + ' ' + str(Foe.legs))
Subject.sayHi()
Foe.bark()
