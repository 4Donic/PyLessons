# file = open(r'CW12\CW12Module.py', 'tr', encoding='utf8')
# file1 = open('test.txt', 'tw')
#
# res = file.read()
# file1.write(res)
# print(res)
#
#
# file.close()
#
# file1.close()
# # #
file = open('test.txt', 'w+')

for i in range(10):
    file.write('test info {}\n'.format(i))

file.seek(0, 0)
res = file.read()
print('res = ', res)

for i in range(10):
    file.write('new info {}\n'.format(i))

file.close()