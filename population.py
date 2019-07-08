import numpy as np

def initializePopulationReal(dimension, lower, upper, initPopulation):
    return (upper - lower)*(np.random.rand(initPopulation, dimension)) + lower

def initializePopulationBin(dimension, initPopulation):
    return np.random.randint(0, 2, size=(initPopulation, dimension))

def initializerPopulationInteger(dimension, lower, upper, initPopulation):
    return np.random.randint(lower, upper, size=(initPopulation, dimension))

def main():
    print(initializePopulationBin(5, 5))

if __name__ == "__main__":
    main()    