line = "Nowy przykladowy napis do kolejnego zadania"

wyrazy = line.split()

dlugosc = sum(len(wyraz) for wyraz in wyrazy)
print(dlugosc)