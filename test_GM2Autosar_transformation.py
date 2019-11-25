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


        #=====FROM MPS=================
        self.full_transformation = []
        self.full_transformation.append(
            ['HMapPN2FiveElements', 'HMapPartition', 'HMapModule', ])  # initSysTemp_CreationRule
        self.full_transformation.append(['HConnECU2VirtualDevice1', ])  # sysmapping_swMapping_SolveRef
        self.full_transformation.append(['HConnVirtualDevice2Distributable1', ])  # compostype_component_SolveRef
        self.full_transformation.append(
            ['HConnectPPortPrototype', 'HConnectRPortPrototype', ])  # compostype_port_SolveRef
        self.full_transformation.append(['HConnVirtualDevice2Distributable2', ])  # mapping_component_SolveRef
        self.full_transformation.append(['HConnECU2VirtualDevice2', ])  # mapping_ecuInstance_SolveRef
        self.transformation_directory = "GM2AUTOSAR_MM/transformation_from_MPS/"

        #=====METAMODELS===============

        self.inputMM = "GM2AUTOSAR_MM/metamodels/Industrial.ecore"
        self.outputMM = "GM2AUTOSAR_MM/metamodels/Autosar.ecore"


        #====CONTRACTS==================

        if not hasattr(args, "integration_contracts") or args.integration_contracts:
            self.contract_directory = "GM2AUTOSAR_MM/Properties/from_eclipse/"

            self.atomic_contracts = [
                "P1",
                "P2",
            ]

            self.if_then_contracts = [
                ["S1_if", "S1_then"],
                # ["M1_if", "M1_then"],
                # ["M3_if", "M3_then"],
            ]

            self.if_then_contracts += [
                # structure is 'if graph', 'then graph'
                # where the 'then graph' is made up of reverse polish notation
                ["M2_if", ["M2_then1", "M2_then2", "NOT", "AND"]],
                ["M4_if", ["M4_then1", "M4_then2", "NOT", "AND"]],
                ["M5_if", ["M5_then1", "M5_then2", "NOT", "AND"]],
                ["M6_if", ["M6_then1", "M6_then2", "NOT", "AND"]],
            ]
        else:
            self.contract_directory = "GM2AUTOSAR_MM/Properties/unit_contracts/"

            self.atomic_contracts = [
                "UnitR01a",
                "UnitR01b",
                "UnitR01c",
                "UnitR02",
                "UnitR03",
                "UnitR04a",
                "UnitR04b",
                "UnitR05",
                "UnitR06",
            ]
            self.if_then_contracts = [
            ]



        #=========PC SAVE LOCATION

        self.pc_save_filename = "pcs_gm.txt"



if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    gm = GMTest(args)
    gm.test_correct(args)
