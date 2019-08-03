import pygmo as pg

class Evaluation:

    def __init__(self, dimension):
        """This class is responsible to avaliate an chromosome

        Arguments:
            dimension {[Integer]} -- [Number of elements in a chromosome]
        """
        self.dimension = dimension
        self.evaluationCounter = 0

    def getDimension(self):
        """Get Dimension Number

        Returns:
            [Integr] -- [Number of elements in a chromosome]
        """
        return self.dimension

    def setDimension(self, dimension):
        """Define number of dimensions

        Arguments:
            dimension {integer} -- [Number of dimensions in array]
        """
        self.dimension = dimension

    def getNumberOfEvaluations(self):
        """Get the number of times a chromosome was avaliated, use as stop criteria

        Returns:
            [Integer] -- [Number of avaliation done]
        """
        return self.evaluationCounter

    def evaluate(self, chromosome, method='rotatedHighConditionedElliptic'):
        """Get fitness for an individual

        Arguments:
            chromosome {[array]} -- [N Dimension chromosome]

        Keyword Arguments:
            method {str} -- [choosed method] (default: {'rotatedHighConditionedElliptic'})

        Raises:
            NotImplementedError: Thrown when a method has not implemented yet

        Returns:
            [float] -- [Individual fitness]
        """
        if method.lower() == 'rotatedhighconditionedelliptic':
            return self.rotatedHighConditionedElliptic(chromosome)
        elif method.lower() == 'rotatedbentcigar':
            return self.rotatedBentCigar(chromosome)
        elif method.lower() == 'shiftedrotatedweierstrass':
            return self.shiftedRotatedWeierstrass(chromosome)
        elif method.lower() == 'shiftedrotatedgriewank':
            return self.shiftedRotatedGriewank(chromosome)
        elif method.lower() == 'shiftedrotatedrastrigin':
            return self.shiftedRotatedRastrigin(chromosome)
        elif method.lower() == 'shiftedrotatedhgbat':
            return self.shiftedRotatedHGBat(chromosome)
        else:
            raise NotImplementedError

    def getFitness(self, problemID, chromosome):
        """Calculate fitness

        Arguments:
            problemID {[Integer]} -- [function to be used]
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [fitness]
        """
        self.evaluationCounter += 1
        return pg.problem(pg.cec2014(problemID, self.dimension)).fitness(chromosome)

    def rotatedHighConditionedElliptic(self, chromosome):
        """[CEC Function 1 Min: 100]

        Arguments:
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [Fitness]
        """
        return self.getFitness(1, chromosome)

    def rotatedBentCigar(self, chromosome):
        """[CEC Function 2 Min: 200]

        Arguments:
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [Fitness]
        """
        return self.getFitness(2, chromosome)

    def shiftedRotatedWeierstrass(self, chromosome):
        """[CEC Function 6 Min: 600]

        Arguments:
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [Fitness]
        """
        return self.getFitness(6, chromosome)

    def shiftedRotatedGriewank(self, chromosome):
        """[CEC Function 7 Min: 700]

        Arguments:
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [Fitness]
        """
        return self.getFitness(7, chromosome)

    def shiftedRotatedRastrigin(self, chromosome):
        """[CEC Function 9 Min: 900]

        Arguments:
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [Fitness]
        """
        return self.getFitness(9, chromosome)

    def shiftedRotatedHGBat(self, chromosome):
        """[CEC Function 14 Min: 1400]

        Arguments:
            chromosome {[array]} -- [Chromosome]

        Returns:
            [float] -- [Fitness]
        """
        return self.getFitness(14, chromosome)
