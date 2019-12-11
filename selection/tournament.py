from selection import Selection
import numpy as np


class Tournament(Selection):

    def __init__(self, population, numberOfSelection, tournamentSize = 4, tournamentProbability = 1, elitism = 0):
        Selection.__init__(self, "Tournament Selection", population, numberOfSelection)
        self.tournamentSize = tournamentSize
        self.tournamentProbability = tournamentProbability
        self.elitism = elitism

    def getElitism(self):
        return self.elitism

    def setElitism(self, elitism):
        self.elitism = elitism

    def select(self):
        self.selecteds = []
        population = self.population.copy()
        elite = 0
        while (elite < self.elitism):
            best = max(population, key=lambda x: x.getFitness())
            del population[population.index(best)]
            self.selecteds.append(best)
            elite += 1

        while len(self.selecteds) < self.numberOfSelections:
            tournamentContest = np.random.choice(population, self.tournamentSize)
            winner = max(tournamentContest, key=lambda x: x.getFitness())
            if np.random.rand() < self.tournamentProbability:
                del population[population.index(winner)]
                self.selecteds.append(winner)
        return self.selecteds



