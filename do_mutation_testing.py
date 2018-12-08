import subprocess

from mutation.mutation_possibilities import MutationPossibilityGenerator
from util.test_script_utils import load_transformation

if __name__ == "__main__":
    print("Hello!")

    transformation_dir = "./ExFamToPerson/"
    inputMM = transformation_dir + "Families_Extended.ecore"
    outputMM = transformation_dir + "Persons_Extended.ecore"

    mpg = MutationPossibilityGenerator(inputMM, outputMM)


    full_transformation = [["HFather2Man"]]

    rules, transformation = load_transformation(transformation_dir + "transformation/", full_transformation)

    rule = list(rules.values())[0]
    poss = mpg.generate_possibilities(rule)


    with open("mutation_testing.txt", "w") as f:

        print("Poss for rule: " + rule.name)
        for p in poss:
            print(p)

            rule_cmd = "--rule_to_mutate=" + rule.name
            poss_cmd = "--mutate=" + str(p).replace(" ", "")
            cmd = ["python3", "test_atlTrans_extended.py", rule_cmd, poss_cmd]
            subprocess.run(cmd)

            f.write("\n\n#############################\n")
            f.write(rule.name + "\n")
            f.write(str(p) + "\n\n")
            with open("sba.txt") as g:
                for line in g:
                    f.write(line)