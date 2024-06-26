import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Lista krajów
countries = [
    "Albania", "Algieria", "Andora", "Anguilla", "Antarktyda", "Antyle Holenderskie",
    "Arabia Saudyjska", "Argentyna", "Armenia", "Aruba", "Australia", "Austria",
    "Azerbejdżan", "Bahamy", "Bahrajn", "Bangladesz", "Barbados", "Belgia",
    "Belize", "Birma", "Boliwia", "Bośnia i Hercegowina", "Botswana", "Brazylia",
    "Bułgaria", "Chile", "Chiny", "Chorwacja", "Curacao", "Cypr", "Czarnogóra",
    "Czechy", "Dania", "Dominika", "Dominikana", "Egipt", "Ekwador", "Emiraty Arabskie",
    "Estonia", "Etiopia", "Filipiny", "Finlandia", "Francja", "Gambia", "Grecja", "Grenada",
    "Gruzja", "Gwadelupa", "Gwatemala", "Hiszpania", "Holandia", "Indie", "Indonezja", "Iran",
    "Irlandia", "Islandia", "Izrael", "Jamajka", "Japonia", "Jordania", "Kajmany",
    "Kambodża", "Kanada", "Katar", "Kazachstan", "Kenia", "Kolumbia", "Korea Południowa",
    "Kosowo", "Kostaryka", "Kuba", "Liban", "Litwa", "Luksemburg", "Łotwa", "Macedonia",
    "Madagaskar", "Malediwy", "Malezja", "Malta", "Maroko", "Martynika", "Mauritius",
    "Meksyk", "Monako", "Mongolia", "Namibia", "Nepal", "Niemcy", "Nikaragua",
    "Norwegia", "Nowa Zelandia", "Oman", "Pakistan", "Panama", "Peru", "Polinezja Francuska",
    "Polska", "Portugalia", "Republika Południowej Afryki", "Reunion", "Rumunia", "Rwanda",
    "Saint Barthelemy", "Saint Lucia", "Saint Martin", "Senegal", "Serbia", "Seszele",
    "Singapur", "Słowacja", "Słowenia", "Sri Lanka", "Stany Zjednoczone Ameryki",
    "Szwajcaria", "Szwecja", "Tajlandia", "Tanzania", "Togo", "Tunezja", "Turcja", "Turks i Caicos", "Uganda",
    "Uzbekistan", "Wenezuela", "Węgry", "Wielka Brytania", "Wietnam", "Włochy",
    "Wyspy Dziewicze (brytyjskie)", "Wyspy Dziewicze (USA)", "Wyspy Zielonego Przylądka",
    "Zimbabwe"

]

# Funkcja obsługująca kliknięcie przycisku kraju
def country_selected(country):
    try:
        # Konfiguracja Selenium z lokalnym chromedriver.exe
        driver = webdriver.Chrome()
        driver.get('https://www.wakacje.pl/wczasy/?src=fromSearch')

        # Ustawienia WebDriverWait
        wait = WebDriverWait(driver, 10)

        # Akceptacja ciasteczek, jeśli istnieje
        try:
            accept = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div/button[2]")
            accept.click()
        except NoSuchElementException:
            pass

        # Znalezienie pola wyszukiwania i wysłanie nazwy kraju
        search_place = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[1]/section/div/div/div/div[1]/div/div/div/input")
        search_place.click()
        time.sleep(1)
        searchbox = driver.find_element(By.CLASS_NAME, "sc-hxqEdz")
        searchbox.send_keys(country)
        time.sleep(2)

        # Wybór pierwszego wyniku wyszukiwania
        picked_country = driver.find_element(By.CLASS_NAME, "sc-1slvi5p-2")
        picked_country.click()

        time.sleep(1)
        # Kliknięcie przycisku Szukaj
        go_search = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div[1]/div[2]/footer/button")))
        go_search.click()

        time.sleep(1)
        # Wybór opcji sortowania (najniższa cena)
        sorting_option = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div")
        sorting_option.click()

        sorting_lowest_price = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]")
        sorting_lowest_price.click()

        try:
            # Pobranie informacji o pierwszej ofercie
            place = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[1]/span")))
            place = place.text

            hotel_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[2]/div/h4")))
            hotel_name = hotel_name.text

            date = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[1]/span[2]")))
            date = date.text

            acces = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[2]/span[2]")))
            acces = acces.text

            food = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[3]/span[2]")))
            food = food.text

            agency = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[2]/div/div[3]/div[4]/span[2]")))
            agency = agency.text

            price = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/main/div/div[2]/div[1]/section/div[1]/a[1]/div[3]/div")))
            price = price.text

        except NoSuchElementException:
            place = "Nieustalono"
            hotel_name = "Nieustalono"
            date = "Nieustalono"
            acces = "Nieustalono"
            food = "Nieustalono"
            agency = "Nieustalono"
            price = "Nieustalono"
        except TimeoutException:
            place = "Nieustalono"
            hotel_name = "Nieustalono"
            date = "Nieustalono"
            acces = "Nieustalono"
            food = "Nieustalono"
            agency = "Nieustalono"
            price = "Nieustalono"

        print('Miejsce:', place)
        print("Nazwa hotelu/Nazwa Wycieczki:", hotel_name)
        print('Data wyjazdu i powrotu:', date)
        print('Miasto wylotu lub "dojazd własny":', acces)
        print("Wyżywienie:", food)
        print("Biuro podróży:", agency)
        print("Uzyskane informacje o ofercie:\n", price)

        time.sleep(500)
        driver.quit()

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        driver.quit()

# Tworzenie interfejsu użytkownika Tkinter
root = tk.Tk()
root.title('VacationFinder')
window_width = 600
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
w = int(screen_width/2 - window_width/2)
h = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{w}+{h}')
root.iconbitmap('ikona.ico')

message = tk.Label(root, text='Witaj Podróżniku!\nWybierz kraj, aby znaleźć możliwie najtańszą ofertę wakacyjną:', wraplength=300)
message.pack(pady=10)

# Tworzenie obszaru przewijania
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Tworzenie przycisków dla krajów
columns = 4
for index, country in enumerate(countries):
    row = index // columns
    column = index % columns
    button = tk.Button(scrollable_frame, text=country, command=lambda c=country: country_selected(c))
    button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

# Ustawienie równomiernego rozłożenia kolumn
for i in range(columns):
    scrollable_frame.grid_columnconfigure(i, weight=1)

root.mainloop()