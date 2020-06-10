class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

result = []
while True:
    value = input('Введите numeric элемент для добавления в список или stop для выхода: ')
    if value == 'stop':
        print(f'список элементов: {result}')
        break
    try:
        if not value.isnumeric():
            raise NotNumber('NaN')
        result.append(int(value))
    except NotNumber as error:
        print('Вводите только числа')