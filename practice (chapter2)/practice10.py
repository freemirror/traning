import sys
L1 = [2, 3, 4]
L2 = L1
L1[0] = 444
print(L1)
print(L2,'\n')

L1 = [5, 7, 78]
L2 = L1.copy()
L1[1] = 56
print(L1, '\n', L2)

lis1 = ['gaga', 'gugu', 'gogo']
lis2 = lis1
lis2[1] = 'goblin'
print(lis1, lis2)

lis1 = ['gaga', 'gugu', 'gogo']
lis2 = lis1[:]
lis2[0]= 'morgul'
print(lis1, lis2)

a = 2
b = 2
print(b is a, b == a)

L1 = [1, 2, 3]
L2 = L1
print(L2 is L1, L2 == L1)

L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(L2 is L1, L2 == L1)
print(sys.getrefcount(L2), 'количество ссылок на объект')
