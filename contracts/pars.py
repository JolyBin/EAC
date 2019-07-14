import requests
import json

test_data = '2724163941'
link = 'https://api-fns.ru/api/egr'
key = '5b633604ab57bc8bc4257f26e6113ada226f3087'
params = {'req': test_data, 'key': key}

response = requests.get(f'https://api-fns.ru/api/egr', params=params).json()
print(response)