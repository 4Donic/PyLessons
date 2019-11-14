"""
Представьте себе бухгалтерскую процедуру, используемую в книжном магазине. Он работает в списке с подсписками, которые выглядят так:
+--------------+------------------------------------+----------+----------------+
| Order Number |       Book Title and Author        | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz         |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz      |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry      |        3 |          32.95 |
|        88112 | Einführung in Python3, Bernd Klein |        3 |          24.99 |
+--------------+------------------------------------+----------+----------------+
(каждая строка таблицы, это подсписок:
[
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80]
]

и т.д.
)
Напишите программу на Python, которая возвращает список кортежей.
Каждый кортеж состоит из номера заказа и произведения цены на товары и количества.
Сумма заказа должена быть увеличен на 10€, если стоимость заказа меньше 100,00 €.
Напишите программу на Python, используя лямбду и карту.
"""
from random import randint
from random import uniform

line = '+--------------+------------------------------------+------------+----------------+\n'
# line = ('+{}+{}+{}+{}+\n'.format('-'*14, '-'*36, '-'*12, '-'*16))

lst = [[randint(1, 10000), 'Learning Python, Mark Lutz', randint(1, 10),         round(float(uniform(5, 40)), 2)],
       [randint(1, 10000), 'Programming Python, Mark Lutz', randint(1, 10),      round(float(uniform(5, 50)), 2)],
       [randint(1, 10000), 'Head First Python, Paul Barry', randint(1, 10),      round(float(uniform(5, 30)), 2)],
       [randint(1, 10000), 'Einführung in Python3, Bernd Klein', randint(1, 10), round(float(uniform(5, 25)), 2)]]

print(line, end='')
print('|{OrderNumber:^14}|{TitleAndAuthor:^36}|{Quantity:^12}|{Price:^16}|\n'.format(
    OrderNumber='Номер заказа', TitleAndAuthor="Автор и название книги", Quantity="Количество", Price="Цена"), end='')

print(line, end='')

for i in range(len(lst)):
    print('|{:>13} | {:<35}|{:>11} |{:>15} |'.format(lst[i][0], lst[i][1], lst[i][2], lst[i][3]))
print(line, end='')

res = []
summ = list(map(lambda x: x[0] and round(x[2]*x[3], 2) if x[2]*x[3] > 100 else round(x[2]*x[3]+10, 2), lst))
for i in range(len(lst)):
    res1 = list()
    res1.append(lst[i][0])
    res1.append(summ[i])
    res.append(tuple(res1))
    res1 = []
for i in range(len(res)):
    print('Цена заказа №{} = {}'.format(res[i][0], res[i][1]))
