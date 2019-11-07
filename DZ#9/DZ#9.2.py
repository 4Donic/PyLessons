"""
10. Написать функцию,циклически сдвигающую целое число на N разрядов
вправо или влево, в зависимости от третьего параметра функции.
Функция должна принимать три параметра: в первом параметре передаётся число для сдвига,
второй параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд),
3-й булевский параметр задаёт направление сдвига (по умолчанию влево (False)).
"""


def sdvig(number, n, vpravo):
    numlist = [int(x) for x in str(number)]
    while n > 0:
        if vpravo:
            for i in range(len(numlist)):
                k = 0
                if i == 0:
                    last = numlist[-1]
                numlist[len(numlist)-1-i] = numlist[len(numlist)-2-i]
                if i == len(numlist)-1:
                    numlist[k] = last
        else:
            for i in range(len(numlist)):
                k = len(numlist)-2
                if i == 0:
                    pre_last = numlist[-1]
                numlist[i - 1] = numlist[i]
                if i == len(numlist) - 1:
                    numlist[k] = pre_last
        n -= 1
    return int(''.join(map(str, numlist)))


print(sdvig(123456, 10, True))
