'''
Created on Sep 6, 2015

@author: levi
'''

from util.new_ecore_utils import EcoreUtils as NewEcoreUtils
from util.ecore_utils2 import EcoreUtils
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

        self.debug = False

        self.eu = EcoreUtils(metamodel)
        self.new_eu = NewEcoreUtils(metamodel)

        self.prunerHelper = PrunerHelper(self.eu, self.new_eu, transformation, rule_names)

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
                    self.prunerHelper.combine_dicts(self.all_missing_contain_links, links_not_found)


        if self.debug:
            missing_count = 0
            for v in self.all_missing_contain_links.values():
                missing_count += len(v)
            print("\nTransformation is missing " + str(missing_count) + " containment links:")
            if missing_count > 0:
                self.prunerHelper.print_dict("All missing containment links", self.all_missing_contain_links)

        #raise Exception()

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



    def combineForAll(self, ruleNames, sourceDict):
        '''
        get all the links built by a set of rules, either containment or missing
        '''
        links = {}
        for ruleName in ruleNames:
            links = self.prunerHelper.combine_dicts(links, sourceDict[ruleName])
        return links


    #@profile
    def isPathConditionStillFeasible(self, pathCondition, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''

        rules_in_pc = self.pc_name_function(pathCondition.name)

        pc_missing = self.combineForAll(rules_in_pc, self.prunerHelper.ruleMissingContLinks)
        if len(pc_missing) == 0:
            return True

        pc_built = self.combineForAll(rules_in_pc, self.prunerHelper.ruleContainmentLinksExtended)

        #print("PC: " + pathCondition.name)
        #self.prunerHelper.print_dict("PC Missing", pc_missing)
        #self.prunerHelper.print_dict("PC Built", pc_built)
        pc_missing = self.prunerHelper.subtract_dicts(pc_missing, pc_built)

        #self.prunerHelper.print_dict("PC Missing After", pc_missing)

        if len(pc_missing) == 0:
            return True

        rule_links = self.combineForAll(rulesToTreat, self.prunerHelper.ruleContainmentLinksExtended)

        missingLinks = self.will_links_be_built(pathCondition.name, pc_missing, rule_links)

        if len(missingLinks) == 0:
            return True

        missingLinks = self.prunerHelper.subtract_dicts(missingLinks, self.all_missing_contain_links)

        if len(missingLinks) == 0:
            return True

        if self.debug:
            print("=========================")
            print("Path condition: " + pathCondition.name)
            self.prunerHelper.print_dict("Missing Links", missingLinks)

            self.prunerHelper.print_dict("Links to be built", rule_links)


            for className, values in missingLinks.items():
                for val in values:
                    link = (className, val[0], val[1])
                    rules_to_find = self.prunerHelper.links_to_rules[link]
                    print([self.rule_names[rule] for rule in rules_to_find])
                    print([self.rule_names[rule] for rule in rulesToTreat])

                    for find_rule in rules_to_find:
                        if find_rule in rulesToTreat:
                            print("ERROR: Pruner incorrectly reports link will not be built!")
                            print(className + " " + str(val))
                            print("Built in rule: " + find_rule)

                            raise Exception()

            # if len(missingContLinks) > 0:
            #     graph_to_dot("missing_" + pathCondition.name, pathCondition)

        if self.debug:
            print("... Pruner Returning False")
        return False
        
        
        
                
        
        