'''
Created on 2013-01-22

@author: levi
'''


from util.parser import load_parser

from util.test_script_base import Test

class ATLTest(Test):

    def __init__(self, args):
        Test.__init__(self)
        
        #============TRANSFORMATION=================
        self.full_transformation = [
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

        self.transformation_directory = "ExFamToPerson/transformation"
        
        #self.transformation_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/transformation/"
        self.artifact_directory = "~/Projects/SyVOLT/"

        #=====METAMODELS===============

        self.inputMM = "~/Projects/SyVOLT/eclipse_integration/metamodels/Families_Extended.ecore"
        self.outputMM = "~/Projects/SyVOLT/eclipse_integration/metamodels/Persons_Extended.ecore"


        #====CONTRACTS==================
        if not hasattr(args, "integration_contracts") or args.integration_contracts:
            self.contract_directory = "ExFamToPerson/contracts"
            self.atomic_contracts = [
                 "Neg_CityCompany",
                 "Neg_CountryCity",
                 "Neg_SchoolOrdFac",
                 "Neg_DaughterMother",
                "Pos_AssocCity",
                "Pos_ChildSchool",
                "Pos_FourMembers",
                "Pos_MotherFather",
                "Pos_ParentCompany",
                "Pos_TownHallComm",
                ]
        else:
            self.contract_directory = "ExFamToPerson/contracts/unit"

            self.atomic_contracts = [
               "UnitCountry2Community",
               "UnitDaughter2Woman",
               "UnitFather2Man",
               "UnitMother2Woman",
               "UnitSon2Man",
               "UnitCity2TownHall",
               "UnitN2D",
               "UnitConnectDaughter",
               "UnitConnectSon",
               "UnitConnectMother",
               "UnitConnectFather",
               "UnitConnectAssoc",
    #            #"UnitConnectCommittee",
               "UnitConnectDistricts",
               "UnitConnectTownHall",
               "UnitConnectOrdSchool",
               "UnitConnectSpecSchool",
            ]

        self.if_then_contracts = [
            #[["Neg_CountryCity"], ["Neg_CityCompany", "Neg_SchoolOrdFac", "AND"]],
            # [["EmptyContract"], ["Pos_FourMembers", "Pos_MotherFather", "AND"]],
        ]


        #=========PC SAVE LOCATION

        self.pc_save_filename = "pcs_atlTrans_extended.txt"



if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    exFam = ATLTest(args)
    exFam.test_correct(args)

    
