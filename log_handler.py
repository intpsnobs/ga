import numpy as np

def show_board(positions: list):
    size = len(positions)
    board = np.full((size, size), '\033[0m.')

    for index, item in enumerate(positions):
        board[index][item-1] = '♕'

    for row in board:
        print("\033[0m|", end=" ")
        for tile in row:
            print('\033[33m'+tile, end=" ")
        print("\033[0m |")

def show_population(population: list, top=10, best=True):
    size_population = len(population)
    print(f"Top {top}:")
    for i in range(size_population if (top>size_population) else top):
        print(f"{population[i][0]}: fit({population[i][1]})")
    print()

    best_individual, best_fitness = population[0]
    if best:
        print("BEST %s: fit(%d) " % (best_individual, best_fitness))
        #show_board(population[0][0])

    worst_individual, wordt_fitness = population[-1]
    print("WORST %s: fit(%d) " % (worst_individual, wordt_fitness))
