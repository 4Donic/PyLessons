"""
2. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество
"""
from random import randint
lst = [randint(0, 100) for _ in range(15)]  # наполнение списка
print(lst)
nech = 0
for i in range(len(lst)-1):
    if lst[i] % 2 != 0:
        lst[i] = 0
        nech += 1
print(lst)
print(nech)
