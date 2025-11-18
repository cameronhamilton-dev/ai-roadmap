import requests

url = "https://httpbin.org/status/404"   # intentionally broken

try:
    r = requests.get(url)
    print("Status code:", r.status_code)

    # THIS will trigger an error for non-200 responses
    r.raise_for_status()

    print("Success:", r.json())

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except Exception as e:
    print("Other error:", e)
