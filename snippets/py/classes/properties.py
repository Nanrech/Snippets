class Person:
    def __init__(self, age):
        self.age = age
    
    @property
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

Samuel = Person(16)
print(Samuel.is_adult)
