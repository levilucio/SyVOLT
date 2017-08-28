'''
Created on Sep 6, 2015

@author: levi
'''


#work around strange importing in Python2
try:
    from pruner.pruner_helper import PrunerHelper
except ImportError:
    from .pruner_helper import PrunerHelper

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
        self.exception_on_exit = False

        self.collect_failure_results = False

        self.prunerHelper = PrunerHelper(metamodel, transformation, rule_names)

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

                # if self.debug:
                #     print("Rule: " + rule.name)
                #     self.prunerHelper.print_list("Missing Links in Rule", missing_links)

                links_not_found = self.will_links_be_built_lists(rule.name, missing_links, self.prunerHelper.ruleContainmentLinksExtended.keys(), require_all_links = True)

                if self.debug and len(links_not_found) > 0:
                    print("\nError for rule: " + self.rule_names[rule.name])
                    self.prunerHelper.print_dict("Missing Links (not found in transformation)", links_not_found)

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

        #record why pcs are being pruned
        self.failure_reasons = {}

    def will_links_be_built_lists(self, rule_name, missing_links, future_contain_rules, require_all_links = False):
        links_not_found = {}

        # all_keys = []
        # for rule in future_contain_rules:
        #     all_keys += list(self.prunerHelper.ruleContainmentLinksExtended[rule].keys())

        if self.debug:
            self.prunerHelper.print_list(rule_name + " Missing Containment links:", missing_links)

        # look at each class that the rule is missing
        for (className, la, lb) in missing_links:
            found_link = False
            if self.debug:
                print("Classname: " + className + " link: " + str([la, lb]))
                try:
                    print("Parents: " + str(self.prunerHelper.mmClassParents[className]))
                except KeyError:
                    pass

            for rule in future_contain_rules:
                if self.debug:
                    print("Looking at rule: " + rule)

                for parent_class in [className] + self.prunerHelper.mmClassParents[className]:
                    try:
                        vals = self.prunerHelper.ruleContainmentLinksExtended[rule][parent_class]
                        if self.debug:
                            print("Parent class: " + parent_class + " Vals: " + str(vals))
                        if (la, lb) in vals:
                            found_link = True
                            break
                    except KeyError:
                        pass

                if found_link:
                    break

            if self.debug:
                print("Found link: " + str(found_link))

            if not found_link:
                try:
                    if (la, lb) not in links_not_found[className]:
                        links_not_found[className].append((la, lb))
                except KeyError:
                    links_not_found[className] = [(la, lb)]

        if self.debug:
            if len(links_not_found) > 0:
                print("Links not found for " + rule_name)
                self.prunerHelper.print_dict("Links Not Found (in transformation)", links_not_found)

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

        #if self.debug:
        #    print(pathCondition.name)
        #self.debug = "Em_1R0-_2R0-_3R0-_4R0-.52" in pathCondition.name
        # if self.debug:
        #     raise Exception(pathCondition.name)


        rules_in_pc = self.pc_name_function(pathCondition.name)

        pc_missing_lists = self.combineForAll_lists(rules_in_pc, self.prunerHelper.ruleMissingContLinks_List)

        if self.debug:
            print("Rules in pc: " + str(rules_in_pc))
            print("Rules in missing list: " + str(self.prunerHelper.ruleMissingContLinks_List.keys()))

            print("Missing lists: " + str(pc_missing_lists))

        if len(pc_missing_lists) == 0:
            if self.debug:
                print("No missing links in rules, returning true")
                if self.exception_on_exit:
                    raise Exception()
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
            return True

        pc_built_lists = self.combineForAll_lists(rules_in_pc, self.prunerHelper.ruleContainmentLinks_List)

        # print("PC: ")
        # for r in rules_in_pc:
        #     print(self.rule_names[r])

        miss_counter = Counter(pc_missing_lists)
        built_counter = Counter(pc_built_lists)

        #print(miss_counter)
        #print(built_counter)

        if self.debug:
            self.prunerHelper.print_list("PC Missing", pc_missing_lists)
            self.prunerHelper.print_list("PC Built", pc_built_lists)

        miss_counter.subtract(built_counter)
        new_pc_missing_lists = [e for e in miss_counter.elements()]

        #self.prunerHelper.print_dict("PC Missing After", pc_missing)

        if len(new_pc_missing_lists) == 0:
            if self.debug:
                print("No missing links after built, returning true")
                if self.exception_on_exit:
                    raise Exception()
            return True

        missingLinks = self.will_links_be_built_lists(pathCondition.name, new_pc_missing_lists, rulesToTreat)

        if len(missingLinks) == 0:
            if self.debug:
                print("Links will be built, returning true")
                if self.exception_on_exit:
                    raise Exception()
            return True

        #not enough copies of the link may be built
        # if it was from a rule already in the pc
        link_already_built = True
        for className, values in missingLinks.items():
            for val in values:
                link = (className, val[0], val[1])
                rules_to_find = self.prunerHelper.links_to_rules[link]
                for r in rules_to_find:
                    if r not in rules_in_pc:
                        link_already_built = False
                        break

        if link_already_built:
            return True

        if self.debug:

            print("=========================")
            print("Path condition: " + pathCondition.name)
            self.prunerHelper.print_dict("Missing Links", missingLinks)
            self.prunerHelper.print_list("Missing Links", new_pc_missing_lists)
            # self.prunerHelper.print_list("Built Links", pc_built_lists)
            #graph_to_dot(pathCondition.name, pathCondition)

            print("Looking for the following rules:")

        if self.debug or self.collect_failure_results:
            for className, values in missingLinks.items():
                for val in values:
                    link = (className, val[0], val[1])
                    rules_to_find = self.prunerHelper.links_to_rules[link]

                    if self.debug:
                        print([self.rule_names[rule] for rule in rules_to_find])
                        print(rules_to_find)

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
        
                
        
        