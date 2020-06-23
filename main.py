from functools import partial
import numpy as np

def binary(size):
    cromos = np.random.choice([0, 1], size=(size,))
    print(f'Size {size} {cromos}')

def gen(population, populationgen):
    print(f'POP {population}') 
    populationgen()

def get_population( value ):
    generator = {
        "BIN": partial(binary, 22)
    }.get(value)
    return partial(partial(gen, 10), generator)


if __name__ == "__main__":
    print(get_population("BIN"))
    get_population("BIN")()