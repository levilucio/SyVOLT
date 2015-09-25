from profiler import *

from PropertyVerification.v2.disambiguate import Disambiguator
from core.himesis_utils import graph_to_dot

import multiprocessing
from multiprocessing import Manager

from PropertyVerification.v2.prover_worker import prover_worker

import time

class ContractProver():

    def __init__(self):
        self.disambig = Disambiguator(0)

    def rule_name_set(self, name):
        rule_split = [rule.split("-")[0] for rule in name.split("_")]
        return rule_split

    def seen_pc_before(self, pc_name, rules):
        pc_rules = self.rule_name_set(pc_name)

        #print("PC Rules: " + str(pc_rules))

        for r in rules:
            #print(pc_rules)
            #print(r)
            result = set(r).issubset(pc_rules)
            if result:
                return True


        return False


    #@do_cprofile
    def prove_contracts(self, pathCondGen, atomic_contracts, if_then_contracts):

        print("Starting to prove contracts:")
        start_time = time.time()


        contract_failed_pcs = {}
        for contract_name, atomic_contract in atomic_contracts:
            contract_failed_pcs[contract_name] = []

        manager = Manager()
        cpu_count = multiprocessing.cpu_count()
        print("CPU Count: " + str(cpu_count))

        pc_queue = manager.Queue()
        results_queue = manager.Queue()

        workers = []

        for i in range(cpu_count):
            new_worker = prover_worker(i, pc_queue, results_queue, atomic_contracts, if_then_contracts)
            new_worker.start()
            workers.append(new_worker)

        for pc, pc_name in pathCondGen.get_path_conditions(expand=False):
            pc_queue.put([pc, pc_name])

        for i in range(cpu_count):
            pc_queue.put([None, "STOP"])

        for worker in workers:
            worker.join()

        for worker in workers:
            r = results_queue.get()

            for contract_name in r.keys():
                contract_failed_pcs[contract_name] += r[contract_name]


        print("")
        for contract_name, atomic_contract in atomic_contracts:
            smallestCounterExamples = []
            smallestCounterExampleSize = 0
            print("\nFailed PCs for " + contract_name + ":")
            for pc_name in sorted(contract_failed_pcs[contract_name]):
                print(pc_name)

                sizeCounter = len(pc_name.split("_"))
                if smallestCounterExampleSize == 0:
                    smallestCounterExamples.append(pc_name)
                    smallestCounterExampleSize = sizeCounter
                else:
                    if sizeCounter < smallestCounterExampleSize:
                        smallestCounterExamples = [pc_name]
                        smallestCounterExampleSize = sizeCounter
                    elif sizeCounter == smallestCounterExampleSize:
                        smallestCounterExamples.append(pc_name)

            print ('The smallest Path Conditions where the contract fails are:')
            print(str(smallestCounterExamples))


        proof_time = time.time() - start_time
        print("Took " + str(proof_time) + " seconds to prove " + str(len(atomic_contracts)) + " contracts")