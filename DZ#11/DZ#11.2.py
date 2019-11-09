"""
3. Заполните список случайными числами и выполните реверс для части списка между элементами с индексами `a` и `b` (включая эти элементы)
"""
from random import randint
lst = [randint(0, 25) for _ in range(15)]  # наполнение списка
a = randint(0, 7)
b = randint(8, 15)
print(lst)
print("a,b = ", a, ",", b, sep="")
print(lst[a:b])

# lst[a:b] = lst[a:b][::-1]
lst[a:b] = reversed(lst[a:b])
print(lst)
