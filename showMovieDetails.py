import sys
import requests
import json
import re

apikey = "e4051cbb"

def control(nameOrId):
    if re.search("[^1-3]",nameOrId):
        raise Exception("Lütfen 1 ve 3 arasında bir sayı giriniz:")


while True:

    try:
        nameOrId = input("isimle arama yapmak istiyorsanız 1i IMDB Id ile arama yapmak istiyorsanız 2i  çıkış yapmak istiyorsanız 3ü seçiniz: ")
        control(nameOrId)
    except Exception as hata:
        print(hata)
        continue

    if nameOrId == "1" :

        try:
            name = input("lütfen bilgilerini öğrenmek istediğiniz filmin ismini giriniz:")
            adress = "http://www.omdbapi.com/?apikey={}&t={}".format(apikey,name)
            connection = requests.get(adress)
            response = connection.json()
            print("Title : {} \nIMDB Id : {}\nReleased : {}\nRuntime : {}\nGenre : {}\nDirector : {}\nActors : {}\n".format(response["Title"],response["imdbID"],response["Released"],response["Runtime"],response["Genre"],response["Director"],response["Actors"]))
        except KeyError:
            print("lütfen film ismini doğru giriniz")
            continue

    elif nameOrId == "2" :
        try:
            id = input("lütfen bilgilerini öğrenmek istediğiniz filmin imdb idsini giriniz: ")
            adress = "http://www.omdbapi.com/?apikey={}&i={}".format(apikey,id)
            connection = requests.get(adress)
            response = connection.json()
            print("Title : {} \nIMDB Id : {}\nReleased : {}\nRuntime : {}\nGenre : {}\nDirector : {}\nActors : {}\n".format(response["Title"],response["imdbID"], response["Released"], response["Runtime"], response["Genre"], response["Director"],response["Actors"]))
        except Exception:
            print("lütfen geçerli id giriniz")
            continue

    elif nameOrId == "3":
        sys.exit(0)

