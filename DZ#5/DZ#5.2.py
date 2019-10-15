"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
  B         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
"""
vertical = ver = int(input("введите высоту: "))
horizontal = hor = (ver*2)-1

for i in range(ver):
    print(i+1, end='\t')
    for j in range(hor):
        if j == hor//2+i or j == hor//2-i or i == ver-1 or hor//2-i < j < hor//2+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
