import numpy as np
import individual as i

class Population:

    def __init__(self, dimension, lowerLimit, upperLimit, initialPopulation):
        self.dimension = dimension
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.initialPopulation = initialPopulation
        self.population = []
        self.setPopulation()

    def getDimension(self):
        return self.dimension

    def setDimentison(self, dimension):
        self.dimension = dimension

    def getLowerLimit(self):
        return self.lowerLimit

    def setLowerLimit(self, lowerLimit):
        self.lowerLimit = lowerLimit

    def getUpperLimit(self):
        return self.upperLimit

    def setUpperLimit(self, upperLimit):
        self.upperLimit = upperLimit

    def getInitialPopulation(self):
        return self.initialPopulation

    def setInitialPopulation(self, initialPopulation):
        self.initialPopulation = initialPopulation

    def setPopulation(self):
        population = (self.getUpperLimit() - self.getLowerLimit())*(np.random.rand(self.initialPopulation, self.dimension)) + self.lowerLimit
        individuals = []
        for chromosome in population:
            individual = i.Individual(chromosome)
            individuals.append(individual)
        self.population = individuals

    def getPopulation(self):
        return self.population


if __name__ == "__main__":
    pop = Population(dimension=10, lowerLimit=-100, upperLimit=100, initialPopulation=2)
    print("Initial Population:\n", pop.getPopulation())
