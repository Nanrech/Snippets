class Clase:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

    @classmethod
    def sayHi(cls):
        print('Hi')

square = Clase.new_square(5)
print(square.calculate_area())
square.sayHi()
