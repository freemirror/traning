x = 3
print(x << 2, bin(x << 2))
print(x | 2, bin(x | 2))
print(x & 1, bin(x & 1))

X = 0b0001
print(X << 2)
print(bin(X << 2))
print(bin(X | 0b010))
print(bin(X & 0b1))
X = 0xFF
print(bin(X))
print(bin(X ^ 0b10101010))
print(int('01010101', 2))
print(hex(85))

X = 99
print(bin(X), X.bit_length(), len(bin(X))-2)
print(bin(256), (256).bit_length(), len(bin(256))-2)
