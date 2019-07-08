import numpy as np

# 1: Rotated High Conditioned Elliptic Function 
def rotatedHighConditionedElliptic(x, dim):
    assert dim > 0
    res = 0
    for i, x_i in enumerate(x):
        res += (1e6)**((i-1)/(dim-1))*x_i**2
    
    return res 

# 2: Bent Cigar Function
def bentCigar(x, dim):
    assert dim > 0    
    return x[0]**2 + 1e6*np.sum(np.array(x[1:D])**2)
    
# 3: Discus Function 
def discus(x, dim):
    assert dim > 0    
    return 1e6*x[0]**2 + np.sum(np.array(x[1:D])**2)

# 6: Weierstrass Function
# def weierstrass(x, dim, k_max=20, a=0.5, b=3):



    
if __name__ == "__main__":
    x = [0, 1, 0, 2]
    D = 4

    print ('Rotated High Conditioned Elliptic:', rotatedHighConditionedElliptic(x, D))
    print ('Bent Cigar Function:', bentCigar(x, D))