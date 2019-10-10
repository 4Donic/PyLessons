"""
x = 12345
y = 0

while x:
    y = y * 10 + x % 10
    x //= 10

print(y)
"""
ver = 5
hor = 5
for i in range(ver):
    print(i+1, end='\t')
    for j in range(hor):
        if j == 0 or j == hor - 1 or i == 0 or i == ver - 1: # or i == j or i == hor - j - 1 or j == hor // 2 or i == ver // 2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
