

print(' ****   *   *  *   *    *   \n'
      ' *  *   *  **  ** **  *   * \n'
      ' *  *   * * *  * * *  ***** \n'
      '******  **  *  *   *  *   * \n'
      '*    *  *   *  *   *  *   *')


x = float(input('Введите X \n'))
y = float(input('Введите У \n'))

print(x, y)
summ = x + y
print("Сумма этих чисел =", summ)
step = x ** y
print("Х в степени У =", step)
div = x // y
ost = x % y  #(div * y - x)*-1
print("Х, целоделенный на У =", div, '\n' "Остаток =", ost)