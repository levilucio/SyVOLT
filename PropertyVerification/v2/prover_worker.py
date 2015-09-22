
from multiprocessing import Process

from core.himesis_utils import expand_graph
from copy import deepcopy


class prover_worker(Process):
    def __init__(self, id, pc_queue, results_queue, atomic_contracts, if_then_contracts):
        super(prover_worker, self).__init__()
        self.id = id
        self.pc_queue = pc_queue
        self.results_queue = results_queue

        self.atomic_contracts = deepcopy(atomic_contracts)
        self.if_then_contracts = deepcopy(if_then_contracts)

        self.contract_failed_pcs = {}
        for contract_name, atomic_contract in atomic_contracts:
            self.contract_failed_pcs[contract_name] = []

    def run(self):
        print("Hello from " + str(self.id))

        while True:

            pc, pc_name = self.pc_queue.get()

            if pc_name == "STOP":
                break

            pc = expand_graph(pc)
            pc.name = pc_name


            if pc.name == "HEmptyPathCondition":
                continue



            for contract_name, atomic_contract in self.atomic_contracts:
                result = atomic_contract.check_isolated(pc)

                # the isolated part did not match
                # skip checking this contract on this pc
                if result == atomic_contract.NO_ISOLATED:
                    # print("NO ISOLATED")
                    continue



                print("\nPC: " + pc.name)
                print("Checking contract: " + contract_name)

                result = atomic_contract.check(pc, verbosity = 0)

                print("Result: " + result)
                if result == atomic_contract.NO_COMPLETE:
                    print("Atomic contract: " + contract_name + " does not hold on " + pc.name + "\n")
                    self.contract_failed_pcs[contract_name].append(pc_name)

        print("Stopping thread " + str(self.id))
        self.results_queue.put(self.contract_failed_pcs)