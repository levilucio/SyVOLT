from profiler import *

from PropertyVerification.v2.disambiguate import Disambiguator
from core.himesis_utils import graph_to_dot

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

        #initialize a dict to hold the rules that a contract will hold on
        contract_rule_dict = {}
        contract_failed_pcs = {}
        for contract_name, atomic_contract in atomic_contracts:
            contract_rule_dict[contract_name] = []
            contract_failed_pcs[contract_name] = []


        for pc in pathCondGen.get_path_conditions():



            if pc.name == "HEmptyPathCondition":
                continue

            # if not pc.name == "HEmptyPathCondition_HRootRule-0_HMotherRule-0_HFatherRule-0_HDaughterRule-0":
            #     continue

            #graph_to_dot(pc.name.replace("-", "_"), pc)

            #print("PC name: " + pc.name)

            for contract_name, atomic_contract in atomic_contracts:



                result = atomic_contract.check_isolated(pc)

                # the isolated part did not match
                # skip checking this contract on this pc
                if result == atomic_contract.NO_ISOLATED:
                    #print("NO ISOLATED")
                    continue
                # else:
                #     print("ISOLATED")



                print("\nPC: " + pc.name)
                print("Checking contract: " + contract_name)



                result = atomic_contract.check(pc, verbosity=0)

                print("Result: " + result)
                if result == atomic_contract.NO_COMPLETE:
                    print("Atomic contract: " + contract_name + " does not hold on " + pc.name + "\n")
                    if pc not in contract_failed_pcs[contract_name]:
                        contract_failed_pcs[contract_name].append(pc)
                # else:
                #     print("Atomic contract: " + contract_name + " does hold on " + pc.name + "\n")
                    #contract_holds = True
                    #break



        print("")
        for contract_name, atomic_contract in atomic_contracts:
            print("\nFailed PCs for " + contract_name + ":")
            for pc in contract_failed_pcs[contract_name]:
                print(pc.name)