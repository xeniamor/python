def power(a, b):
    if b == 0:
        return 1
    return power(a, b - 1) * a

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)