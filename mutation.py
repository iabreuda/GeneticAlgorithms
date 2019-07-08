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
    for row in range(0, parent.shape[0]):
        for column in range(0, parent.shape[1]):
            if (np.random.rand() < probability):
                parent[row][column] = parent[row][column] + np.random.randint(lower, upper)
    return parent    

#Float Representation
def uniformMutation(parent, probability, lower, upper):
    for i in range(len(parent)):
        if (np.random.rand() < probability):
            parent[i] = (upper - lower)*(np.random.rand()) + lower
    return parent        



def main():
    print(uniformMutation(p.initializePopulationReal(5, 0 ,5, 1), 0.5, 0, 5))

if __name__ == "__main__":
    main()        
            
