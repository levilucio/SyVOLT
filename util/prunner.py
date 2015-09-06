'''
Created on Sep 6, 2015

@author: levi
'''

from util.ecore_utils import *

class Prunner(object):
    '''
    checks whether a path condition can be removed from the set of path conditions being built
    based on the fact that missing containment relations cannot be built by the rules that are
    left to symbolically execute
    '''

    def __init__(self, metamodel, transformation):
        '''
        Constructor
        '''
        self.eu = EcoreUtils()
        self.mmContainmentLinks = self.eu.getContaimentLinksForClasses(metamodel)
        
        self.ruleContainmentLinks = {}
        for layer in transformation:
            for rule in layer:
                self.ruleContainmentLinks[rule.name] = self.eu.getContainmentLinksForRule(rule)


    def isPathConditionStillFeasible(self, pathCondition):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''
        classesInPC = self.getClassesBuiltByPathCondition(pathCondition)
        
                
        
        