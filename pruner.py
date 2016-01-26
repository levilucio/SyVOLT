'''
Created on Sep 6, 2015

@author: levi
'''

from util.ecore_utils import *
from core.himesis_utils import graph_to_dot
class Pruner(object):
    '''
    checks whether a path condition can be removed from the set of path conditions being built
    based on the fact that missing containment relations cannot be built by the rules that are
    left to symbolically execute
    '''

    def __init__(self, metamodel, transformation, rule_names):
        '''
        Constructor
        '''

        self.debug = True

        self.eu = EcoreUtils(metamodel)
        self.mmContainmentLinks = self.eu.getContaimentLinksForClasses()
        
        self.ruleContainmentLinks = {}
        self.ruleMissingContLinks = {}

        self.linksToRules = {}

        for layer in transformation:
            for rule in layer:
                self.ruleContainmentLinks[rule.name] = self.eu.getBuiltContainmentLinks(rule)
                self.ruleMissingContLinks[rule.name] = self.eu.getMissingContainmentLinks(rule)

                for contain_link in self.ruleContainmentLinks[rule.name]:

                    try:
                        self.linksToRules[contain_link].append(rule_names[rule.name])
                    except KeyError:
                        self.linksToRules[contain_link] = [rule_names[rule.name]]

                if self.debug:
                    rule_name = rule_names[rule.name]
                    print("Rule containment links: " + rule_name + " = " + str(self.ruleContainmentLinks[rule.name]))
                    print("Missing rule containment links: " + rule_name + " = " + str(self.ruleMissingContLinks[rule.name]))
                    print()

        #test containment links and see if any are missing

        for layer in transformation:
            for rule in layer:

                required_rules = []

                for className in self.ruleMissingContLinks[rule.name]:

                    found_class = False
                    for contain_rule_name, contain_links in self.ruleContainmentLinks.items():
                        if className in contain_links.keys():
                            found_class = True
                            required_rules.append([contain_rule_name, className])

                    if not found_class:
                        raise Exception("Error: No rule builds containment link for class " + className + " from rule.name " + rule_names[rule.name])



        self.mmClassParents = self.eu.getSuperClassInheritanceRelationForClasses()

        # print("mm class parents:")
        # for mm in self.mmClassParents:
        #     print(mm + " : " + str(self.mmClassParents[mm]))

        

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

        contLinksInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)
        
        # if self.debug:
        #     print("Rules to treat: ")
        #     for rule in rulesToTreat:
        #         print(rule)
        #     print("Containment links in rules to treat: " + str(contLinksInRulesToTreat))


        allMissingContLinksFound = True
        contLinksNotFound = []
        
#         # gather all the parents for all the classes that have missing containment links
#         # TODO: should be based on cached data
#         classesWithParentsToTreat = []
#         
#         for className in missingContLinks.keys():
#             classesWithParentsToTreat.extend(self.eu.buildInheritanceDependenciesForClass([className]))
#         
#         classesWithParentsToTreat = list(set(classesWithParentsToTreat))
         
        for className in missingContLinks.keys():

            classPlusParents = self.mmClassParents[className]
            classPlusParents.append(className)

            if set(classPlusParents).intersection(set(contLinksInRulesToTreat.keys())) == set():
                allMissingContLinksFound = False
                contLinksNotFound.append([className, missingContLinks[className]])
                break

            else:
                foundInParent = False
                # TODO: cache the parents
                # check if at least on of the containment links necessary for the class can still
                # be built by one of the remaining rules. It is possible that this will be done by
                # done by a parent of the class in one of the rules.
                parentClasses = self.mmClassParents[className]
                parentClasses.append(className)
                
                for parentClass in parentClasses:
                    if parentClass in contLinksInRulesToTreat.keys():
                        links = [link for link in missingContLinks[className] if link in contLinksInRulesToTreat[parentClass]]
                        if links:
                            foundInParent = True
                            break
                if not foundInParent:
                    allMissingContLinksFound = False
                    contLinksNotFound.append([className, missingContLinks[className]])
                    break
        
        if allMissingContLinksFound:

            if self.debug:
                print("... Pruner Returning True")
            return True
        else:
            if self.debug:
                print("=========================")
                print("Path condition: " + pathCondition.name)
                print("Missing containment links: " + str(contLinksNotFound))

                print("Looking for:")
                for contLink, contLinkEnd in contLinksNotFound:
                    print(self.linksToRules[contLink])

                # if len(missingContLinks) > 0:
                #     graph_to_dot("missing_" + pathCondition.name, pathCondition)

            if self.debug:
                print("... Pruner Returning False")
            return False
        
        
        
                
        
        