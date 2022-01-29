import os

def preobrazovanie_texta(file_directory, file_name):
    delete_list = []
    num = 0
    words = ''
    sign = '( ) [ ] { } , = . * № / \\ 1 2 3 4 5 6 7 8 9 0 - _ \n < > ! ? ; : " ' + chr(8211) + ' ' + chr(187) + ' ' + chr(171) + ' ' + chr(8230) + ' ' + chr(8222) + ' ' + chr(8220) + ' ' + chr(8217) + ' ' + chr(8212)
    sign_list = sign.split(' ')
    file = open_file(file_directory)
    file = file.lower()
    book_sign_list = list(file)
    for i in book_sign_list:
        if i in sign_list:
            book_sign_list[num] = ' '
            if num == 0 and book_sign_list[num] == ' ':
                delete_list.append(0)
        if num > 0:
            if book_sign_list[num] == ' ' and book_sign_list[num - 1] == ' ':
                delete_list.append(num)
        num += 1
    delete_list.reverse()
    for i in delete_list:
        if i == 0:
            book_sign_list.pop(i)
        else:
            book_sign_list.pop(i-1)
    words = words.join(book_sign_list)
    file = open('obrabotannie_knigi//' + 'temp_' + file_name + '.txt', 'w')
    file.write(words)
    file.close()
    words = words.split(' ')
    if words.count('') > 0:
        words.pop(words.index(''))
    raznie_slova = set(words)
    print('Количество уникальных слов = ', len(raznie_slova), '\nВсего слов = ',len(words))
    print('Первоначальный файл обработан\n')
    return words

def vivod_top_10 (words, text_name):
    result_list = []
    min_words_length = int(input('Vvedite minimalnoe kolichestvo znakov dlya slov\n'))
    print('Идет подсчет слов')
    unik_words = list(set(words))
    num = 0
    for i in unik_words:
        if min_words_length > len(i):
            unik_words[num] = '0'
        num += 1
    unik_words = list(set(unik_words))
    unik_words.pop(unik_words.index('0'))
    for i in range(len(unik_words)):
        result_list.append([words.count(unik_words[i]), unik_words[i]])
    result_list.sort()
    result_list.reverse()
    num = 0
    print('10 самых часто упоминаемых слов в файле ',text_name + '.txt\n')
    for i in result_list[:10]:
        num += 1
        print(num, ') ', i)
    return

def open_file (file_name):
    try:
        file = open(file_name, 'r', encoding='utf-8').read()
    except:
        file = open(file_name, 'r').read()
    return file

def vibor_texta ():
    while True:
        textfile_name = input('Введите название файла(книги)\t поддерживается только формат ".txt"\n')
        directory_textfile_original = 'knigi_original//' + textfile_name + '.txt'
        directory_textfile_temp = 'obrabotannie_knigi//' + 'temp_' + textfile_name +'.txt'
        words = ''
        check_file = os.path.exists(directory_textfile_original)
        if check_file == True:
            check_temp = os.path.exists(directory_textfile_temp)
            if check_temp == True:
                input_case = int(input('Обнаружен обработанный файл, желаете продолжить работу с ним или запустить обработку заного?\n В случае если исходный файл изменялся (обработка может занимать длительное время)\n 1 - продолжить, любой другой ввод - обработать\n'))
                if input_case == 1:
                    words = open_file(directory_textfile_temp)
                    words = words.split(' ')
                    raznie_slova = set(words)
                    print('Количество уникальных слов = ', len(raznie_slova), '\nВсего слов = ',len(words))
                else:
                    print('Идет обработка файла')
                    words = preobrazovanie_texta(directory_textfile_original, textfile_name)
            else:
                print('Идет обработка файла')
                words = preobrazovanie_texta(directory_textfile_original, textfile_name)
            break
        else:
            print('Введено некорректное имя файла')
    print('Файл загружен')
    return words, textfile_name

def ochistka_temp():
    directori = r'C:\py_project\bolshie_programmi\razbor_knig\obrabotannie_knigi\\'
    filelist = os.listdir(directori)
    if filelist == []:
        print('Временные файлы отсутсвуют')
    else:
        print('В данный момент существуют следующие временные файлы:')
        for i in range(len(filelist)):
            print(i + 1, ') ', filelist[i])
        input_case = int(input('Удалить все временные фалы? - 1\n Удалить конкретный файл - 2\n Вернуться в прошлое меню - 0\n'))
        if input_case == 1:
            for i in range(len(filelist)):
                os.remove(directori + filelist[i-1])
            print('Временные файлы удалены')
        elif input_case == 2:
            delete_temp_file = int(input('Введите номер файла по списку для удаления\n'))
            os.remove(directori + filelist[delete_temp_file - 1])
    return

def word_freq(words, current_text):
    while True:
        search_word = input('Введите слово для определения его частоты встречи в тексте\n Для выхода из цикла введите "stop"\n')
        if search_word == 'stop':
            break
        print('Слово ' + search_word + ' встречается в тексте ' + current_text + ' ' + str(words.count(search_word)) +' раз(а)')
    return

def books_output():
    directori = r'C:\py_project\bolshie_programmi\razbor_knig\knigi_original\\'
    filelist = os.listdir(directori)
    print(filelist)
    return

print('*' * 10 + '\tАнализатор текста\t' + '*' * 10)
menu_text = '''1) Выбрать новый файл для дальнейшей работы
2) Вывести 10 самых упоминаемых слов из выбранного текста
3) Найти частоту упоминания слова в тексте
4) Очистить темп/ конкретные файлы
5) Анализ текста на новые знаки и вывод в отдельный файл
6) Вывод списка книг
0) Завершить работу программы '''
while True:
    input_menu = int(input('Вывести на экран меню 1 - да\n'))
    if input_menu == 1:
        print(menu_text)
    input_case = int(input('Выберите действие\n'))
    if input_case == 0:
        break
    elif input_case == 1:
        words, current_text = vibor_texta()
    elif input_case == 2:
        vivod_top_10(words, current_text)
    elif input_case == 3:
        word_freq (words, current_text)
    elif input_case == 4:
        ochistka_temp()
    elif input_case == 6:
        books_output()
