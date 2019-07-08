import numpy as np

def initializePopulationReal(dimension, lower, upper, initPopulation):
    return (upper - lower)*(np.random.rand(initPopulation, dimension)) + lower

def initializePopulationBin(dimension, initPopulation):
    return np.random.randint(0, 2, size=(initPopulation, dimension))

def initializerPopulationInteger(dimension, lower, upper, initPopulation):
    return np.random.randint(lower, upper, size=(initPopulation, dimension))

def main():
    print(initializePopulationReal(dimension=10, lower=-100, upper=100, initPopulation=2))

if __name__ == "__main__":
    main()    