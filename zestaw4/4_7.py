def flatten(sequence):
    lista = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            lista.extend(flatten(item))
        else:
            lista.append(item)
    return lista
print(flatten([1,(2,3, (7, 9),[6]), 7, 8]))
