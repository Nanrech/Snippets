class Human:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x
  
Carla = Human()

Carla.set_age(21)
print(Carla.get_age())
print(Carla._age)
