import population as pop
import mutation as mut
import crossover as cross
import evaluation as eva
import parentselection as psel
import survivorselection as ssel
import individual as ind
import numpy as np
import pandas as pd

#Problem contstants
DIMENSION = 2 #Problem dimension for this work is 10 or 30
LOWERLIMIT = -100 #This is given by homework
UPPERLIMIT = 100 #This is given by homework
INITIALSIZE = 40 #Initial size of Population choosed by me
STOPCRITERIA = 10000*DIMENSION #This is given by homework
NUMBEROFPARENTS = INITIALSIZE/2 #This is the number of parents should be selected
NUMBEROFCHILD = INITIALSIZE #Number of children generated to the next offspring
RUNS = 51
ERROR = 1e-8

def evaluate(individuo, evaluation):
    """Calculate fitness - The fitness was inverted to calculate min instead of max

    Arguments:
        individuo {[individual]} -- [Individual Object]
        evaluation {[float]} -- [Fitness]
    """
    individuo.setFitness(
        -1*evaluation.evaluate(
            individuo.getChromosome(),
            method="shiftedRotatedHGBat"
        )
    )

def getGenerationStatistics(generation, population):
    """Statistic information about genereation

    Returns:
        [floats] -- [Statistics]
    """
    best = -1*max(population, key=lambda x: x.getFitness()).getFitness()
    worst = -1*min(population, key=lambda x: x.getFitness()).getFitness()
    fitnessSum = 0
    for individuo in population:
        fitnessSum += -1*individuo.getFitness()
    avarage = fitnessSum/len(population)
    return best, worst, avarage, generation

runNumber = 1
genDf = {"best": [], "worst": [], "avarage": []}
lowestNumberOfGeneration = 1e10
numberOfGenerations = 1e10

while runNumber <= RUNS:
    print("Execution run number: ", runNumber)
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
        if (runNumber == 1):
            genDf['best'].append(best)
            genDf['worst'].append(worst)
            genDf['avarage'].append(avarage)
        elif (generation <= len(genDf['best'])):
            genDf['best'][generation-1] += best
            genDf['worst'][generation-1] += worst
            genDf['avarage'][generation-1] += avarage

        offSpring = []
        #Select Parents
        selectedParents = psel.ParentSelection(population, NUMBEROFPARENTS, method="fitnessproportional").select(method="tournamentselection")

        while (len(offSpring) <= NUMBEROFCHILD):
            #CrossOver
            firstParent, secondParent = np.random.choice(selectedParents, 2)
            firstChild, secondChild = cross.Crossover().crossOver(firstParent, secondParent, method="singleArithmeticRecombination")

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
            child = mut.Mutation().mutate(parent, method="swapMutation")
            if (child is not None):
                child = ind.Individual(child, generation)
                evaluate(child, evaluation)
                offSpring.append(parent)
                offSpring.append(child)
        #Select Survivors
        selectedSurvivors = ssel.SurvivorSelection(offSpring, INITIALSIZE).survivors(method="ageBased")
        population = selectedSurvivors
        generation += 1 #Increment Generation

    numberOfGenerations = generation
    if (numberOfGenerations < lowestNumberOfGeneration):
        lowestNumberOfGeneration = numberOfGenerations
    runNumber += 1

del genDf['best'][lowestNumberOfGeneration-1:]
del genDf['worst'][lowestNumberOfGeneration-1:]
del genDf['avarage'][lowestNumberOfGeneration-1:]

genDf['best'][:] = [x / RUNS for x in genDf['best']]
genDf['worst'][:] = [x / RUNS for x in genDf['worst']]
genDf['avarage'][:] = [x / RUNS for x in genDf['avarage']]
print("Best: ", genDf['best'][-1])
print("Worst: ", genDf['worst'][-1])
print("Avarage: ", genDf['avarage'][-1])
genDf = pd.DataFrame(genDf).plot.line(subplots=True)
fig = genDf[0].get_figure()
fig.savefig('best.png')