import math
import random
I = 0b10110011
J = '111010110100101'
B = '636354354'
print(bin(I), '\n', hex(I), '\n', oct(I))
print(int(J, 2))
#while True:
#    sdvig = int(input('vvedite sdvig (dlya vihoda 0)\n'))
#    if sdvig == 9:
#        break
#    rez1 = I & sdvig
#    print('', bin(I),'\n', bin(sdvig), '\n', rez1, bin(rez1))
k = -12.213152352532
print(pow(k, 2))
print(abs(k))
print(round(k, 4))                              #округление до знака чтвертого аргумента
num = 1 / 3
print(num)
print('%e' % num)
print('%4.2f' % num)
print('{0:4.2f}'.format(num))
print(repr('spon'))
print(1.2 + 2.2 == 3.3)
print(int(1.2 + 2.2) == int(3.3))
print(5 // 2)
print(5 // - 2)
print(math.floor(2.5), 'math.floor')
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print(round(2.5))
print(round(-2.5))
print(int(2.5))
print(int(-2.5))
print(int('E4', 16), int('11000', 2), int('51354131235215', 8))
num4 = 231847
print(num4.bit_length())
print(math.e)
print(math.pi)
print(math.sqrt(4096))
print(pow(5,4))
print(pow(144, 0.5))
print(random.random())
print(random.randint(1,16))
lis = ['gogik', 7, {'Bob':'name'}, math.pi]
print(random.choice(lis))
lis2 = ['fifo', 'shisho', 'magnus','gopnik']
random.shuffle(lis2)
print(lis2)
random.shuffle(lis)
print(lis)
