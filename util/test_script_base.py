import time

from path_condition_generator import PathConditionGenerator

from pyramify.PyRamify import PyRamify

from util.test_script_utils import set_artifact_directory, get_sub_and_super_classes, set_supertypes, load_contracts, save_pcs, load_pcs, load_transformation
from util.slicer import Slicer

from core.himesis_utils import load_directory

from PropertyVerification.ContractProver import ContractProver


class Test:

    def __init__(self):
        self.artifact_directory = ""
        self.transformation_directory = ""
        self.contract_directory = ""

        self.full_transformation = []
        self.rules = []
        self.transformation = []

        self.ruleTraceCheckers = {}
        self.matchRulePatterns = {}
        self.ruleCombinators = {}
        self.overlapping_rules = {}
        self.subsumption = {}
        self.loopingRuleSubsumption = {}

        self.subclasses_dict = {}
        self.superclasses_dict = {}

        self.atomic_contracts = []
        self.if_then_contracts = []
        self.prop_if_then_contracts = []

        self.inputMM = ""
        self.outputMM = ""

        self.pc_save_filename = ""

    def test_correct(self, args):
        set_artifact_directory(self.artifact_directory)

        self.rules, self.transformation = load_transformation(self.transformation_directory, self.full_transformation)


        pyramify = PyRamify(verbosity = args.verbosity, draw_svg = args.draw_svg)

        [self.rules, self.ruleTraceCheckers, self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory(self.transformation_directory, self.transformation)

        self.subclasses_dict, self.superclasses_dict = get_sub_and_super_classes(self.inputMM, self.outputMM)

        set_supertypes(self.superclasses_dict, self.rules, self.transformation, self.ruleTraceCheckers,
                       self.matchRulePatterns, self.ruleCombinators)

        # load the contracts

        contracts = load_directory(self.contract_directory)

        self.atomic_contracts, self.if_then_contracts = load_contracts(contracts, self.superclasses_dict,
                                                                       self.atomic_contracts, self.if_then_contracts,
                                                                       args.draw_svg)

        slicer = Slicer(self.rules, self.transformation, self.superclasses_dict, self.overlapping_rules, self.atomic_contracts)

        if args.slice > -1:
            contract, self.atomic_contracts, self.if_then_contracts = slicer.get_contract(args.slice,
                                                                                          self.atomic_contracts,
                                                                                          self.if_then_contracts)
            self.rules, self.transformation = slicer.slice_transformation(contract)

        # raise Exception()

        s = PathConditionGenerator(self.transformation, self.outputMM, self.ruleCombinators, self.ruleTraceCheckers, self.overlapping_rules, self.subsumption,
                                   self.loopingRuleSubsumption, args)  #
        # raise Exception()

        if not args.pc_filename is None:
            if len(args.pc_filename) == 0:
                loaded_pc_dict = load_pcs(self.pc_save_filename)
            else:
                loaded_pc_dict = load_pcs(args.pc_filename)
            s.load_saved_pcs(loaded_pc_dict)

            pc_time = "(PCs loaded)"
        else:
            ts0 = time.time()
            s.build_path_conditions()
            ts1 = time.time()

            pc_time = ts1 - ts0
            print("\n\nTime to build the set of path conditions: " + str(pc_time))

            save_pcs(s, self.pc_save_filename)

        print("Number of path conditions: " + str(s.num_path_conditions))

        # print("printing path conditions")
        # s.print_path_conditions_screen()
        #
        #        s.print_path_conditions_file()
        # raise Exception()

        print("\n===================")
        print("\n===================")
        print("\nContract proving:")
        s.verbosity = 0
        contract_prover = ContractProver(slicer, self.superclasses_dict)
        contract_prover.show_progress_bar = args.show_progress_bar
        contract_prover.prove_contracts(s, self.atomic_contracts, self.if_then_contracts)
        print("\n\nTime to build the set of path conditions: " + str(pc_time))
        print("Number of path conditions: " + str(s.num_path_conditions))