import galapagos
from numpy import ndarray


def fitness(individual: ndarray):
    dim = len(individual)
    fit = dim*(dim-1)
    for i in range(len(individual)-1):
        for j in range(i+1, len(individual)):
            fit -= 2*(abs(individual[i]-individual[j]) == abs(i-j))
    return individual, fit


if __name__ == "__main__":
    galapagos.run(
        fitness,
        config_file="n_queens.cfg"
    )
