from core.himesis_utils import graph_to_dot

def select_rules(full_transformation, num_rules):
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
        mms_required = set([mm for mm in graph_mms if mm not in contract_mms_to_remove])

    else:
        mms_required = set([mm for mm in graph_mms if mm not in rule_mms_to_remove])

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


    print("MMs Required: " + str(mms_required))


    required_rules = []

    for layer in transformation:
        found_rule = False
        for rule in layer:
            if rule.name == graph.name:
                found_rule = True
                break

            if rule in required_rules:
                continue

            rule_mms = set([mm for mm in rule.vs["mm__"] if mm not in rule_mms_to_remove])

            print("\nRule " + rule.name + " MMS: " + str(rule_mms))

            rule_added = False
            for mm in mms_required:
                if mm in rule_mms:
                    required_rules.append(rule)

                    #print("Add rule: " + rule.name + " with mms: " + str(rule_mms))
                    rule_added = True
                    continue

            if rule_added:
                continue
        if found_rule:
            break

    return required_rules



def slice_transformation(rules, transformation, contract, args):

    contract = contract[1].CompleteQuantified

    print("Slicing for: " + contract.name)

    # graph_to_dot(contract.name, contract)
    # for layer in transformation:
    #     for rule in layer:
    #         graph_to_dot(rule.name, rule)

    required_rules = find_required_rules(contract, transformation, True)

    rr_names = [rule.name for rule in required_rules]
    print("Required rules: " + str(rr_names))

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

        if len(new_layer) > 0:
            new_transformation.append(new_layer)


    return new_rules, new_transformation