dlugosc = input("Podaj długość miarki: ")
dlugosc_linijki = int(dlugosc)
linijka_gora = "|"
linijka_dol = "0"
if(dlugosc.isnumeric()):
    for i in range (dlugosc_linijki):
        linijka_gora += "....|"
        
        numery = f"{i+1:>5}"
        linijka_dol += numery
    miarka = f"{linijka_gora}\n{linijka_dol}"
    


print(miarka)

