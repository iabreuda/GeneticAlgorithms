import numpy as np
import population as p

#Binary Representation
def binaryMutation(parent, probability):
    for row in range(0, parent.shape[0]):
        for column in range(0, parent.shape[1]):
            if (np.random.rand() < probability):
                parent[row][column] = 1 - parent[row][column]
    return parent

#Integer Representation
def IntegerRandomResetting(parent, probability, lower, upper):
    for row in range(0, parent.shape[0]):
        for column in range(0, parent.shape[1]):
            if (np.random.rand() < probability):
                parent[row][column] = np.random.randint(lower, upper)
    return parent    


#Validar se depois da soma os valores passaram os limites da populacao
def creepMutation(parent, probability, lower, upper):
    print(parent)
    for row in range(0, parent.shape[0]):
        for column in range(0, parent.shape[1]):
            if (np.random.rand() < probability):
                parent[row][column] = parent[row][column] + np.random.randint(lower, upper)
    return parent    

#Float Representation
#def uniformMutation():


def main():
    print(creepMutation(p.initializerPopulationInteger(10, 0 ,5, 1), 0.2, -1, 2))

if __name__ == "__main__":
    main()        
            
