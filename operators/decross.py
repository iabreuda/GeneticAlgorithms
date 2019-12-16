from crossover import CrossOver
import numpy as np
import sys
sys.path.append('../problems')
from group import Group
from individual import Individual

class DECross(CrossOver):

    def __init__(self, firstParent, secondParent, co=0.8):
        CrossOver.__init__(self, "DE CrossOver", firstParent, secondParent) #First parent is Base Individuo and Second is Trial Vector
        self.co = co


    def make(self):
        chromosomeLen = len(self.firstParent.getChromosome())
        childChromosome = np.zeros(chromosomeLen)
        position = np.random.randint(chromosomeLen)
        for gene in range(chromosomeLen):
            if np.random.rand() < self.co or gene == position:
                childChromosome[gene] = self.secondParent.getChromosome()[gene]
            else:
                childChromosome[gene] = self.firstParent.getChromosome()[gene]

        child = Individual(childChromosome)

        return child
