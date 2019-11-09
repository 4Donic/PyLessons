"""
4. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000, и возвращающую `True`, если оно простое, и
`False` - иначе.
"""


def is_prime(numb):
    if numb == 1:
        return False
    else:
        for x in range(2, numb):
            if numb % x == 0:
                return False
        return True


# from random import randint
# numb = randint(0, 1000)
# print(numb)
numb = int(input("Число от 0 до 1000: "))
print(is_prime(numb))
