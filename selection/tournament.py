from selection import Selection
import numpy as np


class Tournament(Selection):

    def __init__(self, population, numberOfSelection, tournamentSize = 4, tournamentProbability = 1):
        Selection.__init__(self, "Tournament Selection", population, numberOfSelection)
        self.tournamentSize = tournamentSize
        self.tournamentProbability = tournamentProbability

    def select(self):
        self.selecteds = []
        while len(self.selecteds) < self.numberOfSelections:
            population = self.population.copy()
            tournamentContest = np.random.choice(population, self.tournamentSize)
            winner = max(tournamentContest, key=lambda x: x.getFitness())
            if np.random.rand() < self.tournamentProbability:
                del population[population.index(winner)]
                self.selecteds.append(winner)
        return self.selecteds



