print(2 ** 16)
print(2 / 5, 2 / 5.0)
print('spam' + 'spam')
S = 'ham'
print('eggs' + S, S * 5)
print(S[:0])
print('green %s and %s' % ('eggs', S))
print('green {0} and {1}'.format('eggs', S))
print(('x',) [0])
print(('x', 'y')[1])
L =[1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2], L[-2:])
print([L[2], L[3]])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))
print({'a':1, 'b':2}['b'])
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0
print(D['x'] + D['w'])
D [(1,2,3)] = 4
print(list(D.keys()), list(D.values()), (1,2,3) in D)
zz = [[]], ['', [], (), {}, None]
print(zz)
print(type(zz))

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(L[-100:50])
L[5:2] = 'gg'
print(L, L[5:1])

L2 = [44, 65, 87, 91, 81, 20, 65, 44, 66, 123]
L2[6] = []
print(L2)
L2[5:8] = []
print(L2)
del L2[0]
print(L2)
del L2[1:]
print(L2)

X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X, Y)

D = {}
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)

D1 = dict(a = 11, b = 54, c = 'hophey lalaley')
D1['d'] = 'spam'
print(D1)
D = {'a': 21}
D1 = {'g':98, 'y': 54}
D2 = sorted(D) + sorted(D1)
print(D2, sorted(D), sorted(D1))

S = 'spam'
print(S[1][0][0][0][0])
Ls = ['s', 'a', 'p', 'm']
print(Ls[1][0][0][0][0])

S = 'spam'
S = S[0:1] + 'l' + S[2:]
print(S)
S = 'spam'
S = S[0] + 'l' + S[2] + S[3]
print(S)

Me = {'name':{'first':'Tim', 'last':'Robo', 'third':'Olegovna'}, 'age':23,
'job':{'company':'IBM', 'post':'coder'}, 'adress':{'city':'NY', 'stret':'5th street'},
 'email':'fredcom.zilo.re', 'phone':9129234828}
print(Me)
print(Me['name'], Me['email'])

stri = 'Hello file world!'
F = open('myfile.txt', 'w')
F.write(stri)
F.close()

F = open('myfile.txt', 'r').read()
print(F)
