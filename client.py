import requests
import threading
from time import sleep

url = 'http://localhost:6000/100MB.bin'
headers = {}

# Retry logic for robustness
def req():
    try:
        res = requests.get(url, headers=headers, timeout=10)
        print(f"Response Code: {res.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

for i in range(30):
    threading.Thread(target=req).start()
    sleep(1)