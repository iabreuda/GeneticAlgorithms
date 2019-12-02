class CrossOver(object):

    def __init__(self, name, firstParent, secondParent, crossOverProbability = 0.85):
        self.firstParent = firstParent
        self.secondParent = secondParent
        self.crossOverProbability = crossOverProbability
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getFirstParent(self):
        return self.firstParent

    def setFirstParent(self, firstParent):
        self.firstParent = firstParent

    def getSecondParent(self):
        return self.secondParent

    def setSecondParent(self, secondParent):
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
            [float] -- Crossover probability
        """
        return self.crossoverProbability

    def make(self):
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")





