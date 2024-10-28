sekwencja1 = input("Podaj pierwsza sekwencje znakow: ")
sekwencja2 = input("Podaj druga sekwencje znakow: ")
zestaw1 = set(sekwencja1)
zestaw2 = set(sekwencja2)

wspolne = list(zestaw1.intersection(zestaw2))
suma = list(zestaw1.union(zestaw2))

print(wspolne)
print(suma)

