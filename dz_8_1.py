class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'все верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('09 - 06 - 2020')
print(today)
print(Date.valid(9, 6, 2025))
print(today.valid(11, 13, 2011))
print(Date.valid(32, 11, 2000))
print(Date.valid(1, 11, 2000))
print(Date.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
