def quadratic(a, b, c):
    pos = (-b + ((b**2 - 4*a*c) ** 0.5)) / (2 * a)
    neg = (-b - ((b**2 - 4*a*c) ** 0.5)) / (2 * a)
    values = (pos, neg)
    return values
