from os import system
from time import sleep
from sys import platform

if platform == 'darwin' or platform == 'linux':
    from getch import getch
elif platform == 'win32':
    from msvcrt import getch
else:
    print("Неизвестная платформа")
    exit(1)

if platform == 'darwin':
    SCAN_CODE = 91
    UP = 65
    DOWN = 66
    RIGHT = 67
    LEFT = 68
elif platform == 'win32':
    SCAN_CODE = 224
    UP = 72
    DOWN = 80
    RIGHT = 77
    LEFT = 75

# while True:
#     c = getch()
#     print(ord(c))
SPACE = 32
EMPTY_FIELD = 16


def clear_scr():
    if platform == 'darwin' or platform == 'linux':
        system('clear')
    elif platform == 'win32':
        system('cls')


def field(lst):
    clear_scr()

    print("Use arrow keys to move")
    print("Press SPACE key to stop")
    print()
    print('+----+----+----+----+')
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print('|{value:^4}'.format(
                value=lst[i][j] if lst[i][j] != EMPTY_FIELD else ''),
                end='')


def moveUp(lst, x, y):


    return x,y
