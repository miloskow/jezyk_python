sekwencja = [[],[4],(1,2),[3,4],(5,6,7)]
wynik = []

for element in sekwencja:
    suma = 0
    for i in element:
        suma += i
    wynik.append(suma)
    
print(wynik)