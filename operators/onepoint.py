from crossover import CrossOver
import numpy as np

class OnePoint(CrossOver):

    def __init__(self, firstParent, secondParent):
        """Class responsible to handle one point crossover

        Arguments:
            firstParent {individual} -- first individual to be recombinated
            secondParent {individual} -- second individual to be recombinated
        """
        CrossOver.__init__(self, "One Point CrossOver", firstParent, secondParent)


    def make(self):
        """realize one point crossover

        Returns:
            individual; individual -- First child; second child. this is not used in group problem
        """
        position = np.random.randint(1, len(self.getFirstParent().getChromosome()))
        firstChild = np.append(self.getFirstParent().getChromosome()[0:position], self.getSecondParent().getChromosome()[position:])
        secondChild = np.append(self.getSecondParent().getChromosome()[0:position], self.getFirstParent().getChromosome()[position:])
        return firstChild, secondChild