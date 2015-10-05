from profiler import *

#from PropertyVerification.v2.disambiguate import Disambiguator
from core.himesis_utils import graph_to_dot

import multiprocessing
from multiprocessing import Manager

from PropertyVerification.v2.prover_worker import prover_worker

import time

class ContractProver():

    def __init__(self):
        #self.disambig = Disambiguator(0)

        self.verbosity = 2

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

        self.verbosity = pathCondGen.verbosity

        print("\nStarting to prove contracts:")
        start_time = time.time()


        contract_failed_pcs = {}
        contract_succeeded_pcs = {}
        for contract_name, atomic_contract in atomic_contracts:
            contract_failed_pcs[contract_name] = []
            contract_succeeded_pcs[contract_name] = []

        manager = Manager()
        cpu_count = multiprocessing.cpu_count()
        print("CPU Count: " + str(cpu_count))

        pc_queue = manager.Queue()
        results_queue = manager.Queue()

        workers = []

        rules = []
        rules_seen = []

        for layer in pathCondGen.transformation:
            for rule in layer:
                
                real_name = pathCondGen.rule_names[rule.name]
                rules.append(real_name)

        for i in range(cpu_count):
            new_worker = prover_worker(i, self.verbosity, pc_queue, results_queue, atomic_contracts, if_then_contracts)
            new_worker.start()
            workers.append(new_worker)

        for pc, pc_name in pathCondGen.get_path_conditions(expand=False):
            rules_in_pc = pc_name.split("_")

            for rs in rules_in_pc:
                rs_2 = rs.split("-")[0]
                rules_seen.append(rs_2)
                
            pc_queue.put([pc, pc_name])

        rules_seen= list(set(rules_seen))
        #print("Rules seen: " + str(rules_seen))
        for rule in rules:
            if rule not in rules_seen:
                print("ERROR: Rule " + rule + " was not executed!")


        for i in range(cpu_count):
            pc_queue.put([None, "STOP"])

        for worker in workers:
            worker.join()

        for worker in workers:
            [fail, succeed] = results_queue.get()

            for contract_name in fail.keys():
                contract_failed_pcs[contract_name] += fail[contract_name]
            for contract_name in succeed.keys():
                contract_succeeded_pcs[contract_name] += succeed[contract_name]


        print("")
        for contract_name, atomic_contract in atomic_contracts:
            smallestCounterExamples = []
            smallestCounterExampleSize = 0
            print("\nSuccessful PCs for " + contract_name + ":")
            for pc_name in sorted(contract_succeeded_pcs[contract_name]):
                print(pc_name)
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

            print ('\nThe smallest Path Conditions where the contract fails are:')
            print(str(smallestCounterExamples))
            print('\n')


        proof_time = time.time() - start_time
        print("Took " + str(proof_time) + " seconds to prove " + str(len(atomic_contracts)) + " contracts\n")
