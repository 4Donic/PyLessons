"""
2. Написать функцию `is_year_leap`, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False
иначе.
"""


def is_year_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(True)
        return True
    else:
        print(False)
        return False


year = int(input("Введите год, чтобы узнать, является ли он високосным: "))
is_year_leap(year)
