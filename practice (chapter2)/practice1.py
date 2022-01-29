import math
import random
'''f = open(r'C:\Users\Артём\Desktop\valya.txt').read()
print(f)'''
print(len(str(2 ** 10)))
print(math.pi ** 5)
print(math.sqrt(77))
print(random.random() * 55 / 54)
string11 = 'privet kartoha'
print(string11)
print(string11[7:], string11[:6])
print(string11[-7:], string11[:-7])
print(len(string11)-15)
print(string11[3:13])
print(string11 + ' Valya tebya lyubit')
print((string11[7:] + ' ') * 88)
string2 = string11 + ' Valya'
print(string2)
lis = list(string11)
print(lis)
lis[11] = 'gagaga'
print(lis)
string34 = ''.join(lis)
print(type(string34))

slova = 'privet drug vet'
listo = []
listo = slova.find('ve')
print(listo, type(listo))
print(slova.replace('vet', 'govnet'))

print(string11.isalpha())
s = 'a'
print(s.isalpha())
h = 34435353454
print(str(h).isdigit())
s = 'HhYHkHIhuyGgJLK'
print(s.lower(), s.upper())
string222 = 'ggg ,kkk    ,sdf  sd f sdf,wer w, er    sfgs,s  d df,s,, s d , f , sd, ,d,f                  '
print(string222.strip().split(','))
print(dir(string222))
print(help(string222.replace))
