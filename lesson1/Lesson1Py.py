# DZ №1, третье задание в картинке

# №4
print("Задание 4") # Имя звездами
print(' ****   *   *  *   *    *   \n'
      ' *  *   *  **  ** **  *   * \n'
      ' *  *   * * *  * * *  ***** \n'
      '******  **  *  *   *  *   * \n'
      '*    *  *   *  *   *  *   *')

# №5
print("Задание 5")
print('Escape sequences\n'
      '\\a      Bell (alert)\n'
      '\\b      Backspace\n'
      '\\n      New line\n'
      '\\t      Horizontal tab\n'
      '\\\      Backslash \\ \n'
      '\\”      Double quotation mark “\n'
      '\\’      Single quotation mark ‘')

# №6
print("Задание 6")
x = int(input('Введите X \n'))
y = int(input('Введите У \n'))
print(x, y)
summ = x + y
print("Сумма этих чисел =", summ)
div = x // y
ost = x % y  # (div * y - x)*-1
print("Х, целоделенный на У =", div, '\n' "Остаток от деления =", ost)
step = x ** y
print("Х в степени У =", step)
