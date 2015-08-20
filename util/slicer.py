from core.himesis_plus import look_for_attached


class Slicer():


    def __init__(self, rules, transformation):

        self.backward_links = {}
        self.direct_links = {}
        self.match_elements = {}
        self.apply_elements = {}

        self.rules = rules
        self.transformation = transformation

        for r in self.rules.values():
            self.decompose_graph(r)


    def decompose_graph(self, graph):
        #decompose graph into directLinks, backwardLinks, and isolated elements


        #print("Decomposing graph: " + graph.name)
        direct_links = []
        backward_links = []
        match_elements = []
        apply_elements = []

        vs = graph.vs
        for i in range(len(vs)):
            v = vs[i]
            mm = v["mm__"]

            if "directLink" in mm:
                direct_links.append(i)
            elif "trace_link" in mm or "backward_link" in mm:
                backward_links.append(i)
            else:
                if mm in ["MatchModel", "ApplyModel", "paired_with"]:
                    continue

                neighbours = look_for_attached(i, graph)
                for n in neighbours[:1]:
                    n_mm = vs[n]["mm__"]
                    if n_mm == "match_contains":
                        match_elements.append(mm)
                        break
                    elif n_mm == "apply_contains":
                        apply_elements.append(mm)
                        break


        self.direct_links[graph.name] = []
        for dl in direct_links:

            neighbours = look_for_attached(dl, graph)
            n0 = vs[neighbours[0]]["mm__"].replace("MT_pre__","")
            n1 = vs[neighbours[1]]["mm__"].replace("MT_pre__","")
            self.direct_links[graph.name].append((n0, n1))

        #print("Direct links: " + str(self.direct_links[graph.name]))

        self.backward_links[graph.name] = []
        for bl in backward_links:

            neighbours = look_for_attached(bl, graph)
            n0 = vs[neighbours[0]]["mm__"].replace("MT_pre__","")
            n1 = vs[neighbours[1]]["mm__"].replace("MT_pre__","")
            self.backward_links[graph.name].append((n0, n1))

       # print("Backward links: " + str(self.backward_links[graph.name]))

        self.match_elements[graph.name] = match_elements
        self.apply_elements[graph.name] = apply_elements

        #print("Match contains: " + str(match_elements))
        #print("Apply contains: " + str(apply_elements))



    def find_required_rules(self, graph, transformation, is_contract = False):

        graph_mms = graph.vs["mm__"]

        contract_mms_to_remove = ['MT_pre__directLink_S', 'MT_pre__directLink_T', 'MT_pre__trace_link',
                                  # Remove this
                                  'MT_pre__leftExpr', 'MT_pre__hasAttribute_S', 'MT_pre__Attribute',
                                  'MT_pre__rightExpr', 'MT_pre__hasAttribute_T', 'MT_pre__Equation',
                                  'MT_pre__hasAttr_S', 'MT_pre__hasAttr_T', 'MT_pre__Constant'
                                  ]

        rule_mms_to_remove = ['match_contains', 'apply_contains',
                              'directLink_S', 'directLink_T',
                              'trace_link', 'backward_link',
                              'ApplyModel', 'MatchModel', 'paired_with',
                              # Remove this
                              'leftExpr', 'hasAttribute_S', 'Attribute',
                              'rightExpr', 'hasAttribute_T', 'Equation',
                              'hasAttr_S', 'hasAttr_T', 'Constant'
                              ]



        #take off the MT_pre__ if this is a contract
        if is_contract:
            mms_required = list(set([mm for mm in graph_mms if mm not in contract_mms_to_remove]))

        else:
            mms_required = list(([mm for mm in graph_mms if mm not in rule_mms_to_remove]))

        if is_contract:
            mms_required = [mm[8:] for mm in mms_required]

        try:
            supertypes = graph["superclasses_dict"]
        except KeyError:
            print("Graph: " + graph.name + " does not have a superclasses dict")
            supertypes = []

        #print("MMs Required Before: " + str(mms_required))

        if supertypes:
            for mm in mms_required:

                for s in supertypes:
                    if mm in supertypes[s]:
                        mms_required.append(s)

        #remove duplicates
        mms_required = sorted(list(set(mms_required)))
        #print("MMs Required After: " + str(mms_required))


        required_rules = []

        for layer in transformation:

            if graph in layer:
                break

            for rule in layer:

                if rule in required_rules:
                    continue

                rule_mms = set([mm for mm in rule.vs["mm__"] if mm not in rule_mms_to_remove])

                #print("\nRule " + rule.name + " MMS: " + str(rule_mms))

                for mm in mms_required:
                    if mm in rule_mms:
                        required_rules.append(rule)

                        #print("Add rule: " + rule.name + " with mms: " + str(rule_mms))
                        break

        return required_rules



    def slice_transformation(self, contract):

        contract = contract[1].CompleteQuantified

        print("Slicing for: " + contract.name)

        self.decompose_graph(contract)

        raise Exception()

        # graph_to_dot(contract.name, contract)
        # for layer in transformation:
        #     for rule in layer:
        #         graph_to_dot(rule.name, rule)

        required_rules = self.find_required_rules(contract, transformation, True)

        rr_names = [rule.name for rule in required_rules]
        #print("Required rules: " + str(rr_names))

        for rr in required_rules:

            new_rrs = self.find_required_rules(rr, self.transformation)
            for new_rr in new_rrs:
                if new_rr not in required_rules:
                    required_rules.append(new_rr)

        rr_names = [rule.name for rule in required_rules]
        print("Required rules: " + str(sorted(set(rr_names))))



        new_rules = {}
        for k in self.rules.keys():
            if k in rr_names:
                new_rules[k] = self.rules[k]


        new_transformation = []
        for layer in self.transformation:
            new_layer = []
            for rule in layer:
                if rule.name in rr_names:
                    new_layer.append(rule)

            if len(new_layer) > 0:
                new_transformation.append(new_layer)


        return new_rules, new_transformation