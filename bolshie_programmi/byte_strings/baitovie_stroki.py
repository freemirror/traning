import random

def ochistka_baza():
    proverka_zapolnennost = open('baza.txt', 'r').read()
    if proverka_zapolnennost != '':
            ochistka = int(input('baza soderjit dannie, jelaete ochistit? (1 - da, 0 net)\n'))
            if ochistka == 1:
                proverka_zapolnennost = open('baza.txt', 'w')
                proverka_zapolnennost.close()
    return

def zapolnenie(D, numerat = 0):
    kolvo = int(input('Vvedite kol-vo baitovih strok po 8 bait) \n')) * 8
    for i in range(kolvo):
        byt = int(random.random() * 10 ** 8 )
        if byt < 10000000:
            byt = byt * 10 + int(random.random() *10)
            if byt < 10000000:
                byt = byt * 10 + int(random.random() *10)
                if byt < 10000000:
                    byt = byt * 10 + int(random.random() *10)
        D.append(str(byt))
    baza = open('baza.txt', 'a')
    for element in D:
        baza.write(element)
        baza.write(' ')
        numerat += 1
        if numerat >= 8:
            baza.write('\n')
            numerat = 0
    baza.close()
    return D

def vivod():
    bazaza = open('baza.txt', 'r').read()
    print(bazaza)
    spis = bazaza.split(' ')
    srez_vivod = int(input('jelaete pervie i drugoi stilbec (1 - da, 0 - net)?\n'))
    if srez_vivod == 1:
        srez = int(input('vvedite vtoroi stolbec 2-8\n'))
        print('\n')
        for i in range(0, len(spis) - 1, 8):
            print(spis[i],' ' * 9 * (srez - 2), spis[i + srez - 1])
    return

x = 1
while x == 1:
    L = []
    ochistka_baza()
    L = zapolnenie(L)
    vivod()
    x = int(input('hotite prodoljit (1 - da, 0 - net)?\n'))
