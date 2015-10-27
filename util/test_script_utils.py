from core.himesis_utils import graph_to_dot
from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

def select_rules(full_transformation, num_rules):
    selected_transformation = []

    print("Selecting " + str(num_rules) + " rules")

    i = 1
    for layer in range(len(full_transformation)):
        selected_transformation.append([])
        for rule in full_transformation[layer]:
            selected_transformation[layer].append(rule)
            i += 1
            if i > num_rules:
                print("Returning: " + str(selected_transformation))
                return selected_transformation




def get_sub_and_super_classes(inputMM, outputMM):
    subclasses_dict = {}



    inMM = EcoreUtils(inputMM)
    subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(inMM.getMetamodelClassNames())

    inMMinheritanceTree = inMM.getSubClassInheritanceRelationForClasses()

    for className in inMMinheritanceTree:
        subclasses_dict["MT_pre__" + className] = buildPreListFromClassNames(inMMinheritanceTree[className])

    outMM = EcoreUtils(outputMM)
    subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(outMM.getMetamodelClassNames())

    outMMinheritanceTree = outMM.getSubClassInheritanceRelationForClasses()
    for className in outMMinheritanceTree:
        subclasses_dict["MT_pre__" + className] = buildPreListFromClassNames(outMMinheritanceTree[className])


    superclasses_dict = {}

    inMMinheritanceTree = inMM.getSuperClassInheritanceRelationForClasses()
    for super in inMMinheritanceTree:
        inMMinheritanceTree[super].append("MetaModelElement_S")

    outMMinheritanceTree = outMM.getSuperClassInheritanceRelationForClasses()
    for super in outMMinheritanceTree:
        outMMinheritanceTree[super].append("MetaModelElement_T")

    superclasses_dict.update(inMMinheritanceTree)
    superclasses_dict.update(outMMinheritanceTree)

    #remove duplicates
    for superclass in superclasses_dict.keys():
        superclasses_dict[superclass] = list(set(superclasses_dict[superclass]))


    #
    # print("\n\n")
    # print("Subclasses dict:")
    # for subclass in sorted(list(subclasses_dict.keys())):
    #     sub_list = [sub.replace("MT_pre__", "") for sub in subclasses_dict[subclass]]
    #     print(subclass.replace("MT_pre__", "") + " : " + str(sub_list))
    # print("\n")
    # print("Superclasses dict:")
    # for superclass in sorted(list(superclasses_dict.keys())):
    #     print(superclass + " : " + str(sorted(superclasses_dict[superclass])))
    # print("\n\n")


    return subclasses_dict, superclasses_dict