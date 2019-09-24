from util.ecore_utils import EcoreUtils
from util.test_script_utils import load_transformation
from mutation.mutator import MutationOperators
from collections import defaultdict
from copy import deepcopy


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

    def collect_nodes(self, rule, get_match_nodes):
        nodes = []

        if get_match_nodes:
            mm = self.inMM.classes
        else:
            mm = self.outMM.classes

        for node in rule.vs:

            #check metamodel first
            if node["mm__"] in mm:

                #check to see if mm in both match and apply
                containing_node = rule.neighbors(node, 2)[0]
                contain_mm = rule.vs[containing_node]["mm__"].lower()

                if get_match_nodes and "match" in contain_mm:
                    nodes.append(node)
                elif not get_match_nodes and "apply" in contain_mm:
                    nodes.append(node)
        return nodes

    def generate_possibilities(self, rule, transformation):

        #start with the baseline (no) mutation
        poss = self.NONE()
        poss += self.ADD_CLASS(rule)
        poss += self.ADD_ASSOC(rule)
        poss += self.ADD_BACK_LINK(rule, transformation)
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

    def NONE(self):
        return [(MutationOperators.NONE.name,)]

    def ADD_CLASS(self, rule):
        poss = []

        for m in self.inMM.classes:
            match_model_node = [i for i, node in enumerate(rule.vs) if node["mm__"] == "MatchModel"][0]

            # add the possibility
            poss_tuple = (MutationOperators.ADD_CLASS.name, m, True, match_model_node)
            poss.append(poss_tuple)

        for m in self.outMM.classes:
            apply_model_node = [i for i, node in enumerate(rule.vs) if node["mm__"] == "ApplyModel"][0]

            # add the possibility
            poss_tuple = (MutationOperators.ADD_CLASS.name, m, False, apply_model_node)
            poss.append(poss_tuple)

        return poss

    def gen_assocs(self, nodes, rels):
        poss_rels = []

        # get all possibilities of assocs between nodes
        for i, n1 in enumerate(nodes):
            for j, n2 in enumerate(nodes):
                n1_mm = n1["mm__"]
                n2_mm = n2["mm__"]

                # skip if there is no assoc in the metamodel
                if n1_mm not in rels:
                    continue

                # generate the possible assocs
                rels_to_choose = []
                for r in rels[n1_mm]:
                    if r[0] == n2_mm:
                        rels_to_choose.append(r)

                if not rels_to_choose:
                    continue

                # generate the concrete possiblities
                for rtc in rels_to_choose:
                    rel_tuple = (rtc[1], i, j)
                    poss_rels.append(rel_tuple)
        return poss_rels

    # does this assoc already exist in the graph?
    def does_rel_exist(self, rule, rel, src, trgt):
        from_src = []
        to_trgt = []

        # populate the list of nodes to/from the src and target
        for edge in rule.es:
            if edge.source == src:
                from_src.append(edge.target)
            if edge.target == trgt:
                to_trgt.append(edge.source)

        # do the intersection
        rels_between = list(set(from_src) & set(to_trgt))

        # see whether any assoc has this value already
        for r in rels_between:
            if rule.vs[r]["attr1"] == rel:
                return True

        return False

    def ADD_ASSOC(self, rule):

        poss = []

        # TODO: Assuming no conflicts
        rels = deepcopy(self.inMM.rels)
        rels.update(self.outMM.rels)

        # get the possible list of assocs
        assocs = self.gen_assocs(list(rule.vs), rels)
        for assoc in assocs:

            # skip ones that exist already
            if self.does_rel_exist(rule, assoc[0], assoc[1], assoc[2]):
                continue

            # check whether this is match or apply
            mm1 = rule.vs[assoc[1]]["mm__"]
            is_in_match = mm1 in self.inMM.classes

            poss_tuple = (MutationOperators.ADD_ASSOC.name, assoc[0], assoc[1], assoc[2], is_in_match)
            poss.append(poss_tuple)

        return poss

    def ADD_BACK_LINK(self, rule, transformation):

        # get the match and apply nodes
        match_nodes = self.collect_nodes(rule, True)
        apply_nodes = self.collect_nodes(rule, False)

        # print("Match nodes: " + str([n["mm__"] for n in match_nodes]))
        # print("Apply nodes: " + str([n["mm__"] for n in apply_nodes]))

        # generate all the combos
        combos = []
        for m in match_nodes:
            for a in apply_nodes:
                combo = [m, a, False]
                combos.append(combo)

        # collect all the past rules in the transformation
        past_rules = []
        for layer in transformation:
            names = [r.name for r in layer]
            if rule.name in names:
                break
            for r in layer:
                past_rules.append(r)

        # mark all those combos where the apply element
        # could have been created from the match elements
        for past_rule in past_rules:

            for i, combo in enumerate(combos):
                m, a, found = combo
                if found:
                    continue

                # TODO: Handle inheritance here
                if m["mm__"] in past_rule.vs["mm__"] and \
                        a["mm__"] in past_rule.vs["mm__"]:
                    combos[i][2] = True

        nodes = list(rule.vs)

        # collect existing backward links
        back_link_index = [nodes.index(n) for n in nodes if n["mm__"] == "backward_link"]
        back_links = defaultdict(dict)
        for bl in back_link_index:
            for edge in rule.es:
                if edge.source == bl:
                    back_links[bl]["trgt"] = edge.target
                if edge.target == bl:
                    back_links[bl]["src"] = edge.source

        poss = []
        for c in combos:
            # this apply element could have been created from
            # this match element
            if not c[2]:
                continue

            match_index = nodes.index(c[0])
            apply_index = nodes.index(c[1])

            # check if the backward link already exists
            exists = False
            for bl, val in back_links.items():
                if match_index == val['trgt'] and apply_index == val["src"]:
                    exists = True

            if not exists:
                # add the possibility
                poss_tuple = (MutationOperators.ADD_BACK_LINK.name, match_index, apply_index)
                poss.append(poss_tuple)

        return poss

    def ADD_EQUATION(self, rule):
        return []

    def DELETE_ELEMENT(self, rule):
        poss = []

        match_nodes = self.collect_nodes(rule, True)

        for i, v in enumerate(rule.vs):
            mm = v["mm__"]
            if mm in self.structural_classes:
                continue

            #do not remove the only match node
            if len(match_nodes) == 1:
                index = list(rule.vs).index(match_nodes[0])
                if i == index:
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
