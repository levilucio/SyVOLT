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

from util.test_script_utils import select_rules, get_sub_and_super_classes
from util.slicer import Slicer

from core.himesis_utils import graph_to_dot, load_directory

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.ContractProver import ContractProver

from PropertyVerification.v2.if_then_contract import IfThenContract
from PropertyVerification.v2.prop_logic import NotContract, AndContract


#contracts



from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test:

    def setUp(self, args):

        full_transformation = [
            ['HCountry2Community'],
            ['HFather2Man'],
            ['HMother2Woman'],
            ['HDaughter2Woman'],
            ['HSon2Man'],
            ['HNeighborhood2District'],
            ['HCity2TownHall', 'HCityCompany2Association'],

            ['HcopersonsSolveRefCountryFamilyParentCommunityMan'],
            ['HcopersonsSolveRefCountryFamilyParentCommunityWoman'],

            ['HcopersonsSolveRefCountryFamilyChildCommunityMan'],
            ['HcopersonsSolveRefCountryFamilyChildCommunityWoman'],

            ['HcotownHallsSolveRefCountryCityCommunityTownHall',
             'HcoassociationsSolveRefCountryCityCompanyCommunityAssociation',
            'HacommitteeSolveRefCompanyCityAssociationCommittee'],
            ['HtworkersSolveRefCompanyParentCityTownHallPerson'],
            ['HtdistrictsSolveRefCityNeighborhoodTownHallDistrict'],
            ['HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson'],
            ['HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson']

        ]
        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)

        self.rules, self.transformation = pyramify.get_rules("ExFamToPerson/transformation", full_transformation)


        inputMM = "ExFamToPerson/Families_Extended.ecore"
        outputMM = "ExFamToPerson/Persons_Extended.ecore"

        self.subclasses_dict, self.superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        pre_metamodel = ["MT_pre__FamiliesToPersons_MM", "MoTifRule"]
        post_metamodel = ["MT_post__FamiliesToPersons_MM", "MoTifRule"]

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, self.subclasses_dict, self.superclasses_dict)


        #load the contractsp





        # also make sure the transformation has this information
        for rule in self.rules.values():
            rule["superclasses_dict"] = self.superclasses_dict

        for layer in self.transformation:
            for rule in layer:
                rule["superclasses_dict"] = self.superclasses_dict

        contracts = load_directory("ExFamToPerson/contracts")

        contracts_to_load = [
            "Neg_CityCompany",
            "Neg_CountryCity",
            "Neg_SchoolOrdFac",
            "Pos_AssocCity",
            "Pos_ChildSchool",
            "Pos_DaughterMother",
            "Pos_FourMembers",
            "Pos_MotherFather",
            "Pos_ParentCompany",
            "Pos_TownHallComm"
        ]

        self.atomic_contracts = []

        print("Contracts:")
        for c in contracts:
            print(c)

        for contract_name in contracts_to_load:

            h_contract_name = "H" + contract_name

            iso = contracts[h_contract_name + "_IsolatedLHS"]
            iso["superclasses_dict"] = self.superclasses_dict

            connected = contracts[h_contract_name + "_ConnectedLHS"]
            connected["superclasses_dict"] = self.superclasses_dict

            complete = contracts[h_contract_name + "_CompleteLHS"]
            complete["superclasses_dict"] = self.superclasses_dict

            if args.draw_svg:
                graph_to_dot("contract_" + complete.name, complete)

            self.atomic_contracts.append([contract_name, AtomicContract(iso, connected, complete)])


        slicer = Slicer(self.rules, self.transformation)

        if args.slice > 0:
            contract = self.atomic_contracts[args.slice - 1]
            print("Slicing for contract number " + str(args.slice) + " : " + contract[0])

            self.atomic_contracts = [contract]

            print("Number rules before: " + str(len(self.rules)))
            self.new_rules, self.new_transformation = slicer.slice_transformation(contract)
            print("Number rules after: " + str(len(self.rules)))

        #raise Exception()

    def test_correct(self,args):

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
            pyramify.ramify_directory("ExFamToPerson/transformation/", self.transformation)
 
        pyramify.set_supertypes(self.superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)


        print("superclasses_dict:")
        for mm in self.superclasses_dict:
            print(mm + " : " + str(self.superclasses_dict[mm]))

        #raise Exception()
 
        s = PathConditionGenerator(self.transformation, "ExFamToPerson/Persons_Extended.ecore", self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)#


        #raise Exception()
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
 
        pc_time = ts1 - ts0
        print("\n\nTime to build the set of path conditions: " + str(pc_time))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))

        # import sys
        # sys.exit()
#         #check if the correct number of path conditions were produced
#         if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:
# 
#             #TODO: Make this an exception
#             num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
#             print(num_pcs_s)
#             #raise Exception(num_pcs_s)
#


        print("printing path conditions")
        #s.print_path_conditions_screen()
# 
#        s.print_path_conditions_file()
# # 
# #
#         #raise Exception()
# 
#
        #raise Exception()

        print("\nContract proving:")

        s.verbosity = 0

        contract_prover = ContractProver()

        contract_prover.prove_contracts(s, self.atomic_contracts, [])#self.if_then_contracts)
        print("\n\nTime to build the set of path conditions: " + str(pc_time))
        #        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))

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


    exFam = Test()
    exFam.setUp(args)
    exFam.test_correct(args)

    
