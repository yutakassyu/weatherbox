# coding:utf-8
import requests
import json
import sys
import os
import datetime

API_KEY = "34620c3e89f3be422ee406ec1daed0a1"
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

city_name = "Minato"
url = api.format(city = city_name, key = API_KEY)
print(url)
response = requests.get(url)
data = json.loads(response.text)

#weather  MAC made
for key in data['weather']:
    print(type(key))
    wthr = key['main']
    print(wthr)     

