import pygmo as pg

class Evaluation:

    def __init__(self, dimension):
        self.dimension = dimension
        self.evaluationCounter = 0

    def getDimension(self):
        return self.dimension

    def setDimension(self, dimension):
        self.dimension = dimension

    def getNumberOfEvaluations(self):
        return self.evaluationCounter

    def evaluate(self, chromosome, method='rotatedHighConditionedElliptic'):
        if method.lower() == 'rotatedhighconditionedelliptic':
            return self.rotatedHighConditionedElliptic(chromosome)
        if method.lower() == 'rotatedbentcigar':
            return self.rotatedBentCigar(chromosome)
        if method.lower() == 'shiftedrotatedweierstrass':
            return self.shiftedRotatedWeierstrass(chromosome)
        if method.lower() == 'shiftedrotatedgriewank':
            return self.shiftedRotatedGriewank(chromosome)
        if method.lower() == 'shiftedrotatedrastrigin':
            return self.shiftedRotatedRastrigin(chromosome)
        if method.lower() == 'shiftedrotatedhgbat':
            return self.shiftedRotatedHGBat(chromosome)
        else:
            raise NotImplementedError

    def getFitness(self, problemID, chromosome):
        self.evaluationCounter += 1
        return pg.problem(pg.cec2014(problemID, self.dimension)).fitness(chromosome)

    def rotatedHighConditionedElliptic(self, chromosome):
        return self.getFitness(1, chromosome)

    def rotatedBentCigar(self, chromosome):
        return self.getFitness(2, chromosome)

    def shiftedRotatedWeierstrass(self, chromosome):
        return self.getFitness(6, chromosome)

    def shiftedRotatedGriewank(self, chromosome):
        return self.getFitness(7, chromosome)

    def shiftedRotatedRastrigin(self, chromosome):
        return self.getFitness(9, chromosome)

    def shiftedRotatedHGBat(self, chromosome):
        return self.getFitness(14, chromosome)


if __name__ == "__main__":
    x = [0, 1]
    D = 2
    p = Evaluation(D)

    print('Rotated High Conditioned Elliptic:', p.evaluate(x, "rotatedHighConditionedElliptic"))
    print('Evaluation Counters:', p.getNumberOfEvaluations())