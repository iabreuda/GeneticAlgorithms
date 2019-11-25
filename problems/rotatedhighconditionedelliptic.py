from CEC2014 import CEC2014
from problem import Problem
import pygmo as pg

class RotatedHighConditionedElliptic(CEC2014):

    def __init__(self):
        """This class is responsible to describe problem specification

        Arguments:
            name {string} -- Name of the problem
        """
        Problem.__init__(self, "Rotated High Conditioned Elliptic")
        CEC2014.__init__(self)

    def evaluate(self, chromosome):
        return pg.problem(pg.cec2014(1, self.getDimension())).fitness(chromosome)
