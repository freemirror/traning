#f = open('data.txt', 'w')
#f.write('Hello\n')
#f.write('World End\n')
#f.close()
#f = open('data.txt')
#print(f)
#text = f.read()
#print(text)
#print(len(text))
t = open('data2.txt', 'w')                                                      #Создать файл в режиме записи
t.write('Привет мир, как слышно?\n\n')                                          #Записать в него строку
t.close()
t = open('data2.txt')
print(t)
text = t.read()
print(text)
t2 = open('data2.txt')
print(t2)
text2 = t2.read()
print(text2, len(text2), len(text))
print(text2.split())
for line in open('data2.txt'):
    print(line)
print(dir(text2))