from collections import namedtuple
L=[]
K = (1, 2, 'hj', L)
print(K)
L.append('kkk')
L.append(853)
print(K)
T = tuple('spam')
print(T)
T = 54, 23, 524, 52, 421, 342, 342, 4231
print([x * 2 for x in T])
T = tuple('Valya lyubit kartohu')
print(T.index('k'))
print(T.count('u'))
print(T)
T = (1, 2, 3, 4)
print(T[0], T[1:3])
T = ['cc', 'aa', 'dd', 'bb']
tmp = list(T)
tmp.sort()
print(tmp)
T = tuple(tmp)
print(T)
print(sorted(T))
T = (1, 2, 3, 4, 5)
L = [x +20 for x in T]
print(L)
T = (1, [2, 3], 4)
T[1][1] = 'gobot'
print(T)
bob = dict(name='Bob', age='40,5', jobs=['dev','mgr'])
print(tuple(bob.values()))
print(list(bob.values()))
print('\n\n')
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age = 40.5, jobs=['dev','mgr'])
print(bob)
print(bob[0], bob[2])
print(bob.name, bob.jobs)
O = bob._asdict()
print('\n\nb\n\n',O['name'], O['jobs'])
print(O, '\n')
bob = Rec('Bob', 40.5, ['dev', 'mgr'])
name, age, jobs = bob
print(name, jobs)
for x in bob:
    print('\n', x)
print('\n')
bob = {'name':'Bob', 'age':40.5, 'jobs':['dev', 'mgr ']}
name, age, job = bob.values()
print(name, job)
for x in bob:
    print(bob[x])
