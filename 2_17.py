line = "tekst do posortowania alfabetycznie i pod wzgledem dlugosci "

wyrazy = line.split()

posortowane = sorted(wyrazy)
posortowane_po_dlugosci = sorted(wyrazy, key=len)

print(posortowane)
print(posortowane_po_dlugosci)