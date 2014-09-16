import requests
import json

URL = 'https://api.datamarket.azure.com/Bing/Search/v1/Web?$format=json'
API_KEY = 'SECRET_API_KEY'

def request(query):
    r = requests.get(URL, auth=('', API_KEY), params={'Query':'\'' + query + '\''})
    return r.json()['d']['results']
