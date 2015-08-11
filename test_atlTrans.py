'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time
import sys

from path_condition_generator import PathConditionGenerator

from t_core.matcher import Matcher
from t_core.messages import Packet

from PyRamify import PyRamify

from core.himesis_utils import graph_to_dot
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.state_property import StateProperty
from PropertyVerification.atomic_state_property import AtomicStateProperty
from PropertyVerification.and_state_property import AndStateProperty
from PropertyVerification.or_state_property import OrStateProperty
from PropertyVerification.not_state_property import NotStateProperty
from PropertyVerification.implication_state_property import ImplicationStateProperty
from PropertyVerification.Not import Not #StateSpace Prop
from PropertyVerification.Implication import Implication #StateSpace Prop
from PropertyVerification.And import And #StateSpace Prop
from PropertyVerification.Or import Or #StateSpace Prop
from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
#from lib2to3.fixer_util import p1

from PropertyVerification.PropertyVerifier import PropertyVerifier


#positive

from PropertyVerification.HEmpty_IsolatedConnectedLHS import HEmpty_IsolatedConnectedLHS

# from ATLTrans.properties.HfourMembers_IsolatedLHS import HfourMembers_IsolatedLHS
# from ATLTrans.properties.HfourMembers_ConnectedLHS import HfourMembers_ConnectedLHS
# from ATLTrans.properties.HfourMembers_CompleteLHS import HfourMembers_CompleteLHS
# 
# from ATLTrans.properties.HmotherFather_IsolatedLHS import HmotherFather_IsolatedLHS
# from ATLTrans.properties.HmotherFather_ConnectedLHS import HmotherFather_ConnectedLHS
# from ATLTrans.properties.HmotherFather_CompleteLHS import HmotherFather_CompleteLHS
# 
# 
# #negative
# from ATLTrans.properties.HdaughterMother_IsolatedLHS import HdaughterMother_IsolatedLHS
# from ATLTrans.properties.HdaughterMother_ConnectedLHS import HdaughterMother_ConnectedLHS
# from ATLTrans.properties.HdaughterMother_CompleteLHS import HdaughterMother_CompleteLHS


#implication
from FamiliesToPersons_MM.Properties.Positive.Himesis.HCommunityPerson1_IsolatedLHS import HCommunityPerson1_IsolatedLHS
from FamiliesToPersons_MM.Properties.Positive.Himesis.HCommunityPerson1_ConnectedLHS import HCommunityPerson1_ConnectedLHS
from FamiliesToPersons_MM.Properties.Positive.Himesis.HCommunityPerson1_CompleteLHS import HCommunityPerson1_CompleteLHS

from FamiliesToPersons_MM.Properties.Positive.Himesis.HCommunityPerson2_IsolatedLHS import HCommunityPerson2_IsolatedLHS
from FamiliesToPersons_MM.Properties.Positive.Himesis.HCommunityPerson2_ConnectedLHS import HCommunityPerson2_ConnectedLHS
from FamiliesToPersons_MM.Properties.Positive.Himesis.HCommunityPerson2_CompleteLHS import HCommunityPerson2_CompleteLHS



from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):

        full_transformation = [
            ['HRootRule'],
            ['HMotherRule'],
            ['HFatherRule'],
            ['HSonRule'],
            ['HDaughterRule'],
            ['HUnionMotherRule'],
            ['HUnionManRule'],
            ['HUnionDaughterRule'],
            ['HUnionSonRule']
        ]
        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)

        self.rules, self.transformation = pyramify.get_rules("ATLTrans/w_equations/", full_transformation)

        #print("Rules: " + str(self.rules.keys()))


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

    def test_correct_uml2kiltera(self,args):

#'HMapHeirarchyOfStates2HeirarchyOfProcs':  'HTransition2QInstSIBLING': < 'HState2HProcDef': 'HCompositeState2ProcDef':  'HTransition2ListenBranch':  'HExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans':  'HBasicStateNoOutgoing2ProcDef':  'HBasicState2ProcDef': , 'HState2ProcDef'

#Layer1: State2ProcDef
#Layer2: BasicStateNoOutgoing2ProcDef, BasicState2ProcDef, CompositeState2ProcDef
#Layer3: ExitPoint2BProcDef_WhetherOrNotExitPtHasOutgoingTrans, State2HProcDef
#Layer4: Transition2QInstSIBLING
#Layer5: Transition2ListenBranch
#Layer6: MapHeirarchyOfStates2HeirarchyOfProcs

