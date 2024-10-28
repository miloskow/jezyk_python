while(True):
    dane = input("Podaj liczbe: ")
    if (dane == "stop"):
        break
    elif(dane.isnumeric()):
        x = int(dane)
        print(x, x*x*x)
    else:
        print("Proszę podać liczbę")