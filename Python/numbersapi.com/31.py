import requests

res = requests.get("http://numbersapi.com/31/math?json=true")
data = res.json()
print(data['found'])
