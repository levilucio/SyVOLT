from copy import deepcopy

class PrunerHelper:

    def __init__(self, eu, transformation):

        self.eu = eu

        self.ruleContainmentLinks = {"HEmpty": {}}
        self.ruleMissingContLinks = {"HEmpty": {}}

        self.ruleContainmentLinksExtended = {"HEmpty": {}}
        self.ruleMissingContLinksExtended = {"HEmpty": {}}

        self.mmClassParents = self.eu.getSuperClassInheritanceRelationForClasses()

        self.links_to_rules = {}

        for layer in transformation:
            for rule in layer:
                self.ruleContainmentLinks[rule.name] = self.eu.getBuiltContainmentLinks(rule)
                self.ruleMissingContLinks[rule.name] = self.eu.getMissingContainmentLinks(rule)

                print("\n================\nRule: " + rule.name)
                self.print_dict("Rule containment links:", self.ruleContainmentLinks[rule.name])
                self.ruleContainmentLinksExtended[rule.name] = self.extend_links(self.ruleContainmentLinks[rule.name])
                self.print_dict("ruleContainmentLinksExtended:", self.ruleContainmentLinksExtended[rule.name])

                for classname, clinks in self.ruleContainmentLinksExtended[rule.name].items():
                    for clink in clinks:
                        link = (classname, clink[0], clink[1])
                        try:
                            self.links_to_rules[link].append(rule.name)
                        except KeyError:
                            self.links_to_rules[link] = [rule.name]

                # self.print_dict("ruleMissingContLinks:", self.ruleMissingContLinks[rule.name])
                self.ruleMissingContLinksExtended[rule.name] = self.extend_links(self.ruleMissingContLinks[rule.name])
                # self.print_dict("ruleMissingContLinksExtended:", self.ruleMissingContLinksExtended[rule.name])


        # for links, rules in self.links_to_rules.items():
        #     print(links)
        #     print(rules)

        # build the list of contain links for each layer
        self.layer_contain_links = []
        for layer in transformation:
            layer_links = {}
            for rule in layer:
                rule_links = self.ruleContainmentLinksExtended[rule.name]

                for classname, links in rule_links.items():
                    if classname not in layer_links:
                        layer_links[classname] = links
                    else:
                        for link in links:
                            if link not in layer_links[classname]:
                                layer_links[classname].append(link)

            self.layer_contain_links.append(layer_links)

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