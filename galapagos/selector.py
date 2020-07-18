
import random
import numpy as np


def fitness_proportionate_selection(population, num=2):
    selected = []
    max     = sum([c[1] for c in population])
    pick    = random.uniform(0, max)
    current = 0
    for _ in range(2):
        for chromosome in population:
            current += chromosome[1]
            if current > pick:
                selected.append(chromosome)
                break

    return np.array(selected, dtype=object)
