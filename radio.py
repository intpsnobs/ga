import galapagos
from galapagos.utils import binaryToInt
from numpy import ndarray
from galapagos.selector import fitness_proportionate_selection

# Problema do Radio
# 40 funcionarios
# S = Radio Standard: 1/dia -> R$30 (Restricao: max 24 funcionarios)
# L = Radio Luxo: 2/dia -> R$40 (Restricao: max 32 funcionarios)
# f(x) =


def fitness(ind: ndarray):
    xrl = binaryToInt(ind[:len(ind)//2])
    xrs = binaryToInt(ind[len(ind)//2:])
    # rs [0-24] -> 5 bits
    # rl [0-16] -> 5 bits
    rl = 0+(16/31)*xrl
    rs = 0+(24/31)*xrs

    r = -1
    FOn = (30*rs + 40*rl)/1360
    Hn = max(0, rs + 2*rl - 40)/16
    fit = FOn + r*Hn

    return ind, fit


if __name__ == "__main__":
    galapagos.run(
        fitness,
        selector=fitness_proportionate_selection,
        config_file="radio.cfg"
    )


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
