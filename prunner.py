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
        self.eu = EcoreUtils(metamodel)
        self.mmContainmentLinks = self.eu.getContaimentLinksForClasses()
        
        self.ruleContainmentLinks = {}
        for layer in transformation:
            for rule in layer:
                self.ruleContainmentLinks[rule.name] = self.eu.getBuiltContainmentLinks(rule)              
        

    def getContainmentLinksBuiltByRuleSet(self, ruleNames):
        '''
        get all the containment links built by a set of rules
        '''
        builtContainmentLinks = {}
        for ruleName in ruleNames:
            builtContainmentLinks.update(self.ruleContainmentLinks[ruleName])
            
        return builtContainmentLinks


    def getClassesLinksBuiltByRuleSet(self, ruleNames):
        '''
        get all the classes built by a set of rules
        '''
        builtClasses = []
        for ruleName in ruleNames:
            builtClasses.extend(self.ruleClasses[ruleName])
            
        return builtClasses


    def isPathConditionStillFeasible(self, pathCondition, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''
        missingContLinks = self.eu.getMissingContainmentLinks(pathCondition)
        
#         print("Path condition: " + pathCondition.name)   
#         print("Missing containment links: " + str(missingContLinks))                     
                
        contLinksInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)
        
#         print("Containment links in rules to treat: " + str(contLinksInRulesToTreat))   
        
        allMissingContLinksFound = True 
                
        for className in missingContLinks.keys():
            if className not in contLinksInRulesToTreat.keys():
                allMissingContLinksFound = False
                break
            elif set(missingContLinks[className]).intersection(set([contLinksInRulesToTreat[className]])) == set():
                allMissingContLinksFound = False
                break
        
        if allMissingContLinksFound:
            return True
        else: 
            return False
        
        
        
                
        
        