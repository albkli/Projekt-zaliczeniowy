import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_tours():
    country = entry.get()
    if country:
        driver = webdriver.Chrome()
        driver.get('https://www.wakacje.pl/wczasy/?src=fromSearch')

        # Wyszukiwanie państwa (dostosuj do rzeczywistej strony)
        search_box = driver.find_element('id', "__next")
        search_box.send_keys(country)
        search_box.send_keys(Keys.RETURN)

        # Pobieranie wyników wyszukiwania (dostosuj do rzeczywistej strony)
        results = driver.find_elements(By.CLASS_NAME, "result-item")  # Zmień 'result' na 'result-item'

        tour_info = []
        for result in results:
            tour_info.append(result.text)

        driver.quit()

        # Wyświetlanie wyników w nowym okienku TKinter
        result_window = tk.Toplevel(root)
        result_window.title(f"Wyniki wyszukiwania dla {country}")

        for info in tour_info:
            label = tk.Label(result_window, text=info)
            label.pack(pady=5)

    else:
        messagebox.showwarning("Brak danych", "Proszę wpisać nazwę państwa")

# Stworzenie interfejsu użytkownika
root = tk.Tk()
root.title('VacationFinder')
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
w = int(screen_width / 2 - window_width / 2)
h = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{w}+{h}')
root.iconbitmap('ikona.ico')

message = tk.Label(root, text='Dzień dobry Podróżniku!\n\n Pomogę znaleźć Ci najlepszą ofertę, wpisz Państwo, które Cię interesuje\n', wraplength=root.winfo_width())
message.pack()

frame = tk.Frame(root)
frame.pack()

entry_text = tk.StringVar()
label = tk.Label(frame, text='Państwo:')
label.pack()
entry = tk.Entry(frame, textvariable=entry_text)
entry.pack()

button = tk.Button(root, text="Szukaj", command=search_tours)
button.pack(pady=10)

root.mainloop()
