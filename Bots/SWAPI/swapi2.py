from pprint import pprint

import requests

characters = []
response = requests.get('https://www.swapi.tech/api/people/?name=luke')
response = response.json()
pprint(response)
