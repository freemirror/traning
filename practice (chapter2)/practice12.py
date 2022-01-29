S = 'bugaresh'
S = S[:3] + 'ururur' + S[-3:]
print(S)
S = 'bugaresh'
S = S.replace('ar', 'irm')
print(S)
st = 'aa$bb$cc$dd$'.replace('$', 'SPAM')
print(st)
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')                                                          #.find возвращает -1 если строка не найдена
print(where)
S = S[:where] + 'EGGS' + S[(where + 4):]
print(S)
S = 'xxxxSPAMxxxxSPAMxxxx'
S = S.replace('SPAM', 'EGGS', 1)
print(S)
S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'x'
S = ''.join(L)                                                                  #Собрать строку из списка по пустому разделителю
print(S)
S = '\n'.join(L)
print(S)
S = '_'.join(L)
print(S)
S = 'xxxxSPAMxxxxSPAMxxxx'
if 'xxxx' in S:
    print('Hurray')
print(help(S.upper))

L = ['bob', 'dilan', 'harper', 'mike', 'shanin', 'Jorge', 'pipe', 'gordon']
N = [1, 2, 3, 4, 5, 6, 7, 8]
S =''
for i in range(len(N)):
    S = S + 'Person named %s is %s driver\n' % (L[i], N[i] )
print(S)
bob='fet'
geg='michel'
print('boba %(bob)s and gorge %(geg)s make a love' % vars())
D = {'john':1, 'kino':2}
print('mister %(john)s and master %(kino)s' % D)
