import time
from config import parse
from population import get_population
from functools import partial
import numpy as np
from multiprocessing import Pool
from log_handler import show_board, show_population

# Problema do Radio
# 40 funcionarios
# S = Radio Standard: 1/dia -> R$30 (Restricao: max 24 funcionarios)
# L = Radio Luxo: 2/dia -> R$40 (Restricao: max 32 funcionarios)
# f(x) = 

if __name__ == "__main__":
    population = get_population(**parse("radio.cfg"))()
    print(population)
    def fitness(ind : list):
        pass
        #fit = 

    pool = Pool(4)
    start_time = time.time()
    try:
        evaluated_population = pool.map(fitness, population)
    except:
        pass
    finally:
        pool.close()
        pool.join()

    evaluated_population.sort(key=lambda x: x[1])
    
    show_population(evaluated_population)
    
'''
conjunto: radio standart, luxo
dominio:
rs [0-24] -> 5 bits
rl [0-16] -> 5 bits

cromosomo: 10bits

rs + 2rl  =< 40

fitness: normalizacoao da FO das restricoes (H) e definicao do coeficiente de penalidade(r)

fit= FOn + rHn
r = -1

FOn = (30RS + 40RL)/1360

Hn = max(0, RS + 2RL - 40)/16
'''