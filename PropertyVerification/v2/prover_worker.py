
from multiprocessing import Process

from core.himesis_utils import expand_graph
from copy import deepcopy


class prover_worker(Process):
    def __init__(self, id, verbosity, pc_queue, results_queue, atomic_contracts, if_then_contracts):
        super(prover_worker, self).__init__()
        self.id = id
        self.pc_queue = pc_queue
        self.results_queue = results_queue
        self.verbosity = verbosity

        self.atomic_contracts = deepcopy(atomic_contracts)
        self.if_then_contracts = deepcopy(if_then_contracts)
        self.all_contracts = self.atomic_contracts + self.if_then_contracts

        self.contract_failed_pcs = {}
        self.contract_succeeded_pcs = {}
        for contract_name, contract in self.all_contracts:
            self.contract_failed_pcs[contract_name] = []
            self.contract_succeeded_pcs[contract_name] = []

    def run(self):

        while True:

            pc, pc_name = self.pc_queue.get()

            if pc_name == "STOP":
                break

            pc = expand_graph(pc)
            pc.name = pc_name


            if pc.name == "HEmptyPathCondition":
                continue

            if pc.name != "HEmptyPathCondition_HRootRule-0_HSonRule-0_HUnionSonRule-P0":
                continue

            for contract_name, contract in self.all_contracts:
                result = contract.check_isolated(pc)

                # the isolated part did not match
                # skip checking this contract on this pc
                if result == contract.NO_ISOLATED:
                    # print("NO ISOLATED")
                    continue


                if self.verbosity > 1:
                    print("\nPC: " + pc.name)
                    print("Checking contract: " + contract_name)

                result = contract.check(pc, verbosity = self.verbosity)

                if self.verbosity > 1:
                    print("Result: " + result)


                if result == contract.NO_COMPLETE:
                    #if self.verbosity > 0:
                        #print("Atomic contract: " + contract_name + " does not hold on " + pc.name + "\n")
                    self.contract_failed_pcs[contract_name].append(pc_name)
                if result == contract.COMPLETE_FOUND:
                    self.contract_succeeded_pcs[contract_name].append(pc_name)

        self.results_queue.put([self.contract_failed_pcs, self.contract_succeeded_pcs])
