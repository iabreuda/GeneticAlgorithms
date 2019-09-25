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
DIMENSION = 30 #Problem dimension for this work is 10 or 30
LOWERLIMIT = -100 #This is given by homework
UPPERLIMIT = 100 #This is given by homework
INITIALSIZE = 80 #Initial size of Population choosed by me
STOPCRITERIA = 10000*DIMENSION #This is given by homework
NUMBEROFPARENTS = 15 #This is the number of parents should be selected
NUMBEROFCHILD = INITIALSIZE #Number of children generated to the next offspring
RUNS = 51
MINIMUN = 100
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
            method="rotatedHighConditionedElliptic"
        )
    )

def getGenerationStatistics(generation, population):
    """Statistic information about genereation

    Returns:
        [floats] -- [Statistics]
    """
    fitness = []
    for individuo in population:
        fitness.append(-1*individuo.getFitness())
    np_arr = np.array(fitness)

    best = np.amin(np_arr)
    worst = np.amax(np_arr)
    avarage = np.mean(np_arr)
    worst = np.amax(np_arr)
    median = np.median(np_arr)
    std = np.std(np_arr)

    return best, worst, avarage, generation, median, std

file = open("GA_F1_Statistics_30_Mod_A.csv","w")
file.write("Best;Worst;Avarage;Median;Std;SuccessRate\n")
evol = open("GA_F1_GEN_30_Mod_A.csv","w")
evol.write("0.0*MaxFES;0.001*MaxFES;0.01*MaxFES;0.1*MaxFES;0.2*MaxFES;0.3*MaxFES;0.4*MaxFES;0.5*MaxFES;0.6*MaxFES;0.7*MaxFES;0.8*MaxFES;0.9*MaxFES;1.0*MaxFES\n")

runNumber = 1
runDf = {"best": [], "worst": [], "avarage": [], "median": [], "std": []}
genDf = {"best": [], "worst": [], "avarage": []}
lastPop = []
lowestNumberOfGeneration = 1e10
numberOfGenerations = 1e10
success = 0

while runNumber <= RUNS:
    print("Execution run number: ", runNumber)
    testDf = {"best": [], "worst": [], "avarage": []}
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
        best, worst, avarage, generation, median, std = getGenerationStatistics(generation, population)
        testDf['best'].append(best)
        testDf['worst'].append(worst)
        testDf['avarage'].append(avarage)

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
            child = mut.Mutation().mutate(parent, method="nonUniformGaussianMutation")
            if (child is not None):
                child = ind.Individual(child, generation)
                evaluate(child, evaluation)
                offSpring.append(parent)
                offSpring.append(child)
        #Select Survivors
        selectedSurvivors = ssel.SurvivorSelection(offSpring, INITIALSIZE).survivors(method="ageBased")
        population = selectedSurvivors
        generation += 1 #Increment Generation
    #This work just for last populaton in last generation
    best, worst, avarage, generation, median, std = getGenerationStatistics(generation, population)
    if (abs(best - MINIMUN) < ERROR):
        success += 1
    runDf['best'].append(best)
    runDf['worst'].append(worst)
    runDf['avarage'].append(avarage)
    runDf['median'].append(median)
    runDf['std'].append(std)
    #create an array containing all last pop during the runs
    for individuo in population:
        lastPop.append(-1*individuo.getFitness())

    numberOfGenerations = generation
    if (numberOfGenerations < lowestNumberOfGeneration):
        lowestNumberOfGeneration = numberOfGenerations
    runNumber += 1
    evol.write(
        str(testDf['best'][0]) + ";" +
        str(testDf['best'][round(generation*0.001)]) + ";" +
        str(testDf['best'][round(generation*0.01)]) + ";" +
        str(testDf['best'][round(generation*0.1)]) + ";" +
        str(testDf['best'][round(generation*0.2)]) + ";" +
        str(testDf['best'][round(generation*0.3)]) + ";" +
        str(testDf['best'][round(generation*0.4)]) + ";" +
        str(testDf['best'][round(generation*0.5)]) + ";" +
        str(testDf['best'][round(generation*0.6)]) + ";" +
        str(testDf['best'][round(generation*0.7)]) + ";" +
        str(testDf['best'][round(generation*0.8)]) + ";" +
        str(testDf['best'][round(generation*0.9)]) + ";" +
        str(testDf['best'][generation-2]) + ";\n")

np_lp = np.array(lastPop)
best = np.amin(np_lp)
worst = np.amax(np_lp)
avarage = np.mean(np_lp)
worst = np.amax(np_lp)
median = np.median(np_lp)
std = np.std(np_lp)
successRate = (success/RUNS)*100

file.write(str(best) + ";" + str(worst) + ";" + str(avarage) + ";" + str(median) + ";" + str(std) + ";" + str(successRate) + "\n")
file.close()
