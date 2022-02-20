class SpecialString:
    def __init__(self,cont):
        self.cont = cont
    def __truediv__(self,other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("Spam, this will go above the other string")
hello = SpecialString("If you insert anything here it'll just print an equal (to its length) ammount of equal signs above it")
print(spam/hello)
