import requests

url = "https://httpbin.org/get"

params = {
    "name": "cameron",
    "week": 2
}

r = requests.get(url, params=params)

print("Final URL:", r.url)
print("Args returned by server:", r.json()["args"])
