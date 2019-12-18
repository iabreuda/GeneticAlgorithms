def validateInteger(variable, errorDescription):
    """Allow only integer variable

    Arguments:
        variable {any} -- variable to be analysed
        errorDescription {string} -- Message to be shown in error case

    Raises:
        Exception: Variable should be int
    """
    if not isinstance(variable, int):
        raise Exception(errorDescription)

def validateList(variable, errorDescription):
    """Allow only list variable

    Arguments:
        variable {any} -- variable to be analysed
        errorDescription {string} -- Message to be shown in error case

    Raises:
        Exception: Variable should be list
    """
    if not isinstance(variable, list):
        raise Exception(errorDescription)

def validadeMinMaxConstraint(min, max, errorDescription):
    """min must be less than max

    Arguments:
        min {int} -- lower limit
        max {int} -- upper limit
        errorDescription {string} -- message to be shown in error case

    Raises:
        Exception: Min must be less tahn max
    """
    if (min > max):
        raise Exception(errorDescription)

def validateMatrix(matrix, dimension, errorDescription):
    """matrix must be quadratic

    Arguments:
        matrix {array} -- matrix array combination
        dimension {int} -- matrix dimension
        errorDescription {string} -- message to be shown in error case

    Raises:
        Exception: Matrix must have dimension and be quadratic
    """
    n = len(matrix)
    m = len(matrix[0])
    if (n != m or n != dimension):
        raise Exception(errorDescription)