import decimal
import fractions
z = decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')
y = 0.1 + 0.1 + 0.1 - 0.3
print(z, y)
z = decimal.Decimal(1) / decimal.Decimal(7)
print(z)
decimal.getcontext().prec = 4                                                   #ограничение на вывод до 4ех цифр после точки
z = decimal.Decimal(1) / decimal.Decimal(7)
print(z, '\n\n\n\n\n')

z = decimal.Decimal(1) / decimal.Decimal(7)
print(z)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    z = decimal.Decimal(1) / decimal.Decimal(7)
    print(z)
z = decimal.Decimal(1) / decimal.Decimal(7)
print(z)

x = fractions.Fraction(1,3)
print('\n\n\n', x)
y = fractions.Fraction(10,15)
print(y)
print(x + y, '\n', x * y)
z = fractions.Fraction(0.25)
print(z)
print(fractions.Fraction('0.25') + fractions.Fraction('1.25'))

print((2.5).as_integer_ratio())                                                 #преобразование в  дробь
f = 3.33
z = fractions.Fraction(*f.as_integer_ratio())
print(z, float(z))
print(fractions.Fraction.from_float(1.75))
a = fractions.Fraction(22517998136852479, 13510798882111488)                    #упрощение до ближайшей дроби
print(a)
print(a.limit_denominator(10))
a = {523, 234, 23428, 2342, 'tre'}
print(a)
