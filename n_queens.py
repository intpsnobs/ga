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
            if (abs(individual[i]-individual[j]) == abs(i-j)):
                print((i,j))
            fit -= 2*(abs(individual[i]-individual[j]) == abs(i-j))
    return individual, fit/(dim*(dim-1))


if __name__ == "__main__":
    t = [54, 43, 46, 10, 14, 62, 22, 59, 19, 29, 40, 36, 55,  7, 18, 47, 31, 53, 34, 37,  4, 50,  3, 16,
     48, 51, 63, 61, 56, 32,  9, 64,  1,  2, 26, 41, 28, 49, 24, 13,  5, 30, 27, 23, 52, 35, 44, 38,
     20,  6, 57, 12, 45, 39, 25, 42, 60,  8, 17, 15, 33, 58, 11, 21]
    print(fitness(t))
    # plot_runs(
    #     gp.run(
    #         fitness,
    #         mutation_function=mt.swap,
    #         crossover_function=cr.pmx,
    #         select_function=sl.fitness_proportionate_selection,
    #         config_file="n_queens.cfg"
    #     )
    # )
