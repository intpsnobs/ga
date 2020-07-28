from galapagos import population, config
import numpy as np
from multiprocessing import Pool
from os import environ
from functools import reduce


def select(population: np.ndarray, selection_function: callable):
    population = list(population)
    population = np.array(population, dtype=object)

    elite = population[-1]
    if environ["EL"] == "true":
        selected = selection_function(population[:-1:])
    else:
        selected = selection_function(population)

    return selected, elite


def evaluate(fitness: callable, population: np.ndarray, pool_size: int):
    pool = Pool(pool_size)

    evaluated_population = pool.map(fitness, population)
    evaluated_population.sort(key=lambda x: x[1])

    pool.close()
    pool.join()

    return evaluated_population


def mutate(population: np.ndarray, mutation_function: callable) -> np.ndarray:
    individual_chance = np.random.rand(len(population))

    for i in range(len(individual_chance)-1):
        if individual_chance[i] <= float(environ["PM"]):
            population[i] = mutation_function(population[i])

    return population


def crossover(population: np.ndarray, crossover_function: callable) -> np.ndarray:
    individual_chance = np.random.rand(len(population))

    for i in range(0, len(individual_chance)-1, 2):
        if individual_chance[i] <= float(environ["PC"]):
            population[i], population[i + 1] = crossover_function(population[i], population[i+1])

    return population


def run(fitness: callable,
        select_function: callable,
        crossover_function: callable,
        mutation_function: callable,
        config_file: str = "input.cfg",
        pool_size: int = 4):

    config.parse(config_file)

    population_gen = population.get()

    runs = []

    for _ in range(int(environ["RUN"])):
        generation = []
        pop = population_gen()
        for _ in range(int(environ["GEN"])):
            evaluated = evaluate(fitness, pop, pool_size)
            print(evaluated[0][1])
            avg = reduce(lambda a, b: a+b[1], evaluated, initial=0.0)/len(evaluated)
            print(avg, end="\n\n\n")
            generation.append(
                {"best": evaluated[-1], "avg": avg, "worst": evaluated[0]})

            selected, elite = select(
                evaluated,
                select_function
            )

            pop = mutate(
                crossover(
                    selected,
                    crossover_function),
                mutation_function
            )

            if environ["EL"] == "true":
                pop = np.concatenate([[elite[0]], pop])

        runs.append(np.array(generation, dtype=object))
        print("Run %d completed" % len(runs))

    # runs.sort(key=lambda x: x[0]["best"][1])
    return np.array(runs)
    # print(np.array_str(new_population), end="\n\n\n")

    # print(np.array_str(crossover(new_population, crossover_function)))

