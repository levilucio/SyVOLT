

'''
Created on 2013-01-22

@author: levi
'''

from util.parser import load_parser

from util.test_script_base import Test


class UMLTest(Test):
    def __init__(self, args):
        super(UMLTest, self).__init__()

        # ============TRANSFORMATION=================
        do_handbuilt_transformation = args.handbuilt

        if do_handbuilt_transformation:
            r0 = 'HState2ProcDef'
            r1 = 'HMapRootElementRule'
            r2 = 'HRuleConnect2RootElement'
            r3 = 'HMapHeirarchyOfStates2HeirarchyOfProcs'
            r4 = 'HBasicStateNoOutgoing2ProcDef'
            r5 = 'HBasicState2ProcDef'
            r6 = 'HCompositeState2ProcDef'
            r7 = 'HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans'
            r8 = 'HState2HProcDef'
            r9 = 'HState2CProcDef'
            r10 = 'HTransition2QInstSIBLING'
            r11 = 'HTransition2QInstOUT'
            r12 = 'HTransition2Inst'
            r13 = 'HTransition2ListenBranch'
            r14 = 'HConnectOutputsOfExitPoint2BProcDefTransition2QInst'
            r15 = 'HTransition2HListenBranch'
            r16 = 'HConnectOPState2CProcDefTransition2InstotherInTransitions'

            self.full_transformation = [[r1, ], [r0, ], [r4, r5, r6, ], [r7, r8, r9, ], [r10, r11, r12, ],
                                   [r13, r14, r15, r16, ], [r2], [r3, ], ]

            self.transformation_directory = "UMLRT2Kiltera_MM/transformation/no_contains/"

        else:
            r0 = 'HMapRootElementRule'
            r1 = 'HState2ProcDef'
            r2 = 'HBasicState2ProcDef'
            r3 = 'HBasicStateNoOutgoing2ProcDef'
            r4 = 'HCompositeState2ProcDef'
            r5 = 'HState2HProcDef'
            r6 = 'HState2CProcDef'
            r7 = 'HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans'
            r8 = 'HTransition2QInstSIBLING'
            r9 = 'HTransition2QInstOUT'
            r10 = 'HTransition2Inst'
            r11 = 'HTransition2ListenBranch'
            r12 = 'HConnectOutputsOfExitPoint2BProcDefTransition2QInst'
            r13 = 'HTransitionHListenBranch'
            r14 = 'HConnectOPState2CProcDefTransition2InstotherInTransitions'
            r15 = 'HRuleConnect2RootElement'
            r16 = 'HMapHierarchyOfStates2HierarchyOfProcs'

            # full_transformation = [[r0, ], [r1, ], [r2, ], [r3, ], [r4, ], [r5, ], [r6, ], [r7, ], [r8, ], [r9, ],
            #                        [r10, ], [r11, ], [r12, ], [r13, ], [r14, ], [r15, ], [r16, ], ]
            self.full_transformation = [[r0], [r1, ], [r3, r2, r4, ], [r7, r5, r6, ], [r8, r9, r10, ],
                                   [r11, r12, r13, r14, ], [r15], [r16, ], ]

            self.transformation_directory = "UMLRT2Kiltera_MM/transformation/from_ATL/"

        # =====METAMODELS===============

        self.inputMM = "UMLRT2Kiltera_MM/transformation_for_prunning/metamodels/rt_new.ecore"
        self.outputMM = "UMLRT2Kiltera_MM/transformation_for_prunning/metamodels/klt_new.ecore"

        # ====CONTRACTS==================

        self.contract_directory = "UMLRT2Kiltera_MM/Properties/from_thesis/"

        self.atomic_contracts = [
            "PP1",
            "PP2",
            "PP3",
            "PP4",
            # #"PP5",
        ]

        self.if_then_contracts = [
            ["MM5_if", "MM5_then"],
            ["MM6_if", "MM6_then"],
            ["MM7_if", "MM7_then"],
            ["MM11_if", "MM11_then"],
            ["SS1_if", "SS1_then"],
            # skip this one
            # #["SS2_if", "SS2_then"],
            # ["SS3_if1", "SS3_then1"],
            # ["SS3_if2", "SS3_then2"],
        ]

        self.prop_if_then_contracts = [
            # structure is 'if graph', 'then graph'
            # where the 'then graph' is made up of reverse polish notation
            ["MM1_if", ["MM1_then1", "MM1_then2", "NOT", "AND"]],
            ["MM2_if", ["MM2_then1", "MM2_then2", "NOT", "AND"]],
            ["MM3_if", ["MM3_then1", "MM3_then2", "NOT", "AND"]],
            ["MM4_if", ["MM4_then1", "MM4_then2", "NOT", "AND"]],
            ["MM8_if", ["MM8_then1", "MM8_then2", "NOT", "AND", "MM8_then1", "NOT", "OR"]],
            ["MM9_if", ["MM9_then1", "MM9_then2", "NOT", "AND", "MM9_then1", "NOT", "OR"]],
            ["MM10_if", ["MM10_then1", "MM10_then2", "NOT", "AND", "MM10_then1", "NOT", "OR"]],
            # skip this one
            #  #[["SS3_if1", "SS3_if2", "NOT", "AND"], ["SS3_then1", "SS3_then2", "NOT", "AND"]],
        ]

        # =========PC SAVE LOCATION

        self.pc_save_filename = "pcs_uml.txt"


if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    test = UMLTest(args)
    test.test_correct(args)


