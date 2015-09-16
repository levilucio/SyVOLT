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

        self.ruleClasses = {}
        for layer in transformation:
            for rule in layer:
                self.ruleClasses[rule.name] = self.eu.getBuiltClasses(rule)                
        

    def getContainmentLinksBuiltByRuleSet(self, ruleNames):
        '''
        get all the containment links built by a set of rules
        '''
        builtContainmentLinks = []
        for ruleName in ruleNames:
            builtContainmentLinks.extend(self.ruleContainmentLinks[ruleName])
            
        return builtContainmentLinks


    def getClassesLinksBuiltByRuleSet(self, ruleNames):
        '''
        get all the classes built by a set of rules
        '''
        builtClasses = []
        for ruleName in ruleNames:
            builtClasses.extend(self.ruleClasses[ruleName])
            
        return builtClasses


    def isPathConditionStillFeasible(self, pathCondition, treatedRules, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''
        classesInPC = self.eu.getBuiltClasses(pathCondition)
        
        #print("Classes in PC: " + str(classesInPC))
        
        requiredContainmentInPC = []
        for classInPC in classesInPC:
            requiredContainmentInPC.extend(self.mmContainmentLinks[classInPC])
            
        requiredContainmentInPC = list(set(requiredContainmentInPC))
        
        requiredClassesInPC = []
        for reqContRel in requiredContainmentInPC:
            requiredClassesInPC.append(reqContRel[0])
            requiredClassesInPC.append(reqContRel[2])
        requiredClassesInPC = list(set(requiredClassesInPC))
            
        #print("Required classes in PC: " + str(requiredClassesInPC))                     
        
        containmentInTreatedRules = self.getContainmentLinksBuiltByRuleSet(treatedRules)
        classesInTreatedRules = self.getClassesLinksBuiltByRuleSet(treatedRules)
        
        #print("Classes in treated rules: " + str(classesInTreatedRules))            
        #print("Treated rules: " + str(treatedRules)) 
                
        containmentInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)
        classesInRulesToTreat = self.getClassesLinksBuiltByRuleSet(rulesToTreat)
        
        #print("Classes in rules to treat: " + str(classesInRulesToTreat))  
        #print("Treated rules: " + str(rulesToTreat)) 
                
        alreadyBuiltContainments = set(requiredContainmentInPC) - set(containmentInTreatedRules)
        containmentAfterAllRulesApplied = set(alreadyBuiltContainments) - set(containmentInRulesToTreat)
        
        alreadyBuiltClasses = set(requiredClassesInPC) - set(classesInTreatedRules)
        classesAfterAllRulesApplied = set(alreadyBuiltClasses) - set(classesInRulesToTreat)        
        
        if containmentAfterAllRulesApplied == set() and classesAfterAllRulesApplied == set():
            return True
        else:
#             print("-----------------------------------------------------------------")
#             print("-----------------------------------------------------------------")
#             print("INCONSISTENT CONTAINMENT")       
            return False
        
        
        
                
        
        