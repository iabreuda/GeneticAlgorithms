from crossover import CrossOver
import numpy as np

class OnePoint(CrossOver):

    def __init__(self, firstParent, secondParent):
        CrossOver.__init__(self, "One Point CrossOver", firstParent, secondParent)


    def make(self):
        position = np.random.randint(1, len(self.getFirstParent().getChromosome()))
        firstChild = np.append(self.getFirstParent().getChromosome()[0:position], self.getSecondParent().getChromosome()[position:])
        secondChild = np.append(self.getSecondParent().getChromosome()[0:position], self.getFirstParent().getChromosome()[position:])
        return firstChild, secondChild