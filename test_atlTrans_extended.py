'''
Created on 2013-01-22

@author: levi
'''


from util.parser import load_parser

from util.test_script_base import Test

class ATLTest(Test):

    def __init__(self):
        super(ATLTest, self).__init__()

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

        self.transformation_directory = "ExFamToPerson/transformation/no_contains"


        #=====METAMODELS===============

        self.inputMM = "ExFamToPerson/Families_Extended.ecore"
        self.outputMM = "ExFamToPerson/Persons_Extended.ecore"


        #====CONTRACTS==================

        self.contract_directory = "ExFamToPerson/contracts"

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

        self.prop_if_then_contracts = []


        #=========PC SAVE LOCATION

        self.pc_save_filename = "pcs_atlTrans_extended.txt"



if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    exFam = ATLTest()
    exFam.test_correct(args)

    
