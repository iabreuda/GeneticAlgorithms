from individual import Individual
import sys
sys.path.append('instances/')
sys.path.append('problems/')
from mdgpinstancereader import MDGPInstanceReader
from individual import Individual
import timeit

start = timeit.default_timer()

problem = MDGPInstanceReader("instances/RanInt/RanInt_n960_ss_10.txt")
population = problem.initialSolution(30)

stop = timeit.default_timer()

for ind in population:
    problem.evaluate(ind)
    print(ind.getFitness())

timeInMinues = (stop-start)
print('Time: ', timeInMinues)



#Your statements here



