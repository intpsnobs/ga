from galapagos import population, config
import numpy as np
from multiprocessing import Pool


def evaluate(fitness: callable, populate: callable, pool_size: int):
    pool = Pool(pool_size)

    evaluated_population = pool.map(fitness, populate())

    pool.close()
    pool.join()

    return evaluated_population


def run(fitness: callable, selector: callable, config_file: str = "input.cfg", pool_size: int = 4):
    params = config.parse(config_file)

    populate = population.get(params)

    new_population = populate(selector(evaluate(fitness, populate, pool_size)))

    print(np.array_str(new_population))
