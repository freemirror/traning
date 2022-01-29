S = 'gagaga'
L1 = [1,2]
D = {'gogol':'big', 'great':'fooldead'}
L = [S, L1, D]
print(L)
S = S + 'gugus'
L1[0] = 5
L1.append(7)
D['foot']= 'desert'
D.pop('gogol')
print(L)
L[0] = S
print(L)
D['greazley'] = {'bear':'ant', 'golo':'desk'}
print(D['greazley']['golo'], D['greazley'])
L2 = list('Jora lyubit Lizu')
L3 = list(range(-142,678, 73))
print(L2, L3)
D = dict( gon = 'ttt', jop = 'ppp')
D2 = {2:'jol'}
print(D, D2, D['gon'], D2[2])
L5 = [3, 7, 4564]
L5.extend([7547,88,2345234,754])
L5.append([4,3])
L5.insert(3, 744564645654)
L5.insert(99,0)
print('\n\n\n', L5, L5[8], L5[9])
L5.pop(8)
L5.sort()
print(L5)
L5.reverse()
print(L5)
L5.clear()
print(L5)
L5 =[]
print(L5)
L5.extend([7547,88,2345234,754])
L5.append([4,3])
L5.insert(3, 744564645654)
L5.insert(99,0)
L5.remove(88)
print(L5)
del L5[:2]
print(L5)
del L5[2]
print(L5)
print(L5[2])
L5.insert(3, 777)
L5[4:7] = [54, 234, 1,3]
print(L5)
L4 = [[x * 7 / 10, x * 2 - 5, x] for x in  range(0,5)]
print(L4)

L = [221, 112, 3234, 46, 535, 46, 27, 88, 459, 27, 27, 267]
print(L.index(46), L.count(27))
