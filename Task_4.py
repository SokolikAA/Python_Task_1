# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('введите число долек по длине: '))
m = int(input('введите число долек по ширине: '))
k = int(input('введите число долек, которые хотите отломить: '))

if k == int(n * m):
    print(n, ' ', m, ' ', k, ' -> ', 'no')
elif k % n == 0 or k % m == 0:
    print(n, ' ', m, ' ', k, ' -> ', 'yes')
else:
    print(n, ' ', m, ' ', k, ' -> ', 'no')
