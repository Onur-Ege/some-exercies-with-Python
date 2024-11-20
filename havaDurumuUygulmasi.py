import requests
import json

apikey = "29acb7430de603befdc69b1d8cd6857e"
loopControl = True

while loopControl:

    city = input("Lütfen hava durumunu öğrenmek istediğiniz şehiri giriniz:")
    adresForLatAndLon = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit=5&appid={}".format(city,apikey)

    connection1 = requests.get(adresForLatAndLon)
    adres1 = connection1.json()

    try:
        lat = adres1[0]["lat"]
        lon = adres1[0]["lon"]
    except IndexError:
        print("Lütfen şehir ismini doğru giriniz:")
        continue

    adresForWheather = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&lang=tr&units=metric".format(lat,lon,apikey)

    connection2 = requests.get(adresForWheather)
    adres2 = connection2.json()

    weather = adres2["weather"][0]["description"]
    temperature = adres2["main"]["temp"]
    humidity = adres2["main"]["humidity"]

    print("Weather description: " + weather.title())
    print("Temperature: ",end="")
    print(temperature)
    print("Humidity: ",end="")
    print(humidity)

    loop = input("Devam etmek istemiyorsanız 1'i tuşlayınız .")

    if loop == "1":
        loopControl = False



