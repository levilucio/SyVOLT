from copy import deepcopy

class PrunerHelper:

    def __init__(self, eu, transformation, rule_names):

        self.eu = eu

        self.rule_names = rule_names

        self.ruleContainmentLinks = {"HEmpty": {}}
        self.ruleMissingContLinks = {"HEmpty": {}}

        self.ruleContainmentLinksExtended = {"HEmpty": {}}
        #self.ruleMissingContLinksExtended = {"HEmpty": {}}

        self.mmClassParents = self.eu.getSuperClassInheritanceRelationForClasses()

        self.links_to_rules = {}

        for layer in transformation:
            for rule in layer:
                self.ruleContainmentLinks[rule.name] = self.eu.getBuiltContainmentLinks(rule)

                #print("\n================\nRule: " + self.rule_names[rule.name])
                #self.print_dict("Rule containment links", self.ruleContainmentLinks[rule.name])
                self.ruleContainmentLinksExtended[rule.name] = self.extend_links(self.ruleContainmentLinks[rule.name])
                #self.print_dict("ruleContainmentLinksExtended", self.ruleContainmentLinksExtended[rule.name])

                for classname, clinks in self.ruleContainmentLinksExtended[rule.name].items():
                    for clink in clinks:
                        link = (classname, clink[0], clink[1])
                        try:
                            self.links_to_rules[link].append(rule.name)
                        except KeyError:
                            self.links_to_rules[link] = [rule.name]

                #print("\nRule: " + rule.name)
                self.ruleMissingContLinks[rule.name] = self.eu.getMissingContainmentLinks(rule)

                #self.print_dict("ruleMissingContLinks (before removing built)", self.ruleMissingContLinks[rule.name])

                #remove those missing cont links which are built in the same rule
                missing_links_copy = deepcopy(self.ruleMissingContLinks[rule.name])
                self.ruleMissingContLinks[rule.name] = self.subtract_dicts(missing_links_copy, self.ruleContainmentLinksExtended[rule.name])


                # print("rule: " + rule.name)
                # self.print_dict("ruleMissingContLinks", self.ruleMissingContLinks[rule.name])
                # self.print_dict("cont links", self.ruleContainmentLinksExtended[rule.name])
                #self.ruleMissingContLinksExtended[rule.name] = self.extend_links(self.ruleMissingContLinks[rule.name])
                #self.print_dict("ruleMissingContLinksExtended", self.ruleMissingContLinksExtended[rule.name])


        #raise Exception()

        # for links, rules in self.links_to_rules.items():
        #     print(links)
        #     print(rules)


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

        new_links = dict.copy(links)

        for classname, clinks in links.items():
            parent_links = self.generate_parent_links(clinks)
            new_links[classname] = parent_links

            if classname not in self.mmClassParents:
                continue

            for classname_parent in self.mmClassParents[classname]:
                try:
                    new_links[classname_parent] += deepcopy(parent_links)
                except KeyError:
                    new_links[classname_parent] = deepcopy(parent_links)

        return new_links


    def generate_parent_links(self, links):
        new_links = deepcopy(links)
        for link in new_links:
            classname = link[0]
            linkname = link[1]
            if classname not in self.mmClassParents:
                continue
            for parent in self.mmClassParents[classname]:
                new_links.append((parent, linkname))
        return new_links


    def print_dict(self, name, d):
        print("\n" + name + ":")
        for k, v in sorted(d.items()):
            print(k + " :")
            try:
                for c in sorted(v):
                    print("\t" + str(c) + " : " + str(v[c]))
            except TypeError:
                for c in sorted(v):
                    print("\t" + str(c))