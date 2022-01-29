
print("spam's",'\n', 's\np\ta\x00m')
print(r'\temp\spam')
print(b'sp\xc4m', u'sp\u00c4m')
s = 'pool'
print(s * 23, s + 'game')
print(s[0], len(s), s[:2])
print(s.find('oo'))
le = 'pool is gool'
for i in le:
    print(i + 'brbrbr')
title = "Meaning" 'of' "life"
print(title)
'''f = open(r'C:\py_project\new\text.dat', 'w')
f.write(title)
f.close()'''
print('Ni! ' * 4)
str10 = 'Valya Lyubit Kartohu'
for i in str10:
    print(i, end=' ')
print('h' in str10, 'z' in str10)
str101 = 'Valya Lyubit Kartohu Ochen Ochen i malenkuyu i bolshuyu'
print(len(str101))
print(str101[:-50], str101[6:12], str101[-42:-35 ], str101[:], str101[-3])
print(str101[::2])                                                              #Нарезание и вывод каждого второго символа.
print(str101[::-1])
print('\n\n\n',str101[slice(5,20)])
print(str101[slice(None, None, -1)])
print(ord('j'), chr(78))                                                        #Коды ASCII
st = 'slam'
st = st.replace('la', 'alamaleicu')
print(st)
st = 'That is %d %s bird!' % (1, 'dead')
print(st)
print(st.find('dead'))
