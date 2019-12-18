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
RUNS = 1
MAXTIME = 1500
FACTOR = [2]
CO = [0.15]

files = ["instances/Surpresa_2_120_ds_18dez.txt"] #instance files

for co in CO:
    for factor in FACTOR:
        for file in files:
            print(file, " Crossover Probability: ", co, " Factor: ", factor)
            stats = Stats()
            runCounter = 0
            while (runCounter < RUNS):
                runCounter += 1
                start = timeit.default_timer() # start time counter
                problem = MDGPInstanceReader(file) # read instance
                population = problem.initialSolution(POPULATION) #get initial solutions

                for ind in population: # evaluate initial solutions
                    problem.evaluate(ind)

                generation = 0
                stop = timeit.default_timer()
                while (stop-start < MAXTIME): # Time stop criteria
                    #Remove these comments if you want to see generational stats
                    #pop = Population(population, generation)
                    #pop.getGenerationalStatistics()
                    offSpring = []
                    generation += 1
                    for index, individualBase in enumerate(population): #all individual must generate one child
                        population.remove(individualBase) #Removes individual base from selection
                        firstAgent, secondAgent, thirdAgent = np.random.choice(population, 3, replace=False) #Cannot choice individual Base
                        population.insert(index, individualBase) # reinsert individual base
                        trialVector = DERand(firstAgent, secondAgent, thirdAgent, factor).make() #create trial vector using mutation
                        child = DECross(individualBase, trialVector, co).make() # crete child using individual base and trial vector
                        child.setGroups(problem.cloneGroups())
                        problem.populateRealGroups(child) #real-int conversion
                        problem.balanceGroups(child) #Balance doesnot change chromossome!
                        problem.evaluate(child) # evaluate child
                        offSpring.append(child)
                    for key, child in enumerate(offSpring): #deterministc survivor criteria
                        if (child.getFitness() > population[key].getFitness()):
                            population.remove(population[key])
                            population.insert(key, child)
                    stop = timeit.default_timer()
                timeInSeconds = (stop-start)
                stats.addExecutionTime(timeInSeconds)
                stats.addPopulation(population)
                stats.addEvaluationCounter(problem.getEvaluateCounter())
            stats.getStatistics()
