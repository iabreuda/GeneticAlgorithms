import numpy as np

class Stats(object):

    def __init__(self):
        self.population = []
        self.executionTime = []
        self.evaluationCounter = []

    def getPopulation(self):
        return self.population

    def setPopulation(self, population):
        self.population = population

    def addPopulation(self, population):
        self.population += population

    def getExecutionTime(self):
        return self.executionTime

    def setExecutionTime(self, executionTime):
        self.executionTime = executionTime

    def addExecutionTime(self, executionTime):
        self.executionTime.append(executionTime)

    def getEvaluationCounter(self):
        return self.evaluationCounter

    def setEvaluationCounter(self, evaluationCounter):
        self.evaluationCounter = evaluationCounter

    def addEvaluationCounter(self, evaluationCounter):
        self.evaluationCounter.append(evaluationCounter)

    def getStatistics(self):
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