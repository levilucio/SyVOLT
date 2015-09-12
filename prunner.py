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
                self.ruleContainmentLinks[rule.name] = self.eu.getContainmentLinksForRuleOrPC(rule)



    def getContainmentLinksBuiltByRuleSet(self, ruleNames):
        '''
        get all the containment links built by a set of rules
        '''
        builtContainmentLinks = []
        for ruleName in ruleNames:
            builtContainmentLinks.extend(self.ruleContainmentLinks[ruleName])
            
        return builtContainmentLinks



    def isPathConditionStillFeasible(self, pathCondition, treatedRules, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''
        classesInPC = self.eu.getClassesBuiltByPathCondition(pathCondition)
        
        print("Classes in PC: " + str(classesInPC))
        
        requiredContainmentInPC = []
        for classInPC in classesInPC:
            requiredContainmentInPC.extend(self.mmContainmentLinks[classInPC])
            
        requiredContainmentInPC = list(set(requiredContainmentInPC))
            
        print("Required containment in PC: " + str(requiredContainmentInPC))                     
        
        containmentInTreatedRules = self.getContainmentLinksBuiltByRuleSet(treatedRules)
        
        print("Containment in treated rules: " + str(containmentInTreatedRules))            
        print("Treated rules: " + str(treatedRules)) 
                
        containmentInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)
        
        print("Containment in rules to treat: " + str(containmentInRulesToTreat))  
        print("Treated rules: " + str(rulesToTreat)) 
                
        alreadyBuiltContainments = set(requiredContainmentInPC) - set(containmentInTreatedRules)
        afterAllRulesApplied = set(alreadyBuiltContainments) - set(containmentInRulesToTreat)
        
        if afterAllRulesApplied == set():
            return True
        else:
            print("-----------------------------------------------------------------")
            print("-----------------------------------------------------------------")
            print("ICONSISTEST CONTINEMAME")       
            return False
        
        
        
                
        
        