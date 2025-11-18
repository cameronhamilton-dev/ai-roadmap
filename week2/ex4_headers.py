import requests

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "CameronAI-Training/1.0",
    "X-Client": "LearningAPIs"
}

r = requests.get(url, headers=headers)

print("Server saw these headers:")
print(r.json()["headers"])
