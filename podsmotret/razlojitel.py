string1 = input('vvedite stroku\n')
dlinna = len(string1)
print(dlinna)
schetchik = 0
for char in string1:
    print('*',' ' * schetchik, char, ' ' * dlinna, '*')
    schetchik+=1
    dlinna-=1
