"""
4. Написать функцию `season`, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому
этот месяц принадлежит (зима, весна, лето или осень).
"""


def season(month):
    if 1 <= month <= 12:
        if month == 12 or 1 <= month <= 2:
            print("Zima")
            return "Zima"
        elif 3 <= month <= 5:
            print("Vesna")
            return "Vesna"
        elif 6 <= month <= 9:
            print("Leto")
            return "Leto"
        else:
            print("Osen")
            return "Osen"
    else:
        print("Вы ввели несуществующий номер месяца\n")


month = int(input("Введине номер месяца"))

season(month)
