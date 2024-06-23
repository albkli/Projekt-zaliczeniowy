import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


# Konfiguracja Selenium z lokalnym chromedriver.exe
driver = webdriver.Chrome()
timesleep= 100
driver.get('https://www.wakacje.pl/wczasy/?src=fromSearch')

# Wyszukiwanie państwa (dostosuj do rzeczywistej strony)
accept = driver.find_element("xpath", "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")
accept.click()
driver.implicitly_wait(10)

search_place = driver.find_element("xpath", "//*[@id='__next']/div[2]/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input")
search_place.click()
driver.implicitly_wait(10)

searchbox = driver.find_element("xpath", "/html/body/div[7]/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/input")
searchbox.send_keys("Hiszpania")
driver.implicitly_wait(10)

picked_country = driver.find_element("xpath", "/html/body/div[7]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/ul[1]/li[2]/label/div")
picked_country.click()

go_search = driver.find_element("xpath", "/html/body/div[7]/div/div[1]/div[2]/footer/button")
go_search.click()

sort_option = driver.find_element("xpath", "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/span")
sort_option.click()

sort_option = driver.find_element("xpath", "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div[1]/span")
sort_option.click()

time.sleep(500)
# search_box = driver.find_element('id', "__next")
# search_box.send_keys("Francja")
# search_box.send_keys(Keys.RETURN)
