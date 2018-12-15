from util.ecore_utils import EcoreUtils
from util.test_script_utils import load_transformation
from mutation.mutator import MutationOperators

class MutationPossibilityGenerator:





    def __init__(self, inputMM, outputMM):
        self.inMM = EcoreUtils(inputMM)
        self.outMM = EcoreUtils(outputMM)

        self.structural_classes = ["MatchModel", "ApplyModel", "paired_with",
                                                               "match_contains", "apply_contains"
                                   ]
        self.link_classes = ["directLink_S", "directLink_T", "backward_link"]

    def get_children(self, v):
        isInMatch = v["mm__"] in self.inMM.classes

        if isInMatch:
            return self.inMM.mmClassChildren
        else:
            return self.outMM.mmClassChildren

    def get_parents(self, v):
        isInMatch = v["mm__"] in self.inMM.classes

        if isInMatch:
            return self.inMM.mmClassParents
        else:
            return self.outMM.mmClassParents

    def generate_possibilities(self, rule):

        poss = []
        poss += self.element_replacement(rule)
        poss += self.element_deletion(rule)

        print("Possibilities for " + rule.name + ":")
        for p in poss:
            print(p)

        # raise Exception()

        return poss

    # REPLACE BY ANOTHER CLASS
    def element_replacement(self, rule):

        poss = []
        for i, v in enumerate(rule.vs):
            mm = v["mm__"]
            if mm in self.structural_classes or mm in self.link_classes:
                continue

            children = self.get_children(v)
            parents = self.get_parents(v)

            if mm in children:
                for child in children[mm]:
                    poss_tuple = (MutationOperators.RENAME_CLASS.name, i, child)
                    poss.append(poss_tuple)

            if mm in parents:
                for parent in parents[mm]:
                    poss_tuple = (MutationOperators.RENAME_CLASS.name, i, parent)
                    poss.append(poss_tuple)

        return poss

    # DELETE ELEMENT
    def element_deletion(self, rule):

        poss = []
        for i, v in enumerate(rule.vs):
            mm = v["mm__"]
            if mm in self.structural_classes:
                continue

            poss_tuple = (MutationOperators.DELETE_ELEMENT.name, i)
            poss.append(poss_tuple)

        return poss