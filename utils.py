def validateInteger(variable, errorDescription):
    if not isinstance(variable, int):
        raise Exception(errorDescription)

def validateList(variable, errorDescription):
    if not isinstance(variable, list):
        raise Exception(errorDescription)

def validadeMinMaxConstraint(min, max, errorDescription):
    if (min > max):
        raise Exception(errorDescription)

def validateMatrix(matrix, dimension, errorDescription):
    n = len(matrix)
    m = len(matrix[0])
    if (n != m or n != dimension):
        raise Exception(errorDescription)