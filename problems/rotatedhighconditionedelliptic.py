from CEC2014 import CEC2014
from problem import Problem
import pygmo as pg

class RotatedHighConditionedElliptic(CEC2014):

    def __init__(self):
        """This class is responsible for problem Rotated HighConditioned Elliptic
        Arguments:
            name {string} -- Name of the problem
        """
        Problem.__init__(self, "Rotated High Conditioned Elliptic")
        CEC2014.__init__(self)

    def evaluate(self, chromosome):
        """method to get fitness of an individual

        Arguments:
            chromosome {array} -- array containing variable problems value

        Returns:
            float -- Fitness of the problem
        """
        return pg.problem(pg.cec2014(1, self.getDimension())).fitness(chromosome)
