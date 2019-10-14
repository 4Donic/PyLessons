"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
  A         *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *
"""

vertical = ver = 7  # int(input("введите высоту"))
horizontal = hor = (ver*2)-1

# for i in range(ver):
#     print(i+1, end='\t')
#     for j in range(1,1+i):
#         print('* ', end='')
#     print("\n", end='')

for i in range(ver):
    print(i+1, end='\t')
    for j in range(hor):
        if j == hor // 2 and i == 0 or j == hor//2+i and i != 0 or j == hor//2-i and i != 0 or i == ver-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
