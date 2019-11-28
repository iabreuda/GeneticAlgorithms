import numpy as np
import individual as i

class Individual:

    def __init__(self, chromosome, generation = 0, fitness = 0):
        """Class responsible to create a new individual

        Arguments:
            chromosome {Array} -- Array of N dimension

        Keyword Arguments:
            generation {int} -- [When the individuo was generated] (default: {0})
            fitness {float} -- [Fitness of the individuo] (default: {0})
        """
        self.generation = generation
        self.chromosome = chromosome
        self.fitness = fitness
        self.rank = None
        self.choosedProbability = None
        self.factor = None
        self.crossProbability = None

    def setFactor(self, factor):
        """Define factor of the individuo creation

        Arguments:
            factor {[Integer]} -- [Number of individuo factor]
        """
        self.factor = factor

    def getFactor(self):
        """Get factor for this individuo

        Returns:
            [integer] -- [factor number like an year]
        """
        return self.factor

    def setCrossProbability(self, crossProbability):
        """Define crossProbability of the individuo creation

        Arguments:
            crossProbability {[Integer]} -- [Number of individuo crossProbability]
        """
        self.crossProbability = crossProbability

    def getCrossProbability(self):
        """Get crossProbability for this individuo

        Returns:
            [integer] -- [crossProbability number like an year]
        """
        return self.crossProbability

    def setGeneration(self, generation):
        """Define generation of the individuo creation

        Arguments:
            generation {[Integer]} -- [Number of individuo generation]
        """
        self.generation = generation

    def getGeneration(self):
        """Get generation for this individuo

        Returns:
            [integer] -- [Generation number like an year]
        """
        return self.generation

    def setChromosome(self, chromosome):
        """Define individual chromosome

        Arguments:
            chromosome {Array} -- [N dimension array]
        """
        self.chromosome = chromosome

    def getChromosome(self):
        """Get individual chromossome

        Returns:
            [Array] -- [Return an array containing individual chromossome]
        """
        return self.chromosome

    def setFitness(self, fitness):
        """Cost Function result

        Arguments:
            fitness {[float]} -- [Individual cost function result]
        """
        self.fitness = fitness

    def getFitness(self):
        """Get individual cost

        Returns:
            [float] -- [Cost of this individual]
        """
        return self.fitness

    def setRank(self, rank):
        """set a Position of this individual related to other in a populaton

        Arguments:
            rank {integer} -- [Where this individual is in a population fitness rank]
        """
        self.rank = rank

    def getRank(self):
        """Get individual rank

        Returns:
            [integer] -- [Individual rank position]
        """
        return self.rank

    def setChoosedProbability(self, choosedProbability):
        """Define a probability to the individual be choosed in a population
        the sum of probability for all individual in a population should be normalized

        Arguments:
            choosedProbability {float} -- [Selected Probability]
        """
        self.choosedProbability = choosedProbability

    def getChoosedProbability(self):
        """Get Probability to be selected in a population

        Returns:
            [float] -- [Probability to be selected]
        """
        return self.choosedProbability
