import numpy as np
import os

def bit_flip(chromosome: np.ndarray) -> np.ndarray:
    choose = np.random.rand(len(chromosome))

    for i in range(len(choose)):
        if choose[i] < 0.5:
            chromosome[i] = 1 if chromosome[i] == 0 else 0
    
    return chromosome
    
def swap(chromosome: np.ndarray):
    point_1 = np.random.randint(len(chromosome))
    point_2 = np.random.randint(len(chromosome))
    while point_1 == point_2:
        point_2 = np.random.randint(len(chromosome))
    chromosome[point_1], chromosome[point_2] = chromosome[point_2], chromosome[point_1]

    return chromosome
