def select_rules(self, full_transformation, num_rules):
    selected_transformation = []

    print("Selecting " + str(num_rules) + " rules")

    i = 1
    for layer in range(len(full_transformation)):
        selected_transformation.append([])
        for rule in full_transformation[layer]:
            selected_transformation[layer].append(rule)
            i += 1
            if i > num_rules:
                print("Returning: " + str(selected_transformation))
                return selected_transformation



def find_required_rules(graph, transformation, is_contract = False):

    graph_mms = graph.vs["mm__"]





    #take off the MT_pre__ if this is a contract
    if is_contract:
        mms_required = set([mm for mm in graph_mms if mm not in ['MT_pre__directLink_S', 'MT_pre__directLink_T', 'MT_pre__trace_link']])
    else:
        mms_required = set([mm for mm in graph_mms if mm not in ['match_contains', 'apply_contains',
                                                                 'directLink_S', 'directLink_T',
                                                                 'trace_link', 'backward_link',
                                                                 'ApplyModel', 'MatchModel', 'paired_with']])

    if is_contract:
        mms_required = [mm[8:] for mm in mms_required]

    try:
        supertypes = graph["superclasses_dict"]
    except KeyError:
        print("Graph: " + graph.name + " does not have a superclasses dict")
        supertypes = []

    if supertypes:
        for mm in mms_required:
            if mm in supertypes:
                mms_required += supertypes[mm]

    #remove duplicates
    mms_required = list(set(mms_required))


    #print("MMs Required: " + str(mms_required))


    required_rules = []

    for layer in transformation:
        for rule in layer:

            rule_mms = set(rule.vs["mm__"])

            #print("Rule MMS: " + str(rule_mms))

            rule_added = False
            for mm in mms_required:
                if mm in rule_mms and rule not in required_rules:
                    required_rules.append(rule)
                    rule_added = True
                    continue

            if rule_added:
                continue

    return required_rules



def slice_transformation(rules, transformation, contracts, args):

    contract = contracts[0][1].CompleteQuantified

    print("Slicing for: " + contract.name)

    required_rules = find_required_rules(contract, transformation, True)

    rr_names = [rule.name for rule in required_rules]

    for rr in required_rules:

        new_rrs = find_required_rules(rr, transformation)
        for new_rr in new_rrs:
            if new_rr not in required_rules:
                required_rules.append(new_rr)

    rr_names = [rule.name for rule in required_rules]
    print("Required rules: " + str(rr_names))



    new_rules = {}
    for k in rules.keys():
        if k in rr_names:
            new_rules[k] = rules[k]


    new_transformation = []
    for layer in transformation:
        new_layer = []
        for rule in layer:
            if rule.name in rr_names:
                new_layer.append(rule)
        new_transformation.append(new_layer)


    return new_rules, new_transformation