'''
Created on 2013-01-22

@author: levi
'''


from util.parser import load_parser

from util.test_script_base import Test

class ATLTest(Test):

    def __init__(self):
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

        #self.transformation_directory = "ExFamToPerson/transformation"
        
        self.transformation_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/transformation/"
        self.artifact_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/"

        #=====METAMODELS===============

        self.inputMM = "/home/dcx/Projects/SyVOLT/tmp/backend/ecore/Families.ecore"
        self.outputMM = "/home/dcx/Projects/SyVOLT/tmp/backend/ecore/Persons.ecore"


        #====CONTRACTS==================

        #self.contract_directory = "ExFamToPerson/contracts"
        self.contract_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/contracts/"

        self.atomic_contracts = [
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

        self.if_then_contracts = []

        self.if_then_contracts += []


        #=========PC SAVE LOCATION

        self.pc_save_filename = "pcs_atlTrans_extended.txt"



if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    exFam = ATLTest()
    exFam.test_correct(args)

    
