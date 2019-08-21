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
DIMENSION = 10 #Problem dimension for this work is 10 or 30
LOWERLIMIT = -100 #This is given by homework
UPPERLIMIT = 100 #This is given by homework
INITIALSIZE = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105] #Initial size of Population choosed by me
FACTOR = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
CO = [0.05, 0.1, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
STOPCRITERIA = 10000*DIMENSION #This is given by homework
NUMBEROFPARENTS = 4 #This is the number of parents should be selected
NUMBEROFCHILD = 1 #Number of children generated to the next offspring
RUNS = 2
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
    best = -1*max(population, key=lambda x: x.getFitness()).getFitness()
    worst = -1*min(population, key=lambda x: x.getFitness()).getFitness()
    fitnessSum = 0
    for individuo in population:
        fitnessSum += -1*individuo.getFitness()
    avarage = fitnessSum/len(population)
    return best, worst, avarage, generation

file = open("de.csv","w")
file.write("Population Size;CrossOver Rate;Fator;Best;Worst;Avarage\n")

for popSize in INITIALSIZE:
    for coRate in CO:
        for weight in FACTOR:
            print("Population: " + str(popSize) + "; CrossOver Rate: " + str(coRate) + "; Factor: " + str(weight))
            runNumber = 1
            genDf = {"best": [], "worst": [], "avarage": []}
            lowestNumberOfGeneration = 1e10
            numberOfGenerations = 1e10

            while runNumber <= RUNS:
                print("Execution run number: ", runNumber)
                #Creating initial population
                population = pop.Population(DIMENSION, LOWERLIMIT, UPPERLIMIT, popSize).getPopulation() #This is an list containing instance of Individual Object

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
                    base, firstAgent, secondAgent, thirdAgent = np.random.choice(population, 4, replace=False)
                    child = cross.Crossover(probability=coRate).crossOver(
                        firstAgent,
                        secondAgent,
                        thirdAgent,
                        base,
                        factor=weight,
                        method="DECrossOver"
                    )
                    child = ind.Individual(child, generation)
                    evaluate(child, evaluation)
                    if (base.getFitness() < child.getFitness()):
                        population[population.index(base)] = child
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
            file.write(str(popSize) + ";"  + str(coRate) + ";" + str(weight) + ";" + str(genDf['best'][-1]) + ";" + str(genDf['worst'][-1]) + ";" + str(genDf['avarage'][-1]) + "\n")
file.close()

    #print("===== Statisitics for Initial Pop = ", popSize)
    #print("Best: ", genDf['best'][-1])
    #print("Worst: ", genDf['worst'][-1])
    #print("Avarage: ", genDf['avarage'][-1])
    #genDf = pd.DataFrame(genDf).plot.line(subplots=True)
    #fig = genDf[0].get_figure()
    #fig.savefig('best' + str(popSize) + '.png')