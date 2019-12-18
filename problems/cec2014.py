from problem import Problem
import sys
sys.path.append('..')
import individual as i
import numpy as np

class CEC2014(Problem):

    def __init__(self, dimension=10, lowerLimit=-100, upperLimit=100, initialPopulation=50):
        """This class handle problems from CEC2014 competion it is used to test algoritmhs and isn't related with
        group problem

        Keyword Arguments:
            dimension {int} -- number of problem's variable (default: {10})
            lowerLimit {int} -- lower limit in search space (default: {-100})
            upperLimit {int} -- upper limit in search space (default: {100})
            initialPopulation {int} -- size of initial solutions (default: {50})
        """

        self.dimension = dimension
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.initialPopulation = initialPopulation
        self.population = []

    def getDimension(self):
        """Current number of dimensions

        Returns:
            [Integer] -- [Number of problem dimension]
        """
        return self.dimension

    def setDimension(self, dimension):
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

    def initialSolution(self):
        """Initialize problem solutions

        Returns:
            array -- Array of individuals in initial solution
        """
        self.setPopulation()
        return self.getPopulation()
