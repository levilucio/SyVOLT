from copy import deepcopy
from util.ecore_utils import EcoreUtils

class PrunerHelper:

    def __init__(self, metamodel, transformation, rule_names):

        self.debug = 0

        # raise Exception()
        self.rule_names = rule_names

        empty_pc_name = "Em"
        ruleContainmentLinks = {empty_pc_name: {}}
        self.ruleMissingContLinks = {empty_pc_name: {}}

        self.ruleContainmentLinksExtended = {empty_pc_name: {}}
        #self.ruleMissingContLinksExtended = {"HEmpty": {}}

        self.ruleContainmentLinks_List = {empty_pc_name: []}
        self.ruleMissingContLinks_List = {empty_pc_name: []}

        eu = EcoreUtils(metamodel)
        self.mmClassParents = eu.getSuperClassInheritanceRelationForClasses()
        self.mmClassChildren = eu.getSubClassInheritanceRelationForClasses()

        self.links_to_rules = {}

        #print("Transformation: " + str(transformation))

        for layer in transformation:
            for rule in layer:

                ruleContainmentLinks[rule.name] = eu.getBuiltContainmentLinks(rule)

                if self.debug:
                    print("\n================\nRule: " + self.rule_names[rule.name] + " = " + rule.name)
                    self.display("Rule containment links", ruleContainmentLinks[rule.name])

                self.ruleContainmentLinksExtended[rule.name] = self.extend_links(ruleContainmentLinks[rule.name])

                #if self.debug:
                #    self.display("ruleContainmentLinksExtended", self.ruleContainmentLinksExtended[rule.name])

                for classname, clinks in self.ruleContainmentLinksExtended[rule.name].items():
                    for clink in clinks:
                        #link = (classname, clink[0], clink[1])
                        link = (clink[0], clink[1])

                        try:
                            if rule.name not in self.links_to_rules[link]:
                                self.links_to_rules[link].append(rule.name)
                        except KeyError:
                            self.links_to_rules[link] = [rule.name]

                #print("\nRule: " + rule.name)
                self.ruleMissingContLinks[rule.name] = eu.getMissingContainmentLinks(rule)

                if self.debug:
                    self.display("ruleMissingContLinks (before removing built)", self.ruleMissingContLinks[rule.name])

                #remove those missing cont links which are built in the same rule
                #missing_links_copy = deepcopy(self.ruleMissingContLinks[rule.name])
                #self.ruleMissingContLinks[rule.name] = self.subtract_dicts(missing_links_copy, self.ruleContainmentLinksExtended[rule.name])


                new_containment_links = self.remove_built_links(self.ruleMissingContLinks[rule.name], self.ruleContainmentLinksExtended[rule.name])


                #if self.debug:
                #    self.display("New missing containment links", new_containment_links)

                self.ruleMissingContLinks[rule.name] = new_containment_links

                self.ruleContainmentLinks_List[rule.name] = self.collapse_dict(self.ruleContainmentLinksExtended[rule.name])
                self.ruleMissingContLinks_List[rule.name] = self.collapse_dict(self.ruleMissingContLinks[rule.name])

                if self.debug:

                    self.display("Rule {0} Missing Links".format(rule.name), self.ruleMissingContLinks[rule.name])

                    self.display("Rule {0} Built Links".format(rule.name), self.ruleContainmentLinks_List[rule.name])


                # print("rule: " + rule.name)
                #self.display("ruleMissingContLinks", self.ruleMissingContLinks_List[rule.name])
                #self.display("cont links", self.ruleContainmentLinks_List[rule.name])
                #self.ruleMissingContLinksExtended[rule.name] = self.extend_links(self.ruleMissingContLinks[rule.name])
                #self.display("ruleMissingContLinksExtended", self.ruleMissingContLinksExtended[rule.name])


        #raise Exception()

        # for links, rules in self.links_to_rules.items():
        #     print(links)
        #     print(rules)
        # raise Exception()

    def remove_built_links(self, missing, built):
        new_containment_links = {}

        for classname, clinks in missing.items():
            # print(classname)
            # print(clinks)

            for clink in clinks:
                cl, link_name = clink

                found_link = False

                try:
                    # print(self.ruleMissingContLinks[rule.name][classname])

                    for built_link in built[classname]:
                        if built_link[1] == link_name:
                            found_link = True


                except KeyError:
                    if self.debug > 1:
                        print("Couldn't find " + classname)

                if not found_link:
                    if not classname in new_containment_links.keys():
                        new_containment_links[classname] = []
                    new_containment_links[classname].append(clink)

                else:
                    if self.debug > 1:
                        print("Found link: " + str(clink))

        return new_containment_links


    def collapse_dict(self, d):
        l = []
        for key, values in d.items():
            for v in values:
                l.append((key, v[0], v[1]))
        return l


    def remove_all_missing_links(self, all_missing_links):
        for rule, links in self.ruleMissingContLinks.items():
            self.ruleMissingContLinks[rule] = self.subtract_dicts(self.ruleMissingContLinks[rule], all_missing_links)
            self.ruleMissingContLinks_List[rule] = self.collapse_dict(self.ruleMissingContLinks[rule])

            #self.display("self.ruleMissingContLinks_List[" + rule + "]", self.ruleMissingContLinks_List[rule])

    def combine_dicts(self, d1, d2):
        for key, value in d2.items():
            if key not in d1:
                d1[key] = [v for v in value]
                continue
            for v in value:
                if v not in d1[key]:
                    d1[key].append(v)
        return d1

    #take everything out of d1 that is in d2
    def subtract_dicts(self, d1, d2):
        for key, values in d2.items():
            if key not in d1:
                continue

            for val in values:
                try:
                    d1[key].remove(val)
                except ValueError:
                    pass
        d1 = {k:v for k, v in d1.items() if v }
        return d1

    def compare_dicts(self, d1, d2, throw_exception=False):
        for key, values in d1.items():
            if key not in d2.keys():
                print("Key: " + key + " is not in second dict!")
                if throw_exception:
                    raise Exception()
            else:
                for val in values:
                    if val not in d2[key]:
                        print("Value: " + str(val) + " is not in first dict!")
                        print(key + " " + str(val))
                        if throw_exception:
                            raise Exception()

        for key, values in d2.items():
            if key not in d1.keys():
                print("Key: " + key + " is not in first dict!")
                if throw_exception:
                    raise Exception()
            else:
                for val in values:
                    if val not in d1[key]:
                        print("Value: " + str(val) + " is not in first dict!")
                        print(key + " " + str(val))
                        if throw_exception:
                            raise Exception()

    def extend_links(self, links):
        if len(links) == 0:
            return {}

        new_links = deepcopy(links)

        # for classname, clinks in links.items():
        #     child_links = self.generate_child_links(clinks)
        #     new_links[classname] = child_links
        #
        #     if classname not in self.mmClassParents:
        #         continue
        #
        #     for classname_parent in self.mmClassParents[classname]:
        #         #print("Class: " + classname + " Parent: " + classname_parent)
        #         try:
        #             new_links[classname_parent] += deepcopy(child_links)
        #         except KeyError:
        #             new_links[classname_parent] = deepcopy(child_links)

        return new_links


    def generate_child_links(self, links):
        new_links = deepcopy(links)
        for link in new_links:
            classname = link[0]
            linkname = link[1]
            if classname not in self.mmClassChildren:
                continue
            for child in self.mmClassChildren[classname]:
                new_links.append((child, linkname))
        return new_links


    def display(self, name, t):
        print("\n" + name + ":")
        if str(type(t)) == "<class 'list'>":
            print(sorted(t))
        else:
            for k, v in sorted(t.items()):
                print(str(k) + " :")
                try:
                    for c in sorted(v):
                        print("\t" + str(c) + " : " + str(v[c]))
                except TypeError:
                    for c in sorted(v):
                        print("\t" + str(c))
