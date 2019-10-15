size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end='')
    print()

# for i in range(ver):
#     print(i+1, end='\t')
#     for j in range(1,1+i):
#         print('* ', end='')
#     print("\n", end='')
