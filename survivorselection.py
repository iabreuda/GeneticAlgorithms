import numpy as np
import math as m

class SurvivorSelection:

    def __init__(self, population, populationSize):
        """This class is responsible to select who will survive for next generation

        Arguments:
            population {Array} -- [The whole population for this generation]
            populationSize {Integer} -- [Number of individuals wanted in next generation]
        """
        self.population = population
        self.populationSize = populationSize

    def survivors(self, method='ageBased'):
        """Choose de survivor method to be used

        Keyword Arguments:
            method {str} -- Choosed method (default: {'ageBased'})

        Raises:
            NotImplementedError: Thrown when a method has not implemented yet

        Returns:
            [list] -- List of individuals to next generation
        """
        if method.lower() == 'agebased':
            return self.ageBased()
        elif method.lower() == 'fitnessbased':
            return self.fitnessBased()
        else:
            raise NotImplementedError

    def ageBased(self):
        """Survive youngest individuals

        Returns:
            [Array] -- Survivors for the next generation
        """
        self.population.sort(key=lambda x: x.getGeneration(), reverse = True)
        return self.population[:self.populationSize]

    def fitnessBased(self):
        """Survive youngest individuals

        Returns:
            [Array] -- Survivors for the next generation
        """
        self.population.sort(key=lambda x: x.getFitness(), reverse = True)
        return self.population[:self.populationSize]
