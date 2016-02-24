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

        self.debug = False

        self.eu = EcoreUtils(metamodel)
        #self.mmContainmentLinks = self.eu.getContainmentLinksForClasses()
        
        self.ruleContainmentLinks = {}
        self.ruleMissingContLinks = {}

        self.linksToRules = {}

        self.mmClassParents = self.eu.getSuperClassInheritanceRelationForClasses()
        self.mmClassChildren = self.eu.getSubClassInheritanceRelationForClasses()

        for layer in transformation:
            for rule in layer:
                self.ruleContainmentLinks[rule.name] = self.eu.getBuiltContainmentLinks(rule)
                self.ruleMissingContLinks[rule.name] = self.eu.getMissingContainmentLinks(rule)

                for contain_link in self.ruleContainmentLinks[rule.name]:
                    try:
                        self.linksToRules[contain_link].append(rule_names[rule.name])
                    except KeyError:
                        self.linksToRules[contain_link] = [rule_names[rule.name]]

        #test containment links and see if any are missing
        required_rules = {}
        for layer in transformation:
            for rule in layer:

                required_rules[rule.name] = {}

                #look at each class that the rule is missing
                for className, link_names in self.ruleMissingContLinks[rule.name].items():

                    #look at each link the class is missing
                    for source_class_name, link_name in link_names:

                        found_link = False

                        # print("\nLooking for:")
                        # print(className + " : " + source_class_name + " : " + link_name)
                        #
                        # print(self.ruleContainmentLinks)

                        link = (source_class_name, link_name)

                        #look at the other rules
                        for contain_rule_name, contain_links in self.ruleContainmentLinks.items():

                            if not contain_links:
                                continue

                            real_contain_rule_name = rule_names[contain_rule_name]

                            #print(real_contain_rule_name + " : " + str(contain_links))

                            parentClasses = []
                            if className in self.mmClassParents:
                                parentClasses = self.mmClassParents[className]

                            childClasses = []
                            if className in self.mmClassChildren:
                                childClasses = self.mmClassChildren[className]

                            for cl_name in [className] + parentClasses + childClasses:
                                if cl_name in contain_links.keys() and link in contain_links[cl_name]:
                                    found_link = True
                                    break

                        if found_link:
                            full_link_name = className + "/" + link_name

                            try:
                                if real_contain_rule_name not in required_rules[rule.name][full_link_name]:
                                    required_rules[rule.name][full_link_name].append(real_contain_rule_name)
                            except KeyError:
                                required_rules[rule.name][full_link_name] = [real_contain_rule_name]
                        else:
                            message = "Error: No rule builds containment link '" + link_name + "' for class " + className + " from rule.name " + rule_names[rule.name]
                            required_rules[rule.name][className + "/" + link_name] = ["None!"]

                            print(message)

                            print("Containment links:")
                            for k, v in self.ruleContainmentLinks.items():
                                print(k + " : " + str(v))

                            if self.debug:
                               raise Exception(message)




        if self.debug:
            for layer in transformation:
                for rule in layer:
                    rule_name = rule_names[rule.name]
                    print("\nRule: " + rule_name)
                    if len(self.ruleContainmentLinks[rule.name]) > 0:
                        print("Provides containment links: ")
                        for k, v in self.ruleContainmentLinks[rule.name].items():
                            print(str(k) + " : " + str(v))
                    if len(required_rules[rule.name]) > 0:
                        print("\nMissing rule containment links: ")
                        for k, v in required_rules[rule.name].items():
                            print(str(k) + " : " + str(v))
                    print()

            print("MM class parents:")
            for mm in sorted(self.mmClassParents):
                print(mm + " : " + str(self.mmClassParents[mm]))
        

    def getContainmentLinksBuiltByRuleSet(self, ruleNames):
        '''
        get all the containment links built by a set of rules
        '''
        builtContainmentLinks = {}
        for ruleName in ruleNames:
            for className in self.ruleContainmentLinks[ruleName].keys():
                if className in builtContainmentLinks:
                    for link in self.ruleContainmentLinks[ruleName][className]:
                        if link not in builtContainmentLinks[className]:
                            builtContainmentLinks[className].append(link)
                else:
                    builtContainmentLinks[className] = self.ruleContainmentLinks[ruleName][className]

        # print("\nRulenames: " + str(ruleNames))
        # for c in builtContainmentLinks:
        #     print(c + " : " + str(builtContainmentLinks[c]))
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
            for link in missingContLinks[className]:
                foundLink = False


                parentClasses = []
                if className in self.mmClassParents:
                    parentClasses = self.mmClassParents[className]

                childClasses = []
                if className in self.mmClassChildren:
                    childClasses = self.mmClassChildren[className]

                for cl_name in [className] + parentClasses + childClasses:

                    if cl_name in contLinksInRulesToTreat and link in contLinksInRulesToTreat[cl_name]:
                        foundLink = True
                        continue

                if not foundLink:
                    contLinksNotFound.append((className, link[0], link[1]))
                    allMissingContLinksFound = False

            # classPlusParents = self.mmClassParents[className]
            # classPlusParents.append(className)
            #
            # print(classPlusParents)
            # print(contLinksInRulesToTreat)
            # raise Exception()

            # if set(classPlusParents).intersection(set(contLinksInRulesToTreat.keys())) == set():
            #     allMissingContLinksFound = False
            #     contLinksNotFound.append([className, missingContLinks[className]])
            #     break
            #
            # else:
            #     foundInParent = False
            #     # TODO: cache the parents
            #     # check if at least on of the containment links necessary for the class can still
            #     # be built by one of the remaining rules. It is possible that this will be done by
            #     # done by a parent of the class in one of the rules.
            #     parentClasses = self.mmClassParents[className]
            #     parentClasses.append(className)
            #
            #     for parentClass in parentClasses:
            #         if parentClass in contLinksInRulesToTreat.keys():
            #             links = [link for link in missingContLinks[className] if link in contLinksInRulesToTreat[parentClass]]
            #             if links:
            #                 foundInParent = True
            #                 break
            #     if not foundInParent:
            #         allMissingContLinksFound = False
            #         contLinksNotFound.append([className, missingContLinks[className]])
            #         break
        
        if allMissingContLinksFound:

            #if self.debug:
            #    print("... Pruner Returning True")
            return True
        else:
            if self.debug:
                print("=========================")
                print("Path condition: " + pathCondition.name)
                print("Missing containment links: " + str(contLinksNotFound))

                print("Links to be built:")
                for className, links in contLinksInRulesToTreat.items():
                    print(className + " : " + str(links))

                print("Looking for:")
                for contLink, a, b in contLinksNotFound:
                    print(self.linksToRules[contLink])

                # if len(missingContLinks) > 0:
                #     graph_to_dot("missing_" + pathCondition.name, pathCondition)

            if self.debug:
                print("... Pruner Returning False")
            return False
        
        
        
                
        
        