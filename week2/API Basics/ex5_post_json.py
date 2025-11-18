import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Cameron",
    "goal": "AI Integration Engineer",
    "week": 2
}

r = requests.post(url, json=payload)

print("Server received this JSON:")
print(r.json()["json"])
