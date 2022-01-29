a = 'ku ku'
b = 777
c = 'John Machael Bendis'
print(a, b, c, '\n')
input('zagruzka modulya i vivod na ekran teh je peremennih\n')
exec(open('modul1.py').read())
print(a, b, c)
