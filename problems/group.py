import sys
sys.path.append('..')
from utils import validateInteger, validateList, validadeMinMaxConstraint

class Group():
    def __init__(self, index, minElements, maxElements):
        validateInteger(index, "Index number must be integer")
        validateInteger(minElements, "Number of min elements must be integer")
        validateInteger(maxElements, "Number of max elements must be integer")
        validadeMinMaxConstraint(minElements, maxElements, "Minimum must no be higher than maximum")
        self.index =  index
        self.minElements = minElements
        self.maxElements = maxElements
        self.elements = []
        self.fitness = 0

    def getIndex(self):
        return self.index

    def setIndex(self, index):
        self.index = index

    def getMinElements(self):
        return self.minElements

    def setMinElements(self, minElements):
        self.minElements = minElements

    def getMaxElements(self):
        return self.maxElements

    def setMaxElements(self, maxElements):
        self.maxElements = maxElements

    def getElements(self):
        return self.elements

    def setElements(self, elements):
        self.clearElements()
        self.elements = elements

    def addElements(self, element):
        self.elements.append(element)

    def removeElements(self, element):
        self.elements.remove(element)

    def groupStatus(self):
        if (len(self.elements) >= self.minElements and len(self.elements) <= self.maxElements):
            return 0
        elif (len(self.elements) < self.minElements):
            return len(self.elements) - self.minElements
        elif (len(self.elements) > self.maxElements):
            return len(self.elements) - self.maxElements
        raise Exception("Unavailable Status")

    def clearElements(self):
        self.elements = []

    def getFitness(self):
        return self.fitness

    def setFitness(self, fitness):
        self.fitness = fitness

    def isFull(self):
        return len(self.elements) == self.maxElements

