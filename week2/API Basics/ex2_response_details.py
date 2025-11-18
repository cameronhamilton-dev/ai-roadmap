import requests

r = requests.get("https://httpbin.org/get")

print("Status code:", r.status_code)
print("Final URL:", r.url)
print("Response headers:", r.headers)
print("JSON body:", r.json())
