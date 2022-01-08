class Human:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def method(self):
        print('aquí')
    def morir(self):
        print('ded')

class Compañero(Human):
    def sayHi(self):
        print('Buenas tardes, me llamo ' + self.name + ' y me gusta el número ' + self.number)
    
    def method(self):
        print('13')
        super().method()
    
class Enemigo(Human):
    def sayHi(self):
        print('no lmao')

    def method(self):
        print('31')
        super().morir()
    
Carlos = Compañero('Carlos', '5')
Roberto = Enemigo('Rober', '3')

Carlos.method()
Carlos.sayHi()
Roberto.sayHi()
