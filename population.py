import numpy as np

class Population:

    def __init__(self, dimension, lowerLimit, upperLimit, initialPopulation):
        self.dimension = dimension
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.initialPopulation = initialPopulation

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

    def createPopulation(self):
        return (self.getUpperLimit() - self.getLowerLimit())*(np.random.rand(self.initialPopulation, self.dimension)) + self.lowerLimit


if __name__ == "__main__":
    pop = Population(dimension=10, lowerLimit=-100, upperLimit=100, initialPopulation=2)
    print("Initial Population:\n", pop.createPopulation())
