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


        #test containment links and see if any are missing
        self.all_missing_contain_links = []

        for layer_num in range(len(transformation)):
            for rule in transformation[layer_num]:

                print(rule.name)

                missing_links = self.prunerHelper.ruleMissingContLinks[rule.name]

                print(missing_links)

        # for layer in transformation:
        #     for rule in layer:
        #
        #         #get the contain links for the other rules
        #         contain_links_to_build = {}
        #         for rule_name, contain_links in self.ruleContainmentLinks.items():
        #             if rule_name != rule.name:
        #                 self.combine_dicts(contain_links_to_build, contain_links)
        #
        #         links_not_found = self.will_links_be_built(rule.name, self.ruleMissingContLinks[rule.name], contain_links_to_build, require_all_links = True)
        #
        #         if len(links_not_found) > 0:
        #             print("\nError for rule: " + self.rule_names[rule.name])
        #             self.print_missing_links(links_not_found, rule)

        # if self.debug:
        #     self.print_dict("Containment links", self.ruleContainmentLinks)

        if self.debug:
            print("\nTransformation is missing " + str(len(self.all_missing_contain_links)) + " containment links:")
            for missing_link in sorted(self.all_missing_contain_links):
                print(missing_link[0] + " -> " + missing_link[1] + " -> " + missing_link[2])

        raise Exception()




    def print_missing_links(self, links_not_found, rule):
        # map to where link was inherited from
        original_links = self.eu.originalLinks

        print("Rule is missing containment links: ")
        for l in sorted(links_not_found, key=itemgetter(1,2,0)):
            if l not in self.all_missing_contain_links:
                self.all_missing_contain_links.append(l)

            className = l[0]
            missing_link = (l[1], l[2], className)
            print(missing_link[0] + " -> " + missing_link[1] + " -> " + className)

            try:
                inherited_links = original_links[className]
                if (missing_link[0], missing_link[1]) in inherited_links:
                    class_inherited_from = inherited_links[(missing_link[0], missing_link[1])]
                    print("\tInherited from:")
                    print("\t" + str(class_inherited_from) + " -> " + missing_link[1] + " -> " + className)
                else:
                    pass
                    # print("Not inherited")
                    #
                    # for k in sorted(original_links[className].keys()):
                    #     print(k)
                    #     print(original_links[className][k])

            except KeyError:
                pass
                # print("Not inherited")
                # print(original_links)


    def will_links_be_built(self, rule_name, contain_links, future_contain_links, require_all_links = False):

        links_not_found = []

        if len(contain_links) == 0:
            return []

        debug = False

        # if "L0R2" in rule_name:
        #      debug = True

        if debug:
            self.print_dict(rule_name + " Missing Containment links:", contain_links)

        # look at each class that the rule is missing
        for className, link_names in sorted(contain_links.items()):
            parentClasses = []
            if className in self.mmClassParents:
                parentClasses = self.mmClassParents[className]

            childClasses = []
            if className in self.mmClassChildren:
                childClasses = self.mmClassChildren[className]

            # look at each link the class is missing

            found_one_contain_link = False
            for source_class_name, link_name in sorted(link_names, key=itemgetter(0, 1)):
                found_link = False

                if debug:
                    print("\nLooking for:")
                    print(className + " : " + source_class_name + " : " + link_name)
                #print(str([className] + parentClasses + childClasses))

                #print(self.ruleContainmentLinks)

                if not require_all_links and found_one_contain_link:
                    break

                #try all possibilities for the className
                for cl_name in [className] + parentClasses + childClasses:
                    if cl_name not in future_contain_links.keys():
                        continue

                    if found_link:
                        break

                    #look at all links
                    for other_link in future_contain_links[cl_name]:

                        #print("\n\tComparing to:")
                        #print("\t" + cl_name + " : " + other_link[0] + " : " + other_link[1])


                        #the link name doesn't match
                        if link_name != other_link[1]:
                            continue

                        #now check to see if the source class is in the inheritance heirarchy
                        source_class = [source_class_name]
                        if source_class_name in self.mmClassParents:
                            source_class += self.mmClassParents[source_class_name]
                        if source_class_name in self.mmClassChildren:
                            source_class += self.mmClassChildren[source_class_name]

                        if other_link[0] not in source_class:
                            #print("Source class not in heirarchy")
                            continue

                        if debug:
                            print("Matched on: " + str(other_link))
                        #print("Found the link")
                        found_link = True
                        found_one_contain_link = True
                        break

                if not found_link:
                    links_not_found.append((className, source_class_name, link_name))

        if debug:
            if len(links_not_found) > 0:
                print("Links not found for " + rule_name)
                for link in sorted(links_not_found):
                    print(link)

            #raise Exception()
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
        
        
        
                
        
        