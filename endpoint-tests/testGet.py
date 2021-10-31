import requests

r = requests.get("https://us-central1-tsa-buses.cloudfunctions.net/testGet")
print(r.text)