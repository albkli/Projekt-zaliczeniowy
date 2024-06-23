from selenium import webdriver
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_tours():
    country = entry.get()
    if country:
        # Tutaj dodamy kod do wyszukiwania informacji za pomocą Selenium
        # Na razie wyświetlimy tylko wprowadzone państwo
        messagebox.showinfo("Wyszukiwane Państwo", f"Państwo: {country}")
    else:
        messagebox.showwarning("Brak danych", "Proszę wpisać nazwę państwa")

# Stworzenie interfejsu użytkownika
root = tk.Tk()

root.title('VacationFinder')
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
w = int(screen_width/2-window_width/2)
h = int(screen_height/2-window_height/2)
root.geometry(f'{window_width}x{window_height}+{w}+{h}')
root.iconbitmap('ikona.ico')

message = tk.Label(root, text='Dzień dobry Podróżniku!\n\n Pomogę znaleźć Ci najlepszą ofertę, wpisz Państwo, które Cię interesuje\n', wraplength=root.winfo_width())
message.pack()

frame = tk.Frame(root)
frame.pack()

entry_text = tk.StringVar()
label = tk.Label(frame, text = 'Państwo:')
label.pack()
entry = tk.Entry(frame, textvariable = entry_text)
entry.pack()

button = tk.Button(root, text="Szukaj", command=search_tours)
button.pack(pady=10)

root.mainloop()

