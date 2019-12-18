class Selection(object):
    def __init__(self, name, population, numberOfSelections):
        """Base Class for selection methods

        Arguments:
            name {string} -- Method's name
            population {array} -- Array with individuals
            numberOfSelections {integer} -- Number of individuals to be selected
        """
        self.population = population
        self.name = name
        self.numberOfSelections = numberOfSelections
        self.selecteds = []
        self.ranking()

    def getNumberOfSelections(self):
        """Get number of selections

        Returns:
            integer -- Number of individuals to be selected
        """
        return self.numberOfSelections

    def setNumberOfSelections(self, numberOfSelections):
        """Changes number of selections in run time

        Arguments:
            numberOfSelections {integer} -- Number of individuals to be selected
        """
        self.numberOfSelections = numberOfSelections

    def getPopulation(self):
        """Get population array

        Returns:
            array -- List of all individuals in this population
        """
        return self.population

    def setPopulation(self, population):
        """Define a new population array

        Arguments:
            population {array} -- Change population in run time
        """
        self.population = population

    def ranking(self):
        """Sort populate by fitness where rank 1 has lowest fitness and the highest rank has the highest fitness
        """
        self.population.sort(key=lambda x: x.getFitness()) #Sort Individuo by Fitness
        for individuo in self.population:
            individuo.setRank(self.population.index(individuo) + 1)

    def select(self):
        """Child class must implement this method

        Raises:
            NotImplementedError: When a child doesn't implement this method
        """
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")