class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    devidend = int(input('делимое: '))
    division = int(input('делитель: '))
    if not division:
        raise DivByZero('нельзя делить на 0')
    print(f'Результат: {devidend / division}')

except ValueError:
    print('вводите только числа')
except DivByZero as error:
    print(error)
