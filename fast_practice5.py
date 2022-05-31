import requests

PRACTICUM_TOKEN = 'AQAAAAAMoyM-AAYckZZN_vwEd09wuUrxSj8Nric'
ENDPOINT = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
HEADERS = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}

timestamp = 1651363200
params = {'from_date': timestamp}

response = requests.get(ENDPOINT, headers=HEADERS, params=params).json()
print(response)
