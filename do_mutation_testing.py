import subprocess
import datetime
import os, sys
from time import sleep

from collections import defaultdict

from mutation.mutation_possibilities import MutationPossibilityGenerator
from util.test_script_utils import load_transformation

from test_atlTrans_extended import ATLTest as FamToPersons
from test_GM2Autosar_transformation import GMTest
from test_umlToKiltera import UMLTest as UML2Kiltera
from test_uml2er import ProverTest as UML2ER
from test_RSS2ATOM import RSS2ATOMTest
from test_mbeddr import MBEddr

def do_mutation_testing(mpg, rules, transformation, test_script, use_integration_contracts):
    print_output = False

    poss_dict = {}
    mutation_count = 0

    xml_filename = "mutation_testing.xml"
    in_xml_filename = "./sba.xml"
    with open(xml_filename, "w") as f:

        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')

        f.write('<mutation_testing>\n')

        f.write('<header')
        f.write(' date="' + str(datetime.datetime.now()) + '">\n')
        for rule in rules.values():
            poss = mpg.generate_possibilities(rule, transformation)
            poss_dict[rule.name] = poss
            mutation_count += len(poss)

            f.write('<mutation rule_name="' + rule.name + '" mutations="' + str(poss) + '"/>\n')

        f.write('</header>\n')

        curr_mutation_count = 0
        for rule_name, poss_set in poss_dict.items():
            f.write('<mutation_set rule_name="' + rule_name + '">\n')

            print("Poss for rule: " + rule_name)
            for p in poss_set:

                print("Running mutation " + str(curr_mutation_count + 1) +
                      " out of " + str(mutation_count) + "...")
                print(p)

                curr_mutation_count += 1

                f.write('<mutation operation="' + str(p) + '">\n')

                rule_cmd = "--rule_to_mutate=" + rule_name
                poss_cmd = "--mutate=" + str(p).replace(" ", "")
                saving_cmd = "--skip_saving"
                pickle_cmd = "--skip_pickle"
                pruning_cmd = "--skip_pruning"

                cmd = ["python3", test_script, rule_cmd, poss_cmd, saving_cmd, pickle_cmd]

                if not use_integration_contracts:
                    contracts_cmd = "--unit_contracts"
                    cmd.append(contracts_cmd)

                # print(" ".join(cmd))

                if print_output:
                    subprocess.run(cmd)
                else:
                    subprocess.run(cmd, stdout=subprocess.PIPE)  # , stderr = subprocess.PIPE)

                # f.write(rule.name + "\n")
                # f.write(str(p) + "\n\n")
                with open(in_xml_filename) as g:
                    for line in g:
                        f.write(line)
                f.write('</mutation>\n')

            f.write('</mutation_set>\n')

        f.write('</mutation_testing>\n')


if __name__ == "__main__":
    print("Performing mutations...")

    test_script = ""
    transformation_dir = ""
    inputMM = ""
    outputMM = ""
    full_transformation = []

    trans = "F2P"
    use_integration_contracts = False

    if len(sys.argv) > 1:
        trans = sys.argv[1]

    if len(sys.argv) > 2:
        use_integration_contracts = "True" in sys.argv[2] or "True" in sys.argv[2]

    print("Mutating transformation: " + trans)
    print("Using integration contracts: " + str(use_integration_contracts))

    if len(sys.argv) > 1:
        trans = sys.argv[1]

    if trans == "F2P":
        #### FAMILIES TO PERSONS
        class Temp:
            integration_contracts = use_integration_contracts
        F2P = FamToPersons(Temp())
        test_script = "test_atlTrans_extended.py"
        transformation_dir = F2P.transformation_directory
        inputMM = F2P.inputMM
        outputMM = F2P.outputMM
        full_transformation = F2P.full_transformation

    elif trans == "RSS":
        #### RSSToATOM
        class Temp:
            integration_contracts = use_integration_contracts
        RSS2ATOM = RSS2ATOMTest(Temp())
        test_script = "test_RSS2ATOM.py"
        transformation_dir = RSS2ATOM.transformation_directory
        inputMM = RSS2ATOM.inputMM
        outputMM = RSS2ATOM.outputMM
        full_transformation = RSS2ATOM.full_transformation

    elif trans == "UML2ER":
        #### UML2ER
        class Temp:
            integration_contracts = use_integration_contracts
        UML2ER = UML2ER(Temp())
        test_script = "test_uml2er.py"
        transformation_dir = UML2ER.transformation_directory
        inputMM = UML2ER.inputMM
        outputMM = UML2ER.outputMM
        full_transformation = UML2ER.full_transformation

    elif trans == "GM":
        #### GM2AUTOSAR
        class Temp:
            handbuilt = False
            integration_contracts = use_integration_contracts
        GM2AUTOSAR = GMTest(Temp())
        test_script = "test_GM2Autosar_transformation.py"
        transformation_dir = GM2AUTOSAR.transformation_directory
        inputMM = GM2AUTOSAR.inputMM
        outputMM = GM2AUTOSAR.outputMM
        full_transformation = GM2AUTOSAR.full_transformation

    elif trans == "Kiltera":
        #### UML2Kiltera
        class Temp:
            handbuilt = False
            integration_contracts = use_integration_contracts
        UML2Kiltera_ = UML2Kiltera(Temp())
        test_script = "test_umlToKiltera.py"
        transformation_dir = UML2Kiltera_.transformation_directory
        inputMM = UML2Kiltera_.inputMM
        outputMM = UML2Kiltera_.outputMM
        full_transformation = UML2Kiltera_.full_transformation

    mpg = MutationPossibilityGenerator(os.path.expanduser(inputMM), os.path.expanduser(outputMM))

    rules, transformation = load_transformation(transformation_dir, full_transformation)

    do_only_generation = False

    if do_only_generation:
        posses = []
        for rule in rules.values():
            posses += mpg.generate_possibilities(rule, transformation)

        # group mutations by type
        muts_by_type = defaultdict(int)
        for p in posses:
            mut_type = p[0]
            muts_by_type[mut_type] += 1

        for t in sorted(muts_by_type):
            print(t + " : " + str(muts_by_type[t]))

        print("Number of possibilities: " + str(len(posses)))
    else:
        do_mutation_testing(mpg, rules, transformation, test_script, use_integration_contracts)
