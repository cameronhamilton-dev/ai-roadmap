import requests

url = "https://httpbin.org/anything"

params = {
    "limit": 5,
    "category": "test"
}

headers = {
    "User-Agent": "CameronAI/3.0",
    "X-Client-ID": "LearningAPIs"
}

payload = {
    "message": "Hello from Cameron",
    "week": 2,
    "status": "learning"
}

try:
    r = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload,
        timeout=5
    )

    r.raise_for_status()

    print("Final URL:", r.url)
    print("\nHeaders the server saw:")
    print(r.json()["headers"])

    print("\nJSON the server received:")
    print(r.json()["json"])

except requests.exceptions.Timeout:
    print("The request timed out!")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except Exception as e:
    print("Other error:", e)
