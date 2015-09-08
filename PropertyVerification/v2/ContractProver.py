from PropertyVerification.v2.disambiguate import Disambiguator

class ContractProver():

    def __init__(self):
        self.disambig = Disambiguator(0)


    def prove_contracts(self, pathCondGen, atomic_contracts, if_then_contracts):

        for pc in pathCondGen.get_path_conditions():
            print(pc.name)

            disambig_dict = {}
            for name, atomic_contract in atomic_contracts:

                result = atomic_contract.check_isolated(pc)

                # the isolated part did not match
                # skip checking this contract on this pc
                if result == atomic_contract.NO_ISOLATED:
                    continue

                #get the list of mms that will be disambigged on
                contract_mms = self.disambig.set_contract(atomic_contract)

                #check to see if we've already disambigged these for these mms
                if str(contract_mms) in disambig_dict:
                    disambig_pcs = disambig_dict[str(contract_mms)]
                else:
                    #do the disambigging
                    disambig_pcs = self.disambig.disambiguate(pc)
                    disambig_dict[str(contract_mms)] = disambig_pcs

                print("Length disambig pcs: " + str(len(disambig_pcs)))
                #
                # for dpc in disambig_pcs:
                #     result = atomic_contract.check(dpc)
                #
                #     print("Result: " + result)
                #
                #     if result == atomic_contract.NO_COMPLETE:
                #         print("Atomic contract: " + name + " does not hold on " + pc.name + "\n")