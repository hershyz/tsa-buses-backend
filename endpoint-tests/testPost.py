import requests

payload = {
    "name": "hershey"
}

r = requests.post("https://us-central1-tsa-buses.cloudfunctions.net/testPost", params=payload)
print(r.text)