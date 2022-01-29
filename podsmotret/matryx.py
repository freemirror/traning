Mat = [[131,543,636],
       [653,242,564],
       [333,111,232]]
print(Mat[0])
stolbec2 = [row[1] for row in Mat if row[1] % 2 == 0]
print(stolbec2)
diag = [Mat[i][i] for i in [2, 1, 0]]
print(diag)
bb = [c + 'f' for c in 'morg']
print(bb)
M2 = [[x + 54, (x + 40) / 5, 2 ** (x + 1)] for x in range(4)]
print(M2)
row3 = [row[2] for row in M2]
print(row3)
