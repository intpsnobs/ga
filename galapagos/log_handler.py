import numpy as np
import math
import matplotlib.pyplot as plt
from os import environ
from scipy.interpolate import CubicSpline


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
    for i in range(size_population if (top > size_population) else top):
        print(f"{population[i][0]}: fit({population[i][1]})")
    print()

    best_individual, best_fitness = population[0]
    if best:
        print("BEST %s: fit(%f) " % (best_individual, best_fitness))
        # show_board(best_individual)

    worst_individual, worst_fitness = population[-1]
    print("WORST %s: fit(%f) " % (worst_individual, worst_fitness))


def show_winner(hist: dict):
    print("=============Winner===============")
    print("chromosome: \n%s" % np.array_str(hist["champion"][0]))
    print("fitness: %f" % hist["champion"][1])
    print("==================================")


def plot_runs(hist: dict):
    runs_num = int(environ["RUN"])

    y = runs_num // 2

    x = 2

    fig, axs = plt.subplots(x, y, figsize=(10, 10), constrained_layout=True)
    fig.suptitle('%s | best fit: %.4f' %
                 (environ["GA_TITLE"], hist["champion"][1]), fontsize=16)

    run = 0
    for line in axs:
        for ax in line:
            best = [x[1] for x in hist["runs"][run]["best"]]
            worst = [x[1] for x in hist["runs"][run]["worst"]]
            avg = [x for x in hist["runs"][run]["avg"]]

            ax.plot(best, label="best")
            spline = CubicSpline(list(range(len(worst))), worst)
            ax.plot([spline(i) for i in range(len(worst))],
                    color='r', label="worst", alpha=0.4, linestyle='dotted')
            ax.plot(avg, color='k', label="avg", alpha=0.9, linestyle='dashed')
            ax.legend()
            ax.set_title('run: %d | best fit: %.4f' %
                         (run+1, hist["runs"][run]["winner"][1]))
            ax.set_xlabel("Generations")
            ax.set_ylabel("Fitness")
            run = run+1

    plt.show()
