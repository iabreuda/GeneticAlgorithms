import sys
sys.path.append('..')
from utils import validateInteger, validateList, validadeMinMaxConstraint

class Group():
    def __init__(self, index, minElements, maxElements):
        """Class responsible to handle groups

        Arguments:
            index {int} -- Group number
            minElements {int} -- Lowest number of elements allowed in this group
            maxElements {int} -- Highest number of elements allowed in this group
        """
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
        """Get group number

        Returns:
            int -- Group number
        """
        return self.index

    def setIndex(self, index):
        """Define group number in run time

        Arguments:
            index {int} -- Group number
        """
        self.index = index

    def getMinElements(self):
        """ Lowest number of elements allowed in group

        Returns:
            int -- Minimum number of elements
        """
        return self.minElements

    def setMinElements(self, minElements):
        """Define Lowest number of elements allowed in group

        Arguments:
            minElements {int} -- Minimum number of elements
        """
        self.minElements = minElements

    def getMaxElements(self):
        """ Highest number of elements allowed in group

        Returns:
            int -- Maximum number of elements
        """
        return self.maxElements

    def setMaxElements(self, maxElements):
        """Define Highest number of elements allowed in group

        Arguments:
            minElements {int} -- Maximum number of elements
        """
        self.maxElements = maxElements

    def getElements(self):
        """All elements in a group

        Returns:
            array -- group elements
        """
        return self.elements

    def setElements(self, elements):
        """Define groups elements in run time

        Arguments:
            elements {array} -- array with elements
        """
        self.clearElements()
        self.elements = elements

    def addElement(self, element):
        """Add one element in current group

        Arguments:
            element {int} -- Element to be added in this group
        """
        self.elements.append(element)

    def addElements(self, elements):
        """Merge a list of elements in an existing group

        Arguments:
            elements {array} -- List containing elements
        """
        self.elements += elements

    def removeElements(self, element):
        """Removes one element from list of elements

        Arguments:
            element {int} -- Element to be removed in this group
        """
        self.elements.remove(element)

    def groupStatus(self):
        """Return number of elements distance from limits

        Raises:
            Exception: Undesirable status

        Returns:
            int -- Zero if groups in bounderies, negative if has less element than lower limit posititve otherwise
        """
        if (len(self.elements) >= self.minElements and len(self.elements) <= self.maxElements):
            return 0
        elif (len(self.elements) < self.minElements):
            return len(self.elements) - self.minElements
        elif (len(self.elements) > self.maxElements):
            return len(self.elements) - self.maxElements
        raise Exception("Unavailable Status")

    def clearElements(self):
        """Clean element list
        """
        self.elements = []

    def getFitness(self):
        """Get fitness of this group

        Returns:
            float -- fitness of a group
        """
        return self.fitness

    def setFitness(self, fitness):
        """define a group fitness

        Arguments:
            fitness {float} -- set in run time fitness related to this group
        """
        self.fitness = fitness

    def isFull(self):
        """Verify if group is in max constraint

        Returns:
            bool -- Grour is full? True: False
        """
        return len(self.elements) == self.maxElements

