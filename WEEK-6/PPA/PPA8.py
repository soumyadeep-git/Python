def factors(n):
    F = set()
    for i in range(1, n + 1):
        if n % i == 0:
            F.add(i)
    return F
def common_factors(a, b):
    fa = factors(a)
    fb = factors(b)
    return fa.intersection(fb)
def factors_upto(n):
    D = dict()
    for i in range(1, n + 1):
        D[i] = factors(i)
    return D