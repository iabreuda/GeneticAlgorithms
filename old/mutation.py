import numpy as np
import math as m

class Mutation:

    def __init__(self, probability = 0.01):
        """Class renponsible to handle mutation

        Keyword Arguments:
            probability {float} -- [Mutation probability should be consider for each gene in a chromosome] (default: {0.01})
        """
        self.mutationGeneProbability = probability #Default Probability for SGA is 0.01

    def setHesserMutationGeneProbability(self, chromosomeLenght, populationSize, generationCounter, alfa=1, beta=1, gama=1):
        """This is a probability to change a gene changing by generation

        Arguments:
            chromosomeLenght {[integer]} -- [Dimension of problem]
            populationSize {[integer]} -- [Popuplation size]
            generationCounter {[integer]} -- [Year of generation]

        Keyword Arguments:
            alfa {float} -- [Constant] (default: {1})
            beta {float} -- [Constant] (default: {1})
            gama {float} -- [Constant] (default: {1})
        """
        self.mutationGeneProbability = (m.sqrt(alfa/beta)*
            (m.exp((-1*gama*generationCounter)/2)/
            populationSize*m.sqrt(chromosomeLenght)))

    def setMutationGeneProbability(self, probability):
        """[Define a probability to change a gene]

        Arguments:
            probability {[float]} -- [probability to change a gene]
        """
        self.mutationGeneProbability = probability

    def getMutationGeneProbability(self):
        """[Get gene mutation probability]

        Returns:
            [float] -- [Gene mutation probability]
        """
        return self.mutationGeneProbability

    def mutate(self, parent, method='swapMutation', lowerLimit=-100, upperLimit = 100, mean=0, deviation=1):
        """[Generate a chromossomes from a parents recombination]

        Arguments:
            parent {[individual]} -- [Instance of individual class]

        Keyword Arguments:
            method {str} -- [Choosed Method] (default: {'swapMutation'})
            lowerLimit {float} -- [Lower limit] (default: {-100})
            upperLimit {float} -- [Upper limit] (default: {100})
            mean {float} -- [Gauss mean] (default: {0})
            deviation {float} -- [Gauss deviatin] (default: {1})

        Raises:
            NotImplementedError: Thrown when a method has not implemented yet

        Returns:
            [Array] -- Chromossome array for a childs
        """
        if method.lower() == 'swapmutation':
            return self.swapMutation(parent)
        elif method.lower() == 'nonuniformgaussianmutation':
            return self.nonUniformGaussianMutation(parent, lowerLimit, upperLimit, mean, deviation)
        elif method.lower() == 'uniformmutation':
            return self.uniformMutation(parent, lowerLimit, upperLimit)
        else:
            raise NotImplementedError

    def swapMutation(self, parent):
        """swap Mutation Method described in Pg45 of text book

        Arguments:
            parent {[Individual]} -- [Instance of individual class]

        Returns:
            [Array] -- Chromossome array for a childs
        """
        if (np.random.rand() < self.getMutationGeneProbability()):
            mutatedChromosome = parent.getChromosome().copy()
            pos1, pos2 = np.random.randint(len(mutatedChromosome), size=2)
            firstPosition, secondPosition = mutatedChromosome[pos1], mutatedChromosome[pos2]
            mutatedChromosome[pos1], mutatedChromosome[pos2]  = secondPosition, firstPosition
            if (not np.array_equal(mutatedChromosome, parent.getChromosome())):
                return mutatedChromosome
        return None

    def uniformMutation(self, parent, lowerLimit, upperLimit):
        """Uniforme Mutation Method described in Pg44 of text book

        Arguments:
            parent {[Individual]} -- [Instance of individual class]
            lowerLimit {[float]} -- [Lower limit]
            upperLimit {[float]} -- [Upper limit]

        Returns:
            [Array] -- Chromossome array for a childs
        """
        mutatedChromosome = parent.getChromosome().copy()
        for i in range(len(mutatedChromosome)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                mutatedChromosome[i] = (upperLimit - lowerLimit)*(np.random.rand()) + lowerLimit
        if (not np.array_equal(mutatedChromosome, parent.getChromosome())):
            return mutatedChromosome
        return None

    def nonUniformGaussianMutation(self, parent, lowerLimit, upperLimit, mean, deviation):
        """Non Uniforme Mutation Method described in Pg44 of text book

        Arguments:
            parent {[Individual]} -- [Instance of individual class]
            lowerLimit {[float]} -- [Lower limit]
            upperLimit {[float]} -- [Upper limit]
            mean {[float]} -- [Gaussian mean]
            deviation {[foat]} -- [Gaussian deviation]

        Returns:
            [Array] -- Chromossome array for a childs
        """
        mutatedChromosome = parent.getChromosome().copy()
        for i in range(len(mutatedChromosome)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                mutatedChromosome[i] += np.random.normal(mean, deviation)
                if (mutatedChromosome[i] < lowerLimit):
                    mutatedChromosome[i] = lowerLimit
                elif (mutatedChromosome[i] > upperLimit):
                    mutatedChromosome[i] = upperLimit
        if (not np.array_equal(mutatedChromosome, parent.getChromosome())):
            return mutatedChromosome
        return None

