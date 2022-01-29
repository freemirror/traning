dict33 = {'food' : 'Spam', 'quantity' : 4, 'color' : 'pink'}
print(dict33['food'], dict33['color'])
dict33['quantity'] += 1
print(dict33['quantity'])
dict2 = {}
dict2['name'] = 'Billi'
dict2['job'] = 'driver'
dict2['age'] = 40
print(dict2)
richard = dict (name = 'Richard' , job = 'King' , age = 55)
print(richard)
richard3 = dict(zip(['name', 'job', 'age'],['Richard3', 'King', 34]))
print('\n', richard3)
rec = {'name' : {'first': 'Bobbie', 'last':'Brawn'}, 'jobs':['dev','mgr'], 'age': 42.5}
print(rec['name']['last'])
print(rec['jobs'][1],'\n', rec['age'])
rec['jobs'].append('janitor')
print(rec['jobs'])
dict7 = {'a':1, 'b':2, 'c':3}
dict7['e'] = 99
print(dict7)
print('f' in dict7)
if not 'f' in dict7:
    print('missing')
value = dict7.get('k', 8)
print(dict7)
print(value)
value = dict7['f'] if 'f' in dict7 else 0
print(value)

dict7['d'] = 1662
print(dict7)
Ks = list(dict7.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
    print(key, '=>', dict7[key])
for key in sorted(dict7):
    print(key, '=>', dict7[key])
for i in 'gagagach':
    print(i.upper())
x = 4
while x > 0:
    print('badabams' * x)
    x-=1

T = (1, 2, 3, 4)
print(T, '\n', T[2], '\n',len(T))
print(T.index(1))

T2 = (1, 2, 3, 3, 5, 1, 2, 1)
print(T2.count(1))                                                  #вхождение аргумента метода в кортеж
