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
    return x[0]**2 + 1e6*np.sum(np.array(x[1:dim])**2)
    
# 3: Discus Function 
def discus(x, dim):
    assert dim > 0    
    return 1e6*x[0]**2 + np.sum(np.array(x[1:dim])**2)

# 6: Weierstrass Function
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
def griewank(x, dim):
    x = np.array(x[:dim])
    prod = 0
    for i, x_i in enumerate(x):
        prod *= np.cos(x_i/np.sqrt(i+1))

    return 1/4000.0*np.sum((x**2))-prod+1

# 9: Modified Schwefel’s Function
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


# 14: Expanded Scaffer’s F6 Function
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

    print ('Rotated High Conditioned Elliptic:', rotatedHighConditionedElliptic(x, D))
    print ('Bent Cigar Function:', bentCigar(x, D))
    print ('Discuss:', discus(x, D))
    print ('Weierstrass: ', weierstrass(x, D, a = .5, b=3, k_max=20))
    print ('Griewank:', griewank(x, D))
    print ('Modified Schwefel’s Function: ', modifiedSchwefel(x, D))
    print ('Expanded Scaffer’s F6:', expandedScafferF6(x, D))