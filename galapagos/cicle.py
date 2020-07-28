from galapagos import population, config, log_handler
import numpy as np
from multiprocessing import Pool
from os import environ
from functools import reduce
from tqdm import tqdm


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


def crossover(population: np.ndarray, crossover: callable) -> np.ndarray:
    individual_chance = np.random.rand(len(population))

    for i in range(0, len(individual_chance)-1, 2):
        if individual_chance[i] <= float(environ["PC"]):
            population[i], population[i + 1] = crossover(
                population[i],
                population[i+1]
            )

    return population


def generation_run(
        population: np.ndarray,
        fitness: callable,
        select_function: callable,
        crossover_function: callable,
        mutation_function: callable,
        pool_size: int,
        run: int
) -> dict:
    generations_hist = {"best": [], "avg": [],
                        "worst": [], "winner": (None, -1)}

    for _ in tqdm(range(int(environ["GEN"])), desc=f'Run {run}', unit=" gen"):

        evaluated = evaluate(fitness, population, pool_size)

        avg = reduce(lambda a, b: a+b[1], evaluated, 0)/len(evaluated)

        generations_hist["best"].append(evaluated[-1])
        generations_hist["avg"].append(avg)
        generations_hist["worst"].append(evaluated[0])
        generations_hist["winner"] = max(
            evaluated[-1],
            generations_hist["winner"],
            key=lambda x: x[1]
        )

        selected, elite = select(evaluated, select_function)

        population = mutate(
            crossover(
                selected,
                crossover_function
            ),
            mutation_function
        )

        if environ["EL"] == "true":
            population = np.concatenate([[elite[0]], population])

    generations_hist["best"] = np.array(generations_hist["best"], object)
    generations_hist["avg"] = np.array(generations_hist["avg"], object)
    generations_hist["worst"] = np.array(generations_hist["worst"], object)

    return generations_hist


def run(
    fitness: callable,
    select_function: callable,
    crossover_function: callable,
    mutation_function: callable,
    config_file: str = "input.cfg",
    pool_size: int = 4
) -> dict:

    config.parse(config_file)

    populator = population.get()

    runs_hist = {"champion": (None, -1), "runs": []}

    for run in range(int(environ["RUN"])):

        generation_hist = generation_run(
            populator(),
            fitness,
            select_function,
            crossover_function,
            mutation_function,
            pool_size,
            run+1
        )
        
        runs_hist["champion"] = max(
            runs_hist["champion"], 
            generation_hist["winner"],
            key=lambda x: x[1]
        )
        runs_hist["runs"].append(generation_hist)

    runs_hist["runs"] = np.array(runs_hist["runs"], dtype=object)

    log_handler.show_winner(runs_hist)

    return runs_hist