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
MAXTIME = 3
FACTOR = 0.5
CO = 0.8

files = ["instances/RanReal/RanReal_n120_ds_01.txt", "instances/RanReal/RanReal_n120_ds_02.txt",
"instances/RanReal/RanReal_n120_ds_03.txt", "instances/RanReal/RanReal_n120_ds_04.txt",
"instances/RanReal/RanReal_n120_ds_05.txt", "instances/RanReal/RanReal_n120_ds_06.txt",
"instances/RanReal/RanReal_n120_ds_07.txt", "instances/RanReal/RanReal_n120_ds_08.txt",
"instances/RanReal/RanReal_n120_ds_09.txt", "instances/RanReal/RanReal_n120_ds_10.txt"]

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
            #pop = Population(population, generation)
            #pop.getGenerationalStatistics()
            for individualBase in population:
                generation += 1
                #Removes individual base from selection
                firstAgent, secondAgent, thirdAgent = np.random.choice(population - individualBase, 3, replace=False)

            stop = timeit.default_timer()
        timeInSeconds = (stop-start)
        stats.addExecutionTime(timeInSeconds)
        stats.addPopulation(population)
        stats.addEvaluationCounter(problem.getEvaluateCounter())
    stats.getStatistics()
