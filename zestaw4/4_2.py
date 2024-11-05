def make_ruler(dlugosc):
    linijka_gora = "|"
    linijka_dol = "0"
    if(dlugosc.isnumeric()):
        for i in range (dlugosc):
            linijka_gora += "....|"
            
            numery = f"{i+1:>5}"
            linijka_dol += numery
        miarka = f"{linijka_gora}\n{linijka_dol}"
        return miarka
    
def make_grid(rows, columns):  
    linia = "+"
    boki = "|"

    for j in range(int(rows)):
        linia += "---+"
        boki += "   |"

    kratka = linia
    for i in range(int(columns)):
        kratka += '\n' + boki + '\n' + linia
    
    return kratka

        
