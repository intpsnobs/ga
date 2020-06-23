from config import parse
from population import get_population
from functools import partial
import numpy as np

if __name__ == "__main__":
    population = get_population(**parse("input.cfg"))()

    test_indv = [5, 7, 1, 3, 6, 4, 2, 8]

    def fitness(ind: list):
        fit = 0
        for i in range(len(ind)-1):
            for j in range(i+1, len(ind)):
                fit += (abs(ind[i]-ind[j]) == abs(i-j))
        return ind, fit

    evaluated_population = list(map(fitness, population))
    evaluated_population.sort(key=lambda x: x[1])

    print()
    print(*evaluated_population, sep='\n')
    print()
    best_individual, best_fitness = evaluated_population[0]
    print("🔝 : %s -> %d " % (best_individual, best_fitness))
    worst_individual, wordt_fitness = evaluated_population[-1]
    print("💩 : %s -> %d " % (worst_individual, wordt_fitness))

    board = np.full((8, 8), '\033[0m.')

    for index, item in enumerate(best_individual):
        board[index][item-1] = '♕'

    for row in board:
        print("\033[0m|", end=" ")
        for tile in row:
            print('\033[33m'+tile, end=" ")
        print("\033[0m |")
    print("\n")
