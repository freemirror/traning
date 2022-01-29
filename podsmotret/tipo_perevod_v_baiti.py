I = int(input('please input dec number\n'))
print('len dec system ', len(str(I)))
str = bin(I)
str2 = str[2:]
print('bin system ', str2)
print('len bin system ',len(str2))
ran = len(str2) // 8
print(ran, ' full bloacks of bin system')
for x in range(ran):
    print(str2[x * 8: x * 8 + 8])
