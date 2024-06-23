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
search_box = driver.find_element('id', "__next")