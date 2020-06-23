from functools import partial
import numpy as np
import math

def binary_random(size: int):
    return np.random.choice([0, 1], size=size)

def integer_permutation(size: int, min: int, max: int):
    return np.random.permutation(range(math.floor(min), math.floor(max+1)))

def integer_random(size: int, min: int, max: int):
    return np.random.choice(range(math.floor(min), math.floor(max+1)), size)

def real_random(size: int, min: int, max: int):
    return np.random.uniform(min, max, size)

def gen(population: int, populationgen: int):
    return np.array([populationgen() for _ in range(population)])


def get_population(key: str, population_size : int, chromosome_size: int, min=0.0, max=10.0):
    generator = {
        "BIN": partial(binary_random, chromosome_size),
        "INT_PERM": partial(integer_permutation, chromosome_size, min, max),
        "INT": partial(integer_random, chromosome_size, min, max),
        "REAL": partial(real_random, chromosome_size, min, max)
    }

    if key not in generator:
        raise Exception("Population", (f'key "{key}"" does not exist use one of {[i for i in generator]} instead'))

    return partial(partial(gen, population_size), generator.get(key))