"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
  C         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   *
    *               *
      *           *
        *       *
          *   *
            *

"""
vertical = ver = int(input("введите высоту (нечетное число): "))
horizontal = hor = ver

for i in range(ver):
    print(i+1, end='\t')
    for j in range(hor):
        if j == hor//2+i or j == hor//2-i or hor//2-i < j < hor//2+i and i <= ver//2 or j == -hor//2+i+1 or j == hor-1-i+hor//2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
