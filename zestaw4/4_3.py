def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    elif n == 1 or n == 0:
        return n