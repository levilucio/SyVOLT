from profiler import *

from PropertyVerification.ContractDebugger import ContractDebugger
from core.himesis_utils import graph_to_dot, expand_graph, get_filename

import multiprocessing
from multiprocessing import Manager

from PropertyVerification.prover_worker import prover_worker

from util.progress import ProgressBar

import time
from time import sleep

class ContractProver:

    def __init__(self, slicer, superclasses_dict):
        #self.disambig = Disambiguator(0)

        self.verbosity = 2

        self.pathCondGen = None

        self.draw_success_failed = False

        #used for debugging the contract
        self.slicer = slicer
        self.superclasses_dict = superclasses_dict

    def find_smallest_pc(self, pc_names):
        smallest = []
        smallestSize = 0

        for pc_name in pc_names:
            sizeCounter = len(pc_name.split("_"))
            if smallestSize == 0:
                smallest.append(pc_name)
                smallestSize = sizeCounter
            else:
                if sizeCounter < smallestSize:
                    smallest = [pc_name]
                    smallestSize = sizeCounter
                elif sizeCounter == smallestSize:
                    smallest.append(pc_name)

        return smallest


    #@do_cprofile
    #@profile
    def prove_contracts(self, pathCondGen, atomic_contracts, if_then_contracts):

        self.verbosity = pathCondGen.verbosity
        self.pathCondGen = pathCondGen

        all_contracts = atomic_contracts + if_then_contracts

        print("\nStarting to prove contracts:")
        start_time = time.time()

        contract_failed_pcs = {}
        contract_succeeded_pcs = {}
        for contract_name, atomic_contract in all_contracts:
            print("Proving: " + atomic_contract.to_string())
            contract_failed_pcs[contract_name] = []
            contract_succeeded_pcs[contract_name] = []

        manager = Manager()
        cpu_count = multiprocessing.cpu_count()
        print("CPU Count: " + str(cpu_count))

        pc_queue = manager.Queue()
        results_queue = manager.Queue()

        workers = []

        for i in range(cpu_count):
            new_worker = prover_worker(i, self.verbosity, pc_queue, results_queue, atomic_contracts, if_then_contracts)
            new_worker.start()
            workers.append(new_worker)

        for pc, pc_name in pathCondGen.get_path_conditions(expand=False):
            pc_queue.put(pc)

        for i in range(cpu_count):
            pc_queue.put(None)

        #start a progress bar
        pc_set_length = pathCondGen.num_path_conditions
        progress_bar = ProgressBar(pc_set_length)

        len_pc_queue = pc_queue.qsize()
        while len_pc_queue > 0:
            progress_bar.update_progress(pc_set_length - len_pc_queue)
            sleep(1)
            len_pc_queue = pc_queue.qsize()

        for worker in workers:
            worker.join()

        for worker in workers:
            [fail, succeed] = results_queue.get()

            print("Thread finished at time: " + str(time.time() - start_time))

            for contract_name in fail.keys():
                contract_failed_pcs[contract_name] += fail[contract_name]
            for contract_name in succeed.keys():
                contract_succeeded_pcs[contract_name] += succeed[contract_name]



        proof_time = time.time() - start_time


        print("")
        for contract_name, atomic_contract in all_contracts:

            self.report_success_fail("Succeeded", contract_succeeded_pcs, contract_name)

            self.report_success_fail("Failed", contract_failed_pcs, contract_name)

            if self.draw_success_failed:
                atomic_contract.draw()

        print("Summary:")
        for contract_name, atomic_contract in all_contracts:
            print("Name:" + contract_name)
            print("\tNum Succeeded Contracts: " + str(len(contract_succeeded_pcs[contract_name])))
            print("\tNum Failed Contracts: " + str(len(contract_failed_pcs[contract_name])))

        print("Took " + str(proof_time) + " seconds to prove " + str(len(atomic_contracts + if_then_contracts)) + " contracts\n")

        if len(all_contracts) == 1:
            cd = ContractDebugger(self.pathCondGen, self.slicer, self.superclasses_dict)
            contract_name, contract = all_contracts[0]
            if len(contract_failed_pcs[contract_name]) > 0:
                cd.explain_failures(contract_name, contract, contract_succeeded_pcs[contract_name], contract_failed_pcs[contract_name], self.find_smallest_pc(contract_failed_pcs[contract_name]))

    def report_success_fail(self, status, list_of_pcs, contract_name):
        num_contracts_to_print = 20

        print("\n" + str(len(list_of_pcs[contract_name])) + " " + status + " PCs for " + contract_name + ":")

        if len(list_of_pcs[contract_name]) < num_contracts_to_print:
            for pc_name in sorted(list_of_pcs[contract_name]):
                self.print_name(pc_name)
        else:
            print("More than " + str(num_contracts_to_print) + " contracts")

        print ('\nSmallest Path Conditions where the contract ' + status + ':')
        smallest_pc_set = self.find_smallest_pc(list_of_pcs[contract_name])
        for pc_name in smallest_pc_set:
            self.print_name(pc_name)
            print("Filename: " + get_filename(pc_name))

            if self.draw_success_failed:
                shrunk_pc = self.pathCondGen.pc_dict[pc_name]
                pc = expand_graph(shrunk_pc)
                graph_to_dot(contract_name + "_" + status + "_" + pc.name, pc)

        print('\n')

    def print_name(self, name):

        contract_name_max_size = 300

        name = name[:contract_name_max_size]
        real_name_list = self.pathCondGen.rules_in_pc_real_name(name)
        print("_".join(real_name_list))