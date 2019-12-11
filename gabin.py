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
RUNS = 20
MAXTIME = 120
files = ["instances/RanReal/RanReal_n480_ds_01.txt", "instances/RanReal/RanReal_n480_ds_02.txt",
"instances/RanReal/RanReal_n480_ds_03.txt", "instances/RanReal/RanReal_n480_ds_04.txt",
"instances/RanReal/RanReal_n480_ds_05.txt", "instances/RanReal/RanReal_n480_ds_06.txt",
"instances/RanReal/RanReal_n480_ds_07.txt", "instances/RanReal/RanReal_n480_ds_08.txt",
"instances/RanReal/RanReal_n480_ds_09.txt", "instances/RanReal/RanReal_n480_ds_10.txt"]
for file in files:
    print(file)
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
            pop = Population(population, generation)
            #pop.getGenerationalStatistics()
            generation += 1
            offSpring = []
            while (len(offSpring) < NUMBEROFCHILDS):
                selectionMethod = Tournament(population, 2)
                firstParent, secondParent = selectionMethod.select()
                crossOver = GroupPoint(firstParent, secondParent)
                if np.random.rand() < crossOver.getCrossoverProbability():
                    crossChild = crossOver.make()
                    problem.balanceGroups(crossChild)
                    problem.evaluate(crossChild)
                    offSpring.append(crossChild)

                selectionMethod.setNumberOfSelections(1)
                mutationParent = selectionMethod.select()
                mutation = GroupSwap(mutationParent[0])
                mutChild = mutation.make()
                if mutChild is not None:
                    problem.evaluate(mutChild)
                    offSpring.append(mutChild)
            nextGeneration  = offSpring + population

            ##Only fitness care - Avoid Keep equal individups
            for a in nextGeneration:
                for b in nextGeneration:
                    if (a != b and a.fitness == b.fitness):
                        del nextGeneration[nextGeneration.index(b)]

            selectionMethod.setPopulation(nextGeneration)
            selectionMethod.setNumberOfSelections(POPULATION)
            selectionMethod.setElitism(POPULATION/3)
            population = selectionMethod.select()
            selectionMethod.setElitism(0)
            stop = timeit.default_timer()
        timeInSeconds = (stop-start)
        stats.addExecutionTime(timeInSeconds)
        stats.addPopulation(population)
        stats.addEvaluationCounter(problem.getEvaluateCounter())
    stats.getStatistics()
