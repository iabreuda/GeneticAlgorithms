import sys
sys.path.append('instances/')
sys.path.append('problems/')
sys.path.append('operators/')
sys.path.append('selection/')
from mdgpinstancereader import MDGPInstanceReader
from grouppoint import GroupPoint
from groupswap import GroupSwap
from tournament import Tournament
from individual import Individual
from population import Population
from stats import Stats

import timeit
import numpy as np

POPULATION = 30
NUMBEROFCHILDS = 30
RUNS = 1
MAXTIME = 1500
files = ["instances/Surpresa_2_120_ds_18dez.txt"] #instance files

for file in files:
    print(file)
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
            #Remove comments bellow if you want check convergence through generation
            #pop = Population(population, generation)
            #pop.getGenerationalStatistics()
            generation += 1
            offSpring = []
            while (len(offSpring) < NUMBEROFCHILDS): #do it until reach number of childs that will make new generation
                selectionMethod = Tournament(population, 2) # initialize selection method with 2 selection individuals
                firstParent, secondParent = selectionMethod.select() #select 2 individuals
                crossOver = GroupPoint(firstParent, secondParent) #crossover these 2 individuals
                if np.random.rand() < crossOver.getCrossoverProbability(): # add childs to next generation with a probability
                    crossChild = crossOver.make()
                    problem.balanceGroups(crossChild) #balance child to avoid invalid individuals
                    problem.evaluate(crossChild) #get child fitness
                    offSpring.append(crossChild) #add to next generation

                selectionMethod.setNumberOfSelections(1) #change number off selection in torneio to be 1
                mutationParent = selectionMethod.select() #select one individual
                mutation = GroupSwap(mutationParent[0])
                mutChild = mutation.make() #mutate this individual
                if mutChild is not None: #only if child is different from parent
                    problem.balanceGroups(mutChild) #balance child
                    problem.evaluate(mutChild) #evaluate fitness
                    offSpring.append(mutChild) #add to next generation
            nextGeneration  = offSpring + population #merge atual population to next generation

            #Removes individuals with same fitness in order to keep diversity
            for a in nextGeneration:
                for b in nextGeneration:
                    if (a != b and a.fitness == b.fitness):
                        del nextGeneration[nextGeneration.index(b)]

            selectionMethod.setPopulation(nextGeneration) #add new population to make selection
            selectionMethod.setNumberOfSelections(POPULATION) #change number of selection to population size
            selectionMethod.setElitism(POPULATION/3) #define elitism property in these selection to be 1/3 of pop size
            population = selectionMethod.select() #create a new pop under this selection
            selectionMethod.setElitism(0) #set elitism to zero
            stop = timeit.default_timer()
        timeInSeconds = (stop-start)
        stats.addExecutionTime(timeInSeconds)
        stats.addPopulation(population)
        stats.addEvaluationCounter(problem.getEvaluateCounter())
    stats.getStatistics()
