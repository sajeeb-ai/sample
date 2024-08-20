class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
    def __init__(self,number,number1):
        super().__init__(number)
        self.number1=number1
    def __str__(self):
        if self.number1<0:
            return f'{self.number} - {abs(self.number1)}i'
        else:
            return f'{self.number} + {self.number1}i'
    def __add__(self,other):
        return ComplexNumber(super().__add__(other.number),(self.number1+other.number1))
    def __sub__(self,other):
        return ComplexNumber(super().__sub__(other.number),(self.number1-other.number1))

r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)