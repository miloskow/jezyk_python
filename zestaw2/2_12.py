line = "Przykladowy tekst do zadania"

wyrazy = line.split()


pierwsze_znaki = ''.join(wyraz[0] for wyraz in wyrazy)
print(pierwsze_znaki)

ostatnie_znaki = ''.join(wyraz[-1] for wyraz in wyrazy)
print(ostatnie_znaki)
