str_file_all = open(r'C:\py_project\file_practice\ruch_file.txt', encoding='utf8').read()
print(str_file_all, '\n\n\n\n')
str_file_300 = open(r'C:\py_project\file_practice\ruch_file.txt', encoding='utf8').read(300)
print(str_file_300, '\n\n\n\n')
file_r = open(r'C:\py_project\file_practice\ruch_file.txt', encoding='utf8')
str12 = file_r.readline()
L = file_r.readlines()
print(L[3:8],'\n\n\n\n', str12)
str = 'gobot lyubit gabot'
file = open(r'C:\py_project\file_practice\file1.txt', 'w')
file.write(str)
file.writelines(L[:8])
file.close()
for line in open(r'C:\py_project\file_practice\ruch_file2.txt', encoding='utf8'):
    L.append(line)
print('\n\n\n', L)
print('\n\n\n', open(r'C:\py_project\file_practice\file1.txt').read())