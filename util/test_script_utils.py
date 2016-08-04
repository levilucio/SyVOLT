from core.himesis_utils import graph_to_dot, load_class
from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.if_then_contract import IfThenContract
from PropertyVerification.v2.prop_logic import *

import os

# get all the rules in the transformation
def load_transformation(dir_name, full_transformation):
    print("Loading transformation from directory: " + dir_name)

    rules = {}
    transformation = []

    for layer in full_transformation:
        new_layer = []
        for rule_name in layer:
            print("Loading rule: " + rule_name)

            # add the rule to the rules dict
            rule = load_class(dir_name + "/" + rule_name + ".py")
            rules.update(rule)

            new_layer.append(list(rule.values())[0])

        transformation.append(new_layer)

    return rules, transformation


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




def get_sub_and_super_classes(inputMM, outputMM):
    subclasses_dict = {}



    inMM = EcoreUtils(inputMM)
    subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(inMM.getMetamodelClassNames())

    inMMinheritanceTree = inMM.getSubClassInheritanceRelationForClasses()

    for className in inMMinheritanceTree:
        subclasses_dict["MT_pre__" + className] = buildPreListFromClassNames(inMMinheritanceTree[className])

    outMM = EcoreUtils(outputMM)
    subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(outMM.getMetamodelClassNames())

    outMMinheritanceTree = outMM.getSubClassInheritanceRelationForClasses()
    for className in outMMinheritanceTree:
        subclasses_dict["MT_pre__" + className] = buildPreListFromClassNames(outMMinheritanceTree[className])


    superclasses_dict = {}

    inMMinheritanceTree = inMM.getSuperClassInheritanceRelationForClasses()
    for super in inMMinheritanceTree:
        inMMinheritanceTree[super].append("MetaModelElement_S")

    outMMinheritanceTree = outMM.getSuperClassInheritanceRelationForClasses()
    for super in outMMinheritanceTree:
        outMMinheritanceTree[super].append("MetaModelElement_T")

    superclasses_dict.update(inMMinheritanceTree)
    superclasses_dict.update(outMMinheritanceTree)

    #remove duplicates
    for superclass in superclasses_dict.keys():
        superclasses_dict[superclass] = list(set(superclasses_dict[superclass]))


    #
    # print("\n\n")
    # print("Subclasses dict:")
    # for subclass in sorted(list(subclasses_dict.keys())):
    #     sub_list = [sub.replace("MT_pre__", "") for sub in subclasses_dict[subclass]]
    #     print(subclass.replace("MT_pre__", "") + " : " + str(sub_list))
    # print("\n")
    # print("Superclasses dict:")
    # for superclass in sorted(list(superclasses_dict.keys())):
    #     print(superclass + " : " + str(sorted(superclasses_dict[superclass])))
    # print("\n\n")


    return subclasses_dict, superclasses_dict

#============================

#renames elements from one metamodel into another metamodel
def changeGraphMetamodel(mapping, directory):
    print("Starting to rename elements in graphs")
    #print("Mapping: " + str(mapping))

    for d in os.listdir(directory):
        if not os.path.isdir(directory + d):
            continue

        # ignore svn dirs
        if d.startswith('.') or d.startswith("__"):
            continue

        graph_dir = directory + d + "/Himesis/"

        try:
            files = os.listdir(graph_dir)
        except OSError:
            print("Warning: " + graph_dir + " does not exist")
            files = []

        for f in files:

            if f.startswith("__") or not f.endswith(".py") or f.startswith("."):
                continue

            #print("Examining " + graph_dir + f)

            graph_file = graph_dir + f
            try:
                g = load_class(graph_file)
            except ImportError:
                print("ERROR " + graph_file)
                continue

            name = list(g.keys())[0]
            graph = list(g.values())[0]

            for node in graph.vs:
                if not node["mm__"] in mapping.keys():
                    continue

                #set the new subtypes
                node["mm__"] = mapping[node["mm__"]]

            #need to compile rule back in order to update the file
            graph.compile(graph_dir)

    print("Finished changing graph metamodels\n")

#change the proper prover matchers and rewriters to
#refer to the correct metamodel
def changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict, supertypes, dsltransInstallDir = "."):
    print("Starting to change property prover metamodel")

    property_prover_rules_dir = dsltransInstallDir + "/property_prover_rules/"
    print("Rules dir: " + property_prover_rules_dir)
    for d in os.listdir(property_prover_rules_dir):

        if not os.path.isdir(property_prover_rules_dir + d):
            continue

        #ignore svn dirs
        if d.startswith('.') or d.startswith("__"):
            continue

        rule_dir = property_prover_rules_dir + d + "/Himesis/"

        try:
            files = os.listdir(rule_dir)
        except OSError:
            print("Warning: " + rule_dir + " does not exist")
            files = []

        for f in files:
            if not f.endswith(".py") or f.startswith("__") or f.startswith("."):
                continue

            rule_file = rule_dir + f

            try:
                rule = load_class(rule_file)
            except ImportError as e:
                print("ERROR loading " + rule_file)
                traceback.print_exc()
                continue

            name = list(rule.keys())[0]
            graph = list(rule.values())[0]

            #TODO: Make this less fragile
            if "LHS" in f:
                graph["mm__"] = pre_metamodel
            elif "RHS" in f:
                graph["mm__"] = post_metamodel
            else:
                raise Exception("Error: Not LHS or RHS rule")

            graph["superclasses_dict"] = supertypes

            #need to compile rule back in order to update the file
            graph.compile(rule_dir)

    print("Finished changing property prover metamodel\n")

