import sys
sys.path.append('instances/')
sys.path.append('problems/')
sys.path.append('operators/')
sys.path.append('selection/')
from mdgpinstancereader import MDGPInstanceReader
from decross import DECross
from derand import DERand
from individual import Individual
from population import Population
from stats import Stats

import timeit
import numpy as np

POPULATION = 30
NUMBEROFCHILDS = 30
RUNS = 20
MAXTIME = 600
#FACTOR = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
#CO = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
FACTOR = [2]
CO = [0.15]

files = ["instances/RanReal/RanReal_n960_ds_01.txt", "instances/RanReal/RanReal_n960_ds_02.txt",
"instances/RanReal/RanReal_n960_ds_03.txt", "instances/RanReal/RanReal_n960_ds_04.txt",
"instances/RanReal/RanReal_n960_ds_05.txt", "instances/RanReal/RanReal_n960_ds_06.txt",
"instances/RanReal/RanReal_n960_ds_07.txt", "instances/RanReal/RanReal_n960_ds_08.txt",
"instances/RanReal/RanReal_n960_ds_09.txt", "instances/RanReal/RanReal_n960_ds_10.txt"]

for co in CO:
    for factor in FACTOR:
        for file in files:
            print(file, " Crossover Probability: ", co, " Factor: ", factor)
            stats = Stats()
            runCounter = 0
            while (runCounter < RUNS):
                runCounter += 1
                start = timeit.default_timer()
                problem = MDGPInstanceReader(file)
                population = problem.initialSolution(POPULATION)

                for ind in population:
                    problem.evaluate(ind)

                generation = 0
                stop = timeit.default_timer()
                while (stop-start < MAXTIME):
                    #pop = Population(population, generation)
                    #pop.getGenerationalStatistics()
                    offSpring = []
                    generation += 1
                    for index, individualBase in enumerate(population):
                        population.remove(individualBase) #Removes individual base from selection
                        firstAgent, secondAgent, thirdAgent = np.random.choice(population, 3, replace=False) #Cannot choice individual Base
                        population.insert(index, individualBase)
                        trialVector = DERand(firstAgent, secondAgent, thirdAgent, factor).make()
                        child = DECross(individualBase, trialVector, co).make()
                        child.setGroups(problem.cloneGroups())
                        problem.populateRealGroups(child)
                        problem.balanceGroups(child) #Balance doesnot change chromossome!
                        problem.evaluate(child)
                        #print("Child: ", child.getFitness(), "Base: ", individualBase.getFitness())
                        offSpring.append(child)
                        #Selection Criteria
                        """
                        if (child.getFitness() > individualBase.getFitness()):
                            population.insert(index, child)
                        else:
                            population.insert(index, individualBase)
                        """
                    #Create new population
                    #print(population)
                    for key, child in enumerate(offSpring):
                        if (child.getFitness() > population[key].getFitness()):
                            population.remove(population[key])
                            population.insert(key, child)

                            #for grp in child.getGroups():
                                #print(grp.getIndex(), grp.getElements())
                    #print(population)
                    #raise Exception("JJJ")

                    stop = timeit.default_timer()
                timeInSeconds = (stop-start)
                stats.addExecutionTime(timeInSeconds)
                stats.addPopulation(population)
                stats.addEvaluationCounter(problem.getEvaluateCounter())
            stats.getStatistics()
