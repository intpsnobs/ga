import time
from config import parse
from population import get_population
from functools import partial
import numpy as np
from multiprocessing import Pool
from log_handler import show_board, show_population

if __name__ == "__main__":
    population = get_population(**parse("input.cfg"))()

    def fitness(ind: list):
        fit = 0
        for i in range(len(ind)-1):
            for j in range(i+1, len(ind)):
                fit += (abs(ind[i]-ind[j]) == abs(i-j))
        return ind, fit

    pool = Pool(4)
    start_time = time.time()
    evaluated_population = pool.map(fitness, population)
    pool.close()
    pool.join()

    evaluated_population.sort(key=lambda x: x[1])
    
    show_population(evaluated_population)
    


