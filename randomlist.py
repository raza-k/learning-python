import random


def randoms():
    x = 100
    y = []
    for i in range(5):
        x = random.randint(1, x)
        y.append(x)
    return y


print(randoms())
