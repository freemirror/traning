import random
x = set('abcde')
y = set('bdxyz')
z = set('abc')
t = set('abc')
print(x, y)
print(x - y)
print('объединение ', x | y )
print('пересечение ', x & y)
print('исключающее ИЛИ ', x ^ y)
print('надмножество и подмножество', z < x, x < z, z > t)
print('z' in y, 'z' in x)
print(x.intersection(y), ' тоже самое что и &')
z.add('gaga')
print(z)
z.update(y)
print(z, ' объединение')
z.remove('gaga')
print(z)
print(len(z))
for i in set('abc'): print(i * 4)
lis = ['f', 'd', 54]
z = set(lis)
print(z)
z = set((34, 5, 'fgd'))
S = {1, 2}
print(S.union([3, 4]))                                                          #позволяет объединять элементы множества и итерируемых объектов(списки, кортежи)
S = S.union([3, 4])
print(S.issubset(range(-1, 5)), ' Вхождение в интервал')
S.add((1, 2, 9))
print(S, ' словари и списки добавить нельзя')
print((1, 2, 9) in S, 9 in S)
P = frozenset('spas')
print(P, 'Р - неизменяемое множество')
P = frozenset([1, 2, 3, 'pam'])
print(P)
L = {c * 5 for c in 'Valya lyubit kartohu'}
print(L)
L = [1, 2, 3, 4, 5]
print(set(L))
L = set(L)
L = list(L)
print(L)
L = [1, 2, 3, 4, 5, 1, 1, 23, 3, 23, 454, 12, 3, 4, 5, 56]
print(list(set(L)), 'удаление дубликатов')
print(set('qwertyuiop') - set('qwetryiucvdkljf'), 'то что есть в пером множестве но нет во втором')
print(set(dir(list)) - set(dir(dict)), 'различия методов применимых к списку но неприменимых к словарю')
F = set()
for i in range(1000):
    F.add(random.randint(1,1000))
print(len(F))
engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print('bob' in engineers)
print(engineers & managers)
print(engineers | managers)
print(engineers - managers)
print(managers - engineers)
print(engineers > managers)
print({'bob', 'sue'} < engineers )
print(managers ^ engineers)
