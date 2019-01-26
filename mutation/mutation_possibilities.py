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
        poss += self.ADD_CLASS(rule)
        poss += self.ADD_ASSOC(rule)
        poss += self.ADD_BACK_LINK(rule)
        poss += self.ADD_EQUATION(rule)

        poss += self.DELETE_ELEMENT(rule)
        poss += self.DELETE_EQUATION(rule)

        poss += self.RENAME_CLASS(rule)
        poss += self.RENAME_ASSOC(rule)

        poss += self.MODIFY_EQUATION(rule)

        print("Possibilities for " + rule.name + ":")
        for p in poss:
            print(p)

        # raise Exception()

        return poss

    def ADD_CLASS(self, rule):
        return []

    def ADD_ASSOC(self, rule):
        return []

    def ADD_BACK_LINK(self, rule):
        return []

    def ADD_EQUATION(self, rule):
        return []

    def DELETE_ELEMENT(self, rule):
        poss = []
        for i, v in enumerate(rule.vs):
            mm = v["mm__"]
            if mm in self.structural_classes:
                continue

            poss_tuple = (MutationOperators.DELETE_ELEMENT.name, i)
            poss.append(poss_tuple)

        return poss

    # REPLACE BY ANOTHER CLASS (PARENT OR CHILD)
    def RENAME_CLASS(self, rule):
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

    def RENAME_ASSOC(self, rule):
        poss = []
        for i, v in enumerate(rule.vs):
            mm = v["mm__"]

            if mm not in ["directLink_S", "directLink_T"]:
                continue

            options = []
            rels = None
            if mm == "directLink_S":
                rels = self.inMM.rels
            else:
                rels = self.outMM.rels

            for key, value in rels.items():

                # only consider replacements where the assoc name appears
                # for example, replace Family->fathers->Parent with Family->daughters->Child
                found_assoc = False
                for val in value:
                    assoc_name = val[1]
                    if assoc_name == v["attr1"]:
                        found_assoc = True

                if not found_assoc:
                    continue

                for val in value:
                    assoc_name = val[1]

                    # don't rename this assoc
                    if assoc_name != v["attr1"]:
                        poss_tuple = (MutationOperators.RENAME_ASSOC.name, i, assoc_name)
                        poss.append(poss_tuple)

        return poss

    def DELETE_EQUATION(self, rule):
        poss = []
        for i, _ in enumerate(rule["equations"]):
            poss_tuple = (MutationOperators.DELETE_EQUATION.name, i)
            poss.append(poss_tuple)
        return poss

    # MODIFY EQUATION
    # IMPLEMENTED:
    # - REPLACE CONCAT WITH EACH PIECE
    # - REPLACE REF WITH ANOTHER REF FROM SAME CLASS OR PARENT

    def MODIFY_EQUATION(self, rule):
        poss = []

        # print(rule["equations"])

        for i, eq in enumerate(rule["equations"]):

            head, tail = eq

            new_head_poss = self.get_eq_poss(head, rule, is_match=False)
            new_tail_poss = self.get_eq_poss(tail, rule)

            # print("Head poss:")
            # for p in new_head_poss:
            #     print(p)
            #
            # print("Tail poss:")
            # for p in new_tail_poss:
            #     print(p)

            for new_head in [head] + new_head_poss:
                for new_tail in [tail] + new_tail_poss:

                    if new_head == head and new_tail == tail:
                        continue

                    new_eq = (new_head, new_tail)
                    poss_tuple = (MutationOperators.MODIFY_EQUATION.name, i, new_eq)
                    poss.append(poss_tuple)

        return poss

    def get_eq_poss(self, ref, rule, is_match=True):
        # print("Ref: " + str(ref))

        poss = []

        # Replace the concat with one of the two sides
        if ref[0] == 'concat':
            concat_args = ref[1]
            poss.append(concat_args[0])
            poss.append(concat_args[1])

            switch = ('concat', (concat_args[1], concat_args[0]))
            poss.append(switch)

            first_poss = self.get_eq_poss(concat_args[0], rule, is_match=True)
            second_poss = self.get_eq_poss(concat_args[1], rule, is_match=True)

            for p in first_poss:
                new_p = ('concat', (p, concat_args[1]))
                poss.append(new_p)

            for p in second_poss:
                new_p = ('concat', (concat_args[0], p))
                poss.append(new_p)
            return poss

        if is_match:
            attribs = self.inMM.attribs
        else:
            attribs = self.outMM.attribs

        # replace ref with another ref from same class or parent class
        for i, node in enumerate(rule.vs):

            mm = node["mm__"]

            if is_match and mm not in self.inMM.classes:
                continue

            if not is_match and mm not in self.outMM.classes:
                continue

            parents = self.get_parents(node)
            cl = [mm] + parents[mm]
            for c in cl:

                if c not in attribs:
                    continue

                for attrib in attribs[c]:

                    if i == ref[0] and attrib == ref[1]:
                        continue

                    new_ref = (i, attrib)
                    poss.append(new_ref)
        return poss
