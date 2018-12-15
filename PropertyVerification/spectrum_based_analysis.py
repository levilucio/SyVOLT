class SpectrumBasedAnalyzer:

    def print_spectrum_based_analysis_info(self, pathCondGen, all_contracts, contract_succeeded_pcs, contract_failed_pcs):

        print("Starting spectrum-based analysis...")

        filename = "sba.xml"

        print("Writing to file: " + filename)
        with open(filename, "w") as f:

            f.write("<contract_satisfaction>")
            f.write("\n")
            for (c_name, _) in all_contracts:
                f.write('<contract name="' + c_name + '" ')
                f.write("succeed='" + str(len(contract_succeeded_pcs[c_name])) + "'")
                f.write(" ")
                f.write("failed='" + str(len(contract_failed_pcs[c_name])) + "'")
                f.write("/>\n")
            f.write("</contract_satisfaction>\n")

            f.write("<rules>")
            f.write("\n")
            for layer in pathCondGen.transformation:
                for rule in layer:
                    f.write('<rule name="' + pathCondGen.rule_names[rule.name] + '"/>')
                    f.write("\n")
            f.write("</rules>\n")


            f.write("<contracts>")
            f.write("\n")
            for (c_name, _) in all_contracts:
                f.write('<contract name="' + c_name + '"/>')
                f.write("\n")
            f.write("</contracts>\n")

            f.write("<rules_for_each_path_condition>")
            f.write("\n")
            i = 0
            for _, pc_name in pathCondGen.get_path_conditions(expand = False, get_pretty_name = True):

                # f.write(pc_name)
                rules = pathCondGen.rules_in_pc_name(pc_name)
                if len(rules) == 1:
                    continue
                rules.remove("HEmptyPathCondition")
                f.write("<PC num='" + str(i) + "' ")
                i += 1

                f.write('rules="')
                for r in rules:
                    f.write(r + ",")
                f.write('"/>\n')

            f.write("</rules_for_each_path_condition>\n")

            f.write("<contracts_for_each_path_condition>")
            f.write("\n")
            i = 0
            for _, pc_name in pathCondGen.get_path_conditions(expand = False, get_pretty_name = False):
                # print(pc_name)
                if pc_name == "Em.0":
                    continue
                f.write("<PC num='" + str(i) + "' ")
                i += 1

                f.write("sat_contracts='")

                for contract_name in contract_succeeded_pcs:
                    if pc_name in contract_succeeded_pcs[contract_name]:
                        f.write(contract_name + ",")

                f.write("' ")

                f.write("nonsat_contracts='")

                for contract_name in contract_failed_pcs:
                    if pc_name in contract_failed_pcs[contract_name]:
                        f.write(contract_name + ",")

                f.write("' />\n")
            f.write("</contracts_for_each_path_condition>\n")



        print("Finished spectrum-based analysis")