dist = 0                    #Длинна маршрута
total_time = 0              #Общее время пути
stop_time = 0               #Время коротких остановок
meal_time = 0               #Время остановок на прием пищи
sleep_time = 0              #Временя на остановки для сна
refueling_time = 0          #Время на заправку
average_speed = 0           #Средняя скорость
consumption_gas = 0         #Расход бензина на 100 киометров
tank_capasity = 0           #Емкость бака
gas_cost = 0                #Стоимость литра бензина
freq_stop = 0               #Количество коротких остановок в день
freq_meal = 0               #Количество остановок на прием пищи в день
fuel_in_tank = 0            #Текущее количество бензина
#time = 0                    #Расчетное время
refueling_stop = 0          #Количество остановок на заправку
day_dist = 0                #Расстояние в день
gas_cash = 0                #Стоимость бензина на всю поездку

print('*'*80,"\n\t\t\t Программа путевой компьютер\n")
dist = float(input('Введите общее расстояние до цели в километрах\n'))
gas_cost = float(input('Введите стоимость листра бензина\n'))
consumption_gas = float(input('Введите средний расход бензина на 100 километров\n'))
tank_capasity = float(input('Введите емкость бака автомобиля в литрах\n'))
freq_stop = float(input('Введите количество в день коротких остановок\n'))
freq_meal = int(input('Введите количество остановок в день на прием пищи\n'))
stop_time = float(input('Введите время коротких остановок в минутах\n'))
meal_time = float(input('Введите время остановок на прием пищи в минутах\n'))
sleep_time = float(input('Введите время остановок на сон в часах\n'))*60
refueling_time = float(input('Введите время остановок на дозаправку в минутах\n'))
average_speed = float(input('Введите среднюю скорость движения в километрах в час\n'))
fuel_in_tank = float(input('Введите текущее количество бензина\n'))

while True:
    while True:
        day_dist = (24 * 60 - freq_meal* meal_time - sleep_time - stop_time * freq_stop - refueling_stop * refueling_time) * average_speed
        x = day_dist - x
        if fuel_in_tank < x / consumption_gas:
            refueling_stop =+ 1
            x = x - fuel_in_tank * 100 / consumption_gas
            fuel_in_tank = tank_capasity
        else:
            break
            gas_cash = day_dist
    x = 0
    if dist / average_speed > (dist / average_speed - freq_meal * meal_time - freq_stop * stop_time - sleep_time - refueling_stop * refueling_time):

    else:
        break
