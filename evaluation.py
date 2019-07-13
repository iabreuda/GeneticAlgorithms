import numpy as np

# Auxiliary Functions

def shiftVector(x, function_number):
    """ Offsets all elements of vector x by elements of vector offset """    
    offset = np.loadtxt('./input_data/shift_data_{}.txt'.format(function_number))[:len(x)]        
    return np.array(x)-offset

def rotateVector(x, function_number):
    """ Rotates the x function according to function_number file located in ./input_data/M_function_number_Ddim.txt"""    
    rotation = np.loadtxt('./input_data/M_{}_D{}.txt'.format(function_number, len(x)))            
    return np.array(x).dot(rotation)

def shiftRotateVector(x, function_number, shift_flag=True, rotate_flag=True, shift_rate=1): 
    """ :param x (np.array): 
        :param offset (np.array): 
        :rotation (np.array): rotation matrix
        :shift_flag (boolean): 
        :rotate_flag (boolean): 
        :shift_rate (float): 
    """

    if (shift_flag):   
        x_shift = shiftVector(x, function_number)
        # Shrink to the original search space 
        x_shrink = shift_rate*x_shift
        if not rotate_flag:
            return x_shrink
        return rotateVector(x_shrink, function_number)        
    
    # Shrink to the original search space 
    x_shrink = shift_rate*x    
    if not rotate_flag:
        return x_shrink

    return shiftVector(x_shrink, function_number)

def getCecFunction(function_number):
    switcher = {
        1: rotatedHighConditionedElliptic,
        2: rotatedBentCigar,
        6: shiftedRotatedWeierstrass,
        7: shiftedRotatedGriewank,
        9: shiftedRotatedRastrigin,
        14: shiftRotatedHGBat
    }
    return switcher.get(function_number, lambda: "Invalid function number: " + str(function_number))


# 1: High Conditioned Elliptic Function 
def rotatedHighConditionedElliptic(x, dim, function_number):
    x_rot = rotateVector(x, function_number)
    return highConditionedElliptic(x_rot, dim)

def highConditionedElliptic(x, dim):
    assert dim > 0
    res = 0
    for i, x_i in enumerate(x):
        res += (1e6)**((i-1)/(dim-1))*x_i**2
    
    return res 

# 2: Bent Cigar Function
def rotatedBentCigar(x, dim, function_number):
    x_rot = rotateVector(x, function_number)
    return bentCigar(x_rot, dim)

def bentCigar(x, dim):
    assert dim > 0    
    return x[0]**2 + 1e6*np.sum(np.array(x[1:dim])**2)
    
# 3: Discus Function 
def discus(x, dim):
    assert dim > 0    
    return 1e6*x[0]**2 + np.sum(np.array(x[1:dim])**2)

# 6: Weierstrass Function
def shiftedRotatedWeierstrass(x, dim, function_number, a = .5, b=3, k_max=20, shift_flag=True, rotate_flag=True, shift_rate=1):
    x_shifted_rot = shiftRotateVector(x, function_number, shift_flag=shift_flag, rotate_flag=rotate_flag, shift_rate=shift_rate)
    return weierstrass(x_shifted_rot, dim, a = .5, b=3, k_max=20)

def weierstrass(x, dim, a = .5, b=3, k_max=20):
    assert dim > 0
    x = np.array(x[:dim])
    sum_a, sum_b = 0, 0    
    for i, x_i in enumerate(x):
        for k in np.arange(k_max):
            sum_a += (a**k)*np.cos(2*np.pi*(b**k)*(x_i+0.5))
    for k in np.arange(k_max):
        sum_b += (a**k)*np.cos(2*np.pi*(b**k)*0.5)
        
    return sum_a-dim*sum_b

# 7: Griewank’s Function
def shiftedRotatedGriewank(x, dim, function_number, shift_flag=True, rotate_flag=True, shift_rate=1):
    x_shifted_rot = shiftRotateVector(x, function_number, shift_flag=shift_flag, rotate_flag=rotate_flag, shift_rate=shift_rate)
    return griewank(x_shifted_rot, dim)

def griewank(x, dim):
    x = np.array(x[:dim])
    prod = 0
    for i, x_i in enumerate(x):
        prod *= np.cos(x_i/np.sqrt(i+1))

    return 1/4000.0*np.sum((x**2))-prod+1

# 9: Rastrigin's Function
def shiftedRotatedRastrigin(x, dim, function_number, shift_flag=True, rotate_flag=True, shift_rate=1):
    x_shifted_rot = shiftRotateVector(x, function_number, shift_flag=shift_flag, rotate_flag=rotate_flag, shift_rate=shift_rate)
    return rastrigin(x_shifted_rot, dim)

def rastrigin(x, dim):
    assert dim > 0
    x = np.array(x[:dim])
    return np.sum(x**2-10*np.cos(2*np.pi*x)+10) 

# 10: Schwefel's Function
def shiftedRotatedSchwefel(x, dim, function_number, shift_flag=True, rotate_flag=True, shift_rate=1):
    x_shifted_rot = shiftRotateVector(x, function_number, shift_flag=shift_flag, rotate_flag=rotate_flag, shift_rate=shift_rate)
    return modifiedSchwefel(x_shifted_rot, dim)

def modifiedSchwefel(x, dim):
    assert dim > 0
    x = np.array(x[:dim])    
    res = 0
    def g(z):
        if abs(z) <= 500:
            return z*np.sin(np.sqrt(abs(z)))
        elif z > 500:
            return (500 - z%500)*np.sin(np.sqrt(abs(500-z%500)))-((z-500)**2)/(10000*dim)
        return (-500 + z%500)*np.sin(np.sqrt(abs(-500+z%500)))-((z+500)**2)/(10000*dim)
    for x_i in x:
        x_i = x_i+4.209687462275036e2
        res += g(x_i)
    
    return 418.9829*dim-res

# 14: HGBat Function
def shiftRotatedHGBat(x, dim, function_number, shift_flag=True, rotate_flag=True, shift_rate=1):
    x_shifted_rot = shiftRotateVector(x, function_number, shift_flag=shift_flag, rotate_flag=rotate_flag, shift_rate=shift_rate)
    return HGBat(x_shifted_rot, dim)

def HGBat(x, dim):
    assert dim > 0
    x = np.array(x)[:dim]
    return np.sqrt(np.sum(x**2)**2-np.sum(x)**2)+(0.5*np.sum(x**2)+np.sum(x))/dim + 0.5


# 16: Expanded Scaffer’s F6 Function
def expandedScafferF6(x, dim):
    assert dim > 0
    x = np.array(x[:dim])
    g = lambda x, y: .5+((np.sin(np.sqrt(x**2+y**2)))**2-0.5)/((1+.001*(x**2+y**2))**2)    
    res = 0
    for i in np.arange(len(x)-1):
        res += g(x[i], x[i+1])
    
    return res + g(x[-1], x[0])


if __name__ == "__main__":
    x = [0, 1, 0, 2]
    D = 4

    print (getCecFunction(2))

    print ('Rotated High Conditioned Elliptic:', highConditionedElliptic(x, D))
    print ('Bent Cigar Function:', bentCigar(x, D))
    print ('Discuss:', discus(x, D))
    print ('Weierstrass: ', weierstrass(x, D, a = .5, b=3, k_max=20))
    print ('Griewank:', griewank(x, D))
    print ('Modified Schwefel’s Function: ', modifiedSchwefel(x, D))
    print ('Expanded Scaffer’s F6:', expandedScafferF6(x, D))