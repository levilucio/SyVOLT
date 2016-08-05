
'''
Created on 2013-01-22

@author: levi
'''

from util.parser import load_parser

from util.test_script_base import Test


class MBEddr(Test):
    def __init__(self):
        super(MBEddr, self).__init__()

        # ============TRANSFORMATION=================
        r0 = 'Hlayer0rule0'
        r1 = 'Hlayer0rule1'
        r2 = 'Hlayer0rule2'
        r3 = 'Hlayer0rule3'
        r4 = 'Hlayer0rule4'
        r5 = 'Hlayer0rule6'
        r6 = 'Hlayer0rule7'
        r7 = 'Hlayer0rule8'
        r8 = 'Hlayer0rule9'
        r9 = 'Hlayer0rule10'
        r10 = 'Hlayer0rule11'
        r11 = 'Hlayer1rule0'
        r12 = 'Hlayer1rule1'
        r13 = 'Hlayer1rule2'
        r14 = 'Hlayer1rule3'
        r15 = 'Hlayer1rule4'
        r16 = 'Hlayer1rule5'
        r17 = 'Hlayer1rule6'
        r18 = 'Hlayer1rule7'
        r19 = 'Hlayer1rule8'
        r20 = 'Hlayer1rule9'
        r21 = 'Hlayer1rule10'
        r22 = 'Hlayer1rule11'
        r23 = 'Hlayer1rule12'
        r24 = 'Hlayer1rule13'
        r25 = 'Hlayer1rule14'
        r26 = 'Hlayer1rule15'
        r27 = 'Hlayer2rule1'
        r28 = 'Hlayer2rule2'
        r29 = 'Hlayer2rule3'
        r30 = 'Hlayer3rule0'
        r31 = 'Hlayer3rule1'
        r32 = 'Hlayer3rule2'
        r33 = 'Hlayer3rule3'
        r34 = 'Hlayer3rule4'
        r33copy = 'Hlayer3rule3'
        r34copy = 'Hlayer3rule4'
        r35 = 'Hlayer3rule5'
        r36 = 'Hlayer4rule0'
        r37 = 'Hlayer4rule1'
        r38 = 'Hlayer4rule2'
        r39 = 'Hlayer4rule3'
        r40 = 'Hlayer5rule0'
        r41 = 'Hlayer5rule1'
        r42 = 'Hlayer5rule2'
        r43 = 'Hlayer5rule3'
        r44 = 'Hlayer5rule4'
        r45 = 'Hlayer5rule5'
        r46 = 'Hlayer6rule0'

        self.full_transformation = [[r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, ],
                               [r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, ],
                               [r27, r28, r29, ], [r30, r31, r32, r33, r34, r33copy, r34copy, r35, ],
                               [r36, r37, r38, r39, ],
                               [r40, r41, r42, r43, r44, r45, ], [r46, ],
                               ]

        self.transformation_directory = "mbeddr2C_MM/real_transformation/no_contains"

        # =====METAMODELS===============

        self.inputMM = "./mbeddr2C_MM/ecore_metamodels/Module.ecore"
        self.outputMM = "./mbeddr2C_MM/ecore_metamodels/C.ecore"

        # ====CONTRACTS==================

        self.contract_directory = "mbeddr2C_MM/Contracts/"

        self.atomic_contracts = [
            'AssignmentInstance',
            'GlobalVarGetsCorrectFunctionAddressAtInit',
            'Simple',
            'VerySimple'
        ]

        self.if_then_contracts = []

        self.prop_if_then_contracts = []

        # =========PC SAVE LOCATION

        self.pc_save_filename = "pcs_mbeddr.txt"


if __name__ == "__main__":
    parser = load_parser()
    args = parser.parse_args()

    mbeddr = MBEddr()
    mbeddr.test_correct(args)


