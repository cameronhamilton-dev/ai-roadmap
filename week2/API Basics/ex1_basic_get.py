import requests

r=requests.get('https://httpbin.org/get')

print('Raw response text:\n', r.text)