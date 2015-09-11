from profiler import *

from PropertyVerification.v2.disambiguate import Disambiguator

class ContractProver():

    def __init__(self):
        self.disambig = Disambiguator(0)

    def rule_name_set(self, name):
        rule_split = [rule.split("-")[0] for rule in name.split("_")]
        return rule_split

    def seen_pc_before(self, pc_name, rules):
        pc_rules = self.rule_name_set(pc_name)

        for r in rules:
            #print(pc_rules)
            #print(r)
            result = set(pc_rules).issubset(r)
            if result:
                return True


        return False


    #@do_cprofile
    def prove_contracts(self, pathCondGen, atomic_contracts, if_then_contracts):

        #initialize a dict to hold the rules that a contract will hold on
        contract_rule_dict = {}
        for contract_name, atomic_contract in atomic_contracts:
            contract_rule_dict[contract_name] = []

        for pc in pathCondGen.get_path_conditions():

            print("\nPC: " + pc.name)

            disambig_dict = {}
            for contract_name, atomic_contract in atomic_contracts:


                print("Checking contract: " + contract_name)
                result = atomic_contract.check_isolated(pc)

                # the isolated part did not match
                # skip checking this contract on this pc
                if result == atomic_contract.NO_ISOLATED:
                    continue



                rules = contract_rule_dict[contract_name]
                print("Is in contract_rule_dict: " + str(rules))

                result = self.seen_pc_before(pc.name, rules)
                print("Result: " + str(result))

                #get the list of mms that will be disambigged on
                contract_mms = self.disambig.set_contract(atomic_contract)

                #check to see if we've already disambigged these for these mms
                if str(contract_mms) in disambig_dict:
                    disambig_pcs = disambig_dict[str(contract_mms)]
                else:
                    #do the disambigging
                    disambig_pcs = self.disambig.disambiguate(pc)
                    #disambig_pcs.append(pc)
                    disambig_dict[str(contract_mms)] = disambig_pcs


                dpcs = [dpc for dpc in disambig_pcs]


                print("Length disambig pcs: " + str(len(dpcs)))

                for dpc in dpcs:
                    print("DPC: " + dpc.name)
                    result = atomic_contract.check(dpc)

                    #print("Result: " + str(result))

                    if result == atomic_contract.NO_COMPLETE:
                        print("Atomic contract: " + contract_name + " does not hold on " + pc.name + "\n")
                    else:
                        print("Atomic contract: " + contract_name + " does hold on " + pc.name + "\n")
                        contract_rule_dict[contract_name].append(self.rule_name_set(pc.name))