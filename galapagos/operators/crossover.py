import numpy as np


def one_point(parent1, parent2):
    index = int(np.random.uniform(low=1, high=len(parent1)-1))
    return [np.hstack([parent1[:index], parent2[index:]]), np.hstack([parent2[:index], parent1[index:]])]

def two_points(parent1, parent2):
    index = int(np.random.uniform(low=1, high=len(parent1)-1))
    return [np.hstack([parent1[:index], parent2[index:]]), np.hstack([parent2[:index], parent1[index:]])]
# manda um zapper as 3 da manha, a essa hora quero estar no 18 sonokkkkkkk sou um novo homem
# agora eu durmo eu deveria estar na cama ja mamae vai brigar ;-; :'( eu tbm bo mimi amanha a 
# gente ve isso mokandamos uma msg ja esclarece bastante okok xoxoxo xoxo <3 boa noite  git push
# taD:
print(one_point(np.array([1, 1, 1, 1, 1, 1, 1],dtype="uint8"), np.array([0, 0, 0, 0, 0, 0, 0],dtype="uint8")))


#WOLOLO q? boa noite fazendo commit, ok. to vazano, faro faro