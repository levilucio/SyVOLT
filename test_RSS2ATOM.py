'''
Created on 2013-01-22

@author: levi
'''


from util.parser import load_parser

from util.test_script_base import Test

class RSS2ATOMTest(Test):

    def __init__(self):
        Test.__init__(self)
        
        #============TRANSFORMATION=================
        self.full_transformation = [
            ['HCategory2Category'],
            ['HChannel2ATOM'],
            ['HItem2Entry'],

            ['HoutcategoriesSolveRefChannelCategoryATOMCategory'],
            ['HoutcontentSolveRefItemEntryContent'],

            ['HoutentrieSolveRefChannelATOMEntry'],
            ['HoutgeneratorSolveRefChannelATOMGenerator'],

        ]

        self.transformation_directory = "RSS2ATOM/transformation"
        
        #self.transformation_directory = "/home/dcx/Projects/SyVOLT/tmp/backend/transformation/"
        self.artifact_directory = "~/Projects/SyVOLT/"

        #=====METAMODELS===============

        self.inputMM = "~/Projects/SyVOLT/RSS2ATOM/RSS.ecore"
        self.outputMM = "~/Projects/SyVOLT/RSS2ATOM/ATOM.ecore"


        #====CONTRACTS==================

        self.contract_directory = "RSS2ATOM/contracts"

        self.atomic_contracts = [
             "ChannelProduction",
             "EntryContent",
        ]

        self.if_then_contracts = [
            #[["Neg_CountryCity"], ["Neg_CityCompany", "Neg_SchoolOrdFac", "AND"]],
            # [["EmptyContract"], ["Pos_FourMembers", "Pos_MotherFather", "AND"]],
        ]


        #=========PC SAVE LOCATION

        self.pc_save_filename = "pcs_rss2atom.txt"



if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    test = RSS2ATOMTest()
    test.test_correct(args)

    
