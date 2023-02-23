import requests
def pog():
    try:
        city = input('Введите город: ')
    except Exception as e:
        print("Exception (find):", e)
        pass

    api_url ="http://api.openweathermap.org/data/2.5/weather"
    parametr = { "q":[city],
             "units" : "metric",
            "appid":"aa2e2c84ed4a53a0941701439de11f0b"
    }

    res = requests.get(api_url, params = parametr)
    d = res.json()
    print(f'Температура в {city} равна {d["main"]["temp"]} градусов, '
    f'по ощущениям  {d["main"]["feels_like"]}, '
    f'скорость ветра {d["wind"]["speed"]} м/с, '
    f'Облачность,{d["clouds"]["all"]}%  '
      )
    x = input("для закрытия введите exit, для повтора yes :")
    if x == 'yes':
        pog()

pog()
