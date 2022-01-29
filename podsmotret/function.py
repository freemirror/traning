def summa(num1, num2):
    num3 = num1 + num2
    return num3

def compos(num1, num2):
    num3 = num1 * num2
    return num3

def exponent(num1, num2):
    num3 = num1 ** num2
    return num3

x1 = int(input('vvedite pervoe chislo\n'))
x2 = int(input('Vvedite vtoroe chislo\n'))
x3 = summa(x1, x2)
x4 = compos(x1, x2)
x5 = exponent(x1, x2)
print('\n', x3, '\t', x4, '\t', x5)
