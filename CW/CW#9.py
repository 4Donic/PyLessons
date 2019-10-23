# # 1
# s = "12 21 24  24 3 5 84 6 8"
# lst = s.split()
# dct = {}
# for w in lst:
#     dct[w] = dct.get(w, 0) + 1
# print(dct)
#
# # 1
# # 2
#
#
# def summ(a, b):
#     return a + b
#
#
# y = summ
# print(y)
# print(y(4, 5))
#
#
# def do(x, a, b):
#     return x(a, b)
#
#
# print(do(summ, 5, 6))
# # 2
# # 3
# Лямбда
# s = lambda x, y: x + y
# print(s)
# print(type(s))
# print(s(3, 4))
# print((lambda x, y: x + y)(5, 6))
# # 3
# # 4
# map(func, *collection)
#
# temperatures = (33.5, 23, 56, -12)
#
#
# def far(temp):
#     res = float(9) / 5 * temp + 32
#     return round(res, 2)
#
#
# def cel(temp):
#     res = float(5) / 9 * (temp - 32)
#     return round(res, 2)
#
#
# print(temperatures)
# # print(list(map(cel, temperatures)))
# res = list(map(far,temperatures))
# print(list(map(cel,res)))
#
# res = list(map(lambda x: round(float(9) / 5 * x + 32, 2), temperatures))

# filter(func, *coll)
# from random import randint
# lst = [randint(10,100) for _ in range(15)]
# print(lst)
# res = list(filter(lambda x: x % 2, lst))
# print(res)
#
# res = list(filter(lambda x: not x % 2, lst))
# print(res)
# # 4
# # 5
# yield
def countdown1(num):
    res = []
    while num != 0:
        res.append(num-1)
        num -= 1

    return res


print(countdown1(6))


def countdown2(num):
    while num != 0:
        yield num - 1
        num -= 1


it = countdown2(5)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for i in countdown2(5):
    print(i)
