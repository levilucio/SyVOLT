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

from util.test_script_utils import select_rules
from util.slicer import Slicer

from core.himesis_utils import graph_to_dot
# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.ContractProver import ContractProver

from PropertyVerification.v2.if_then_contract import IfThenContract
from PropertyVerification.v2.prop_logic import NotContract, AndContract

# from PropertyVerification.state_property import StateProperty
# from PropertyVerification.atomic_state_property import AtomicStateProperty
# from PropertyVerification.and_state_property import AndStateProperty
# from PropertyVerification.or_state_property import OrStateProperty
# from PropertyVerification.not_state_property import NotStateProperty
# from PropertyVerification.implication_state_property import ImplicationStateProperty
# from PropertyVerification.Not import Not #StateSpace Prop
# from PropertyVerification.Implication import Implication #StateSpace Prop
# from PropertyVerification.And import And #StateSpace Prop
# from PropertyVerification.Or import Or #StateSpace Prop
# from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
# from PropertyVerification.PropertyVerifier import PropertyVerifier
#from lib2to3.fixer_util import p1



#positive

#from PropertyVerification.HEmpty_IsolatedConnectedLHS import HEmpty_IsolatedConnectedLHS

from ATLTrans.props.HfourMembers_IsolatedLHS import HfourMembers_IsolatedLHS
from ATLTrans.props.HfourMembers_ConnectedLHS import HfourMembers_ConnectedLHS
from ATLTrans.props.HfourMembers_CompleteLHS import HfourMembers_CompleteLHS
 
from ATLTrans.props.HmotherFather_IsolatedLHS import HmotherFather_IsolatedLHS
from ATLTrans.props.HmotherFather_ConnectedLHS import HmotherFather_ConnectedLHS
from ATLTrans.props.HmotherFather_CompleteLHS import HmotherFather_CompleteLHS
 
 
#negative
from ATLTrans.props.HdaughterMother_IsolatedLHS import HdaughterMother_IsolatedLHS
from ATLTrans.props.HdaughterMother_ConnectedLHS import HdaughterMother_ConnectedLHS
from ATLTrans.props.HdaughterMother_CompleteLHS import HdaughterMother_CompleteLHS
 
 
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
            ['HMotherRule',
            'HFatherRule',
            'HSonRule',
            'HDaughterRule'],
            ['HUnionMotherRule',
            'HUnionManRule',
            'HUnionDaughterRule',
            'HUnionSonRule']
        ]
        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)

        self.rules, self.transformation = pyramify.get_rules("ATLTrans/w_equations/", full_transformation)


        pre_metamodel = ["MT_pre__FamiliesToPersons_MM", "MoTifRule"]
        post_metamodel = ["MT_post__FamiliesToPersons_MM", "MoTifRule"]

        subclasses_dict = {}

        subclasses_dict["MT_pre__MetaModelElement_S"] =  ["MT_pre__HouseholdRoot","MT_pre__Family", "MT_pre__Member"]

        subclasses_dict["MT_pre__MetaModelElement_T"] = ["MT_pre__CommunityRoot","MT_pre__Person","MT_pre__Man", "MT_pre__Woman"]

        subclasses_dict["MT_pre__Person"] = ["MT_pre__Woman", "MT_pre__Man"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)


        #load the contracts



        # keep a dictionary from each child to its parent
        supertypes = {}

        for supertype in subclasses_dict:
            for subtype in subclasses_dict[supertype]:
                subtype = subtype[8:]
                try:
                    supertypes[subtype].append(supertype[8:])
                except KeyError:
                    supertypes[subtype] = [supertype[8:]]


        # also make sure the transformation has this information
        for rule in self.rules.values():
            rule["superclasses_dict"] = supertypes

        for layer in self.transformation:
            for rule in layer:
                rule["superclasses_dict"] = supertypes

        FourMembers = [HfourMembers_IsolatedLHS(), HfourMembers_ConnectedLHS(), HfourMembers_CompleteLHS()]
        for fm in FourMembers:
            fm["superclasses_dict"] = supertypes
 

 
 
        HMotherFather = [HmotherFather_IsolatedLHS(), HmotherFather_ConnectedLHS(), HmotherFather_CompleteLHS()]
        for c in HMotherFather:
            c["superclasses_dict"] = supertypes
 

 
 
        DaughterMother = [HdaughterMother_IsolatedLHS(), HdaughterMother_ConnectedLHS(), HdaughterMother_CompleteLHS()]
        for c in DaughterMother:
            c["superclasses_dict"] = supertypes


        HFourMembers_atomic = AtomicContract(FourMembers[0], FourMembers[1], FourMembers[2])
        HMotherFather_atomic = AtomicContract(HMotherFather[0], HMotherFather[1], HMotherFather[2])
        HDaughterMother_atomic = AtomicContract(DaughterMother[0], DaughterMother[1], DaughterMother[2])


        CommunityPerson1 = HCommunityPerson1_CompleteLHS()
        CommunityPerson1["superclasses_dict"] = supertypes

        CommunityPerson2 = HCommunityPerson2_CompleteLHS()
        CommunityPerson2["superclasses_dict"] = supertypes

        HCommunityPersonIfClause = AtomicContract(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(), CommunityPerson1)

        HCommunityPersonThenClause1 = AtomicContract(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(),
                                                  CommunityPerson1)

        HCommunityPersonThenClause = AndContract(HCommunityPersonThenClause1,
                                     NotContract(
            AtomicContract(HCommunityPerson2_IsolatedLHS(), HCommunityPerson2_ConnectedLHS(), CommunityPerson2)))
 
        HCommunityPerson_IfThen = IfThenContract(HCommunityPersonIfClause, HCommunityPersonThenClause)

        #atomic_properties = [["HDaughterMother_atomic", HDaughterMother_atomic]]
        self.atomic_contracts = [["HDaughterMother_atomic", HDaughterMother_atomic], ["HFourMembers_atomic", HFourMembers_atomic],["HMotherFather_atomic", HMotherFather_atomic]]


        #self.atomic_contracts = [self.atomic_contracts[0]]
        self.if_then_contracts = [] #[["HCommunityPerson", HCommunityPerson_IfThen]]

        if args.slice > 0:
            contract = self.atomic_contracts[args.slice - 1]
            print("Slicing for contract number " + str(args.slice) + " : " + contract[0])

            slicer = Slicer(self.rules, self.transformation)

            print("Number rules before: " + str(len(self.rules)))
            self.rules, self.transformation = slicer.slice_transformation(contract)
            print("Number rules after: " + str(len(self.rules)))

            raise Exception()

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



        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ATLTrans/w_equations/", self.transformation)



        s = PathConditionGenerator(self.transformation, "ATLTrans/metamodels/Community.ecore", self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)#
   
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
 
        #print("printing path conditions")
        s.print_path_conditions_screen()

        #s.print_path_conditions_file()

        
        print("\nContract proving:")

        s.verbosity = 0

        contract_prover = ContractProver()

        contract_prover.prove_contracts(s, self.atomic_contracts, self.if_then_contracts)


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
    parser.set_defaults(compression = 6)

    parser.add_argument('--slice', type = int, default = 0,
                        help = 'Index of contract to slice for. Range: 0 (no slicing) to #CONTRACTS (default: 0)')
    parser.set_defaults(slice = 0)


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

    
