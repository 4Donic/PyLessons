"""
3. Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких
слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""
s = "11 11 22 22 11 22 33 22 33 44 33 44 33"  # больше всего 22 и 33 - их по 4 штуки каждого
string = s.split()
dct = {}
maxx = 0
idx = str
for word in string:
    dct[word] = dct.get(word, 0) + 1
# print(dct)
# print(len(dct))
# print(dct.items())
for key, value in dct.items():
    if value >= maxx:
        maxx = value
        idx = key
print("Самое часто встречаемое слово и его кол-во в тексте соответственно : ", idx, maxx)
print()
