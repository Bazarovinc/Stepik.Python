def f(x):
    y = 0
    if x <= -2:
        y = 1 - ((x + 2) ** 2)
    elif -2 < x <= 2:
        y = -(x / 2)
    elif x > 2:
        y = ((x - 2) ** 2) + 1
    return (y)
