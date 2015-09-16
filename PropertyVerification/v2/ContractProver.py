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

            disambig_dict = {}
            for contract_name, atomic_contract in atomic_contracts:



                result = atomic_contract.check_isolated(pc)

                # the isolated part did not match
                # skip checking this contract on this pc
                if result == atomic_contract.NO_ISOLATED:
                    print("NO ISOLATED")
                    continue
                # else:
                #     print("ISOLATED")

                print("\nPC: " + pc.name)
                print("Checking contract: " + contract_name)


                result = atomic_contract.check(pc)
                if result == atomic_contract.NO_COMPLETE:
                    print("Atomic contract: " + contract_name + " does not hold on " + pc.name + "\n")
                    if pc not in contract_failed_pcs[contract_name]:
                        contract_failed_pcs[contract_name].append(pc)
                else:
                    print("Atomic contract: " + contract_name + " does hold on " + pc.name + "\n")
                    #contract_holds = True
                    #break

                #rules = contract_rule_dict[contract_name]
                # print("Is in contract_rule_dict: ")
                # for rule in rules:
                #     print(rule)

                # result = self.seen_pc_before(pc.name, rules)
                #
                # if result:
                #     #print("Contract holds because rule set has been seen before")
                #     continue

                # #get the list of mms that will be disambigged on
                # contract_mms = self.disambig.set_contract(atomic_contract)
                #
                # #check to see if we've already disambigged these for these mms
                # if str(contract_mms) in disambig_dict:
                #     disambig_pcs = disambig_dict[str(contract_mms)]
                # else:
                #     #do the disambigging
                #     disambig_pcs = self.disambig.disambiguate(pc)
                #     #disambig_pcs.append(pc)
                #     disambig_dict[str(contract_mms)] = disambig_pcs
                #
                #
                #
                # #print("Length disambig pcs: " + str(len(dpcs)))
                #
                # contract_holds = False
                #
                # for dpc in disambig_pcs:
                #     #print("DPC: " + dpc.name)
                #     result = atomic_contract.check(dpc)
                #
                #     #print("Result: " + str(result))
                #
                #     if result == atomic_contract.NO_COMPLETE:
                #         print("Atomic contract: " + contract_name + " does not hold on " + pc.name + "\n")
                #         if pc not in contract_failed_pcs[contract_name]:
                #             contract_failed_pcs[contract_name].append(pc)
                #     else:
                #         #print("Atomic contract: " + contract_name + " does hold on " + pc.name + "\n")
                #         contract_holds = True
                #         break
                #
                # if contract_holds:
                #     rules = self.rule_name_set(pc.name)
                #     if rules not in contract_rule_dict[contract_name]:
                #         contract_rule_dict[contract_name].append(rules)

        print("")
        for contract_name, atomic_contract in atomic_contracts:
            print("\nFailed PCs for " + contract_name + ":")
            for pc in contract_failed_pcs[contract_name]:
                print(pc.name)