#         a1 = self.rules['HState2ProcDef']
#         b1 = self.rules['HBasicStateNoOutgoing2ProcDef']
#         b2 = self.rules['HBasicState2ProcDef']
#         b3 = self.rules['HCompositeState2ProcDef']

        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)



        #get the expected num from the args
        #expected_num_pcs = args.num_pcs
        expected_num_pcs = 330
                
        #TODO: Change this number if you are modifying the transformation at all
        pre_metamodel = ["MT_pre__FamiliesToPersons_MM", "MoTifRule"]
        post_metamodel = ["MT_post__FamiliesToPersons_MM", "MoTifRule"]

        subclasses_dict = {}

        subclasses_dict["MT_pre__MetaModelElement_S"] =  ["MT_pre__HouseholdRoot","MT_pre__Family", "MT_pre__Member"]

        subclasses_dict["MT_pre__MetaModelElement_T"] = ["MT_pre__CommunityRoot","MT_pre__Person","MT_pre__Man", "MT_pre__Woman"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)


        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ATLTrans/w_equations/", self.transformation)



        s = PathConditionGenerator(self.transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)#
   
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()

        print(s.num_path_conditions)

        pc_time = ts1 - ts0
        print("\n\nTime to build the set of path conditions: " + str(pc_time))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))

        #check if the correct number of path conditions were produced
        if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:

            #TODO: Make this an exception
            num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
            print(num_pcs_s)
            #raise Exception(num_pcs_s)
 
        print("printing path conditions")
        s.print_path_conditions_screen()

        #s.print_path_conditions_file()


#         print("\nProperty proving:")
# 
#         s.verbosity = 0
# 
# 
#         # keep a dictionary from each child to its parent
#         supertypes = {}
# 
#         for supertype in subclasses_dict:
#             for subtype in subclasses_dict[supertype]:
#                 subtype = subtype[8:]
#                 try:
#                     supertypes[subtype].append(supertype[8:])
#                 except KeyError:
#                     supertypes[subtype] = [supertype[8:]]
# 
#         FourMembers = [HfourMembers_IsolatedLHS(), HfourMembers_ConnectedLHS(), HfourMembers_CompleteLHS()]
#         for fm in FourMembers:
#             fm["superclasses_dict"] = supertypes
# 
#         HFourMembers_atomic = AtomicStateProperty(FourMembers[0], FourMembers[1], FourMembers[2])
# 
# 
#         HMotherFather = [HmotherFather_IsolatedLHS(), HmotherFather_ConnectedLHS(), HmotherFather_CompleteLHS()]
#         for c in HMotherFather:
#             c["superclasses_dict"] = supertypes
# 
#         HMotherFather_atomic = AtomicStateProperty(HMotherFather[0], HMotherFather[1], HMotherFather[2])
# 
# 
#         DaughterMother = [HdaughterMother_IsolatedLHS(), HdaughterMother_ConnectedLHS(), HdaughterMother_CompleteLHS()]
#         for c in DaughterMother:
#             c["superclasses_dict"] = supertypes
# 
#         HDaughterMother_atomic = AtomicStateProperty(DaughterMother[0], DaughterMother[1], DaughterMother[2])
# 
# 
# 
#         # HCommunityPersonIfClause = AtomicStateProperty(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(), HCommunityPerson1_CompleteLHS())
#         #
#         #
#         # HCommunityPersonThenClause = AndStateProperty(
#         #     AtomicStateProperty(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(),
#         #         HCommunityPerson1_CompleteLHS()),
#         #     NotStateProperty(
#         #         AtomicStateProperty(HCommunityPerson2_IsolatedLHS(), HCommunityPerson2_ConnectedLHS(),
#         #             HCommunityPerson2_CompleteLHS())))
# 
#         CommunityPerson1 = HCommunityPerson1_CompleteLHS()
#         CommunityPerson1["superclasses_dict"] = supertypes
# 
#         CommunityPerson2 = HCommunityPerson2_CompleteLHS()
#         CommunityPerson2["superclasses_dict"] = supertypes
# 
#         HCommunityPersonIfClause = AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(),
#             CommunityPerson1)
# 
#         HCommunityPersonThenClause = NotStateProperty(
#                 AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(),
#                     CommunityPerson2))
# 
# 
# 
#         #HCommunityPerson1 = AtomicStateProperty(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(), HCommunityPerson1_CompleteLHS())
# 
#         #graph_to_dot("HCommunityPerson1_IsolatedLHS", HCommunityPerson1_IsolatedLHS())
# 
# 
#         #graph_to_dot("HCommunityPerson1_ConnectedLHS", HCommunityPerson1_ConnectedLHS())
# 
#         #graph_to_dot("HCommunityPerson1_CompleteLHS", HCommunityPerson1_CompleteLHS())
# 
# 
#         #graph_to_dot("HCommunityPerson1_CompleteLHS", HCommunityPerson1_CompleteLHS())
#         #graph_to_dot("HCommunityPerson2_CompleteLHS", HCommunityPerson2_CompleteLHS())
# 
#         if args.draw_svg:
#             graph_to_dot("HDaughterMother_ConnectedLHS", HDaughterMother_ConnectedLHS())
#             graph_to_dot("HDaughterMother_CompleteLHS", HDaughterMother_CompleteLHS())
# 
#             graph_to_dot("HMotherFather_IsolatedLHS", HMotherFather_IsolatedLHS())
#             graph_to_dot("HMotherFather_ConnectedLHS", HMotherFather_ConnectedLHS())
#             graph_to_dot("HMotherFather_CompleteLHS", HMotherFather_CompleteLHS())
# 
#             #graph_to_dot("HMotherFather_CompleteLHS", HMotherFather_CompleteLHS())
#             #graph_to_dot("HDaughterMother_CompleteLHS", HDaughterMother_CompleteLHS())
# 
#             #
# 
#             #
#             # for state in s.get_path_conditions():
#             #     graph_to_dot(state.name, state)
# 
#         #atomic_properties = [["HDaughterMother_atomic", HDaughterMother_atomic]]
#         atomic_properties = [["HFourMembers_atomic", HFourMembers_atomic], ["HMotherFather_atomic", HMotherFather_atomic], ["HDaughterMother_atomic", HDaughterMother_atomic]]
# 
#         if_then_properties = []#["HCommunityPerson", HCommunityPersonIfClause, HCommunityPersonThenClause]]
# 
# 
#         #s.verbosity = 2
# 
# 
#         # finalresult = StateProperty.verifyCompositeStateProperty(s, HCommunityPerson1)
#         # if finalresult:
#         #     print("Atomic property: " +"HCommunityPerson1" + " holds")
#         # else:
#         #     print("Atomic property: " + "HCommunityPerson1" + " does not hold")
# 
#         verifier = StateProperty()
#         for name, atomic_prop in atomic_properties:
#            finalresult = verifier.verifyCompositeStateProperty(s, atomic_prop)
#            if len(finalresult) == 0:
#                print("Atomic property: " + name + " holds\n")
#            else:
#                print("Atomic property: " + name + " does not hold\n")
# 
#         for name, i, t in if_then_properties:
#            finalresult = verifier.verifyCompositeStateProperty(s, ImplicationStateProperty(i, t))
#            if len(finalresult) == 0:
#                print("If-then property: " + name + " holds\n")
#            else:
#                print("If-then property: " + name + " does not hold\n")
# 
#         ts1 = time.time()
# 
#         prop_length = len(atomic_properties) + len(if_then_properties)
# 
# 
#         print("\n\nTime to build the set of path conditions: " + str(pc_time))
# 
#         print("\n\nTime to verify " + str(prop_length) + " properties: " + str(ts1 - ts0))


