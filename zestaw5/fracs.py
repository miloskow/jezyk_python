import math

def simplify(frac):
    gcd = math.gcd(frac[0], frac[1])
    return [frac[0]//gcd, frac[1]//gcd]


def add_frac(frac1, frac2):
    num1, denom1 = frac1
    num2, denom2 = frac2
    denom = denom1*denom2
    num = num1*denom2 + num2*denom1
    return simplify([num, denom])


def sub_frac(frac1, frac2): 
    num1, denom1 = frac1
    num2, denom2 = frac2
    denom = denom1*denom2
    num = num1*denom2 - num2*denom1
    return simplify([num, denom])      

def mul_frac(frac1, frac2): 
    num1, denom1 = frac1
    num2, denom2 = frac2
    num = num1*num2
    denom = denom1*denom2
    return simplify([num, denom])

def div_frac(frac1, frac2): 
    num1, denom1 = frac1
    denom2, num2 = frac2
    num = num1*num2
    denom = denom1*denom2
    return simplify([num, denom])


def is_positive(frac):
    num, denom = frac
    return denom*num >=0   

def is_zero(frac): 
    num = frac[0]
    return num ==0        

def cmp_frac(frac1, frac2): 
    frac1s = simplify(frac1)
    frac2s = simplify(frac2)
    num1, denom1 = frac1s
    num2, denom2 = frac2s

    if (num1*denom2 < num2*denom1):
        return -1
    elif (num1*denom2 > num2*denom1):
        return 1
    else:
        return 0

def frac2float(frac): 
    return frac[0]/frac[1]
