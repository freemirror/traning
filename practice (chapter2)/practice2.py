lis = [123, 'ggg', 1.23]
print(len(lis), lis)
print(lis[0])
print(lis[1:])
print(lis[-1:])
lis.append('gagagga')
print(lis)
print((lis + [555, 2342, 'grunt wont work']) * 3)
lis.pop(1)
print(lis)
del lis[1]
print(lis)
lis.insert(0, 'privet')
print(lis)
lis.remove(123)
print(lis)
lis.extend('che kak?')
print(lis)
lis.sort()
print(lis)
lis.reverse()
print(lis)
M = [[1, 2,3], [4, 5, 6], [7, 8, 9]]
print(M, '\n', M[0])
print(M[2][0])
print([a[0] for a in M])
lis1 = [a[1] ** 5 for a in M if a[1] % 2 == 0]
print(lis1)
diag = [M[i][i] for i in [0, 1, 2]]
print(diag)
doubl = [c * 2 for c in 'gagaga']
print(doubl)
lis4 = [(num + 35)/(29-num) for num in range(7)]
print(lis4)
list5 = list(range(-10, 12, 3))
print(list5)
list66 = [[x ** 2, x ** 3, x ** 4] for x in range(2,5)]
print(list66)
list15 = [[x, x +2, x ** 3] for x in range(-9, 15, 3) if x > 0]
print(list15)
G = (sum(a) for a in M)
print(next(G))
print(next(G))
print(next(G))
print(list(map(sum,M)))
print({sum(a) for a in M})
print({i : sum(M[i]) for i in range(3)})
