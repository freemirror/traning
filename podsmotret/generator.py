M2 = [[x + 54, (x + 40) / 5, 2 ** (x + 1)] for x in range(4)]
print(M2)
G = (sum(row) for row in M2)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(list(map(sum, M2)))
