import numpy as np
import math as m

class ParentSelection:

    def __init__(self, population, numberOfParents, method='fitnessProportional'):
        """This class is responsible to select parent to generate children for next generation

        Arguments:
            population {Array} -- [The whole population for this generation]
            numberOfParents {Integer} -- [Number of parents to be select in order to generate next offspring]

        Keyword Arguments:
            method {str} -- [Method to calculate normalized probability for each parent] (default: {'fitnessProportional'})
        """
        self.population = population
        self.numberOfParents = numberOfParents
        self.totalFitness = 0
        self.parents = []
        self.ranking()
        self.choosedProbability(method)

    def ranking(self):
        """Sort populate by fitness where rank 1 has lowest fitness and the highest rank has the highest fitness
        """
        self.population.sort(key=lambda x: x.getFitness()) #Sort Individuo by Fitness
        for individuo in self.population:
            individuo.setRank(self.population.index(individuo) + 1)

    def choosedProbability(self, method):
        """Method to calculate normalized probability for each parent

        Arguments:
            method {string} -- Choosed Method

        Raises:
            NotImplementedError: Thrown when a method has not implemented yet
        """
        if method.lower() == 'fitnessproportional':
            self.fitnessProportional()
        elif method.lower() == 'exponentialranking':
            self.exponentialRanking()
        else:
            raise NotImplementedError

    def fitnessProportional(self):
        """Define probability so select an idividual to be parent using individua_fitness/sum(all_individual_fitness)
        """
        self.totalFitness = 0
        #Acumulate total fitness
        for individuo in self.population:
            self.totalFitness +=  individuo.getFitness()
        #Set individual probability to be choosed
        for individuo in self.population:
            individuo.setChoosedProbability(individuo.getFitness()/self.totalFitness)

    def exponentialRanking(self):
        """Define probability so select an idividual to be parent using an exponential according individual rank
        """
        self.totalFitness = 0
        #Acumulate total fitness
        for individual in self.population:
            self.totalFitness += (1 - m.exp(-1*individual.getRank())) / (m.exp(1))
        #Set individual probability to be choosed
        for individuo in self.population:
            individuo.setChoosedProbability(((1 - m.exp(-1*individual.getRank())) / (m.exp(1))) / self.totalFitness)

    def select(self, method='roulettewheelselection', tournamentSize = 4, tournamentProbability = 1):
        """Choose de selection method to be used

        Keyword Arguments:
            method {str} -- Choosed Method (default: {'rouletewheelselection'})
            tournamentSize {int} -- Number of contest in tournament (default: {3})
            tournamentProbability {int} -- Probability to the winner be accepted (default: {1})

        Raises:
            NotImplementedError: Thrown when a method has not implemented yet

        Returns:
            [list] -- List of individuals responsible to next generation
        """
        if method.lower() == 'roulettewheelselection':
            return self.rouletteWheelSelection()
        elif method.lower() == 'stochasticuniversalsamplingselection':
            return self.stochasticUniversalSamplingSelection()
        elif method.lower() == 'tournamentselection':
            return self.tournamentSelection(tournamentSize, tournamentProbability)
        else:
            raise NotImplementedError


    def rouletteWheelSelection(self):
        """Roulett Method described in Pg62 of text book

        Returns:
            [list] -- List of individuals responsible to next generation
        """
        while len(self.parents) <= self.numberOfParents:
            r = np.random.rand()
            cumulatedProbability = 0
            for individuo in self.population:
                cumulatedProbability += individuo.getChoosedProbability()
                if  r < cumulatedProbability:
                    self.parents.append(individuo)
                    break
        return self.parents

    def stochasticUniversalSamplingSelection(self):
        """SUS Method described in Pg63 of text book
            This method avoid parent repetition if compared with Roullet

        Returns:
            [list] -- List of individuals responsible to next generation
        """
        r = (1/self.numberOfParents) * np.random.random()
        while len(self.parents) < self.numberOfParents:
            cumulatedProbability = 0
            for individuo in self.population:
                cumulatedProbability += individuo.getChoosedProbability()
                if r <= cumulatedProbability:
                    r = r + (1/self.numberOfParents)
                    self.parents.append(individuo)
                    break
        return self.parents

    def tournamentSelection(self, tournamentSize, tournamentProbability):
        """Tournament Method described in Pg64 of text book

        Arguments:
            tournamentSize {int} -- [Number of contest]
            tournamentProbability {int} -- [Probability of winner become parent]

        Returns:
            [list] -- List of individuals responsible to next generation
        """
        while len(self.parents) < self.numberOfParents:
            tournamentContest = np.random.choice(self.population, tournamentSize)
            winner = max(tournamentContest, key=lambda x: x.getFitness())
            if np.random.rand() < tournamentProbability:
                del self.population[self.population.index(winner)]
                self.parents.append(winner)
        return self.parents
