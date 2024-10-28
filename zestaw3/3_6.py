
linia = "+"
boki = "|"
szerokosc = input("Podaj szerokosc kratki: ")
wysokosc = input("Podaj wysokosc kratki: ")

for j in range(int(szerokosc)):
    linia += "---+"
    boki += "   |"

kratka = linia
for i in range(int(wysokosc)):
    kratka += '\n' + boki + '\n' + linia

print(kratka)
