def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left +=1
        right -=1
def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left+1, right-1)