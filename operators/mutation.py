import numpy as np
import math as m

class Mutation(object):

    def __init__(self, name, parent, probability = 0.01):
        """Class renponsible to handle mutation

        Keyword Arguments:
            probability {float} -- [Mutation probability should be consider for each gene in a chromosome] (default: {0.01})
        """
        self.mutationGeneProbability = probability #Default Probability for SGA is 0.01
        self.parent = parent
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getParent(self):
        return self.parent

    def setParent(self, parent):
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
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")
