from core.new_match_algo import NewHimesisMatcher
from random import choice
from core.himesis_utils import expand_graph, graph_to_dot, get_filename

class ContractDebugger:

    def __init__(self, pathCondGen, slicer, superclasses_dict):
        self.pathCondGen = pathCondGen
        self.slicer = slicer
        self.superclasses_dict = superclasses_dict

    def explain_failures(self, contract_name, contract, success_pcs, failed_pcs, smallest_failed):

        print("Explaining why contract fails: " + contract_name)

        contract.draw()

        # print("Success PCs: ")
        # print(success_pcs)

        # print("Failed PCs: ")
        # print(failed_pcs)

        good_rules, bad_rules = self.get_rule_differences(success_pcs, failed_pcs)

        print("Good rules: (Rules in success set and not failure set)")
        print(good_rules)

        print("Bad rules: (Rules common to all in failure set)")
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

        if contract.__name__ == "IfThenContract":
            contract_complete = contract.then_contract.complete
        else:
            contract_complete = contract.complete

        contract_mms = [mm.replace("MT_pre__", "") for mm in contract_complete.vs["mm__"]]

        print("")
        if len(required_iso_elements) > 0:
            print("Contract requires elements from good rules of type:")
            for iso in required_iso_elements:
                print("\t" + contract_mms[iso])

        if len(required_links) > 0:
            print("Contract requires links from good rules of type:")
            for link in required_links:
                n0, n1, nlink = link
                print("\t", end="")
                NewHimesisMatcher.print_link(None, contract_complete, n0, n1, nlink)

        print("")

        failed_pc_name = choice(smallest_failed)

        print("Examining failed pc: " + failed_pc_name)
        print("Filename: " + str(get_filename(failed_pc_name)))
        failed_pc = self.pathCondGen.pc_dict[failed_pc_name]
        failed_pc = expand_graph(failed_pc)

        matcher = NewHimesisMatcher(failed_pc, contract_complete)
        matcher.print_reason_failed = True
        matcher.debug = False

        matcher.superclasses_dict = self.superclasses_dict

        for _ in matcher.match_iter():
            break

        matcher.print_failures()

        #graph_to_dot(contract.complete.name + "_failed_" + failed_pc.name, failed_pc)


    def get_rule_differences(self, success_pcs, failed_pcs):

        rules_in_success = self.get_rules(success_pcs)
        rules_in_failed = self.get_rules(failed_pcs)

        good_rules = sorted([rule for rule in rules_in_success if not rule in rules_in_failed])

        bad_rules = []
        for rule in rules_in_failed:

            #see if this rule is in all failed PCs
            if all(rule in self.pathCondGen.rules_in_pc_real_name(pc) for pc in failed_pcs):

                #see if this rule is not in all success PCs
                if not success_pcs or not all(rule in self.pathCondGen.rules_in_pc_real_name(pc) for pc in success_pcs):
                    bad_rules.append(rule)

        bad_rules = sorted(bad_rules)

        return good_rules, bad_rules

    def get_rules(self, pcs):
        rules = []

        for pc in pcs:
            rules +=  self.pathCondGen.rules_in_pc_real_name(pc)

        return list(set(rules))
