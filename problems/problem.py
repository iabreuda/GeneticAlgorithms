class Problem(object):

    def __init__(self, name):
        """This class is responsible to describe problem specification

        Arguments:
            name {string} -- Name of the problem
        """
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def evaluate(self):
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")

    def initialSolution(self):
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")




