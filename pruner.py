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

        self.rule_names = rule_names

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

                #get the contain links for the other rules
                contain_links_to_build = {}
                for rule_name, contain_links in self.ruleContainmentLinks.items():
                    if rule_name != rule.name:
                        contain_links_to_build.update(contain_links)

                links_not_found = self.will_links_be_built(self.ruleMissingContLinks[rule.name], contain_links_to_build)

                if len(links_not_found) > 0:

                    link = links_not_found[0]
                    className = link[0]
                    source_class_name = link[1]

                    print("\nError for rule: " + self.rule_names[rule.name])
                    print("Missing containment links: ")
                    for l in links_not_found:
                        print(source_class_name + " -> " + l[2] + " -> " + className)

                        for cl, v in self.eu.containmentLinks.items():
                            for conLink in v:

                                if conLink[1] == l[2] and conLink[0] == source_class_name:

                                    if cl == className:
                                        #this contain link is not inherited
                                        continue

                                    print("\tInherited from:")
                                    print("\t" + conLink[0] + " -> " + conLink[1] + " -> " + cl)
                                    break

                    raise Exception()

        print("Containment links:")
        for k, v in sorted(self.ruleContainmentLinks.items()):
            print(k + " :")
            for c in v:
                print("\t" + str(c) + " : " + str(v[c]) )


    def will_links_be_built(self, contain_links, future_contain_links):

        links_not_found = []

        # look at each class that the rule is missing
        for className, link_names in contain_links.items():
            parentClasses = []
            if className in self.mmClassParents:
                parentClasses = self.mmClassParents[className]

            childClasses = []
            if className in self.mmClassChildren:
                childClasses = self.mmClassChildren[className]


            # look at each link the class is missing
            for source_class_name, link_name in link_names:
                found_link = False

                #print("\nLooking for:")
                #print(className + " : " + source_class_name + " : " + link_name)
               # print(str([className] + parentClasses + childClasses))
                #
                # print(self.ruleContainmentLinks)

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

                        #print("Found the link")
                        found_link = True
                        break

                if not found_link:
                    links_not_found.append((className, source_class_name, link_name))

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


    def isPathConditionStillFeasible(self, pathCondition, rulesToTreat):
        '''
        decide whether a path condition can be removed from the path condition set because the
        containment requirements cannot be fulfilled
        '''

        missingContLinks = self.eu.getMissingContainmentLinks(pathCondition)

        contLinksInRulesToTreat = self.getContainmentLinksBuiltByRuleSet(rulesToTreat)

        missingLinks = self.will_links_be_built(missingContLinks, contLinksInRulesToTreat)

        if len(missingLinks) == 0:

            #if self.debug:
            #    print("... Pruner Returning True")
            return True
        else:
            if self.debug:
                print("=========================")
                print("Path condition: " + pathCondition.name)
                print("Missing containment links: " + str(missingLinks))

                print("Links to be built:")
                for className, links in contLinksInRulesToTreat.items():
                    print(className + " : " + str(links))

                print("Looking for:")
                for contLink, a, b in missingLinks:
                    print(self.linksToRules[contLink])

                # if len(missingContLinks) > 0:
                #     graph_to_dot("missing_" + pathCondition.name, pathCondition)

            if self.debug:
                print("... Pruner Returning False")
            return False
        
        
        
                
        
        