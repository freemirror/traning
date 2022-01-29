import random
a = 1
while a:
    players = []
    rand_player = 0
    i = 0
    numb_players = int(input('Сколько игроков будут играть?\n'))
    for i in range(numb_players):
        print('Введите имя игрока № ', i + 1)
        players.append(input())
        i += 1
    i = 0
    print('Сегодня будут играть')
    for i in range(numb_players):
        print(players[i])
        i += 1
    rand_player = random.choice(range(len(players)-1))
    selfkiller = players[rand_player]
    print('Первый ход за ', selfkiller)
    run = 1
    cylinder = [0,0,0,0,0,0]
    while run:
        print(cylinder)
        c = 1
        while c:
            hole = int(input('В какое отверстие засунуть патрон? (1-6)\n'))-1
            if cylinder[hole] == 1:
                print('Смотри внимательнее тут уже есть патрон')
            else:
                cylinder[hole] = 1
                c = 0
                hole = 0
        print('Барабан вращается')
        hole = random.choice(range(len(cylinder)-1))
        print('Боек боет по ', hole + 1, ' отверстию'   )
        if cylinder[hole] == 1:
            print('Пиф-Паф ', selfkiller, 'умер')
            run = 0
        else:
            hole = 0
            if rand_player + 1 < numb_players:
                selfkiller = players[rand_player + 1]
                print('Следующий игрок \n', selfkiller)
                rand_player+=1
            else:
                selfkiller = players[0]
                print('Следующий игрок\n ', selfkiller)
    a = int(input('Желаете продолжить (1-Да, 0-Нет)\n'))
