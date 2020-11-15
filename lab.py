import requests
import json

url = 'http://127.0.0.1:8080'
print('Get with tz', requests.get(url + '/Asia/Seoul').text)
print('Get without tz', requests.get(url).text)
print('Get with wrong tz', requests.get(url + '/M').text, '\n')

data = {'type': 'time', 'tz': 'Asia/Seoul'}
print('Post with wrong json: ', requests.post(url = url, data = data).text)
print('Time with tz: ', requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'time'}
print('Time without tz: ', requests.post(url = url, data = json.dumps(data)).text, '\n')

data = {'type': 'date', 'tz': 'Asia/Seoul'}
print('Date with tz: ', requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'date'}
print('Date without tz: ', requests.post(url = url, data = json.dumps(data)).text, '\n')

data = {'type': 'datediff', 'start': 'Europe/Moscow', 'end': 'Asia/Seoul'}
print('Difference between two dates\t' + requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'datediff', 'start': 'Asia/Seoul', 'end': 'Europe/Moscow'}
print('Difference between two dates (reverse)\t' + requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'datediff', 'end': 'Asia/Singapore'}
print('Difference between server and tz\t' + requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'datediff', 'start': 'Asia/Singapore'}
print('Difference between tz and server\t' + requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'datediff'}
print('Difference between same server tz\t' + requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'datediff', 'start': 'Asia/Singapore', 'end': 'Asia/Seoul'}
print('Difference between two dates\t' + requests.post(url = url, data = json.dumps(data)).text)
data = {'type': 'datediff', 'start': 'Asia/Seoul', 'end': 'Asia/Singapore'}
print('Difference between two dates (reverse)\t' + requests.post(url = url, data = json.dumps(data)).text)
