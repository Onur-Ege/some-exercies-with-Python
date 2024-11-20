from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

pcKullaniciİsmi = ""

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir=C:/Users/{pcKullaniciİsmi}/AppData/Local/Google/Chrome/User Data")
options.add_argument("profile-directory=Profile 1")

def takipcileriCek(kullaniciAdi):

    driver = webdriver.Chrome(options=options)
    url = "https://www.instagram.com/{}/followers/".format(kullaniciAdi)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    followers_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/followers/"]')))
    followers_link.click()
    time.sleep(3)

    takipciListesi = []
    takip = driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]").find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")
    time.sleep(3)

    for i in takip:
        takipciListesi.append(i.text)

    height = driver.execute_script("return document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollHeight;")

    while True:
        driver.execute_script("document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollTo(0,document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollHeight)")

        time.sleep(3)
        yeniliste = driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]").find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")

        for i in yeniliste:
            x = i.text

            if x not in takipciListesi:
                takipciListesi.append(x)

        newHeight = driver.execute_script("return document.querySelector('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6').scrollHeight")

        if height == newHeight:
            break

        height = newHeight

    time.sleep(3)
    driver.close()

    with open ("takip.txt", 'r') as file:
        oldFollowers = [line.strip() for line in file.readlines()]

    yeniler = [eleman for eleman in takipciListesi if eleman not in oldFollowers]

    with open("yeniler.txt", 'w') as file:
        for eleman in yeniler:
            file.write(eleman+'\n')

    with open("takip.txt", 'w') as file:
        for i in takipciListesi:
            file.write(i+"\n")

username = ""
takipcileriCek(username)

