print('%.2f' % 1.2345)
print('%.2f %s' % (1.2345, 99))
print('%s' % 1.23)
print('%s' % (1.23,))
print('%s' % ((1.23,)))
print('{0:.2f}'.format(1.2345))
print('{0:2f} {1}'.format(1.2345, 99))
print('{0}'.format(1.23))
print('{0}'.format((1.23,)))
print('\n' * 3)
print('%(num)i = %(title)s' % dict(num = 7, title ='Strings'))
print('{num:d} = {title:s}'.format(num = 7, title = 'Strings'))
print('{num} = {title}'.format(**dict(num = 7, title = 'Strings')))
L = ['bebe', 'fefu', 'format']
print(''.join(L))

S = 'u'
print('\n', ord(S), chr(ord(S)))
S = 's,pa,m'
print(S[0] + S[2:4] + S[-1] )
print(S.replace(',', ''))
print(''.join(S.split(',')))
S = 'a\nb\x1f\000d'
print(len(S))
for i in S:
    print(ord(i), 'symbol')
