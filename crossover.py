import numpy as np
import population as p

class Crossover:

    def __init__(self, children, probability=0.85):
        self.firstParent = []
        self.secondParent = []
        self.crossoverProbability = probability
        self.children = children

    def setFirstParent(self, parent):
        self.firstParent = parent

    def getFirstParent(self):
        return self.firstParent

    def setSecondParent(self, parent):
        self.secondParent = parent

    def getSecondParent(self):
        return self.secondParent

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children

    def getCrossoverProbability(self):
        return self.crossoverProbability

    def makeCrossOver(self, method='onePointCrossOver', verbose=False):
        if method.lower() == 'onepointcrossover':
            return self.onePointCrossOver(verbose=verbose)
        else:
            raise NotImplementedError

    def onePointCrossOver(self, verbose=False):
        position = np.random.randint(1, len(self.firstParent))
        print ('Onepoint Crossover position: ', position) if verbose else None
        firstChild = np.append(self.firstParent[0:position], self.secondParent[position:])
        secondChild = np.append(self.secondParent[0:position], self.firstParent[position:])
        self.addChild(firstChild)
        self.addChild(secondChild)

if __name__ == "__main__":
    children = []
    c = Crossover(children)
    c.setFirstParent([1.7,2.9,-10,-87.5,16.9,50,-48.7,-34.61,74.7,99.9])
    c.setSecondParent([2.7,3.9,-17,-8.5,1.9,54,28.7,-89.61,-1.7,-99.9])
    c.makeCrossOver(verbose=True)
    print(children)
    print ('parent1: {}\nparent2: {}\nchild1: {}\nchild2: {}'.format(c.getFirstParent(), c.getSecondParent(), c.getChildren()[0], c.getChildren()[1]))
