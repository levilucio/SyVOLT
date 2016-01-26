from core.himesis_utils import graph_to_dot
from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.if_then_contract import IfThenContract
from PropertyVerification.v2.prop_logic import *


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

    