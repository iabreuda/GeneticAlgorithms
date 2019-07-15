import population as p
import mutation as m
import crossover as c
import evaluation as e
import numpy as np

dimension = 10
lowerLimit = -100
upperLimit = 100
initialSize = 2*dimension
population = p.Population(dimension, lowerLimit, upperLimit, initialSize)
initial = population.createPopulation()

evaluation = e.Evaluation(dimension)

aval = list()
for j in initial:
    aval.append(evaluation.rotatedBentCigar(j))

arr = np.array(aval)
parent = initial[np.argsort(arr, axis=0)[:3]]

for i in range (10000):
    parent = initial[np.argsort(arr, axis=0)[:3]]
    generation = list()
    crossover = c.Crossover(generation)
    mutation = m.Mutation(generation)
    mutation.setHesserMutationGeneProbability(dimension, initialSize, i)

    for p in parent:
        crossover.setFirstParent(p[0])
        for d in parent:
            crossover.setSecondParent(d[0])
            if not np.array_equal(p,d):
                if (np.random.rand() < crossover.getCrossoverProbability()):
                    crossover.makeCrossOver()
        mutation.setParent(p[0])
        mutation.nonUniformGaussianMutation()
    for j in generation:
        initial = np.append(initial, [j], axis=0)
        aval = np.append(aval, evaluation.rotatedBentCigar(j))

    initial = initial[np.argsort(aval)[:20]]
    aval = aval[np.argsort(aval)[:20]]

print(aval[np.argsort(aval)[:1]])
