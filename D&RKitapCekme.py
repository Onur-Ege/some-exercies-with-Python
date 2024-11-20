from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://www.dr.com.tr/"

driver.get(url)
time.sleep(2)
driver.maximize_window()
book = driver.find_element(By.CSS_SELECTOR,"body > div.site-container > header > div.site-header-bottom.text-c255.d-none.d-lg-block > div.site-menu.container > ul > li:nth-child(1) > a")
book.click()
time.sleep(2)

find_book = driver.find_element(By.CSS_SELECTOR,"body > div.site-container > header > div.site-header-center.bg-c255.py-10 > div > div > div.search.col-12.col-lg-7.mt-10.mt-lg-0.dr-flex > div.search-wrapper.col-12.col-lg-10.p-0 > input")
find_book.send_keys("şiir")
find_book.send_keys(Keys.ENTER)
time.sleep(3)

for i in range(1,11):

    name = driver.find_element(By.XPATH,"//div[{}]/div/div[3]/div[1]/div[2]/h3[1]".format(i))
    name = name.text

    author = driver.find_element(By.XPATH,"//div[{}]/div/div[3]/div[1]/div[2]/h3[2]".format(i))
    author = author.text

    print(name + " - " + author)

driver.close()