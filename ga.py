import population as pop
import mutation as mut
import crossover as cross
import evaluation as eva
import parentselection as psel
import survivorselection as ssel
import individual as ind
import numpy as np

#Problem contstants
DIMENSION = 10 #Problem dimension for this work is 10 or 30
LOWERLIMIT = -100 #This is given by homework
UPPERLIMIT = 100 #This is given by homework
INITIALSIZE = 100 #Initial size of Population choosed by me
STOPCRITERIA = 10000*DIMENSION #This is given by homework
NUMBEROFPARENTS = INITIALSIZE/5 #This is the number of parents should be selected
NUMBEROFCHILD = INITIALSIZE #Number of children generated to the next offspring

def evaluate(individuo, evaluation):
    """Calculate fitness - The fitness was inverted to calculate min instead of max

    Arguments:
        individuo {[individual]} -- [Individual Object]
        evaluation {[float]} -- [Fitness]
    """
    individuo.setFitness(
        1 / evaluation.evaluate(
            individuo.getChromosome(),
            method="shiftedrotatedgriewank"
        )
    )

def getGenerationStatistics(generation, population):
    """Statistic information about genereation

    Returns:
        [floats] -- [Statistics]
    """
    best = 1 / max(population, key=lambda x: x.getFitness()).getFitness()
    worst = 1 / min(population, key=lambda x: x.getFitness()).getFitness()
    fitnessSum = 0
    for individuo in population:
        fitnessSum += 1 / individuo.getFitness()
    avarage = fitnessSum/len(population)
    return best, worst, avarage, generation

#Creating initial population
population = pop.Population(DIMENSION, LOWERLIMIT, UPPERLIMIT, INITIALSIZE).getPopulation() #This is an list containing instance of Individual Object

#Initialize evaluation class enabling evalutation counter
evaluation = eva.Evaluation(DIMENSION)

for individuo in population:
    #Define inverse Fitness for each individuo from initial population since this is a minimization problem
    evaluate(individuo, evaluation)

#Evaluate until reach the max number of evalutation
generation = 1
while (evaluation.getNumberOfEvaluations() < STOPCRITERIA):
    best, worst, avarage, generation = getGenerationStatistics(generation, population)
    print("Generation: ", generation)
    print("Best Fitness: ", best)
    print("Worst Fitness: ", worst)
    print("Avarage: ", avarage)
    print("------------EOG----------")

    offSpring = []
    #Select Parents
    selectedParents = psel.ParentSelection(population, NUMBEROFPARENTS, method="fitnessProportional").select(method="tournamentSelection")

    while (len(offSpring) <= NUMBEROFCHILD):
        #CrossOver
        firstParent, secondParent = np.random.choice(selectedParents, 2)
        firstChild, secondChild = cross.Crossover().crossOver(firstParent, secondParent, method="wholeArithmeticRecombination")

        if (firstChild is not None):
            firstChild = ind.Individual(firstChild, generation)
            evaluate(firstChild, evaluation)
            offSpring.append(firstParent)
            offSpring.append(firstChild)
        if (secondChild is not None):
            secondChild = ind.Individual(secondChild, generation)
            evaluate(secondChild, evaluation)
            offSpring.append(secondParent)
            offSpring.append(secondChild)
        #Mutation
        parent = np.random.choice(selectedParents)
        child = mut.Mutation().mutate(parent, method="nonUniformGaussianMutation")
        if (child is not None):
            child = ind.Individual(child, generation)
            evaluate(child, evaluation)
            offSpring.append(parent)
            offSpring.append(child)
    #Select Survivors
    selectedSurvivors = ssel.SurvivorSelection(offSpring, INITIALSIZE).survivors(method="fitnessBased")
    population = selectedSurvivors
    generation += 1 #Increment Generation
