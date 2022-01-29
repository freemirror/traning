D = {'bob':{'name':{'first':'Bob', 'last':'duglas'}, 'doljnost':'director'}}
name = 'Jimmie'                                                                 #input('vvedite imya novogo sotrudnika\n')
firstname = name.capitalize()
lastname = 'Johns'                                                              #input('vvedite familiyu sotrudnika\n')
doljnost = 'deliveryboy'                                                        #input('vvedite doljnost\n')
D[name] = {firstname:{'name':{'first':firstname,'last':lastname }, 'doljnost':doljnost}}
print(D)
D1 = dict(name='Bob', job='killer')
print(D1)
D1 = dict([('name','bob'),('age', 40)])
print(D1)
keyslist = ['abrag', 'gorgok']
valueslist = [12, 45]
D2 = dict(zip(keyslist, valueslist))
D2 = dict.fromkeys(['nam', 'age'])
print('\n', D2)
print('last' in D,'\n' * 3)
print(list(D.keys()))
print(list(D1.values()))
print(D1.items())
D1.clear()
print(D1,D2)
D1 = dict(name='Bob', job='killer')
D2 = {'biber':'suck', 'jack':'hero'}
D1.update(D2)
print(D1)
print('\n\n\n', D1.get('name'))
D1['name'] = 'greg'
print(D1)
print(D1.setdefault('name'))
print(D1.popitem())
print(D1.popitem())
print(D1)
print(len(D2))
D1['barbarek'] = 'lol'
print(D1)
del D1['job']
print(D1)
L = list(D1.keys())
print(L)
L1 = D1.keys() & D2.keys()
print(L1, * L1)
S = set([45, 65])
print(S)
D3 = {((x - 4 * x + 1) ** x) // x ** x : x * 2 for x in range(2,7) }
print(D3)
print(D3.get('boom'))

Di = {'bar':15, 'boor':16 , 'moor':17}
Di1 = {'foor':28, 'door':87, 'bar':90}
Di.update(Di1)
print(Di)
print(Di.pop('door'))
print(Di)

table = {'1975':'Holy Grail',
        '1979':'Life Of Brain',
        '1983':'The Meaning Of Life'}
year = '1983'
movie = table[year]
print(movie)
for year in table:
    print(year + '\t' + table[year])
table = {'Holy Grail':'1975',
        'Life Of Brain':'1979',
        'The Meaning Of Life':'1983'}
print([title for (title, year) in table.items() if year == '1975'])
K = 'Holy Grail'
print(table[K])
V ='1975'
print([key for (key, value) in table.items() if value == V])

ip = {(192,168,89,120):'home',(192,168,1,1):'work'}
print(ip[(192,168,89,120)])
print(ip.get((192,168,89,120),0), ip.get((192,168,55,89),0))

try:
    print(ip[192,64,43,123])
except KeyError:
    print('net takogo')

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print('\n', rec['name'])

rec = {'name':'Bob',
        'jobs':['developer', 'manager'],
        'wev':'www.bobs.org/~Bob',
        'home':{'state':'Overworked', 'zip':12345}}
print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])

other = {'Stan':'Smith'}
db = []
db.append(rec)
db.append(other)
print('\n', db[0]['jobs'])

db = {}
db['bob'] = rec
db['sue'] = other
print(db['bob']['jobs'])
print(db['sue'])
print(db)
gor = dict(name = 'bob', age = 40)
goro = dict([('name', 'Bobo'), ('age', 40)])
print('\n', gor, goro)

x = dict.fromkeys(['a', 'b'], 0)
print(x)

D = {}
D['state1'] = True
print(D)
S = set()
S.add('state1')
print(S)
