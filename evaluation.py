import pygmo as pg

class Evaluation:

    def __init__(self, dimension, chromosome):
        self.dimension = dimension
        self.chromosome = chromosome
        self.evaluationCounter = 0

    def getChromosome(self):
        return self.chromosome

    def setChromosome(self, chromosome):

        self.chromosome = chromosome

    def getDimension(self):
        return self.dimension

    def setDimension(self, dimension):
        self.dimension = dimension

    def getNumberOfEvaluations(self):
        return self.evaluationCounter

    def getFitness(self, problemID):
        self.evaluationCounter += 1
        return pg.problem(pg.cec2014(problemID, self.dimension)).fitness(self.chromosome)

    def rotatedHighConditionedElliptic(self):
        return self.getFitness(1)

    def rotatedBentCigar(self):
        return self.getFitness(2)

    def shiftedRotatedWeierstrass(self):
        return self.getFitness(6)

    def shiftedRotatedGriewank(self):
        return self.getFitness(7)

    def shiftedRotatedRastrigin(self):
        return self.getFitness(9)

    def shiftedRotatedHGBat(self):
        return self.getFitness(14)


if __name__ == "__main__":
    x = [0, 1]
    D = 2
    p = Evaluation(D, x)

    print('Rotated High Conditioned Elliptic:', p.rotatedHighConditionedElliptic())
    print('Evaluation Counters:', p.getNumberOfEvaluations())