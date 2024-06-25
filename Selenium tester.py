import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


country = input("Jakie państwo?")

# Konfiguracja Selenium z lokalnym chromedriver.exe
driver = webdriver.Chrome()
driver.get('https://www.wakacje.pl/wczasy/?src=fromSearch')
wait = WebDriverWait(driver, 10)
# Wyszukiwanie państwa
accept = driver.find_element("xpath", "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")
accept.click()
driver.implicitly_wait(10)

search_place = driver.find_element("xpath", "//*[@id='__next']/div[2]/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input")
search_place.click()
driver.implicitly_wait(10)

searchbox = driver.find_element(By.CLASS_NAME, "sc-hxqEdz")
searchbox.send_keys(country)
time.sleep(1)

picked_country = driver.find_element(By.CLASS_NAME, "sc-1slvi5p-2")
picked_country.click()

go_search = driver.find_element("xpath", "/html/body/div[7]/div/div[1]/div[2]/footer/button")
go_search.click()
driver.implicitly_wait(10)

sorting_option = driver.find_element("xpath", "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div")
sorting_option.click()
driver.implicitly_wait(10)

sorting_lowest_price = driver.find_element("xpath", "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]")
sorting_lowest_price.click()


try:
    wait = WebDriverWait(driver, 10)
    place = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[1]/span")))
    place = place.text

    hotel_name = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[2]/div/h4")))
    hotel_name = hotel_name.text

    date = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[1]/span[2]")))
    date = date.text

    acces = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[2]/span[2]")))
    acces = acces.text

    food = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[3]/span[2]")))
    food = food.text

    agency = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[4]/span[2]")))
    agency = agency.text

    price = wait.until((EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[3]/div/div[2]/div/div/h4"))))
    price = price.text

    place_list = place.split()
except NoSuchElementException:
    place_list = [0, 0, 0, 10000]
except TimeoutException:
    place_list = [0, 0, 0, 10000]

print('Miejsce:',place)
print("Nazwa hotelu:", hotel_name)
print('Data wyjazdu i powrotu:',date)
print("Wylot/dojazd własny:", acces)
print("Wyżywienie:", food)
print("Biuro podróży:", agency)

print("Cena:",
      price)
time.sleep(500)
