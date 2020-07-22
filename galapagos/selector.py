
import random
import numpy as np


def fitness_proportionate_selection(population, num=2):
    selected = []
    sum_fit  = float(sum([c[1] for c in population]))

    for _ in range(num):
        lucky_number = random.random()
        prev_probability = 0.0

        for i, c in enumerate(population):
            if (prev_probability + (c[1] / sum_fit)) >= lucky_number:
                selected.append(np.array(c[0]))
                sum_fit -= c[1]
                del population[i]
                break
            prev_probability += c[1] / sum_fit

    return selected

def stochastic_tournament(population, k=2, kp=1):
    def fight(subpop):
        lucky_number = random.random()
        if kp >= lucky_number:
            return subpop[1]
        return subpop[0]
    weights = [1 for i in population]
    return [fight(sorted(random.choices(population, k=k, weights=weights), key=lambda x: x[1])[0::k-1]) for i in population]
    