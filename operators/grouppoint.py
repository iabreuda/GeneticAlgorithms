from crossover import CrossOver
import numpy as np
import sys
sys.path.append('../problems')
from group import Group
from individual import Individual

class GroupPoint(CrossOver):
    def __init__(self, firstParent, secondParent):
        """Class that handle grossover for groups problems

        Arguments:
            firstParent {individual} -- first parent
            secondParent {individual} -- second parent
        """
        CrossOver.__init__(self, "Group Point CrossOver", firstParent, secondParent)


    def make(self):
        """group crossover respecting hybridg GA crossover for group problems

        Returns:
            individual -- child generated after recombination
        """
        numberOfGroups = np.random.randint(1, len(self.getFirstParent().getGroups()))
        secParentGroups = np.random.choice(self.secondParent.getGroups(), numberOfGroups, replace=False)
        groups = []
        allSecElements = []
        numberOfElements = 0

        for grpSec in secParentGroups:
            allSecElements += grpSec.getElements()

        for grpFst in self.getFirstParent().getGroups():
            numberOfElements += len(grpFst.getElements())
            elements = list(set(grpFst.getElements()) - set(allSecElements))
            group = Group(grpFst.getIndex(), grpFst.getMinElements(), grpFst.getMaxElements())
            group.setElements(elements)
            groups.append(group)

        for grpSec in secParentGroups:
            for grpFst in groups:
                if grpSec.getIndex() == grpFst.getIndex():
                    grpFst.addElements(grpSec.getElements())

        child = Individual(np.zeros(numberOfElements))
        child.setGroups(groups)

        return child
