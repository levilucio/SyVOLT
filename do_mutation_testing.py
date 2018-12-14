import subprocess
import datetime

from mutation.mutation_possibilities import MutationPossibilityGenerator
from util.test_script_utils import load_transformation

if __name__ == "__main__":
    print("Performing mutations...")

    transformation_dir = "./ExFamToPerson/"
    inputMM = transformation_dir + "Families_Extended.ecore"
    outputMM = transformation_dir + "Persons_Extended.ecore"

    mpg = MutationPossibilityGenerator(inputMM, outputMM)

    full_transformation = [
        # ['HCountry2Community'],
        ['HFather2Man'],
        # ['HMother2Woman'],
        # ['HDaughter2Woman'],
        # ['HSon2Man'],
        # ['HNeighborhood2District'],
        # ['HCity2TownHall', 'HCityCompany2Association'],
        #
        ['HcopersonsSolveRefCountryFamilyParentCommunityMan'],
        # ['HcopersonsSolveRefCountryFamilyParentCommunityWoman'],
        #
        # ['HcopersonsSolveRefCountryFamilyChildCommunityMan'],
        # ['HcopersonsSolveRefCountryFamilyChildCommunityWoman'],
        #
        # ['HcotownHallsSolveRefCountryCityCommunityTownHall',
        #  'HcoassociationsSolveRefCountryCityCompanyCommunityAssociation',
        #  'HacommitteeSolveRefCompanyCityAssociationCommittee'],
        # ['HtworkersSolveRefCompanyParentCityTownHallPerson'],
        # ['HtdistrictsSolveRefCityNeighborhoodTownHallDistrict'],
        # ['HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictOrdinaryFacilityPerson'],
        # ['HdfacilitiesSolveRefNeighborhoodSchoolServiceChildDistrictSpecialFacilityPerson']

    ]

    rules, transformation = load_transformation(transformation_dir + "transformation/", full_transformation)

    poss_dict = {}

    xml_filename = "mutation_testing.xml"
    in_xml_filename = "sba.xml"
    with open(xml_filename, "w") as f:

        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')

        f.write('<mutation_testing>\n')

        f.write('<header')
        f.write(' date="' + str(datetime.datetime.now()) + '">\n')
        for rule in rules.values():
            poss = mpg.generate_possibilities(rule)
            poss_dict[rule.name] = poss

            f.write('<mutation rule_name="' + rule.name + '" mutation="' + str(poss) + '"/>')

        f.write('</header>\n')

        for rule_name, poss_set in poss_dict.items():
            f.write('<mutation_set rule_name="' + rule_name + '">\n')

            print("Poss for rule: " + rule_name)
            for p in poss_set:
                print(p)

                f.write('<mutation operation="' + str(p) + '">\n')

                rule_cmd = "--rule_to_mutate=" + rule_name
                poss_cmd = "--mutate=" + str(p).replace(" ", "")
                cmd = ["python3", "test_atlTrans_extended.py", rule_cmd, poss_cmd]

                # subprocess.run(cmd)
                subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)


                # f.write(rule.name + "\n")
                # f.write(str(p) + "\n\n")
                with open(in_xml_filename) as g:
                    for line in g:
                        f.write(line)
                f.write('</mutation>\n')

            f.write('</mutation_set>\n')

        f.write('</mutation_testing>\n')
