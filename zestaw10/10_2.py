import tkinter as tk
import random

def losuj_komputer():
    return random.choice(['Papier', 'Kamień', 'Nożyce'])

def okresl_wynik(wybor_gracza, wybor_komputera):
    if wybor_gracza == wybor_komputera:
        return "Remis!"
    elif (wybor_gracza == 'Kamień' and wybor_komputera == 'Nożyce') or \
         (wybor_gracza == 'Nożyce' and wybor_komputera == 'Papier') or \
         (wybor_gracza == 'Papier' and wybor_komputera == 'Kamień'):
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"

def graj(wybor_gracza):
    wybor_komputera = losuj_komputer()
    wynik = okresl_wynik(wybor_gracza, wybor_komputera)
    
    etykieta_wybor_gracza.config(text=f"Twój wybór: {wybor_gracza}")
    etykieta_wybor_komputera.config(text=f"Wybór komputera: {wybor_komputera}")
    etykieta_wynik.config(text=f"Wynik: {wynik}")


okno = tk.Tk()
okno.title("Papier, Kamień, Nożyce")

etykieta_wybor_gracza = tk.Label(okno, text="Twój wybór: ", font=("Arial", 14))
etykieta_wybor_gracza.pack()

etykieta_wybor_komputera = tk.Label(okno, text="Wybór komputera: ", font=("Arial", 14))
etykieta_wybor_komputera.pack()

etykieta_wynik = tk.Label(okno, text="Wynik: ", font=("Arial", 16, 'bold'))
etykieta_wynik.pack()


przycisk_papier = tk.Button(okno, text="Papier", font=("Arial", 14), command=lambda: graj("Papier"))
przycisk_papier.pack(pady=10)

przycisk_kamien = tk.Button(okno, text="Kamień", font=("Arial", 14), command=lambda: graj("Kamień"))
przycisk_kamien.pack(pady=10)

przycisk_nozyce = tk.Button(okno, text="Nożyce", font=("Arial", 14), command=lambda: graj("Nożyce"))
przycisk_nozyce.pack(pady=10)

okno.mainloop()
