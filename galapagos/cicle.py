from galapagos import population, config, selector

from multiprocessing import Pool

def run(fitness: callable, config_file: str = "input.cfg", pool_size: int = 4):
    params = config.parse(config_file)
    print(params)

    population_generator = population.get(params)

    pool = Pool(pool_size)

    evaluated_population = pool.map(fitness, population_generator())

    pool.close()
    pool.join()

    selected = selector.stochastic_tournament(evaluated_population)
    print(selected)
    print(len(selected))
