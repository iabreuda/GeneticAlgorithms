import numpy as np
import individual as i

class Individual:

    def __init__(self, chromosome, generation = 0, fitness = 0):
        self.generation = generation
        self.chromosome = chromosome
        self.fitness = fitness
        self.rank = None
        self.choosedProbability = None

    def setGeneration(self, generation):
        self.generation = generation

    def getGeneration(self):
        return self.generation

    def setChromosome(self, chromosome):
        self.chromosome = chromosome

    def getChromosome(self):
        return self.chromosome

    def setFitness(self, fitness):
        self.fitness = fitness

    def getFitness(self):
        return self.fitness[0]

    def setRank(self, rank):
        self.rank = rank

    def getRank(self):
        return self.rank

    def setChoosedProbability(self, choosedProbability):
        self.choosedProbability = choosedProbability

    def getChoosedProbability(self):
        return self.choosedProbability
