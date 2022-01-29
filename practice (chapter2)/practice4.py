f = open('data.txt', 'w')
print(f.write('Hello\n'))
print(f.write('world\n'))
f.close()
f = open('data.txt', 'r')
str = f.read()
print(str)
print(str.split())
for line in open('data.txt'):
    print(line)

S = 'sp\xc4m'
print(S, S[2])
file = open('unidata.txt', 'w', encoding = 'utf-8')
file.write(S)
file.close()
text = open('unidata.txt', 'r', encoding = 'utf-8').read()                      #Получаем декодированное содержимое файла
print(text, len(text))
raw = open('unidata.txt', 'rb').read()                                          #Реальное содержимое файла
print(raw, len(raw))
print(text.encode('utf-8'))
print(raw.decode('utf-8'))

X = set('spam')                                                                 #Множества - удобны для сортировки, удаления дублей
Y = {'h', 'a', 'm'}
print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)
print({n ** 2 for n in [1, 2,3 ,4]})
print(list(set([1, 2, 1, 3, 1])))                                               #фильтрация дубликатов
print(set('spam') - set('ham'))                                                 #нахождение разницы в коллекциях
print(set('spam') == set('aspm'))                                               #проверка равенства без одной последовательности
