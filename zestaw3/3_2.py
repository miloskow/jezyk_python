
#L = [3, 5, 4] ; L = L.sort() - L sortuje, ale nie zwraca nowej listy
L = [3, 5, 4]
L.sort()

#x, y = 1, 2, 3 do dwoch wartosci przypisujemy trzy zmienne 
x, y, z = 1, 2, 3

#X = 1, 2, 3 ; X[1] = 4 X to krotka, a w nich wartosci nie sa do zmieniania. Mozemy zmienic X na liste
X = [1, 2, 3]
X[1] = 4

#X = [1, 2, 3] ; X[3] = 4 Poniewaz listy sa indeksowane od 0, a mamy 3 elementy w liscie, ostatni indeks
#to 2. Nie ma indeksu 3, taki kod spowoduje IndexError
X= [1, 2, 3] 
X.append(4)     #tak możemy poszerzyć listę

#X = "abc" ; X.append("d") Tym razem append nie zadziała poniewąż X to string, które w pythonie są 
#niemodyfikowalne. Możemy użyć +=
X = "abc" 
X += "d"

#L = list(map(pow, range(8))) Funkcja pow() musi przyjac dwa argumenty - podstawe i wykladnik
