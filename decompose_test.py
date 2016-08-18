from util.decompose_graph import decompose_graph
from core.new_match_algo import NewHimesisMatcher

from core.himesis_utils import expand_graph, set_do_pickle, set_compression

set_do_pickle(True)
set_compression(6)

file_name = "283038437670457923837516267818581708163"

graph = expand_graph(file_name)

print(graph.name)

from core.himesis_utils import load_directory
contracts = load_directory("mbeddr2C_MM/Contracts/")

atomic_contracts = [
    'AssignmentInstance_UniqueAssignment'
]

if_then_contracts = []
prop_if_then_contracts = []

from core.himesis_utils import graph_to_dot, load_directory
from util.test_script_utils import select_rules, get_sub_and_super_classes,\
    load_transformation, changePropertyProverMetamodel, set_supertypes, load_contracts
from util.slicer import Slicer
from util.parser import load_parser
inputMM = "./mbeddr2C_MM/ecore_metamodels/Module.ecore"
outputMM = "./mbeddr2C_MM/ecore_metamodels/C.ecore"
subclasses_dict, superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

atomic_contracts, if_then_contracts = load_contracts(contracts, superclasses_dict,
                                                                       atomic_contracts, if_then_contracts,
                                                                       prop_if_then_contracts,
                                                                       False)

contract =atomic_contracts[0][1]
print(contract)
print(contract.has_pivots())

#graph_to_dot(graph.name, graph, force_trace_links = True)

import time

print("Starting to check")
start_time = time.time()
result = contract.check(graph)
print(result)
print("Finished in " + str(time.time() - start_time) + " seconds")

matcher = NewHimesisMatcher(graph, contract.complete)
matcher.print_reason_failed = True
matcher.debug = False

matcher.superclasses_dict = superclasses_dict

for _ in matcher.match_iter():
    break

matcher.print_failures()