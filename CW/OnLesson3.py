# urok 3
'''
если (у-y0)^2+(x-x0)^2 <= R^2
    Dot is not in circle
Else
    Dot is in circle
'''

x0 = int(input("введите коорд Х (центра) окружности"))
y0 = int(input("введите коорд Y (центра) окружности"))

x1 = int(input("введите коорд Х точки"))
y1 = int(input("введите коорд Y точки"))

r = int(input("введите радиус окр"))

res = (y1 - y0) ** 2 + (x1 - x0) ** 2

if res <= r ** 2:
    print("dot is in")
else:
    print("dot is not in")
