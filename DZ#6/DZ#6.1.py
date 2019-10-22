"""
5. Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите 
количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""

lst = [4, 7, 2, 0, 7, 4, 5, 8, 2, 3, 7]
big = 0
idx = 0
for number in lst[1:-1]:
    idx += 1
    if lst[idx-1]+lst[idx+1] < number:
        big += 1
print("\n", big, sep="")
