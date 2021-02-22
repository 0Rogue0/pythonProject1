import math


def f11(x, y, z):
    return (z ** 6 + z ** 2 / 79 + 50) / (math.exp(y) + 8 * y ** 5 + 28) - (
            math.sin(x) - 17 * y ** 4 + 30) + math.sqrt((math.log(z) - 13 * y ** 2) / (32 * z ** 2 - math.cos(x)))


def f12(x):
    if x < -74:
        return 5(math.tan(x) - math.exp(x)) ** 6 - 8 * x ** 5
    elif (x >= - 74) and (x < -18):
        return (x ** 2 + 13 * x ** 8) ** 4 - math.exp(x)
    elif (x >= -18) and (x < 51):
        return (x ** 4 + x + 14) ** 8 + x ** 6
    elif (x >= 51) and (x < 104):
        return math.log(x - math.tan(x)) - 92 * x ** 4
    elif x >= 104:
        return 37 * x ** 7 - 32 * x ** 2


def f13(n):
    p1 = 0
    for i in range(1, n + 1):
        p1 += (i ** 7 + i ** 8)

    p2 = 0
    for i in range(1, n + 1):
        p2 += (i ** 8 + i ** 6)

    return 12 * p1 - p2


def f14(n):
    if n == 0:
        return 10
    else:
        return 1 / 60 * ((f14(n - 1)) ** 2) - 1 / 3 * (f14(n - 1))
