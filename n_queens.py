import galapagos
from numpy import ndarray
import numpy as np
import galapagos.operators.crossover as cr
import galapagos.operators.mutation as mt
import galapagos.selector as sl
import math
import matplotlib.pyplot as plt
from os import environ



def fitness(individual: ndarray):
    dim = len(individual)
    fit = dim*(dim-1)
    # print(fit)
    for i in range(len(individual)-1):
        for j in range(i+1, len(individual)):
            fit -= 2*(abs(individual[i]-individual[j]) == abs(i-j))
    return individual, fit/(dim*(dim-1))


if __name__ == "__main__":
    print(fitness(list(range(1,9))))
    generations = galapagos.run(
        fitness,
        mutation_function=mt.swap,
        crossover_function=cr.pmx,
        select_function=sl.fitness_proportionate_selection,
        config_file="n_queens.cfg"
    )

    runs = int(environ["RUN"])
    size = math.floor(runs/2)

    fig, axs = plt.subplots(size, 2, figsize=(10,10))

    run = 0
    for line in axs:
        for ax in line:
            best = [x["best"][1] for x in generations[run]]
            ax.plot(best, label="best")
            # ax.plot([x["worst"][1] for x in generations[run]], color='r', label="worst")
            ax.plot([x["avg"] for x in generations[run]], color='k', label="avg")
            ax.legend()
            ax.set_title('run: %d | best fit: %.2f' % (run+1, generations[run][0]["best"][1]))
            ax.set_xlabel("Generations")
            ax.set_ylabel("Fitness")
            run=run+1

    print(generations[0])
    # # for i, generation in enumerate(generations):
    # #     plt.plot([x[1] for x in generation])
    fig.tight_layout(pad=0.4)
    plt.show()


