import numpy as np
import individual as i

class Population:

    def __init__(self, dimension, lowerLimit, upperLimit, initialPopulation):
        """Create a population sample

        Arguments:
            dimension {integer} -- [Number of problems dimension]
            lowerLimit {float} -- [lower limit]
            upperLimit {float} -- [Upper limit]
            initialPopulation {integer} -- [Number of individuals in initial populaton]
        """
        self.dimension = dimension
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.initialPopulation = initialPopulation
        self.population = []
        self.setPopulation()

    def getDimension(self):
        """Current number of dimensions

        Returns:
            [Integer] -- [Number of problem dimension]
        """
        return self.dimension

    def setDimentison(self, dimension):
        """Define a new number of dimensions

        Arguments:
            dimension {integer} -- [Number of elements in chromosome array]
        """
        self.dimension = dimension

    def getLowerLimit(self):
        """Get Inferior limit

        Returns:
            [float] -- inferior limit
        """
        return self.lowerLimit

    def setLowerLimit(self, lowerLimit):
        """Define a new lower limit

        Arguments:
            lowerLimit {float} -- [New lower limit]
        """
        self.lowerLimit = lowerLimit

    def getUpperLimit(self):
        """Get superior limit

        Returns:
            [float] -- superior limit
        """
        return self.upperLimit

    def setUpperLimit(self, upperLimit):
        """Define a new upper limit

        Arguments:
            upperLimit {float} -- [New upper limit]
        """
        self.upperLimit = upperLimit

    def getInitialPopulation(self):
        """Get number of individuals in initial population

        Returns:
            [integer] -- number of individuals in initial population
        """
        return self.initialPopulation

    def setInitialPopulation(self, initialPopulation):
        """Define size of initial population

        Arguments:
            initialPopulation {integer} -- Size of initial population
        """
        self.initialPopulation = initialPopulation

    def setPopulation(self):
        """Create a random population using parameters of this class
        """
        population = (self.getUpperLimit() - self.getLowerLimit())*(np.random.rand(self.initialPopulation, self.dimension)) + self.lowerLimit
        individuals = []
        for chromosome in population:
            individual = i.Individual(chromosome)
            individuals.append(individual)
        self.population = individuals

    def getPopulation(self):
        """Get a population

        Returns:
            [Array] -- Array of individuals
        """
        return self.population

