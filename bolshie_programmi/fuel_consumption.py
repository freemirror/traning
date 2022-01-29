stop_time = 15               #Время коротких остановок
meal_time = 30               #Время остановок на прием пищи
sleep_time = 600              #Временя на остановки для сна
refueling_time = 20          #Время на заправку
average_speed = 90           #Средняя скорость
consumption_gas = 8/100        #Расход бензина перерасчет на 1 км
tank_capasity = 65          #Емкость бака
gas_cost = 45                #Стоимость литра бензина
freq_stop = 3               #Количество коротких остановок в день
freq_meal = 2              #Количество остановок на прием пищи в день
fuel_in_tank = 40            #Текущее количество бензина
#time = 0                    #Расчетное время
refueling_stop = 0          #Количество остановок на заправку
day_dist = 0                #Расстояние в день
gas_cash = 0                #Стоимость бензина на всю поездку
x = 0

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
