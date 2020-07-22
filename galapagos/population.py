from functools import partial
import numpy as np
import math


def binary_random(size: int) -> np.ndarray:
    return np.random.randint(0, 2, size, dtype="uint8")


def integer_permutation(size: int, low: int, hight: int) -> np.ndarray:
    return np.random.permutation(range(math.floor(low), math.floor(hight+1)))


def integer_random(size: int, low: int, hight: int) -> np.ndarray:
    return np.random.randint(math.floor(low), math.floor(hight+1), size)


def real_random(size: int, low: int, hight: int) -> np.ndarray:
    return np.random.uniform(low, hight, size)


def gen(population_size, populationgen: callable, population=[]) -> np.ndarray:
    num = (population_size - len(population))
    return np.array(population + [populationgen() for _ in range(num)])


def get(params) -> callable:
    chromosome_size, low, hight, key = params["chromosome_size"], params["low"], params["hight"], params["key"]

    generator = {
        "BIN": partial(binary_random, chromosome_size),
        "INT_PERM": partial(integer_permutation, chromosome_size, low, hight),
        "INT": partial(integer_random, chromosome_size, low, hight),
        "REAL": partial(real_random, chromosome_size, low, hight)
    }

    if key not in generator:
        raise Exception(
            "Population", (f'key "{key}"" does not exist use one of {[i for i in generator]} instead'))

    return partial(gen, params["population_size"], generator[key])
