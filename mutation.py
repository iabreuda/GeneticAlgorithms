import numpy as np
import math as m

class Mutation:
    """Mutation probability should be consider for each gene in a chromosome"""

    def __init__(self, parent, probability = 0.001):
        self.parent = parent
        self.child = self.parent.copy()
        self.children = []
        self.mutationGeneProbability = probability #Default Probability for SGA is 0.001

    def setHesserMutationGeneProbability(self, chromosomeLenght, populationSize, generationCounter, alfa=1, beta=1, gama=1):
        self.mutationGeneProbability = (m.sqrt(alfa/beta)*
            (m.exp((-1*gama*generationCounter)/2)/
            populationSize*m.sqrt(chromosomeLenght)))

    def setMutationGeneProbability(self, probability):
        self.mutationGeneProbability = probability

    def getMutationGeneProbability(self):
        return self.mutationGeneProbability

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def uniformMutation(self, upperLimit, lowerLimit):
        for i in range(len(self.parent)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                self.child[i] = (upperLimit - lowerLimit)*(np.random.rand()) + lowerLimit
        if (self.child != self.parent):
            self.addChild(self.child)

    def swapMutation(self):
        if (np.random.rand() < self.getMutationGeneProbability()):
            pos1, pos2 = np.random.randint(len(self.child), size=2)
            firstPosition, secondPosition = self.child[pos1], self.child[pos2]
            self.child[pos1], self.child[pos2]  = secondPosition, firstPosition
        if (self.child != self.parent):
            self.addChild(self.child)

    def nonUniformGaussianMutation(self, mean=0, deviation=1, lowerLimit=-100, upperLimit= 100):
        for i in range(len(self.parent)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                self.child[i] += np.random.normal(mean, deviation)
                if (self.child[i] < lowerLimit):
                    self.child[i] = lowerLimit
                elif (self.child[i] > upperLimit):
                    self.child[i] = upperLimit
        if (self.child != self.parent):
            self.addChild(self.child)


if __name__ == "__main__":
    x = [1.7,2.9,-10,-87.5,16.9,50,-48.7,-34.61,74.7,99.9]
    m = Mutation(x)
    m.setMutationGeneProbability(0.8)
    #m.uniformMutation(-100, 100)

    m.nonUniformGaussianMutation()
    print(m.getChildren())



