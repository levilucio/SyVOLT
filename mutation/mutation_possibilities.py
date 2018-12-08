from util.ecore_utils import EcoreUtils
from util.test_script_utils import load_transformation
from mutation.mutator import MutationOperators

class MutationPossibilityGenerator:





    def __init__(self, inputMM, outputMM):
        self.inMM = EcoreUtils(inputMM)
        self.outMM = EcoreUtils(outputMM)

        self.structural_classes = ["MatchModel", "ApplyModel", "paired_with",
                                                               "match_contains", "apply_contains",
                                   "directLink_S", "directLink_T"]

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
        for i, v in enumerate(rule.vs):
            mm = v["mm__"]
            if mm in self.structural_classes:
                continue

            #REPLACE BY ANOTHER CLASS
            children = self.get_children(v)
            parents = self.get_parents(v)

            if mm in children:
                for child in children[mm]:
                    poss_tuple = (i, MutationOperators.RENAME_CLASS, child)
                    poss.append(poss_tuple)

            if mm in parents:
                for parent in parents[mm]:
                    poss_tuple = (i, MutationOperators.RENAME_CLASS, parent)
                    poss.append(poss_tuple)

        return poss