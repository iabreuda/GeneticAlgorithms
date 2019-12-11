import numpy as np

class Population(object):

    def __init__(self, individuals, generation):
        """Create a population sample

        Arguments:
            dimension {integer} -- [Number of problems dimension]
            lowerLimit {float} -- [lower limit]
            upperLimit {float} -- [Upper limit]
            initialPopulation {integer} -- [Number of individuals in initial populaton]
        """
        self.individuals = individuals
        self.generation = generation

    def getGeneration(self):
        return self.generation

    def setGeneration(self, generation):
        self.generation = generation

    def getIndividuals(self):
        return self.individuals

    def setIndividuals(self, individuals):
        self.individuals = individuals

    def getGenerationalStatistics(self):
        fitness = []
        for individuo in self.individuals:
            fitness.append(individuo.getFitness())
        np_arr = np.array(fitness)

        best = np.amax(np_arr)
        avarage = np.mean(np_arr)
        worst = np.amin(np_arr)
        median = np.median(np_arr)
        std = np.std(np_arr)

        print("Gen: ", self.generation, " Best: ", best, " Worst: ", worst, " Avg: ", avarage , " Median: ", median, " Std:", std)