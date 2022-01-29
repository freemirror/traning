#D = { 'car' : 'mazda','food' : 'fish and chips', 'number': 123131}
#print(D['number'] + 222)
#print(D['food'] + ' beer')
#D['plant'] = 'tree'
#print(D['plant'])
#print(D)
#mister = dict(name = 'willey', age = 84, job = 'writter')
#print(mister)
#mister2 = dict(zip(['name', 'age', 'job'],['willey', 84, 'writter']))
#print(mister2)
import decimal
X = set('spam')
Y = {'h', 'a', 'm'}
print(X,Y)
print(X&Y)
print(X|Y)
print(X - Y)
print(X>Y)
B ={n ** 2 for n in [1,2,3,4]}
print(B)
print(list(set([1,2,1,3,1])))
print(set('spam') - set('ham'))
print(set('spam') == set('asmp'))
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])
print((1/2) + (2/3))
d = decimal.Decimal('3.141')
