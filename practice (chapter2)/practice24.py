import struct
code = '>i4sh'
F = open('data.bin', 'wb')
data = struct.pack(code, 7, b'pamp', 8)
print(data)
F.write(data)
F.close()
L = open('data.bin', 'rb').read()
print(L)
print(struct.unpack(code, L))

D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
print(sorted(list(D1.items())))
print(sorted(D1.items()) < sorted(D2.items()))
print(sorted(D1.items()) > sorted(D2.items()))
print(sorted(D1.items()))
