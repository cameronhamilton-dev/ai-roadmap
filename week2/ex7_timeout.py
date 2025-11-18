import requests

url = "https://httpbin.org/delay/10"  # This endpoint waits 10 seconds

try:
    # We only allow a max wait of 3 seconds
    r = requests.get(url, timeout=3)
    print(r.json())

except requests.exceptions.Timeout:
    print("The request timed out!")

except Exception as e:
    print("Some other error occurred:", e)
