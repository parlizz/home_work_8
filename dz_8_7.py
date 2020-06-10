class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + bi'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна:')
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно:')
        return f'{((self.a * other.a) - (self.b * other.b))} + {((self.a * other.b) + (self.b * other.a))}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z_1 = ComplexNumber(2, 1)
z_2 = ComplexNumber(3, 5)

print(z_1 + z_2)
print(z_1 * z_2)