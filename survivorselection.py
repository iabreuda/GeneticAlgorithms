import numpy as np
import math as m

class SurvivorSelection:

    def __init__(self, population, populationSize):
        self.population = population
        self.populationSize = populationSize

    def survivors(self, method='ageBased'):
        if method.lower() == 'agebased':
            return self.ageBased()
        elif method.lower() == 'fitnessbased':
            return self.fitnessBased()
        elif method.lower() == 'mixed':
            return self.mixed(fitnessBased, ageBased)
        else:
            raise NotImplementedError

    def ageBased(self):
        self.population.sort(key=lambda x: x.getGeneration(), reverse = True)
        return self.population[:self.populationSize]

    def fitnessBased(self):
        self.population.sort(key=lambda x: x.getFitness(), reverse = True)
        return self.population[:self.populationSize]
