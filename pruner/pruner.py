'''
Created on Sep 6, 2015

@author: levi
'''

from util.ecore_utils import EcoreUtils
from pruner.pruner_helper import PrunerHelper
from core.himesis_utils import graph_to_dot

from profiler import *
from operator import itemgetter
from collections import Counter

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

        self.prunerHelper = PrunerHelper(self.eu, transformation, rule_names)

        self.rule_names = rule_names
        self.pc_name_function = pc_name_function

        self.rule_set_links = {}

        # test containment links and see if any are missing
        self.all_missing_contain_links = {}

        for layer_num in range(len(transformation)):
            for rule in transformation[layer_num]:
                missing_links = self.prunerHelper.ruleMissingContLinks_List[rule.name]

                if len(missing_links) == 0:
                    continue

                links_not_found = self.will_links_be_built_lists(rule.name, missing_links, self.prunerHelper.ruleContainmentLinksExtended.keys(), require_all_links = True)

                if self.debug and len(links_not_found) > 0:
                    print("\nError for rule: " + self.rule_names[rule.name])
                    self.prunerHelper.print_dict("Missing Links", links_not_found)

                if len(links_not_found):
                    self.prunerHelper.combine_dicts(self.all_missing_contain_links, links_not_found)

        self.prunerHelper.remove_all_missing_links(self.all_missing_contain_links)


        if self.debug:
            missing_count = 0
            for v in self.all_missing_contain_links.values():
                missing_count += len(v)
            print("\nTransformation is missing " + str(missing_count) + " containment links:")
            if missing_count > 0:
                self.prunerHelper.print_dict("All missing containment links", self.all_missing_contain_links)

        #raise Exception()

    def will_links_be_built_lists(self, rule_name, missing_links, future_contain_rules, require_all_links = False):
        links_not_found = {}

        all_keys = []
        for rule in future_contain_rules:
            all_keys += list(self.prunerHelper.ruleContainmentLinksExtended[rule].keys())

        debug = False

        if debug:
            self.prunerHelper.print_dict(rule_name + " Missing Containment links:", missing_links)

        # look at each class that the rule is missing
        for (className, la, lb) in missing_links:
            found_link = True
            if className not in all_keys:
                found_link = False
            else:
                for rule in future_contain_rules:
                    try:
                        vals = self.prunerHelper.ruleContainmentLinksExtended[rule][className]
                        if (la, lb) not in vals:
                            found_link = False
                            break
                    except KeyError:
                        pass

            if not found_link:
                try:
                    if (la, lb) not in links_not_found[className]:
                        links_not_found[className].append((la, lb))
                except KeyError:
                    links_not_found[className] = [(la, lb)]

        if debug:
            if len(links_not_found) > 0:
                print("Links not found for " + rule_name)
                self.prunerHelper.print_dict("Not Found Links", links_not_found)

                raise Exception()
        return links_not_found


    def combineForAll_lists(self, ruleNames, sourceList):
        '''
        get all the links built by a set of rules, either containment or missing
        '''

        d1 = []
        for ruleName in ruleNames:
            d1 += sourceList[ruleName]
        return d1


    #@profile
    def isPathConditionStillFeasible(self, pathCondition, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''

        rules_in_pc = self.pc_name_function(pathCondition.name)

        pc_missing_lists = self.combineForAll_lists(rules_in_pc, self.prunerHelper.ruleMissingContLinks_List)

        if len(pc_missing_lists) == 0:
            return True

        pc_built_lists = self.combineForAll_lists(rules_in_pc, self.prunerHelper.ruleContainmentLinks_List)

        # print("PC: ")
        # for r in rules_in_pc:
        #     print(self.rule_names[r])

        miss_counter = Counter(pc_missing_lists)
        built_counter = Counter(pc_built_lists)

        #print(miss_counter)
        #print(built_counter)
        self.prunerHelper.print_list("PC Missing", pc_missing_lists)
        self.prunerHelper.print_list("PC Built", pc_built_lists)

        miss_counter.subtract(built_counter)
        pc_missing_lists = [e for e in miss_counter.elements()]

        #self.prunerHelper.print_dict("PC Missing After", pc_missing)

        if len(pc_missing_lists) == 0:
            return True

        missingLinks = self.will_links_be_built_lists(pathCondition.name, pc_missing_lists, rulesToTreat)

        if len(missingLinks) == 0:
            return True


        if self.debug:
            print("=========================")
            print("Path condition: " + pathCondition.name)
            self.prunerHelper.print_dict("Missing Links", missingLinks)

            # for className, values in missingLinks.items():
            #     for val in values:
            #         link = (className, val[0], val[1])
            #         rules_to_find = self.prunerHelper.links_to_rules[link]
            #         print([self.rule_names[rule] for rule in rules_to_find])
            #         print([self.rule_names[rule] for rule in rulesToTreat])
            #
            #         for find_rule in rules_to_find:
            #             if find_rule in rulesToTreat:
            #                 print("ERROR: Pruner incorrectly reports link will not be built!")
            #                 print(className + " " + str(val))
            #                 print("Built in rule: " + find_rule)
            #
            #                 raise Exception()

            # if len(missingContLinks) > 0:
            #     graph_to_dot("missing_" + pathCondition.name, pathCondition)

        if self.debug:
            print("... Pruner Returning False")
        return False
        
        
        
                
        
        