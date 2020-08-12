import galapagos as gp
from numpy import ndarray
import numpy as np
import galapagos.operators.crossover as cr
import galapagos.operators.mutation as mt
import galapagos.selector as sl
from galapagos.log_handler import plot_runs, convergence_chart
from galapagos.config import parse 
from numba import njit
from os import environ
import math

def show_table(chromosome: np.ndarray) -> str:
    size = len(chromosome)
    board = np.full((size, size), ".")

    for index, item in enumerate(chromosome):
        board[index][item - 1] = "x"

    out = ""
    for row in board:
        out += "|"
        for tile in row:
            out += tile
        out += " |\n"

    col, profit = 0, 0
    for i in range(len(chromosome) - 1):
        profit += profit_array[(i+1)*(chromosome[i]-1)]
        for j in range(i + 1, len(chromosome)):
            col += 2 * (abs(chromosome[i] - chromosome[j]) == abs(i - j))

    out += f"\ncollisions: {col}\n"
    out += "profit: %f/%f\n"% (profit, max_fit_profit)


    return out

@njit
def fitness(individual: ndarray):
    dim = len(individual)
    fit = dim * (dim - 1)
    max_fit = fit + max_fit_profit*0.001

    profit: float = 0
    for i in range(len(individual) - 1):
        profit += profit_array[(i+1)*(individual[i]-1)]
        for j in range(i + 1, len(individual)):
            fit -= 2 * (abs(individual[i] - individual[j]) == abs(i - j))

    return individual, (fit + profit*0.001) / max_fit


if __name__ == "__main__":
    parse("p_queens.cfg")
    array_length = int(environ.get("DIM"))

    profit_array = np.array(list(map(float,range(1,array_length**2+1))))
    op, po = math.sqrt, math.log10
    for i in range(len(profit_array)):
        profit_array[i] = op(profit_array[i])
        if not (i+1) % array_length:
            po, op = op, po
            continue
    
    max_fit_profit = sum(sorted(profit_array)[-1:-array_length-1:-1])
    # print(fitness(np.array([7, 5, 3, 1, 6, 8, 2, 4])))
    result = gp.run(
        fitness,
        mutation_function=mt.swap,
        crossover_function=cr.pmx,
        select_function=sl.stochastic_tournament,
        config_file="p_queens.cfg",
        phenotype=show_table,
    )

    

    convergence_chart(result, False)
    plot_runs(result)
