class Selection(object):

    def __init__(self, name, population, numberOfSelections):
        """This class is responsible to select parent to generate children for next generation

        Arguments:
            population {Array} -- [The whole population for this generation]
            numberOfParents {Integer} -- [Number of parents to be select in order to generate next offspring]

        Keyword Arguments:
            method {str} -- [Method to calculate normalized probability for each parent] (default: {'fitnessProportional'})
        """
        self.population = population
        self.name = name
        self.numberOfSelections = numberOfSelections
        self.selecteds = []
        self.ranking()

    def getNumberOfSelections(self):
        return self.numberOfSelections

    def setNumberOfSelections(self, numberOfSelections):
        self.numberOfSelections = numberOfSelections

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    def ranking(self):
        """Sort populate by fitness where rank 1 has lowest fitness and the highest rank has the highest fitness
        """
        self.population.sort(key=lambda x: x.getFitness()) #Sort Individuo by Fitness
        for individuo in self.population:
            individuo.setRank(self.population.index(individuo) + 1)

    def select(self):
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")