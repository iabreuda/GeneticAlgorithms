class Problem(object):

    def __init__(self, name):
        """This class is responsible to describe problem specification

        Arguments:
            name {string} -- Name of the problem
        """
        self.name = name
        self.evaluateCounter = 0

    def incrementEvaluateCounter(self):
        """Increment number of time that evaluate function was called
        """
        self.evaluateCounter += 1

    def getEvaluateCounter(self):
        """Get number of evaluations

        Returns:
            int -- Number of time that evaluate function was called
        """
        return self.evaluateCounter

    def setEvaluateCounter(self, evaluateCounter):
        """Define in run time the number of time that evaluate function was called

        Arguments:
            evaluateCounter {int} -- Number of time that evaluate function was called
        """
        self.evaluateCounter = evaluateCounter

    def getName(self):
        """Problem's name

        Returns:
            string -- Name of the problem
        """
        return self.name

    def setName(self, name):
        """Define problem's name in run time

        Arguments:
            name {string} -- Name of the problem
        """
        self.name = name

    def evaluate(self):
        """Function responsible to calculate fitness

        Raises:
            NotImplementedError: Child of problem class must implement this function
        """
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")

    def initialSolution(self):
        """Function responsible to create initial population

        Raises:
            NotImplementedError: Child of problem class must implement this function
        """
        raise NotImplementedError("This is an abstract method. Must be implemented in child class")




