"""
1. Дана строка.
    a. выведите третий символ этой строки.
    b. выведите предпоследний символ этой строки.
    c. выведите первые пять символов этой строки.
    d. выведите всю строку, кроме последних двух символов.
    e. выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная 
    с первого).
    f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
    g. выведите все символы в обратном порядке.
    h. выведите все символы строки через один в обратном порядке, начиная с последнего.
    i. выведите длину данной строки.
"""

s = input("Введите строку: ")
# s = "1234567890"
#    0123456789

print("a", s[2])
print("b", s[-2])
print("c", s[:5])
print("d", s[:-2])
print("e", s[::2])
print("f", s[1::2])
print("g", s[::-1])
print("h", s[-1::-2])
print("i", len(s))
