def sum_sequence(sequence):
    suma = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += sum_sequence(item)
        elif isinstance(item, (int, float)):
            suma += item
    return suma