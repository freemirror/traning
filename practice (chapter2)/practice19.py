L = list(zip(['a', 'b', 'c'], [1, 2, 3]))
print(L)
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)
print(dict(L))
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)

D = {x: x * 4 for x in 'gogol bordello'}
print(D)
D = {c.lower(): c +'!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)
D = {k: 0 for k in ['a', 'b', 'c']}
print(D)
print('\n')
D = dict.fromkeys('spam')
print(D)
D = {k: None for k in 'spam'}
print(D)

D = dict(a = 1, b = 2, c = 3)
print(D)
K = D.keys()
print(K, *K, list(K))
L = list(K)
print(L)
V = D.values()
print(V)
L = list(V)
print(L)
I = D.items()
print(I)
L = list(I)
print(L)
for k in D.keys():
    print(k)
for key in D:
    print(key)
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
K = D.keys()
V = D.values()
print(list(K), list(V))
del D['b']
print(list(K), list(V))
print(K, V)
X = {'x': 4}
print(K | X)

D = {'a': 1, 'b': 2, 'c': 3}
print('\n', D.keys() & D.keys())
print(D.keys() & {'b'})
print(D.keys() & {'b': 1})
print(D.keys() | {'b', 'c', 'd'})

D = {'a': 1}
print('\n', list(D.items()))
print(D.items() | D.keys())
print(D.items() | D)                                                            #Словарь трактуется так же как и его ключи, оператор работает по хэшируемым частям(неизменяемым)
print(D.items() | {('c', 3), ('d', 4)})
print(dict(D.items() | {('c', 3), ('d', 4)}))

D = {'a':1, 'b':2, 'c': 3}
L = list(D)
L.sort()
for x in L:
    print(x, D[x])
print(D)
L = D.keys()
for x in sorted(L):
    print(x, D[x])
print('\n', D)
for x in sorted(D):
    print(x, D[x])
if 't' in D:
    print('in')
else:
    print('not in')
print(D.get('a', 6))                                                            #Значение по ключу 'a' 1 в словаре
print(D.get('k', 6))
