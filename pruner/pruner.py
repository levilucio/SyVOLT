'''
Created on Sep 6, 2015

@author: levi
'''

from util.ecore_utils import EcoreUtils
from pruner.pruner_helper import PrunerHelper
from core.himesis_utils import graph_to_dot

from profiler import *
from operator import itemgetter

class Pruner(object):
    '''
    checks whether a path condition can be removed from the set of path conditions being built
    based on the fact that missing containment relations cannot be built by the rules that are
    left to symbolically execute
    '''

    def __init__(self, metamodel, transformation, rule_names, pc_name_function):
        '''
        Constructor
        '''

        self.debug = True

        self.eu = EcoreUtils(metamodel)

        self.prunerHelper = PrunerHelper(self.eu, transformation)


        self.rule_names = rule_names
        self.pc_name_function = pc_name_function


        all_contain_links = {}

        for layer in transformation:
            for rule in layer:
                all_contain_links = self.prunerHelper.combine_dicts(all_contain_links, self.prunerHelper.ruleContainmentLinksExtended[rule.name])


        # test containment links and see if any are missing
        self.all_missing_contain_links = {}

        for layer_num in range(len(transformation)):
            for rule in transformation[layer_num]:
                missing_links = self.prunerHelper.ruleMissingContLinks[rule.name]

                if len(missing_links) == 0:
                    continue

                links_not_found = self.will_links_be_built(rule.name, missing_links, all_contain_links, require_all_links = True)

                if self.debug and len(links_not_found) > 0:
                    print("\nError for rule: " + self.rule_names[rule.name])
                    self.prunerHelper.print_dict("Missing Links", links_not_found)

                if len(links_not_found):
                    self.combine_dicts(self.all_missing_contain_links, links_not_found)


        if self.debug:
            missing_count = 0
            for v in self.all_missing_contain_links.values():
                missing_count += len(v)
            print("\nTransformation is missing " + str(missing_count) + " containment links:")
            if missing_count > 0:
                self.prunerHelper.print_dict("All missing containment links", self.all_missing_contain_links)


    def will_links_be_built(self, rule_name, missing_links, future_contain_links, require_all_links = False):

        links_not_found = {}

        debug = False

        if debug:
            self.prunerHelper.print_dict(rule_name + " Missing Containment links:", missing_links)

        # look at each class that the rule is missing
        for className, link_names in sorted(missing_links.items()):

            for link in link_names:

                if className not in future_contain_links or link not in future_contain_links[className]:
                    try:
                        if link not in links_not_found[className]:
                            links_not_found[className].append(link)
                    except KeyError:
                        links_not_found[className] = [link]

        if debug:
            if len(links_not_found) > 0:
                print("Links not found for " + rule_name)
                self.prunerHelper.print_dict("Not Found Links", links_not_found)

                raise Exception()
        return links_not_found



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

    def combine_dicts(self, d1, d2):
        for key, value in d2.items():
            if key not in d1:
                d1[key] = [v for v in value]
                continue
            for v in value:
                if v not in d1[key]:
                    d1[key].append(v)

    #@profile
    def isPathConditionStillFeasible(self, pathCondition, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''

        rules_in_pc = self.pc_name_function(pathCondition.name)

        all_missing = {}
        all_built = {}
        for rule in rules_in_pc:
            self.combine_dicts(all_missing, self.ruleMissingContLinks[rule])
            self.combine_dicts(all_built, self.ruleContainmentLinks[rule])

        if len(all_missing) == 0:
            return True

        contLinksInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)
        contLinksInRulesToTreat.update(all_built)


        missingLinks = self.will_links_be_built(pathCondition.name, all_missing, contLinksInRulesToTreat)

        #remove all the containment links we know to be missing
        for ml in self.all_missing_contain_links:
            if ml in missingLinks:
                missingLinks.remove(ml)

        if len(missingLinks) == 0:

            #if self.debug:
            #   print("... Pruner Returning True")
            return True
        else:
            #raise Exception()

            if self.debug:
                print("=========================")
                print("Path condition: " + pathCondition.name)
                print("Missing containment links: " + str(missingLinks))

                # print("Links to be built:")
                # for className, links in contLinksInRulesToTreat.items():
                #     print(className + " : " + str(links))

                print("Future rules:")
                future_rules = [self.rule_names[rule] for rule in rulesToTreat]

                print("Looking for:")
                for contLink, a, b in missingLinks:
                    print(self.linksToRules[contLink])
                    for rule in self.linksToRules[contLink]:
                        if rule in future_rules:
                            rule_index = future_rules.index(rule)
                            print("ERROR: Pruner incorrectly reports link will not be built!")
                            print(contLink)
                            print("Built in rule: " + rule + " which builds:")
                            print(self.ruleContainmentLinks[rulesToTreat[rule_index]])
                            raise Exception()


                # if len(missingContLinks) > 0:
                #     graph_to_dot("missing_" + pathCondition.name, pathCondition)

            if self.debug:
                print("... Pruner Returning False")
            return False
        
        
        
                
        
        