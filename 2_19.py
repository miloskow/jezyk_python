L = [123, 9, 56, 12, 987, 21, 5]

bloki = "".join(str(liczba).zfill(3) for liczba in L)

print(bloki)