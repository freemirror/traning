nachalnoe_chislo = int(input('С какого числа начать проверку\n'))
konechnoe_chislo = int(input('на каком числе окончить проверку\n'))
num = nachalnoe_chislo
iterac = 0
tisyacha = 0
while num != konechnoe_chislo:
    if nachalnoe_chislo > konechnoe_chislo:
        print('Задан неверный интервал')
        break
    x = num
    for x in range(nachalnoe_chislo, konechnoe_chislo):
        while x != 1:
            if x % 2 != 1:
                x = x // 2
            else:
                x = x * 3 + 1
            iterac += 1
    num += 1
    if num % 1000 == 0:
        tisyacha += 1
        print(tisyacha, ' tisyach provereno')
print(iterac)
