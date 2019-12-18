import numpy as np

class Population(object):
    def __init__(self, individuals, generation):
        """Class that handle population

        Arguments:
            individuals {array} -- Array containing individuals
            generation {int} -- Generation number
        """
        self.individuals = individuals
        self.generation = generation

    def getGeneration(self):
        """get generation

        Returns:
            int -- generation number
        """
        return self.generation

    def setGeneration(self, generation):
        """define generation number

        Arguments:
            generation {int} -- generation number
        """
        self.generation = generation

    def getIndividuals(self):
        """all individuals in population

        Returns:
            array -- array containing individuals
        """
        return self.individuals

    def setIndividuals(self, individuals):
        """define population

        Arguments:
            individuals {array} -- array containing individuals
        """
        self.individuals = individuals

    def getGenerationalStatistics(self):
        """Print statistics for each generation
        """
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