from mutation import Mutation
import numpy as np
import sys
sys.path.append('../problems')
from group import Group
from individual import Individual
import copy

class DERand(Mutation):

    def __init__(self, firstAgent, secondAgent, thirdAgent, factor=0.8):
        Mutation.__init__(self, "DE Rand 1 Bin", firstAgent)
        self.firstAgent = firstAgent
        self.secondAgent = secondAgent
        self.thirdAgent = thirdAgent
        self.factor = factor


    def make(self):
        trialVector = self.firstAgent.getChromosome() + self.factor*(self.secondAgent.getChromosome() - self.thirdAgent.getChromosome())
        trialVector = Individual(trialVector)
        return trialVector




