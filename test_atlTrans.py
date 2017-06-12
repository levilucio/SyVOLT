'''
Created on 2013-01-22

@author: levi
'''

from util.parser import load_parser

from util.test_script_base import Test

class ATLTest(Test):
    def __init__(self):
        Test.__init__(self)

        # ============TRANSFORMATION=================
        self.full_transformation = [
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

        self.transformation_directory = "ATLTrans/w_equations/"

        # self.transformation_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/transformation/"
        self.artifact_directory = "/home/dcx/Projects/SyVOLT/"

        # =====METAMODELS===============

        self.inputMM = "/home/dcx/Projects/SyVOLT/ATLTrans/metamodels/Household.ecore"
        self.outputMM = "/home/dcx/Projects/SyVOLT/ATLTrans/metamodels/Community.ecore"

        # ====CONTRACTS==================

        self.contract_directory = "ATLTrans/props/"
        # self.contract_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/contracts/"

        self.atomic_contracts = [
            # "daughterMother",
            # "fourMembers",
            # "motherFather",
        ]
        self.if_then_contracts = [
            # ["S1_if", "S1_then"],
        ]
        self.if_then_contracts += [
            # structure is 'if graph', 'then graph'
            # where the 'then graph' is made up of reverse polish notation
            ["CommunityPerson_if", ["CommunityPerson_then", "NOT"]],
        ]

        # =========PC SAVE LOCATION

        self.pc_save_filename = "pcs_atlTrans.txt"

if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    exFam = ATLTest()
    exFam.test_correct(args)
