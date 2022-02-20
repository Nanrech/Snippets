class Clase_:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Clase_(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Clase_(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Clase_(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Clase_(self.x / other.x, self.y / other.y)
    
    def __floordiv__(self, other):
        return Clase_(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Clase_(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Clase_(self.x ** other.x, self.y ** other.y)

    def __and__(self, other):
        return Clase_(self.x & other.x, self.y & other.y)

    def __xor__(self, other):
        return Clase_(self.x ^ other.x, self.y ^ other.y)

    def __or__(self, other):
        return Clase_(self.x | other.x, self.y | other.y)

    def __lt__(self, other):
        return Clase_(self.x < other.x, self.y < other.y)

    def __le__(self, other):
        return Clase_(self.x <= other.x, self.y <= other.y)

    def __eq__(self, other):
        return Clase_(self.x == other.x, self.y == other.y)
    
    def __ne__(self, other):
        return Clase_(self.x != other.x, self.y != other.y)

    def __gt__(self, other):
        return Clase_(self.x > other.x, self.y > other.y)
    
    def __ge__(self, other):
        return Clase_(self.x >= other.x, self.y >= other.y)

first_sumas = Clase_(5, 7)
second_sumas = Clase_(3, 9)

egg = Clase_(5,2)
egg2 = Clase_(6,1)

result = first_sumas % second_sumas # Replace % with any of the symbols above
print(result.x, result.y)
# Author's note: "haha, lmao"
