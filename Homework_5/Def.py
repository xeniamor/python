def power(a, b):
    if b == 0:
        return 1
    return power(a, b - 1) * a