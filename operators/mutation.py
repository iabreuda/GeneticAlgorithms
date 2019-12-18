import numpy as np
import math as m

class Mutation(object):
    def __init__(self, name, parent, probability = 0.01):
        """Classe responsible to handle mutation

        Arguments:
            name {string} -- Method's name
            parent {individual} -- individual to be mutated

        Keyword Arguments:
            probability {float} -- Mutation probability should be consider for each gene in a chromosome (default: {0.01})
        """
        self.mutationGeneProbability = probability #Default Probability for SGA is 0.01
        self.parent = parent
        self.name = name

    def getName(self):
        """get method's name

        Returns:
            string -- name of mutation method
        """
        return self.name

    def setName(self, name):
        """set name of mutation method

        Arguments:
            name {string} -- name of mutation method
        """
        self.name = name

    def getParent(self):
        """get parent to be mutated

        Returns:
            indivdual -- individual to be mutated
        """
        return self.parent

    def setParent(self, parent):
        """define individual to be mutated

        Arguments:
            parent {individual} -- individual to be mutated
        """
        self.parent = parent

    def setMutationGeneProbability(self, probability):
        """[Define a probability to change a gene]

        Arguments:
            probability {[float]} -- [probability to change a gene]
        """
        self.mutationGeneProbability = probability

    def getMutationGeneProbability(self):
        """[Get gene mutation probability]

        Returns:
            [float] -- [Gene mutation probability]
        """
        return self.mutationGeneProbability

    def make(self):
        """Child class must implement this method in order to make mutation

        Raises:
            NotImplementedError: When a child doesn't implement this method
        """
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")
