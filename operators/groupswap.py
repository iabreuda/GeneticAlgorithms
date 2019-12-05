from mutation import Mutation
import numpy as np
import sys
sys.path.append('../problems')
from group import Group
from individual import Individual
import copy

class GroupSwap(Mutation):

    def __init__(self, parent):
        Mutation.__init__(self, "Swap Group Mutation", parent)


    def make(self):
        copiedGroups = []
        changes = False
        for group in self.parent.getGroups():
            copiedGroups.append(copy.deepcopy(group))

        for cGrp in copiedGroups:
            for element in cGrp.getElements():
                if (np.random.rand() < self.getMutationGeneProbability()):
                    changes = True
                    newGroup = cGrp
                    while (newGroup == cGrp):
                        newGroup = np.random.choice(copiedGroups)
                    newGroupElement = np.random.choice(newGroup.getElements())
                    newGroup.removeElements(newGroupElement)
                    newGroup.addElement(element)
                    cGrp.removeElements(element)
                    cGrp.addElement(newGroupElement)

        if changes:
            numberOfElements = len(copiedGroups[0].getElements())
            child = Individual(np.zeros(numberOfElements))
            child.setGroups(copiedGroups)
            return child
        return None




