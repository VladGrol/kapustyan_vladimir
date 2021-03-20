duration = int(input('Введите продолжительность в секундах: '))
months = duration // 267840
days = (duration - months *267840) // 8640
hours = (duration - months *267840 - days*8640) // 360
minutes = (duration - months *267840 - days*8640 - 360*hours)//60
seconds = (duration - months *267840 - days*8640 - 360*hours - 60*minutes)
if duration < 60:
    print(seconds, 'сек')
elif duration >=60 and duration <360:
    print(minutes, 'мин', seconds, 'сек')
elif duration >= 360 and duration < 8640:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
elif duration >= 8640 and duration < 267840:
    print(days, 'суток', hours, 'час', minutes, 'мин', seconds, 'сек')
elif duration >=267840:
    print('лень')