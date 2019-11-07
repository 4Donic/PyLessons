"""
9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
- список
- метод revers() (или срез [::-1], или вместо revers() использовать insert() тогда не придётся разворачивать список),
чтоб развернуть список, метод join()
- строка ascii_uppercase из модуля string (её можно получить если сделать импорт from string import ascii_uppercase),
 она содержит все буквы латинского алфавита.
"""


def systema(ch, syst):
    from string import ascii_uppercase
    res = []
    while ch != 0:
        res.append(ch % syst)
        ch = ch // syst
    res.reverse()
    leng = 0
    for numb in res:
        if numb > 9:
            res[leng] = ascii_uppercase[numb - 10]
        leng += 1
    res = ''.join(map(str, res))  # Переделка каждого значения в списке в стринг и их соединение
    return res

# # # # # введенное число в введенную систему, или введенное число во все сразу.


print(systema(int(input("Десятичное число: ")), int(input("Желаемая система исчисления"))))

# x = int(input("Десятичное число: "))
# for i in range(2, 37):
#     print("{sys}-ная система".format(sys=i), systema(x, i))
