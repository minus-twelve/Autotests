import requests
s_city = "Moscow,RU"
city_id = 524901
appid = "aa2e2c84ed4a53a0941701439de11f0b"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
        print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
except Exception as e:
    print("Exception (forecast):", e)
    pass
