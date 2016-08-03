'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time
import sys

from path_condition_generator import PathConditionGenerator

from pyramify.PyRamify import PyRamify

from util.test_script_utils import select_rules, get_sub_and_super_classes,\
    load_transformation, changePropertyProverMetamodel, set_supertypes, load_contracts, save_pcs
from util.slicer import Slicer

from core.himesis_utils import graph_to_dot, load_directory

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.v2.atomic_contract import AtomicContract
from PropertyVerification.v2.ContractProver import ContractProver

from PropertyVerification.v2.if_then_contract import IfThenContract
from PropertyVerification.v2.prop_logic import NotContract, AndContract


from util.parser import load_parser

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
        self.rules, self.transformation = load_transformation("ExFamToPerson/transformation/no_contains", full_transformation)



        inputMM = "ExFamToPerson/Families_Extended.ecore"
        outputMM = "ExFamToPerson/Persons_Extended.ecore"

        self.subclasses_dict, self.superclasses_dict = get_sub_and_super_classes(inputMM, outputMM)

        pre_metamodel = ["MT_pre__FamiliesToPersons_MM", "MoTifRule"]
        post_metamodel = ["MT_post__FamiliesToPersons_MM", "MoTifRule"]

        changePropertyProverMetamodel(pre_metamodel, post_metamodel, self.subclasses_dict, self.superclasses_dict)




        #raise Exception()

    def test_correct(self,args):


        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)


 
 
        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ExFamToPerson/transformation/", self.transformation)
 
        set_supertypes(self.superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)


        print("superclasses_dict:")
        for mm in self.superclasses_dict:
            print(mm + " : " + str(self.superclasses_dict[mm]))

#load the contracts

        contracts = load_directory("ExFamToPerson/contracts")

        atomic_contracts = [
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

        if_then_contracts = []
        prop_if_then_contracts = []

        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, self.superclasses_dict,
                                                                       atomic_contracts, if_then_contracts,
                                                                       prop_if_then_contracts,
                                                                       args.draw_svg)

        slicer = Slicer(self.rules, self.transformation, self.superclasses_dict, self.overlapping_rules)

        if args.slice > -1:
            contract, self.atomic_contracts, self.if_then_contracts = slicer.get_contract(args.slice, self.atomic_contracts, self.if_then_contracts)
            self.rules, self.transformation = slicer.slice_transformation(contract)

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

        save_pcs(s, "pcs_atlTrans_extended.txt")


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

        # print("\nContract proving:")
        #
        # s.verbosity = 0
        #
        # contract_prover = ContractProver()
        #
        # contract_prover.prove_contracts(s, self.atomic_contracts, [])#self.if_then_contracts)
        # print("\n\nTime to build the set of path conditions: " + str(pc_time))
        # #        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        # print("Number of path conditions: " + str(s.num_path_conditions))

def _print_states(self, s):
    for state in s.symbStateSpace:
        print("----------")
        if state == ():
            print('Empty')
        else:
            for s in state:
                print(s.name)


if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()


    exFam = Test()
    exFam.setUp(args)
    exFam.test_correct(args)

    
