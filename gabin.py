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

import timeit
import numpy as np

POPULATION = 30
NUMBEROFCHILDS = 30

start = timeit.default_timer()

problem = MDGPInstanceReader("instances/RanInt/RanInt_n120_ss_10.txt")
population = problem.initialSolution(POPULATION)

stop = timeit.default_timer()

for ind in population:
    problem.evaluate(ind)


generation = 0

while (generation < 10000):
    generation += 1
    offSpring = []
    while (len(offSpring) < 30):
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
    selectionMethod.setPopulation(nextGeneration)
    selectionMethod.setNumberOfSelections(30)
    population = selectionMethod.select()
    for ind in population:
        print("Fit:", ind.getFitness())
        for grp in ind.getGroups():
            print(grp.getIndex(), grp.getElements())
    print("Generation: ", generation)
timeInMinues = (stop-start)
print('Time: ', timeInMinues)
