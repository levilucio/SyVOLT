'''
Created on 2013-01-22

@author: levi
'''


from util.parser import load_parser

from util.test_script_base import Test

class GMTest(Test):

    def __init__(self, args):
        super(GMTest, self).__init__()

        #============TRANSFORMATION=================

        do_old_transformation = args.handbuilt

        if do_old_transformation:
            r0 = 'HMapPN2FiveElements'
            r1 = 'HMapPartition'
            r2 = 'HMapModule'
            r3 = 'HConnECU2VirtualDevice1'
            r4 = 'HConnVirtualDevice2Distributable1'
            r5 = 'HConnectPPortPrototype'
            r6 = 'HConnectRPortPrototype'
            r7 = 'HConnVirtualDevice2Distributable2'
            r8 = 'HConnECU2VirtualDevice2'

            self.full_transformation = [[r0, r1, r2, ], [r3, ], [r4, ], [r7, ], [r8, ], [r5, r6, ], ]

            #rule_dir = "GM2AUTOSAR_MM/transformation"

            #use the faulty version, as the ATL code is faulty
            self.transformation_directory = "GM2AUTOSAR_MM/transformation/faulty_from_DSLTrans/"



        else:
            r0 = 'HcreateComponent'
            r1 = 'HinitSysTemp'
            r2 = 'HinitSingleSwc2EcuMapping'
            r3 = 'HsysmappingswMappingSolveRefPhysicalNodePartitionSystemMappingSwcToEcuMapping'
            r4 = 'HcompostypecomponentSolveRefPhysicalNodePartitionModuleCompositionTypeComponentPrototype'
            r5 = 'HcompostypeportSolveRefPhysicalNodePartitionModuleSchedulerServiceCompositionTypePPortPrototype'
            r6 = 'HcompostypeportSolveRefPhysicalNodePartitionModuleSchedulerServiceCompositionTypeRPortPrototype'
            r7 = 'HmappingcomponentSolveRefPartitionModuleSwcToEcuMappingSwCompToEcuMappingcomponent'
            r8 = 'HmappingecuInstanceSolveRefPhysicalNodePartitionSwcToEcuMappingEcuInstance'
            self.full_transformation = [[r0,],[r1,r2,],[r3,],[r4,],[r5],[r6,],[r7,],[r8,],]

            self.transformation_directory = "GM2AUTOSAR_MM/transformation_from_ATL/"


        #=====METAMODELS===============

        self.inputMM = "GM2AUTOSAR_MM/metamodels/Industrial.ecore"
        self.outputMM = "GM2AUTOSAR_MM/metamodels/Autosar.ecore"


        #====CONTRACTS==================

        self.contract_directory = "GM2AUTOSAR_MM/Properties/from_eclipse/"

        self.atomic_contracts = [
            "P1",
            "P2",
        ]

        self.if_then_contracts = [
            ["S1_if", "S1_then"],
            ["M1_if", "M1_then"],
            ["M3_if", "M3_then"],
        ]

        self.prop_if_then_contracts = [
            # structure is 'if graph', 'then graph'
            # where the 'then graph' is made up of reverse polish notation
            ["M2_if", ["M2_then1", "M2_then2", "NOT", "AND"]],
            ["M4_if", ["M4_then1", "M4_then2", "NOT", "AND"]],
            ["M5_if", ["M5_then1", "M5_then2", "NOT", "AND"]],
            ["M6_if", ["M6_then1", "M6_then2", "NOT", "AND"]],
        ]


        #=========PC SAVE LOCATION

        self.pc_save_filename = "pcs_gm.txt"



if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    gm = GMTest(args)
    gm.test_correct(args)
