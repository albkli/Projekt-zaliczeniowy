import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Konfiguracja Selenium z lokalnym chromedriver.exe
driver = webdriver.Chrome()
driver.get('https://www.wakacje.pl/wczasy/?src=fromSearch')

try:
    # Akceptacja ciasteczek
    accept = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")
    accept.click()
    # Wyszukiwanie miejsca
    search_place = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input")
    search_place.click()
    searchbox = driver.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/input")
    searchbox.send_keys("Francja")
    time.sleep(2)
    picked_country = driver.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/ul[1]/li[2]/label/div")
    picked_country.click()
    go_search = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[1]/div[2]/footer/button")
    go_search.click()
    sorting_option = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div")
    sorting_option.click()
    sorting_lowest_price = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]")
    sorting_lowest_price.click()

    # Pobranie nazwy miejsca i nazwy hotelu
    wait = WebDriverWait(driver, 10)
    place = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[1]/span")))
    place_text = place.text

    hotel_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[2]/div/h4")))
    hotel_name = hotel_name.text

    place_list = place_text.split()
except NoSuchElementException:
    place_list = [0, 0, 0, 10000]
except TimeoutException:
    place_list = [0, 0, 0, 10000]

print('Miejsce:', place_list)
# print('Hotel:', hotel_name)

time.sleep(500)  # Pozostawienie otwartego okna na 500 sekund (dla testów)

driver.quit()  # Zamknięcie przeglądarki po zakończeniu działania
