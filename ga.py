import population as p
import mutation as m
import crossover as c
import evaluation as e
import numpy as np

initial = p.initializePopulationReal(10, -100, 100, 20)

aval = list()
for j in initial:
    aval.append(e.bentCigar(j, 10))

arr = np.array(aval)

for i in range (10000000):
    parent = initial[np.argsort(arr)[:3]]

    generation = list()
    for p in parent:
        for d in parent:
            if not np.array_equal(p,d):
                if (np.random.rand() < 0.8):
                    child1, child2 = c.onePointCrossOver(p,d)
                    generation.append(child1)
                    generation.append(child2)
        if (np.random.rand() < 0.2):
            child3 = m.uniformMutation(p,0.2,-100, 100)
            generation.append(child3)


    for j in generation:
        initial = np.append(initial, [j], axis=0)
        aval = np.append(aval, e.bentCigar(j, 10))

    initial = initial[np.argsort(aval)[:20]]
    aval = aval[np.argsort(aval)[:20]]

print(aval[np.argsort(aval)[:1]])
