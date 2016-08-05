from core.new_match_algo import NewHimesisMatcher

class ContractDebugger:

    def __init__(self, pathCondGen, slicer):
        self.pathCondGen = pathCondGen
        self.slicer = slicer

    def explain_failures(self, contract_name, contract, success_pcs, failed_pcs):

        print("Explaining why contract fails: " + contract_name)

        # print("Success PCs: ")
        # print(success_pcs)

        # print("Failed PCs: ")
        # print(failed_pcs)

        good_rules, bad_rules = self.get_rule_differences(success_pcs, failed_pcs)

        print("Good rules: (Rules in success set and not failure set)")
        print(good_rules)

        print("Bad rules: (Rules in failure set and not success set)")
        print(bad_rules)

        required_rules = self.slicer.required_rules[contract_name]

        required_iso_elements = []
        required_links = []

        for gr in good_rules:
            if gr not in required_rules:
                continue

            for element in required_rules[gr]:
                if isinstance(element, int) and element not in required_iso_elements:
                    required_iso_elements.append(element)
                elif isinstance(element, list) and element not in required_links:
                    required_links.append(element)

        # print(required_iso_elements)
        # print(required_links)

        contract_mms = [mm.replace("MT_pre__", "") for mm in contract.complete.vs["mm__"]]

        print("")
        print("Contract requires elements of type:")
        for iso in required_iso_elements:
            print("\t" + contract_mms[iso])

        print("Contract requires links of type:")
        for link in required_links:
            n0, n1, nlink = link
            print("\t", end="")
            NewHimesisMatcher.print_link(None, contract.complete, n0, n1, nlink)

        print("")


    def get_rule_differences(self, success_pcs, failed_pcs):

        rules_in_success = self.get_rules(success_pcs)
        rules_in_failed = self.get_rules(failed_pcs)

        good_rules = sorted([rule for rule in rules_in_success if not rule in rules_in_failed])
        bad_rules = sorted([rule for rule in rules_in_failed if not rule in rules_in_success])

        return good_rules, bad_rules

    def get_rules(self, pcs):
        rules = []

        for pc in pcs:
            rules +=  self.pathCondGen.rules_in_pc_real_name(pc)

        return list(set(rules))
