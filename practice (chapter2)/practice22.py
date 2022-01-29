X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a':1, 'b':2}
L = [1, 2, 3]
F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X,Y,Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()
chars = open('datafile.txt').read()
print(chars,'\n')
F = open('datafile.txt')
line = F.readline()
print(line)
line = F.readline()
line = line.rstrip()
parts = line.split(',')
print(parts)
numbers = [int(P) for P in parts]
print(numbers, '\n')
line = F.readline()
parts = line.split('$')
print(parts)
objects = [eval(P) for P in parts]
print('\n', objects[0], '\n', objects[1])
