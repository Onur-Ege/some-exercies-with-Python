import requests
from bs4 import BeautifulSoup

for i in range(1,11):

    link = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={}".format(i)
    data = BeautifulSoup(requests.get(link).content,"html.parser")

    products = data.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("div",{"class":"product-list product-list--list-page"})

    for product in products:
        name = product.find("a",{"class":"product-list-link"}).find("div",{"class":"product-list__content"})\
        .find("div",{"class":"product-list__product-name"}).find("h3").string

        price = product.find("a",{"class":"product-list-link"}).find("div",{"class":"product-list__content"})\
        .find("div",{"class":"product-list__cost"}).find("div",{"class":"productList-camp"}).find("span",{"class":"product-list__price"}).string

        print(f"Telefon Modeli: {name}\nFiyat: {price}\n")
