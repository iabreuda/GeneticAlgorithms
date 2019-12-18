import numpy as np
import population as p

class Crossover:

    def __init__(self, probability=0.8803):
        """Class responsible to recombine to parents and make to childs

        Keyword Arguments:
            probability {float} -- Chance to do the crossover (default: {0.85})
        """
        self.crossoverProbability = probability

    def setCrossoverProbability(self, probability):
        """Define the probability to accept a recombnatin

        Arguments:
            probability {float} -- Probability to be accept
        """
        self.crossoverProbability = probability

    def getCrossoverProbability(self):
        """Get the current probability to make crossover between two parents

        Returns:
            [float] -- Crossover probability
        """
        return self.crossoverProbability

    def crossOver(self, firstParent, secondParent, thirdParent=None, base=None, factor = 1, method='onePointCrossOver'):
        """Generate two chromossomes from a parents recombination

        Arguments:
            firstParent {Individual} -- Instance of individual class
            secondParent {Individual} -- Instance of individual class

        Keyword Arguments:
            method {str} -- Choosed method (default: {'onePointCrossOver'})

        Raises:
            NotImplementedError: Thrown when a method has not implemented yet

        Returns:
            [Array] -- Chromossome array for the two childs
        """
        if method.lower() == 'decrossover': #No needed to check probability before
            return self.DECrossOver(firstParent, secondParent, thirdParent, base, factor)
        if (np.random.rand() > self.crossoverProbability):
            return None, None
        if method.lower() == 'onepointcrossover':
            return self.onePointCrossOver(firstParent, secondParent)
        elif method.lower() == 'simplerecombination':
            return self.simpleRecombination(firstParent, secondParent)
        elif method.lower() == 'singlearithmeticrecombination':
            return self.singleArithmeticRecombination(firstParent, secondParent)
        elif method.lower() == 'wholearithmeticrecombination':
            return self.wholeArithmeticRecombination(firstParent, secondParent)
        else:
            raise NotImplementedError

    def onePointCrossOver(self, firstParent, secondParent):
        """One point crossover Method described in Pg49 of text book

        Arguments:
            firstParent {Individual} -- Instance of individual class
            secondParent {Individual} -- Instance of individual class

        Returns:
            [Array] -- Chromossome array for the two childs
        """
        position = np.random.randint(1, len(firstParent.getChromosome()))
        firstChild = np.append(firstParent.getChromosome()[0:position], secondParent.getChromosome()[position:])
        secondChild = np.append(secondParent.getChromosome()[0:position], firstParent.getChromosome()[position:])
        return firstChild, secondChild

    def simpleRecombination(self, firstParent, secondParent):
        """Simple recombination Method described in Pg50 of text book

        Arguments:
            firstParent {Individual} -- Instance of individual class
            secondParent {Individual} -- Instance of individual class

        Returns:
            [Array] -- Chromossome array for the two childs
        """
        position = np.random.randint(1, len(firstParent.getChromosome()))
        multiplier = np.random.rand()
        firstChild = []
        secondChild = []
        for gene in range(len(firstParent.getChromosome())):
            if (gene >= position):
                firstChild.append(
                    (firstParent.getChromosome()[gene] + secondParent.getChromosome()[gene]) * (multiplier)
                )
                secondChild.append(
                    (firstParent.getChromosome()[gene] + secondParent.getChromosome()[gene]) * (1 - multiplier)
                )
            else:
                firstChild.append(firstParent.getChromosome()[gene])
                secondChild.append(secondParent.getChromosome()[gene])
        return firstChild, secondChild

    def singleArithmeticRecombination(self, firstParent, secondParent):
        """Single Arithmetich recombination Method described in Pg50 of text book

        Arguments:
            firstParent {Individual} -- Instance of individual class
            secondParent {Individual} -- Instance of individual class

        Returns:
            [Array] -- Chromossome array for the two childs
        """
        position = np.random.randint(1, len(firstParent.getChromosome()))
        multiplier = np.random.rand()
        firstChild = []
        secondChild = []
        for gene in range(len(firstParent.getChromosome())):
            if (gene == position):
                firstChild.append(
                    (firstParent.getChromosome()[gene] + secondParent.getChromosome()[gene]) * (multiplier)
                )
                secondChild.append(
                    (firstParent.getChromosome()[gene] + secondParent.getChromosome()[gene]) * (1 - multiplier)
                )
            else:
                firstChild.append(firstParent.getChromosome()[gene])
                secondChild.append(secondParent.getChromosome()[gene])
        return firstChild, secondChild

    def wholeArithmeticRecombination(self, firstParent, secondParent):
        """Whole Arithmetic recombination Method described in Pg51 of text book

        Arguments:
            firstParent {Individual} -- Instance of individual class
            secondParent {Individual} -- Instance of individual class

        Returns:
            [Array] -- Chromossome array for the two childs
        """
        multiplier = np.random.rand()
        firstChild = []
        secondChild = []
        for gene in range(len(firstParent.getChromosome())):
            firstChild.append(
                (firstParent.getChromosome()[gene] + secondParent.getChromosome()[gene]) * (multiplier)
            )
            secondChild.append(
                (firstParent.getChromosome()[gene] + secondParent.getChromosome()[gene]) * (1 - multiplier)
            )
        return firstChild, secondChild

    def DECrossOver(self, firstAgent, secondAgent, thirdAgent, base, factor):
        newChromosome = base.getChromosome().copy()
        chromosomeLen = len(base.getChromosome())
        position = np.random.randint(chromosomeLen)
        for gene in range(chromosomeLen):
            if np.random.rand() < self.getCrossoverProbability() or gene == position:
                newChromosome[gene] = firstAgent.getChromosome()[gene] + factor*(secondAgent.getChromosome()[gene] - thirdAgent.getChromosome()[gene])
        return newChromosome
