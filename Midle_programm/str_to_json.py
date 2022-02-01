import json
import re
from xml.dom.minidom import Element


def table_title(title_string):
    title = title_string[1:-1].split('","')
    return title


def table_data(data_string):
    data_list = re.split('","|",|,"|L,', data_string)
# Для products_data_all убрать запятую
    for element in data_list:
        if element == 'NUL':
            data_list.insert(data_list.index(element), 'NULL')
            data_list.remove(element)
    return data_list


string_count = 1
string_dict = {}
json_list = []
f_string = open(r'F:\Programming\Code\traning\products_data_all.txt',
                encoding='utf-8').read()
string_list = f_string.split('\n')
structure = table_title(string_list[0])
string_list.pop(0)
for string in string_list:
    data_list = table_data(string[:-1])
# Для products_data_all добавить [:-1]
    string_count += 1
    for column in range(0, len(structure)):
        try:
            string_dict[structure[column]] = data_list[column]
        except IndexError:
            print('Строка N=', string_count, ' не преобразуется\n', string)
    json_string = json.dumps(string_dict, ensure_ascii=False)
    json_list.append(json_string)
    string_dict = {}
json_strings = '[' + ',\n'.join(json_list) + ']'
json_file = open(r'F:\Programming\Code\traning\file.json',
                 'w', encoding='utf-8')
json_file.write(json_strings)
json_file.close()
print('Преобразование выполнено успешно')
