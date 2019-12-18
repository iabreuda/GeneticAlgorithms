import numpy as np
import sys
sys.path.append('../problems/')
sys.path.append('..')
from maximallydiversegroupingproblem import MaximallyDiverseGroupingProblem
from group import Group

def MDGPInstanceReader(path):
    """Reader to instances files

    Arguments:
        path {string} -- instance configuration file

    Returns:
        MaximallyDiverseGroupingProblem -- Instance of MDGP problem
    """
    with open(path) as f:
        lines = f.read().splitlines()

    lines = list(map(lambda x: x.strip().split(" "), lines))

    numberOfElements = int(lines[0][0])
    numberOfGroups = int(lines[0][1])

    distanceMatrix = np.zeros(shape=(numberOfElements,numberOfElements)).tolist()
    for line in lines[1:]:
        distanceMatrix[int(line[0])][int(line[1])] = float(line[2])

    groups = []
    for index in range(numberOfGroups):
        minLimit = int(lines[0][(2*(index + 1)) + 1])
        maxLimit = int(lines[0][(2*(index + 1)) + 2])
        group = Group(index + 1, minLimit , maxLimit)
        groups.append(group)

    return MaximallyDiverseGroupingProblem(groups, numberOfElements, distanceMatrix)


