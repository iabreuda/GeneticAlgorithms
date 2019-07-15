import numpy as np
import math as m

class Mutation:
    """Mutation probability should be consider for each gene in a chromosome"""

    def __init__(self, children, probability = 0.001):
        self.parent = []
        self.children = children
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
        child = self.parent.copy()
        for i in range(len(self.parent)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                child[i] = (upperLimit - lowerLimit)*(np.random.rand()) + lowerLimit
        if (child != self.parent):
            self.addChild(child)

    def swapMutation(self):
        child = self.parent.copy()
        if (np.random.rand() < self.getMutationGeneProbability()):
            pos1, pos2 = np.random.randint(len(child), size=2)
            firstPosition, secondPosition = child[pos1], child[pos2]
            child[pos1], child[pos2]  = secondPosition, firstPosition
        if (child != self.parent):
            self.addChild(child)

    def nonUniformGaussianMutation(self, mean=0, deviation=1, lowerLimit=-100, upperLimit= 100):
        child = self.parent.copy()
        for i in range(len(self.parent)):
            if (np.random.rand() < self.getMutationGeneProbability()):
                child[i] += np.random.normal(mean, deviation)
                if (child[i] < lowerLimit):
                    child[i] = lowerLimit
                elif (child[i] > upperLimit):
                    child[i] = upperLimit

        if (np.array_equal(child,self.parent)):
            self.addChild(child)


if __name__ == "__main__":
    x = [1.7,2.9,-10,-87.5,16.9,50,-48.7,-34.61,74.7,99.9]
    children = []
    m = Mutation(children)
    m.setParent(x)
    m.setMutationGeneProbability(0.8)
    #m.uniformMutation(-100, 100)

    m.nonUniformGaussianMutation()
    print(m.getChildren())



