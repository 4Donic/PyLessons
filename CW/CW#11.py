# # 1
# Stepen'
# def iter_pow(num, exp):
#     res = 1
#     while exp > 0:
#         res *= num
#         exp -= 1
#     return res
#
#
# def recurse_pow(num, exp):
#     if exp == 0:
#         return 1
#
#     return recurse_pow(num, exp - 1) * num
#
#
# print(recurse_pow(2, 5))
# # 1
# # 2
# Faktorial
# def iter_fact(num):
#     res = 1
#     while num > 0:
#         res *= num
#         num -= 1
#     return res
#
#
# def recurs_fact(num):
#     if num < 3:
#         return num
#     return recurs_fact(num-1) * num
#
#
# print(recurs_fact(5))
# # 3
# 0 1 2 3 4 5 6  7  8  9
# 0 1 1 2 3 5 8 13 21 34
# Fibonacci
# def iter_fib(num):
#     x0 = 0
#     x1 = 1
#     while num > 1:
#         res = x0 + x1
#         x0 = x1
#         x1 = res
#         num -= 1
#     return res
#
#
# print(iter_fib(9))
#
#
# def recurs_fib(num):
#     return num if 0 <= num <= 1 else recurs_fib(num-1) + recurs_fib(num-2)
#
#
# print(recurs_fib(10))
# Fibonacci
# # 3
# # 4
