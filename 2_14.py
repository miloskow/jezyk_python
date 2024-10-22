line = "Tekst w ktorym trzeba znalezc najdluzszy wyraz"

wyrazy = line.split()

najdluzszy = max(wyrazy, key=len);
dlugosc = len(najdluzszy)

print(najdluzszy, dlugosc)