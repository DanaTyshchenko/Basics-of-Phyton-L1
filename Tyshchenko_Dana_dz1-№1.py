#Задание №1
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

duration = int(input('Введите число'))

days = duration // seconds_in_day
duration = duration - (days * seconds_in_day)

hours = duration // seconds_in_hour
duration = duration - (hours * seconds_in_hour)

minutes = duration // seconds_in_minute
duration = duration - (minutes * seconds_in_minute)

print (days,'дней', hours,'часов', minutes,'минут', duration, 'секунд')

