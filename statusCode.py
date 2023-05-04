import requests

url = "http://localhost:3002/"

response = requests.get(url)

if response.status_code == 200:
    print("Basic Test Pass and Website up and running")
else:
    print("Oops, something went wrong. Status code:", response.status_code)
