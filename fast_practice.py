import requests


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург',
    'Какабург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    url = make_url(city)
    try:
        response = requests.get(url, params = make_parameters())
    except requests.ConnectionEroor:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
