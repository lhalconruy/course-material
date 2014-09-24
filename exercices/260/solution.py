def euclidean(a, b):
    dif = 0
    for i in range(len(a)):
        dif = dif + (a[i] - b[i])**2
    return dif**0.5


def opt_euclidean(a, b):
    dif = 0
    for i in range(len(a)):
        dif = dif + pow((a[i] - b[i]), 2)
    return pow(dif, 0.5)


def np_euclidean(a, b):
    import numpy as np
    dif = 0
    for i in range(len(a)):
        dif = dif + np.square((a[i] - b[i]))
    return np.sqrt(dif)
