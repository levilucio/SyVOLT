'''
Created on Sep 6, 2015

@author: levi
'''


#work around strange importing in Python2
try:
    from pruner.pruner_helper import PrunerHelper
except ImportError:
    from .pruner_helper import PrunerHelper

from collections import Counter, defaultdict
from copy import deepcopy
import time

class Pruner(object):
    '''
    checks whether a path condition can be removed from the set of path conditions being built
    based on the fact that missing containment relations cannot be built by the rules that are
    left to symbolically execute
    '''

    def __init__(self, do_pruning, metamodel, transformation, rule_names, pc_name_function):
        '''
        Constructor
        '''

        self.do_pruning = do_pruning

        self.debug = 0
        self.exception_on_exit = False

        self.collect_failure_results = False

        self.prunerHelper = PrunerHelper(metamodel, transformation, rule_names)

        self.rule_names = rule_names
        self.pc_name_function = pc_name_function

        self.rule_set_links = {}

        # test containment links and see if any are missing
        self.all_missing_contain_links = {}

        #self.pruning_time = 0

        if self.debug:
            print("\nPruner: Checking if missing containment links are present in the transformation")

        for layer_num in range(len(transformation)):
            for rule in transformation[layer_num]:
                missing_links = self.prunerHelper.ruleMissingContLinks_List[rule.name]

                if len(missing_links) == 0:
                    continue


                # if self.debug:
                #     print("Rule: " + rule.name)
                #     self.prunerHelper.display("Missing Links in Rule", missing_links)

                links_not_found = self.will_links_be_built_lists(rule.name, missing_links, self.prunerHelper.ruleContainmentLinksExtended.keys(), require_specific_link = True)


                if self.debug and len(links_not_found) > 0:
                    print("\nError for rule: " + self.rule_names[rule.name])
                    self.prunerHelper.display("Missing Links (not found in transformation)", links_not_found)

                if links_not_found:
                    #print("Link not found " + str(links_not_found))
                    self.prunerHelper.combine_dicts(self.all_missing_contain_links, links_not_found)


        #raise Exception()

        if self.debug:
            missing_count = 0
            for v in self.all_missing_contain_links.values():
                missing_count += len(v)
            print("\nTransformation is missing " + str(missing_count) + " containment links:")
            if missing_count > 0:
                self.prunerHelper.display("All missing containment links", self.all_missing_contain_links)


        self.prunerHelper.remove_all_missing_links(self.all_missing_contain_links)




        #raise Exception()

        #record why pcs are being pruned
        self.failure_reasons = {}

    def will_links_be_built_lists(self, rule_name, missing_links, future_contain_rules, require_specific_link = False):
        links_not_found = {}

        if self.debug > 1:
            self.prunerHelper.display(rule_name + " Missing Containment links:", missing_links)
            print("Future contain rules: " + str(sorted(future_contain_rules)))

        missing_link_counts = defaultdict(int)
        for link in missing_links:
            missing_link_counts[link] += 1

        found_link_counts = defaultdict(int)

        # look at each class that the rule is missing
        missing_links_sorted = sorted(set(missing_links), key=lambda l: (l[0], l[1], l[2]))
        for (className, la, lb) in missing_links_sorted:

            if self.debug > 1:
                print("Classname: " + className + " link: " + str([la, lb]))
                try:
                    print("Parents: " + str(sorted(self.prunerHelper.mmClassParents[className])))
                except KeyError:
                    pass



            for rule in sorted(future_contain_rules):
                if self.debug > 1:
                    print("\tLooking at rule: " + rule)

                for parent_class in [className] + sorted(self.prunerHelper.mmClassParents[className]):

                    if not require_specific_link:
                        # if the other rule provides ANY containment link to the parent,
                        # assume it can contain us
                        if parent_class in self.prunerHelper.ruleContainmentLinksExtended[rule]:
                            found_link_counts[(className, la, lb)] += 1

                            if self.debug > 1:
                                print("Found link: " + str(rule) + " = " + str((className, la, lb)) + " under classname: " + parent_class)
                                #self.prunerHelper.display("Rule links", self.prunerHelper.ruleContainmentLinksExtended[rule])
                            #break
                    else:
                        try:
                            if self.debug > 1:
                                print("\tParent class: " + parent_class + " Vals: " + str(self.prunerHelper.ruleContainmentLinksExtended[rule]))

                            vals = self.prunerHelper.ruleContainmentLinksExtended[rule][parent_class]

                            if (la, lb) in vals:
                                found_link_counts[(className, la, lb)] += 1
                                #break
                        except KeyError:
                            pass

                #if found_link:
                    #break



            # if not found_link:
            #     try:
            #         if (la, lb) not in links_not_found[className]:
            #             links_not_found[className].append((la, lb))
            #     except KeyError:
            #         links_not_found[className] = [(la, lb)]


        links_not_found = defaultdict(list)


        for link in missing_link_counts:
            #print("Link is: " + str(link))
            if missing_link_counts[link] > found_link_counts[link]:
                #print("Missing links: ")
                #print(missing_link_counts)

                #print("Found links:")
                #print(found_link_counts)

                links_not_found[link[0]].append((link[1], link[2]))
                #raise Exception()


        if self.debug > 1:
            if len(links_not_found) > 0:
                print("Links not found for " + rule_name)
                self.prunerHelper.display("Links Not Found (in transformation)", links_not_found)

                #raise Exception()


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

        if not self.do_pruning:
            return True

        #if self.debug:
        #    print(pathCondition.name)
        #self.debug = "5R3" in pathCondition.name
        # if self.debug:
        #     raise Exception(pathCondition.name)


        #pruning_start_time = time.time()

        rules_in_pc = self.pc_name_function(pathCondition.name)

        pc_missing_lists = self.combineForAll_lists(rules_in_pc, self.prunerHelper.ruleMissingContLinks_List)

        if self.debug:
            print("==Beginning pruner feasibility for " + pathCondition.name)
            print("Rules in pc: " + str(rules_in_pc))
            #print("Rules in missing list: " + str(self.prunerHelper.ruleMissingContLinks_List.keys()))

            print("Looking for PC missing links: " + str(pc_missing_lists))

        if len(pc_missing_lists) == 0:
            if self.debug:
                print("No missing links in rules, returning true")
                if self.exception_on_exit:
                    raise Exception()
            #self.pruning_time += time.time() - pruning_start_time
            return True

        #only keep the number of links needed that we have elements for
        mms = pathCondition.vs["mm__"]
        new_pc_missing_lists = []
        link_count = {}
        for link in pc_missing_lists:
            try:
                link_count[link[0]].append(link)
            except KeyError:
                link_count[link[0]] = [link]

        for key, values in link_count.items():
            count = mms.count(key)
            for i, val in enumerate(values):
                if i == count:
                    break
                new_pc_missing_lists.append(val)

        pc_missing_lists = new_pc_missing_lists

        if len(pc_missing_lists) == 0:
            if self.debug:
                print("No missing links, returning true")
                if self.exception_on_exit:
                    raise Exception()
            #self.pruning_time += time.time() - pruning_start_time
            return True

        missingLinks = self.will_links_be_built_lists(pathCondition.name, new_pc_missing_lists, rulesToTreat + rules_in_pc)

        if len(missingLinks) == 0:
            if self.debug:
                print("Links will be built, returning true")
                if self.exception_on_exit:
                    raise Exception()
            #self.pruning_time += time.time() - pruning_start_time
            return True

        #not enough copies of the link may be built
        # if it was from a rule already in the pc
        link_already_built = True
        for className, values in missingLinks.items():
            for val in values:
                #link = (className, val[0], val[1])
                link = (val[0], val[1])
                try:
                    rules_to_find = self.prunerHelper.links_to_rules[link]
                    for r in rules_to_find:
                        if r not in rules_in_pc:
                            link_already_built = False
                            break
                except KeyError:
                    # pass
                    print("Could not find link: " + str(link))
                    self.prunerHelper.display("Links to rules",self.prunerHelper.links_to_rules)
                    #raise Exception

        if link_already_built:
            #self.pruning_time += time.time() - pruning_start_time
            if self.debug:
                print("Link already built, returning true")
            return True

        if self.debug:

            print("Path condition: " + pathCondition.name)
            self.prunerHelper.display("Could not find these links (built or to be built", missingLinks)
            self.prunerHelper.display("Could not find these links (starting list)", new_pc_missing_lists)
            # self.prunerHelper.print_list("Built Links", pc_built_lists)
            #graph_to_dot(pathCondition.name, pathCondition)

            print("Looking for the following rules:")

        if self.debug or self.collect_failure_results:
            for className, values in missingLinks.items():
                for val in values:
                    link = (className, val[0], val[1])

                    try:
                        rules_to_find = self.prunerHelper.links_to_rules[link]
                    except KeyError:
                        print("No mapping from link: " + str(link) + " to rule")
                        continue

                    if self.debug:
                        print([str(rule) + " = " + str(self.rule_names[rule]) for rule in rules_to_find])

                    for rule in rules_in_pc:

                        if rule not in self.failure_reasons.keys():
                            self.failure_reasons[rule] = {}

                        if link not in self.failure_reasons[rule].keys():
                            self.failure_reasons[rule][link] = []

                        self.failure_reasons[rule][link] += rules_to_find

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
            if self.exception_on_exit:
                raise Exception()
        #self.pruning_time += time.time() - pruning_start_time
        return False
        
    def print_results(self):
        if not self.collect_failure_results:
            return

        if len(self.failure_reasons) == 0:
            return

        print("Pruner Failure Reasons:")
        for rule, links in sorted(self.failure_reasons.items()):
            print(rule)
            for link, rules_to_find in sorted(links.items()):
                print(link)
                print(Counter(rules_to_find).most_common())
        
                
        
        