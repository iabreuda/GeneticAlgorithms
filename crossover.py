import numpy as np
import population as p

class Crossover:

    def __init__(self, probability=0.85):
        self.crossoverProbability = probability

    def setCrossoverProbability(self, probability):
        self.crossoverProbability = probability

    def getCrossoverProbability(self):
        return self.crossoverProbability

    def crossOver(self, firstParent, secondParent, method='onePointCrossOver'):
        if (np.random.rand() > self.crossoverProbability):
            return None, None
        if method.lower() == 'onepointcrossover':
            return self.onePointCrossOver(firstParent, secondParent)
        else:
            raise NotImplementedError

    def onePointCrossOver(self, firstParent, secondParent):
        position = np.random.randint(1, len(firstParent.getChromosome()))
        firstChild = np.append(firstParent.getChromosome()[0:position], secondParent.getChromosome()[position:])
        secondChild = np.append(secondParent.getChromosome()[0:position], firstParent.getChromosome()[position:])
        return firstChild, secondChild

if __name__ == "__main__":
    children = []

