"""
10. В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. Создавать новый
список недопустимо.
"""
lst = [19, 10, 11, 15, 9, 2, 14, 8, 20]
print("Before:", lst)
nmax = lst[0]
nmin = lst[0]
idx = 0
maxidx = 0
minidx = 0
for number in lst:
    if number > nmax:
        nmax = number
        maxidx = idx
    elif number < nmin:
        nmin = number
        minidx = idx
    idx += 1
lst[maxidx] = nmin
lst[minidx] = nmax
print('After: ', lst)