def set_supertypes(superclasses_dict, rules, transformation, ruleTraceCheckers, matchRulePatterns, ruleCombinators):

    print("Changing superclasses for matchers")

    #print(superclasses_dict)

    for ruleTraceChecker in ruleTraceCheckers.values():

        if ruleTraceChecker:
            ruleTraceChecker.superclasses_dict = superclasses_dict

    for mrp in matchRulePatterns.values():
        matcher = mrp[0]

        matcher.superclasses_dict = superclasses_dict

    for rc in ruleCombinators.values():

        for pair in rc:
            matcher = pair[0]

            matcher.superclasses_dict = superclasses_dict

#=================================================


def load_contracts(contracts, superclasses_dict, atomic_names, simple_if_then_names, prop_if_then_names, draw_svg):

    atomic_contracts = []
    for contract_name in atomic_names:
        atomic_contract = load_contract(contract_name, contracts, superclasses_dict)
        atomic_contracts.append([atomic_contract.name, atomic_contract])

    if_then_contracts = []
    for contract_name_if, contract_name_then in simple_if_then_names:
        if_contract = load_contract(contract_name_if, contracts, superclasses_dict)
        then_contract = load_contract(contract_name_then, contracts, superclasses_dict)
        if_then_contract = IfThenContract(if_contract, then_contract)
        if_then_contracts.append([if_then_contract.name, if_then_contract])

    for contract_name_if, prop_equation in prop_if_then_names:

        if type(contract_name_if) is list:
            if_contract = handle_prop(contract_name_if, contracts, superclasses_dict)
        else:
            if_contract = load_contract(contract_name_if, contracts, superclasses_dict)

        then_contract = handle_prop(prop_equation, contracts, superclasses_dict)

        full_contract = IfThenContract(if_contract, then_contract)
        if_then_contracts.append([full_contract.name, full_contract])

    return atomic_contracts, if_then_contracts

def handle_prop(prop_equation, contracts, superclasses_dict):
    prop_stack = []
    for p in prop_equation:
        if p == "AND":
            if len(prop_stack) < 2:
                raise Exception("Contract Prop Logic failure for AND")

            last_1 = prop_stack.pop()
            last_2 = prop_stack.pop()
            c = AndContract(last_1, last_2)
        elif p == "OR":
            if len(prop_stack) < 2:
                raise Exception("Contract Prop Logic failure for OR")

            last_1 = prop_stack.pop()
            last_2 = prop_stack.pop()
            c = OrContract(last_1, last_2)

        elif p == "NOT":
            if len(prop_stack) < 1:
                raise Exception("Contract Prop Logic failure for NOT")

            last = prop_stack.pop()
            c = NotContract(last)

        else:
            c = load_contract(p, contracts, superclasses_dict)

        prop_stack.append(c)
    if len(prop_stack) != 1:
        raise Exception("Contract Prop Logic failure")
    return prop_stack.pop()


def load_contract(contract_name, contracts, superclasses_dict):
    h_contract_name = "H" + contract_name

    iso = contracts[h_contract_name + "_IsolatedLHS"]
    iso["superclasses_dict"] = superclasses_dict

    connected = contracts[h_contract_name + "_ConnectedLHS"]
    connected["superclasses_dict"] = superclasses_dict

    complete = contracts[h_contract_name + "_CompleteLHS"]
    complete["superclasses_dict"] = superclasses_dict



    atomic = AtomicContract(iso, connected, complete)
    return atomic

def save_pcs(pathCondGen, filename):
    with open(filename, 'w') as f:
        f.write(str(pathCondGen.num_path_conditions) + "\n")
        for pc_name in sorted(pathCondGen.currentpathConditionSet):
            pc = pathCondGen.pc_dict[pc_name]
            f.write(pc_name + "\n")
            f.write(pc + "\n")

def load_pcs(filename):
    pc_dict = {}
    print("Opening pc filename: " + filename)
    with open(filename) as f:
        num_pcs = f.readline()
        print("Number of pcs to load: " + str(num_pcs))
        for n in range(int(num_pcs)):
            graph_name = f.readline().strip()
            graph_filename = f.readline().strip()
            pc_dict[graph_name] = int(graph_filename)

    return pc_dict