class SpectrumBasedAnalyzer:

    def print_spectrum_based_analysis_info(self, pathCondGen, all_contracts, contract_succeeded_pcs, contract_failed_pcs):

        print("Starting spectrum-based analysis...")

        filename = "sba.txt"

        print("Writing to file: " + filename)
        with open(filename, "w") as f:

            f.write("Contract Satisfaction:")
            f.write("\n")
            for (c_name, _) in all_contracts:
                f.write(c_name + " - ")
                f.write("Succeed: " + str(len(contract_succeeded_pcs[c_name])))
                f.write(" ")
                f.write("Failed: " + str(len(contract_failed_pcs[c_name])))
                f.write("\n")
            f.write("\n")

            f.write("Rules:")
            f.write("\n")
            for layer in pathCondGen.transformation:
                for rule in layer:
                    f.write(pathCondGen.rule_names[rule.name])
                    f.write("\n")
            f.write("\n")

            f.write("Contracts:")
            f.write("\n")
            for (c_name, _) in all_contracts:
                f.write(c_name)
                f.write("\n")
            f.write("\n")

            f.write("Rules in each path condition:")
            f.write("\n")
            i = 0
            for _, pc_name in pathCondGen.get_path_conditions(expand = False, get_pretty_name = True):

                # f.write(pc_name)
                rules = pathCondGen.rules_in_pc_name(pc_name)
                if len(rules) == 1:
                    continue
                rules.remove("HEmptyPathCondition")
                f.write("PC" + str(i) + ": ")
                i += 1

                for r in rules:
                    f.write(r + ",")
                f.write("\n")

            f.write("\n")

            f.write("Contracts per path condition:")
            f.write("\n")
            i = 0
            for _, pc_name in pathCondGen.get_path_conditions(expand = False, get_pretty_name = False):
                # print(pc_name)
                if pc_name == "Em.0":
                    continue
                f.write("PC" + str(i) + ": ")
                i += 1
                f.write("\n")

                f.write("Sat: ")

                for contract_name in contract_succeeded_pcs:
                    if pc_name in contract_succeeded_pcs[contract_name]:
                        f.write(contract_name + ",")

                f.write("\n")

                f.write("Non Sat: ")

                for contract_name in contract_failed_pcs:
                    if pc_name in contract_failed_pcs[contract_name]:
                        f.write(contract_name + ",")

                f.write("\n")



        print("Finished spectrum-based analysis")