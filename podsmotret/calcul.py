print('\t\t\t Калькулятор', '*'*60)
print("Для выхода из программы введите 'q'")
import winsound
Freq = 1000
Dur = 500
while True:
    sym = input('Введите знак\n')
    if sym == "q":
        break
    if sym in ('+','-','*','/'):
        x = float(input("Введите первое число:\n"))
        y = float(input("Второе число первое число:\n"))
        if sym == '+':
            print('Сумма равна ', x + y)
        elif sym == '-':
            print('Разность равна ', x - y )
        elif sym == '*':
            print('Произведение равно ', x * y)
        elif sym == '/':
            if y == 0:
                winsound.Beep(Freq,Dur)
                print('Делить на 0 нельзя\n')
            else:
                print('Частное равно ', "%.2f" % (x / y))
    else:
        winsound.Beep(Freq,Dur)
        print('Неверный знак операции')