def _print_states(self, s):
    for state in s.symbStateSpace:
        print("----------")
        if state == ():
            print('Empty')
        else:
            for s in state:
                print(s.name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run the uml to kiltera test.')
    parser.add_argument('--skip_tests', dest = 'run_tests', action = 'store_false',
                        help = 'Option to skip the running of matching tests')
    parser.set_defaults(run_tests = True)

    parser.add_argument('--skip_parallel', dest = 'do_parallel', action = 'store_false',
                        help = 'Option to force computation to run single-thread')
    parser.set_defaults(do_parallel = True)

    parser.add_argument('--skip_pickle', dest = 'do_pickle', action = 'store_false',
                        help = 'Option to skip the use of pickling')
    parser.set_defaults(do_pickle = True)

    parser.add_argument('--compression', type = int, default = 6,
                        help = 'Level of compression to use with pickling. Range: 0 (no compression) to 9 (high compression) (default: 6)')
    parser.set_defaults(compression = True)

    parser.add_argument('--no_svg', dest = 'draw_svg', action = 'store_false',
                        help = 'Flag to force svg files to not be drawn')
    parser.set_defaults(draw_svg = True)

    parser.add_argument('--num_pcs', type = int, default = -1,
                        help = 'Number of path conditions which should be produced by this test (default: -1)')

    parser.add_argument('--num_rules', type = int, default = -1,
                        help = 'Number of rules in the transformation (default: -1)')

    parser.add_argument('--verbosity', type = int, default = 0,
                        help = 'Verbosity level (default: 0 - minimum output)')

    args = parser.parse_args()


    uml2kiltera = Test()
    uml2kiltera.setUp(args)
    uml2kiltera.test_correct_uml2kiltera(args)

    
