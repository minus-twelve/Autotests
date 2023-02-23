import requests
s_city = "Moscow,RU"
city_id = 524901
appid = "aa2e2c84ed4a53a0941701439de11f0b"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Обстановка:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass
