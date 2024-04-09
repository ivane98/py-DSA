# ARRAYS
from time import time

def compute_average(n):
    data = []
    start = time()

    for k in range(n):
        data.append(None)
    end = time()

    return (end - start) / n


print(compute_average(100_000))