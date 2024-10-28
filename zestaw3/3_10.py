"""
Słownik został stworzony poprzez ręczne wpisanie. Mógł również zostać utworzony za pomocą
dict: 
rzymskie_na_arabskie = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000), 
w oparciu o listę krotek:
pary = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
rzymskie_na_arabskie = dict(pary) 
albo poprzez zip dla dwóch osobnych list:
klucze = ['I', 'V', 'X']
wartości = [1, 5, 10]
slownik = dict(zip(klucze, wartości))
"""

rzymskie_na_arabskie = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
def roman_to_int(roman):
    rzymskie = list(roman)
    piatki = [5, 50, 500]
    wynik = 0
    ostatni = 0
    for i in rzymskie:
  
        liczba = rzymskie_na_arabskie[i]
        wynik += liczba
       
        if liczba > ostatni:
            if ostatni in piatki: 
                print("Zly format liczby")
                return
            wynik -= 2*ostatni
        ostatni = liczba
    print(wynik)


roman_to_int("XIV")