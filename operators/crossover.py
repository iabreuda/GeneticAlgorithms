class CrossOver(object):
    def __init__(self, name, firstParent, secondParent, crossOverProbability = 0.85):
        """class responsible to handle crossover operations

        Arguments:
            object {[type]} -- [description]
            name {string} -- name of crossover operation
            firstParent {individuo} -- first individuo to cross
            secondParent {individuo} -- second individuo to cross

        Keyword Arguments:
            crossOverProbability {float} -- probability to cross these two individuals (default: {0.85})
        """
        self.firstParent = firstParent
        self.secondParent = secondParent
        self.crossOverProbability = crossOverProbability
        self.name = name

    def getName(self):
        """get name of crossover operation

        Returns:
            string -- name of crossover operation
        """
        return self.name

    def setName(self, name):
        """define crossover name

        Arguments:
            name {string} -- name of crossover operation
        """
        self.name = name

    def getFirstParent(self):
        """get first parent

        Returns:
            individuo -- second individuo to realize crossover
        """
        return self.firstParent

    def setFirstParent(self, firstParent):
        """define first parent to realize crossover

        Arguments:
            firstParent {individuo} -- individuo to realize crossover
        """
        self.firstParent = firstParent

    def getSecondParent(self):
        """get second parent

        Returns:
            individuo -- second individuo to realize crossover
        """
        return self.secondParent

    def setSecondParent(self, secondParent):
        """define second parent to realize crossover

        Arguments:
            secondParent {individuo} -- individuo to realize crossover
        """
        self.secondParent = secondParent

    def setCrossoverProbability(self, probability):
        """Define the probability to accept a recombnatin

        Arguments:
            probability {float} -- Probability to be accept
        """
        self.crossoverProbability = probability

    def getCrossoverProbability(self):
        """Get the current probability to make crossover between two parents

        Returns:
            float -- Crossover probability
        """
        return self.crossOverProbability

    def make(self):
        """Child class must implement this method in order to make crossover

        Raises:
            NotImplementedError: When a child doesn't implement this method
        """
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")





