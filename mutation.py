import numpy as np
import math as m

class Mutation:
    """Mutation probability should be consider for each gene in a chromosome"""

    def __init__(self, probability = 0.2):
        self.mutationGeneProbability = probability #Default Probability for SGA is 0.01

    def setHesserMutationGeneProbability(self, chromosomeLenght, populationSize, generationCounter, alfa=1, beta=1, gama=1):
        self.mutationGeneProbability = (m.sqrt(alfa/beta)*
            (m.exp((-1*gama*generationCounter)/2)/
            populationSize*m.sqrt(chromosomeLenght)))

    def setMutationGeneProbability(self, probability):
        self.mutationGeneProbability = probability

    def getMutationGeneProbability(self):
        return self.mutationGeneProbability

    def mutate(self, parent, method='swapMutation', lowerLimit=-100, upperLimit = 100, mean=0, deviation=1):
        if method.lower() == 'swapmutation':
            return self.swapMutation(parent)
        elif method.lower() == 'nonuniformgaussianmutation':
            return self.nonUniformGaussianMutation(parent, lowerLimit, upperLimit, mean, deviation)
        else:
            raise NotImplementedError

    def swapMutation(self, parent):
        if (np.random.rand() < self.getMutationGeneProbability()):
            mutatedChromosome = parent.getChromosome().copy()
            pos1, pos2 = np.random.randint(len(mutatedChromosome), size=2)
            firstPosition, secondPosition = mutatedChromosome[pos1], mutatedChromosome[pos2]
            mutatedChromosome[pos1], mutatedChromosome[pos2]  = secondPosition, firstPosition
            if (not np.array_equal(mutatedChromosome, parent.getChromosome())):
                return mutatedChromosome
        return None

    def uniformMutation(self, upperLimit, lowerLimit):
        child = self.parent.copy()
        for i in range(len(self.parent)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                child[i] = (upperLimit - lowerLimit)*(np.random.rand()) + lowerLimit
        if (child != self.parent):
            self.addChild(child)

    def nonUniformGaussianMutation(self, parent, lowerLimit, upperLimit, mean, deviation):
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

