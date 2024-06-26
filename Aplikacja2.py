import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Lista krajów
countries = [
    "Egipt", "Grecja", "Hiszpania", "Polska", "Tunezja", "Turcja",
    "Albania", "Algieria", "Andora", "Anguilla", "Antarktyda", "Antyle Holenderskie",
    "Arabia Saudyjska", "Argentyna", "Armenia", "Aruba", "Australia", "Austria",
    "Azerbejdżan", "Bahamy", "Bahrajn", "Bangladesz", "Barbados", "Belgia",
    "Belize", "Birma", "Boliwia", "Bośnia i Hercegowina", "Botswana", "Brazylia",
    "Bułgaria", "Chile", "Chiny", "Chorwacja", "Curacao", "Cypr", "Czarnogóra",
    "Czechy", "Dania", "Dominika", "Dominikana", "Ekwador", "Emiraty Arabskie",
    "Estonia", "Etiopia", "Filipiny", "Finlandia", "Francja", "Gambia", "Grenada",
    "Gruzja", "Gwadelupa", "Gwatemala", "Holandia", "Indie", "Indonezja", "Iran",
    "Irlandia", "Islandia", "Izrael", "Jamajka", "Japonia", "Jordania", "Kajmany",
    "Kambodża", "Kanada", "Katar", "Kazachstan", "Kenia", "Kolumbia", "Korea Południowa",
    "Kosowo", "Kostaryka", "Kuba", "Liban", "Litwa", "Luksemburg", "Łotwa", "Macedonia",
    "Madagaskar", "Malediwy", "Malezja", "Malta", "Maroko", "Martynika", "Mauritius",
    "Meksyk", "Monako", "Mongolia", "Namibia", "Nepal", "Niemcy", "Nikaragua",
    "Norwegia", "Nowa Zelandia", "Oman", "Pakistan", "Panama", "Peru", "Polinezja Francuska",
    "Portugalia", "Republika Południowej Afryki", "Reunion", "Rumunia", "Rwanda",
    "Saint Barthelemy", "Saint Lucia", "Saint Martin", "Senegal", "Serbia", "Seszele",
    "Singapur", "Słowacja", "Słowenia", "Sri Lanka", "Stany Zjednoczone Ameryki",
    "Szwajcaria", "Szwecja", "Tajlandia", "Tanzania", "Togo", "Turks i Caicos", "Uganda",
    "Uzbekistan", "Wenezuela", "Węgry", "Wielka Brytania", "Wietnam", "Włochy",
    "Wyspy Dziewicze (brytyjskie)", "Wyspy Dziewicze (USA)", "Wyspy Zielonego Przylądka",
    "Zimbabwe"
]

# Funkcja obsługująca kliknięcie przycisku kraju
def country_selected(country):
    print(f"Wybrano kraj: {country}")
    # Tutaj możesz dodać kod do obsługi wybranego kraju (np. rozpoczęcie wyszukiwania ofert)

# Stworzenie interfejsu użytkownika
root = tk.Tk()
root.title('VacationFinder')
window_width = 600
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
w = int(screen_width / 2 - window_width / 2)
h = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{w}+{h}')
root.iconbitmap('ikona.ico')

message = tk.Label(root, text='Dzień dobry Podróżniku!\n\nPomogę znaleźć Ci możliwie najtańszą ofertę. Wybierz Państwo, które Cię interesuje\n', wraplength=root.winfo_width())
message.pack()

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

# Tworzenie przycisków dla krajów w 4 kolumnach
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
