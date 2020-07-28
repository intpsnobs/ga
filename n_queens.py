import galapagos as gp
from numpy import ndarray
import numpy as np
import galapagos.operators.crossover as cr
import galapagos.operators.mutation as mt
import galapagos.selector as sl
from galapagos.log_handler import plot_runs


def fitness(individual: ndarray):
    dim = len(individual)
    fit = dim*(dim-1)
    for i in range(len(individual)-1):
        for j in range(i+1, len(individual)):
            fit -= 2*(abs(individual[i]-individual[j]) == abs(i-j))
    return individual, fit/(dim*(dim-1))


if __name__ == "__main__":
    plot_runs(
        gp.run(
            fitness,
            mutation_function=mt.swap,
            crossover_function=cr.pmx,
            select_function=sl.fitness_proportionate_selection,
            config_file="n_queens.cfg"
        )
    )
