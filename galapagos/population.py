from functools import partial
import numpy as np
import math


def binary_random(size: int) -> np.ndarray:
    return np.random.randint(0, 2, size)


def integer_permutation(size: int, min: int, max: int) -> np.ndarray:
    return np.random.permutation(range(math.floor(min), math.floor(max+1)))


def integer_random(size: int, min: int, max: int) -> np.ndarray:
    return np.random.randint(math.floor(min), math.floor(max+1), size)


def real_random(size: int, min: int, max: int) -> np.ndarray:
    return np.random.uniform(min, max, size)


def gen(population: int, populationgen: callable) -> np.ndarray:
    return np.array([populationgen() for _ in range(population)])


def get(params) -> callable:
    chromosome_size, min, max, key = params["chromosome_size"], params["min"], params["max"], params["key"]

    generator = {
        "BIN": partial(binary_random, chromosome_size),
        "INT_PERM": partial(integer_permutation, chromosome_size, min, max),
        "INT": partial(integer_random, chromosome_size, min, max),
        "REAL": partial(real_random, chromosome_size, min, max)
    }

    if key not in generator:
        raise Exception(
            "Population", (f'key "{key}"" does not exist use one of {[i for i in generator]} instead'))

    return partial(gen, params["population_size"], generator[key])
