dix = 'dix'
jem, mem = 'grood', 'druud'
print(dix, jem)
[ jim, bim] = ['jack', 'Daniels']
print(bim)
a, b ,c ,d = 'hoho'
print(a, b, c, d)
a, *b = 'spam'
print(a, *b)
oil = coffe = 'money'
x = 0
while x < 35:
    print('Go to hell!')
    x += 1

nudge = 1
wink = 2
A, B = nudge, wink
print(A, B)
[C , D] = [nudge, wink]
print(C, D)

nudge = 1
wink = 2
nudge, wink = wink, nudge
print('\n', nudge, wink)

string = 'SPAM'
a, b, c, d = string
print(a, d)
a, b, c = string[0], string[1], string[2:]
print(a,b,c)
a, b, c =list(string[:2]) + [string[2:]]
print(a, b, c)
a, b = string[:2]
c = string[2:]
print(a, b, c)
(a, b), c = string[:2], string[2:]
print(a, b, c)
((a, b), c) = ('SP', 'AM')
print(a, b, c)

red, green, blue = range(3)
print(red, blue)
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
a, *b = seq
print(a, '\n',  b)
*a, b = seq
print(a, '\n', b)
a, *b, c = seq
print(a, '\n', b, '\n', c)
a, b, *c = seq
print(a, b, '\n', c)
a, *b = 'spam'
print(a, b)
a, *b, c = 'spam'
print(a, b, c)
a, *b, c =range(4)
print(a, b, c)
S = 'spam'
print(S[0], S[1:])

L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a, b, c, d)
a, b,c, d, *e = seq
print(a, b, c, d, e)
a, b, *c, d, e = seq
print(a, b, c, d, e)
*a, = seq
print(a)

a, *b = seq
print(a, b)
