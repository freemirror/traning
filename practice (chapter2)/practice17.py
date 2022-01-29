L = list(range(0, 12))
print(L)
L[5] = 22
L[4:10] = range(20, 60, 30)
print(L)
print(L * 3)
print(L + list(range(1,9)) )
print(str([2,77]) + 'ggg', '\n', [2,5] + list('kk') )
L2 = list(map(ord, 'badabam'))
print(L2)
print(list(map(abs,[-1, -2, 0, 1, 2])))
L = ['abc', 'ABD', 'aBe']
L.sort()
print('\n', L)
L.sort(key=str.lower)
print(L)
L.sort(key=str.lower, reverse=True)
print(L)
L = ['abc', 'abd', 'abe']
L.sort()
print(L)
L = ['abc', 'abd', 'abe']
print(sorted(L, key=str.lower, reverse=True))
L = ['abc', 'abd', 'abe']
print(sorted([x.lower() for x in L],reverse=True))
L = ['abc', 'abd', 'abe']
L.reverse()
print(L)
print(list(reversed(L)))
L1 = []
L1.append(1)
L1.append(23)
print(L1)
L1.pop()
print(L1)
