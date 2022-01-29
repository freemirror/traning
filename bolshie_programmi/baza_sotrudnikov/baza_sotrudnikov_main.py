def zapolnit_dannie(file_str):                                                  #функция получает соджержимое файла и заполняет переменные мейна
    file_list = file_str.split()
    spisok_vozrastov_lok = []
    spisok_doljnostei_lok = []
    spisok_imen_lok = []
    spisok_sotrudnikov_lok = {}
    scetchik = 0
    for i in file_list:
        scetchik += 1
        if scetchik % 3 == 0:
            spisok_vozrastov_lok.append(i)
        elif scetchik % 3 == 2:
            spisok_doljnostei_lok.append(i)
        elif scetchik % 3 == 1:
            spisok_imen_lok.append(i)
            spisok_sotrudnikov_lok[i] = scetchik // 3
    vsego_sotrudnikov_lok = scetchik // 3
    cube = [spisok_imen_lok, spisok_doljnostei_lok, spisok_vozrastov_lok, spisok_sotrudnikov_lok, vsego_sotrudnikov_lok]
    return cube

print('\t' * 4, 'Sotrudniki firmi')
file = open('Spisok_sotrudnikov.txt', 'r').read()
ret_cube = zapolnit_dannie(file)                                                #Распаковка оболочки возврата функции
spisok_imen = ret_cube[0]
spisok_doljnostei = ret_cube[1]
spisok_vozrastov = ret_cube[2]
spisok_sotrudnikov = ret_cube[3]
vsego_sotrudnikov = ret_cube[4]

while True:
    perekluch = int(input('\t\t****vvedite deistvie**** (9 - vivesti spisok deystvie)\n'))
    if perekluch == 0:                                                                             #выход
        break
    elif perekluch == 1:                                                                           #вывод имен сотрудников с табельными номерами
        if vsego_sotrudnikov == 0:
            print('Dannie po sotrudnikam ne vvedeni')
        else:
            j = 0
            for j in range(vsego_sotrudnikov):
                print(spisok_imen[j-1], ':', spisok_sotrudnikov[spisok_imen[j - 1]] + 1)
    elif perekluch == 2:                                                                           #вывод детальных данных по сотруднику
        perekluch = int(input('Osuschestvit poisk po imeni - 1 ili tabelnomu nomeru - 2?\n'))
        if perekluch == 1:
            name = input('Vvedite imya sotrudnika po kotoromu nujno vivesti dannie\n')
            if name in spisok_imen:
                print('sotrudnik ', name, ' zanimaet doljnost', spisok_doljnostei[spisok_sotrudnikov[name]], ', vozrast ', spisok_vozrastov[spisok_sotrudnikov[name]], 'tabelnie nomer = ', spisok_sotrudnikov[name] + 1)
                input()
            else:
                print('Takogo sotrudnika u nas net')
        elif perekluch == 2:
            tabel_num = int(input('vvedite tabelnie nomer sotrudnika\n'))
            if tabel_num in range(0, vsego_sotrudnikov + 1):
                print('sotrudnik ', spisok_imen[tabel_num - 1], ' zanimaet doljnost', spisok_doljnostei[tabel_num - 1], ', vozrast ', spisok_vozrastov[tabel_num - 1], 'tabelnie nomer = ', tabel_num)
                input()
            else:
                print('Takogo sotrudnika u nas net')
    elif perekluch == 3:                                                                           #добавление новых сотрудников
        i = int(input('Skolko sotrudnikov vam neobhodimo vnesty\n'))
        while i > 0:
            file = open('Spisok_sotrudnikov.txt', 'a')
            name = input('Vvedite imya sotrudnika\n')
            doljnost = input('vvedite doljnost sotrudnika\n')
            vozrast = int(input('vvedite vozrast sotrudnika\n'))
            spisok_imen.append(name)
            spisok_doljnostei.append(doljnost)
            spisok_vozrastov.append(vozrast)
            file.write('%s %s %s\n' % (name, doljnost, vozrast))
            file.close()
            spisok_sotrudnikov[name] = vsego_sotrudnikov
            vsego_sotrudnikov += 1
            i -= 1
    elif perekluch == 4:                                                                           #удаление сотрудника по табельному номеру
        tabel_num = int(input('Vvedite tabelnie nomer sotrudnika dlya udaleniya\n'))
        file = open('Spisok_sotrudnikov.txt', 'w')
        spisok_sotrudnikov.pop(spisok_imen[tabel_num - 1])
        spisok_imen.pop(tabel_num - 1)
        spisok_vozrastov.pop(tabel_num - 1)
        spisok_doljnostei.pop(tabel_num - 1)
        vsego_sotrudnikov -= 1
        scetchik = 0
        for i in spisok_imen:
            spisok_sotrudnikov[i] = scetchik
            scetchik += 1
        for i in range(0, vsego_sotrudnikov):
            file.write('%s %s %s\n' % (spisok_imen[i], spisok_doljnostei[i], str(spisok_vozrastov[i])))
        file.close()
    elif perekluch == 5:                                                                           #полная очистка данных по сотрудникам
        perekluch = int(input('Vi uvereni chto hotite ochistit spisok sotrudnikov? 1 - da 2 - net\n'))
        if perekluch == 2:
            print('Spisok ostalsya bez izmeneniy')
        if perekluch == 1:
            password = int(input('vvedite poral administratora\n'))
            if password == 777:
                spisok_vozrastov = []
                spisok_doljnostei = []
                spisok_sotrudnikov = {}
                spisok_imen = []
                vsego_sotrudnikov = 0
                file = open('Spisok_sotrudnikov.txt', 'w')
                file.close()
                print('Dannie po vsem sotrudnikam udaleni')
    elif perekluch == 6:                                                                           #создание backup
        perekluch = int(input('Vi hotite sdelat backup? 1 - da 2 - net\n'))
        if perekluch == 1:
            file = open('Spisok_sotrudnikov.txt', 'r').read()
            file2 = open('Spisok_sotrudnikov_backup.txt', 'w')
            file2.write(file)
            file2.close()
            print('backup sozdan/obnovlen')
        elif perekluch == 2:
            print('backup ne sozdan/obnovlen')
    elif perekluch == 7:                                                                           #восстановление из backup
            perekluch = int(input('Vi hotite vosstanovit dannie is backupa? 1 - da 2 - net\n'))
            if perekluch == 1:
                password = int(input('Vvedite parol administratora\n'))
                if password == 777:
                    file = open('Spisok_sotrudnikov_backup.txt', 'r').read()
                    file2 = open('Spisok_sotrudnikov.txt', 'w')
                    file2.write(file)
                    file2.close()
                    ret_cube = zapolnit_dannie(file)
                    spisok_imen = ret_cube[0]
                    spisok_doljnostei = ret_cube[1]
                    spisok_vozrastov = ret_cube[2]
                    spisok_sotrudnikov = ret_cube[3]
                    vsego_sotrudnikov = ret_cube[4]
                    print('dannie skopirovani iz backupa')
                else:
                    print('parol ne vernie')
            else:
                print('dannie iz backupa ne skopirivani')
    elif perekluch == 9:                                                                           #вывод подсказки
        print('''1 - vivesti spisok imen
2 - vivesti dannie po sotrudniku
3 - vnesti novih sotrudnikov
4 - udalit sotrudnika po tabelnomu nomeru
5 - udalit vseh
6 - sdelat backup
7 - vosstanovit is backupa
9 - vivesti spisok deystvie
0 - vihod\n''')
