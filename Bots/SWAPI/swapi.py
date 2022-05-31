import requests
from pprint import pprint


response = requests.get('https://www.swapi.tech/api/planets/1/')
pprint(response.json())
print(response.json().get('result').get('properties').get('diameter'))

