import numpy as np

class Stats(object):
    def __init__(self):
        """class that handle globa stats

        Arguments:
            object {[type]} -- [description]
        """
        self.population = []
        self.executionTime = []
        self.evaluationCounter = []

    def getPopulation(self):
        """get population to be calculated in stats

        Returns:
            array -- individuals array
        """
        return self.population

    def setPopulation(self, population):
        """define population to be calculated in stats

        Arguments:
            population {array} -- individuals array
        """
        self.population = population

    def addPopulation(self, population):
        """add population to be calculated in stats

        Arguments:
            population {array} -- individual array
        """
        self.population += population

    def getExecutionTime(self):
        """get execution time

        Returns:
            float -- running time in seconds
        """
        return self.executionTime

    def setExecutionTime(self, executionTime):
        """define execution time

        Arguments:
            executionTime {float} -- running time in seconds
        """
        self.executionTime = executionTime

    def addExecutionTime(self, executionTime):
        """add execution time

        Arguments:
            executionTime {float} -- running time in seconds
        """
        self.executionTime.append(executionTime)

    def getEvaluationCounter(self):
        """get number of evaluatin

        Returns:
            int -- number of evaluation
        """
        return self.evaluationCounter

    def setEvaluationCounter(self, evaluationCounter):
        """define number of evaluation

        Arguments:
            evaluationCounter {int} -- number of evaluation
        """
        self.evaluationCounter = evaluationCounter

    def addEvaluationCounter(self, evaluationCounter):
        """add eval counter

        Arguments:
            evaluationCounter {int} -- number of evaluation
        """
        self.evaluationCounter.append(evaluationCounter)

    def getStatistics(self):
        """Print global stats
        """
        fitness = []
        for individuo in self.population:
            fitness.append(individuo.getFitness())

        best = np.amax(fitness)
        avarage = np.mean(fitness)
        worst = np.amin(fitness)
        median = np.median(fitness)
        std = np.std(fitness)
        avgTime = np.mean(self.executionTime)
        evalCounter = np.mean(self.evaluationCounter)

        print("Global -> Best: ", best, " Worst: ", worst, " Avg: ", avarage , " Median: ", median, " Std:", std, "ExecTime: ", avgTime, " EvalCounter: ", evalCounter)