from problem import Problem
import sys
sys.path.append('..')
from utils import validateInteger, validateList, validateMatrix
import numpy as np
from individual import Individual
import copy


class MaximallyDiverseGroupingProblem(Problem):

    def __init__(self, groups, elements, distanceMatrix):
        """This class is responsible to describe problem specification

        Arguments:
            name {string} -- Name of the problem
        """
        Problem.__init__(self, "Maximally Diverse Grouping Problem")

        validateList(groups, "Groups must be a list of class Group")
        validateInteger(elements, "Number of Elements must be integer")
        validateList(distanceMatrix, "Distance matrix must be a list")
        validateMatrix(distanceMatrix, elements, "Distance matrix must have size Element x Element")

        self.groups = groups
        self.elements = elements
        self.distanceMatrix = distanceMatrix

    def getGroups(self):
        return self.groups

    def setGroups(self, groups):
        self.groups = groups

    def cloneGroups(self):
        groups = []
        for group in self.groups:
            groups.append(copy.deepcopy(group))
        return groups


    def addGroup(self, group):
        if next((g for g in self.groups if g.index == group.getIndex()), None) is None:
            self.groups.append(group)
        else:
            raise Exception("Groups cannot have same Index")

    def balanceGroups(self, individual):
        balanced = False
        while not balanced:
            less = []
            more = []
            slightlyLess = []
            slightlyMore = []

            for group in individual.getGroups():
                if group.groupStatus() < 0:
                    less.append(group)
                elif group.groupStatus() > 0:
                    more.append(group)
                if group.groupStatus() == 0 and len(group.getElements()) >= group.getMinElements() + 1:
                    slightlyMore.append(group)
                if group.groupStatus() == 0 and len(group.getElements()) <= group.getMaxElements() - 1:
                    slightlyLess.append(group)

            if (not less) and (not more):
                balanced =  True
                break
            if (more):
                groupMore = np.random.choice(more)
            else:
                groupMore = np.random.choice(slightlyMore)
            if (less):
                groupLess = np.random.choice(less)
            else:
                groupLess = np.random.choice(slightlyLess)

            element = np.random.choice(groupMore.getElements())
            groupMore.removeElements(element)
            groupLess.addElement(element)
            individual.getChromosome()[element] = groupLess.getIndex()


    def populateGroups(self, individual):
        for element, groupIndex in enumerate(individual.getChromosome()):
            group = next((grp for grp in individual.getGroups() if grp.index == groupIndex), None)
            if (group is None):
                raise Exception("Group could be not finded")
            group.addElement(element)

    def getElements(self):
        return self.elements

    def setElements(self, elements):
        self.elements = elements

    def getDistanceMatrix(self):
        return self.distanceMatrix

    def setDinstanceMatrix(self, distanceMatrix):
        self.distanceMatrix = distanceMatrix

    def getDistance(self, origin, destiny):
        return self.getDistanceMatrix()[origin][destiny]

    def evaluate(self, individual):
        self.incrementEvaluateCounter()
        totalFitness = 0
        for group in individual.getGroups():
            groupFitness = 0
            for origin in group.getElements():
                for destiny in group.getElements():
                    if destiny <= origin:
                        continue
                    groupFitness += self.getDistance(origin, destiny)
            group.setFitness(groupFitness)
            totalFitness += group.getFitness()
        individual.setFitness(totalFitness)

    def initialSolution(self, numberOfSolutions):
        individuals = []
        population = np.random.randint(low=1, high=len(self.groups) + 1, size=(numberOfSolutions, self.elements))
        for chromosome in population:
            individual = Individual(chromosome)
            individual.setGroups(self.cloneGroups())
            self.populateGroups(individual)
            self.balanceGroups(individual)
            individuals.append(individual)
        return individuals