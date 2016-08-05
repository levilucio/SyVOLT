class ContractDebugger:

    def __init__(self, pathCondGen):
        self.pathCondGen = pathCondGen

    def explain_failures(self, contract_name, contract, success_pcs, failed_pcs):

        print("Explaining why contract fails: " + contract_name)

        print(success_pcs)
        print(failed_pcs)

        self.get_rule_differences(success_pcs, failed_pcs)

    def get_rule_differences(self, success_pcs, failed_pcs):

        rules_in_success = self.get_rules(success_pcs)
        rules_in_failed = self.get_rules(failed_pcs)

        good_rules = [rule for rule in rules_in_success if not rule in rules_in_failed]
        bad_rules = [rule for rule in rules_in_failed if not rule in rules_in_success]

        print("Good rules: (Rules in success set and not failure set)")
        print(good_rules)

        print("Bad rules: (Rules in failure set and not success set)")
        print(bad_rules)

    def get_rules(self, pcs):
        rules = []

        for pc in pcs:
            r = self.pathCondGen.rules_in_pc_real_name(pc)
            print(r)

        return rules
