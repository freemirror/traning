while True:
    reply = input('Enter text:\n')
    if reply == 'stop':
        break
    try:
        print(int(reply) ** 2)
    except:
        print('Vvedeno ne chislo')
print('bye')

while True:
    reply = input('Enter text:\n')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad kiso!')
    else:
        num = int(reply)
        if num < 20:
            print('Low')
        else:
            print(num ** 2)
print('Bye')
