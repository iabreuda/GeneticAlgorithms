import numpy as np
import population as p

def onePointCrossOver(parent1, parent2):
    position = np.random.randint(1, parent1.shape[0])
    child1 = np.append(parent1[0:position], parent2[position:])
    child2 = np.append(parent2[0:position], parent1[position:])
    return child1, child2

def main():
    parent1 = p.initializePopulationReal(5, 0 ,5, 1)[0]
    parent2 =  p.initializePopulationReal(5, 0 ,5, 1)[0]
    print(onePointCrossOver(parent1, parent2))

if __name__ == "__main__":
    main()        
            