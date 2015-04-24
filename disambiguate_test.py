'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time

from path_condition_generator import PathConditionGenerator


from PyRamify import PyRamify

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator
from t_core.messages import Packet

from t_core.tc_python.frule import FRule
from t_core.tc_python.arule import ARule

from core.himesis_utils import graph_to_dot
from core.himesis_utils import disjoint_model_union
from core.himesis_utils import clean_graph
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules




from copy import deepcopy
from core.himesis_utils import disjoint_model_union, graph_to_dot

# run 1

from ATLTrans.HManRule import HManRule
from ATLTrans.HWomanRule import HWomanRule

from UMLRT2Kiltera_MM.transformation.Himesis.HTransition2QInstSIBLING import HTransition2QInstSIBLING
from UMLRT2Kiltera_MM.transformation.Himesis.HTransition2QInstOUT import HTransition2QInstOUT


def test_disambiguate():

    pyramify = PyRamify(verbosity = 0)

    do_ATL = False

    if do_ATL:
        pre_metamodel = ["MT_pre__FamiliesToPersons_MM", "MoTifRule"]
        post_metamodel = ["MT_post__FamiliesToPersons_MM", "MoTifRule"]

        subclasses_dict = {}

        subclasses_dict["MT_pre__MetaModelElement_S"] = ["MT_pre__HouseholdRoot", "MT_pre__Family", "MT_pre__Member"]

        subclasses_dict["MT_pre__MetaModelElement_T"] = ["MT_pre__CommunityRoot", "MT_pre__Person", "MT_pre__Man",
                                                         "MT_pre__Woman"]


    else:
        pre_metamodel = ["MT_pre__UMLRT2Kiltera_MM", "MoTifRule"]
        post_metamodel = ["MT_post__UMLRT2Kiltera_MM", "MoTifRule"]

        subclasses_dict = {}

        subclasses_dict["MT_pre__MetaModelElement_S"] = ["MT_pre__OPTIONAL1,", "MT_pre__PhysicalThread", "MT_pre__PortRef",
                                                             "MT_pre__PackageContainer", "MT_pre__Thread", "MT_pre__OUT2",
                                                             "MT_pre__BASE0", \
                                                             "MT_pre__NamedElement", "MT_pre__Element", "MT_pre__OUT1",
                                                             "MT_pre__Signal", "MT_pre__Package", "MT_pre__PortType", \
                                                             "MT_pre__PortConnectorRef", "MT_pre__IN1", "MT_pre__IN0",
                                                             "MT_pre__LogicalThread", "MT_pre__RoleType", "MT_pre__Vertex", \
                                                             "MT_pre__SIBLING0", "MT_pre__InitialPoint",
                                                             "MT_pre__PortConnector", "MT_pre__SignalType",
                                                             "MT_pre__Transition", \
                                                             "MT_pre__EntryPoint", "MT_pre__CONJUGATE1", "MT_pre__Protocol",
                                                             "MT_pre__StateMachine", "MT_pre__Model_S", \
                                                             "MT_pre__StateMachineElement", "MT_pre__Port",
                                                             "MT_pre__TransitionType", "MT_pre__Capsule", "MT_pre__Trigger_S", \
                                                             "MT_pre__State", "MT_pre__PLUGIN2", "MT_pre__Action",
                                                             "MT_pre__CapsuleRole", "MT_pre__ExitPoint", "MT_pre__FIXED0"]


        subclasses_dict["MT_pre__MetaModelElement_T"] = ["MT_pre__Name", "MT_pre__Module", "MT_pre__ConditionBranch",
                                                         "MT_pre__Delay", "MT_pre__LocalDef", \
                                                         "MT_pre__Expr", "MT_pre__ConditionSet", "MT_pre__Proc",
                                                         "MT_pre__MatchCase", "MT_pre__Match", \
                                                         "MT_pre__FuncDef", "MT_pre__Null", "MT_pre__Par", "MT_pre__Inst",
                                                         "MT_pre__Listen", "MT_pre__Site", \
                                                         "MT_pre__New", "MT_pre__PythonRef", "MT_pre__Def", "MT_pre__Seq",
                                                         "MT_pre__ParIndexed", "MT_pre__Condition", \
                                                         "MT_pre__Print", "MT_pre__Pattern", "MT_pre__ListenBranch",
                                                         "MT_pre__ProcDef", "MT_pre__Trigger_T", "MT_pre__Model_T"]

        subclasses_dict["MT_pre__StateMachine"] = ["MT_pre__State"]


    pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)

    from disambiguate import Disambiguator

    disamb = Disambiguator(2)

    if do_ATL:
        merged_rules = disjoint_model_union(HManRule(), HWomanRule())
    else:
        merged_rules = disjoint_model_union(clean_graph(HTransition2QInstSIBLING()), clean_graph(HTransition2QInstOUT()))

    graph_to_dot("merged", merged_rules)


    r = disamb.disambiguate(merged_rules)

    r.append(merged_rules)

    print("Disambiguated: ")
    for dis in r:
        print(dis.name)
        graph_to_dot(dis.name, dis)
        
        

test_disambiguate()