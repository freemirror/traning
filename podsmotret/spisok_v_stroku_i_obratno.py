str = 'kartoha est chesnok'
print(str)
lis = list(str)
print(lis)
str2 = ''.join(lis)         #Обратный перевод из списка в строку через str() не работает
print(str2)






b = bytearray(b'spam')
print(b)
b.extend(b'eggs')
print(b)
print(b.decode())



stroka = 'aaa,dddd,jjjjj,ggggg,ttttt,wwwww,uuuu,ooo'
spisok = stroka.split(',')
print(spisok)
