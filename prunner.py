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
            for className in self.ruleContainmentLinks[ruleName].keys():
                if className in builtContainmentLinks:
                    builtContainmentLinks[className].append(self.ruleContainmentLinks[ruleName][className])
                    builtContainmentLinks[className] = list(set(builtContainmentLinks[className]))
                else:
                    builtContainmentLinks[className] = [self.ruleContainmentLinks[ruleName][className]]
            
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
        
        print("Path condition: " + pathCondition.name)   
        print("Missing containment links: " + str(missingContLinks))                     
                
        contLinksInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)
        
        print("Containment links in rules to treat: " + str(contLinksInRulesToTreat))   
        
        allMissingContLinksFound = True 
                
        for className in missingContLinks.keys():
            if className not in contLinksInRulesToTreat.keys():
                allMissingContLinksFound = False
                break
            else:
                foundInParent = False
                # TODO: cache the parents
                # check if at least on of the containment links necessary for the class can still
                # be built by one of the remaining rules. It is possible that this will be done by
                # done by a parent of the class in one of the rules.
                parentClasses = self.eu.buildInheritanceDependenciesForClass([className])
                parentClasses.append(className)
                for parentClass in parentClasses:
                    if parentClass in contLinksInRulesToTreat.keys():
                        if set(missingContLinks[className]).intersection(set(contLinksInRulesToTreat[parentClass])) != set():
                            foundInParent = True
                            break
                if not foundInParent:
                    allMissingContLinksFound = False
                    break
        
        if allMissingContLinksFound:
            print("... Pruner Returning True")
            return True
        else: 
            print("... Pruner Returning False")
            return False
        
        
        
                
        
        