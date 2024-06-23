import tkinter as tk
from tkinter import messagebox

def search_tours():
    country = entry.get()
    if country:
        # Tutaj dodamy kod do wyszukiwania informacji za pomocą Selenium
        # Na razie wyświetlimy tylko wprowadzone państwo
        messagebox.showinfo("Wyszukiwane Państwo", f"Państwo: {country}")
    else:
        messagebox.showwarning("Brak danych", "Proszę wpisać nazwę państwa")

app = tk.Tk()
app.title("Wyszukiwanie Wycieczek")

label = tk.Label(app, text="Wpisz nazwę państwa:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

button = tk.Button(app, text="Szukaj", command=search_tours)
button.pack(pady=10)

app.mainloop()
