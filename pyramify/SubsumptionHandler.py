
from itertools import permutations
from t_core.messages import Packet
from core.himesis_plus import find_nodes_with_mm
import traceback

class SubsumptionHandler:

    def __init__(self, rules, transformation_layers):
        self.rules = rules
        self.transformation_layers = transformation_layers

        self.loopingRuleSubsumption = []
        self.ruleSubsumption = {}
        self.subsuming_rules = {}

        self.debug = False

    # return the layer a rule occurs in
    def layer_rule_occurs_in(self, rule):
        for layerIndex in range(len(self.transformation_layers)):
            for ruleIndex in range(len(self.transformation_layers[layerIndex])):
                if rule == self.transformation_layers[layerIndex][ruleIndex].name:
                    return layerIndex
        raise Exception("Rule: " + rule + " not found in transformation")

    # find all the rules that subsume a given rule
    def get_subsuming_rules(self, rule):
        foundParent = False
        subsuming_rules = []
        for ruleKey in sorted(self.ruleSubsumption.keys()):
            if rule in set(self.ruleSubsumption[ruleKey]):
                # check for loops when two rules subsume each other
                if rule not in set(subsuming_rules):
                    foundParent = True
                    subsuming_rules.append(ruleKey)
                    subsuming_rules.extend(self.get_subsuming_rules(ruleKey))
        if not foundParent:
            return []
        else:
            return subsuming_rules

    # calculate the partial order induced by rule match subsumption for all rules in the transformation.
    def calculate_rule_subsumption(self, matchRulePatterns):

        rulepairs = list(permutations(sorted(self.rules.keys()),2))

        # keep only the pairs which correspond to subsumption relations (second element subsumes the first)

        pairsToRemove = []

        for pair in rulepairs:
            p = Packet()
            p.graph = self.rules[pair[1]]
            p = matchRulePatterns[pair[0]][0].packet_in(p)

            if not matchRulePatterns[pair[0]][0].is_success:
                pairsToRemove.append(pair)

        rulepairs = [pair for pair in rulepairs if pair not in pairsToRemove]

        ruleChains = []
        ruleSubsumption = {}

        rulepairsCopy = list(rulepairs)
        rulesToRemove = []

        while len(rulepairsCopy) > 0:

            pair = rulepairsCopy.pop(0)

            if (pair[1],pair[0]) in rulepairsCopy:
                # found a loop

                # remove the reversed pair from the list of pairs
                rulepairsCopy.remove((pair[1],pair[0]))

                rulesToRemove.append(pair)
                rulesToRemove.append((pair[1],pair[0]))

                indexOfExistingChain = []

                for chainIndex in range(len(ruleChains)):
                    if pair[0] in ruleChains[chainIndex]:
                        # the new loop is part of a existing chains
                        indexOfExistingChain.append(chainIndex)
                    if pair[1] in ruleChains[chainIndex]:
                        # the new loop is part of a existing chains
                        indexOfExistingChain.append(chainIndex)


                if len(indexOfExistingChain) == 0:
                    #print "going to add to the list of chains"

                    # add the chain to list of chains and set the top and bottom elements
                    ruleChains.append([pair[1],pair[0]])
                    # add the new pair to the subsumption relation
                    ruleSubsumption[pair[1]] = [pair[0]]
                else:
                    # gets merged with existing chain(s)
                    if len(indexOfExistingChain) == 1:
                        #print "going to add to one chain: " + str(pair)
                        # extends one chain
                        # push the new rule to the bottom of the chain
                        newElement = list(set([pair[0],pair[1]]) - set(ruleChains[indexOfExistingChain[0]]))[0]
                        # add the new rule at the end of the existing chain in the subsumption relation
                        ruleSubsumption[ruleChains[indexOfExistingChain[0]][len(ruleChains[indexOfExistingChain[0]])-1]] = [newElement]
                        ruleChains[indexOfExistingChain[0]].append(newElement)

                    elif len(indexOfExistingChain) == 2:
                        if len(indexOfExistingChain) == 2 and indexOfExistingChain[0] == indexOfExistingChain[1]:
                            pass
                            #print "discarding link"
                        else:
                            #print "going to merge two chains"
                            # merges two existing chains
                            chain1 = list(ruleChains[indexOfExistingChain[0]])
                            chain2 = list(ruleChains[indexOfExistingChain[1]])
                            ruleChains.append(chain1.extend(chain2))
                            # add connect the end of one chain to the beginning of the other
                            lastElementOfFirstChain = chain1[len(chain1)-1]
                            firstElementOfSecondChain = chain2[0]
                            ruleSubsumption[lastElementOfFirstChain] = firstElementOfSecondChain
                            del ruleChains[indexOfExistingChain[0]]
                            del ruleChains[indexOfExistingChain[1]]

            # store the information about rules having looping subsumption relations
            self.loopingRuleSubsumption = list(ruleChains)

        remainingRulepairs = [rule for rule in rulepairs if rule not in rulesToRemove]

        # now add all the remaining subsumption relations (not loops) to the ruleSubsumption dictionary

        for pair in remainingRulepairs:
#             print "---------------------------------------"
#             print "Pair: " + str(pair)
            canAdd = True
            # check if the subsuming rule is part of a chain and not the last element of the chain
            # only last elements of chains can have children
            for ruleChain in ruleChains:
                if pair[1] in ruleChain and pair[1] != ruleChain[len(ruleChain)-1]:
#                    print "not the last element of the chain"
                    canAdd = False
                    break
            # check if the subsumed rule is part of a chain and not the first of the chain
            # only first elements of chains can have parents
            for ruleChain in ruleChains:
                if pair[0] in ruleChain and pair[0] != ruleChain[0]:
#                    print "not the first element of the chain"
                    canAdd = False
                    break

            if canAdd:
                if pair[1] in ruleSubsumption.keys():
                    ruleSubsumption[pair[1]].append(pair[0])
                else:
                    ruleSubsumption[pair[1]] = [pair[0]]

        self.ruleSubsumption = ruleSubsumption

        self.subsuming_rules = {}
        for rule in sorted(self.rules.keys()):
            self.subsuming_rules[rule] = self.get_subsuming_rules(rule)

        if self.debug:
            #print("Rule subsumption: " + str(ruleSubsumption))
            print("Subsuming Rules:")
            for rule in sorted(self.subsuming_rules.keys()):
                print(rule + " : " + str(self.subsuming_rules[rule]))
        return ruleSubsumption, self.subsuming_rules

    # Calculate if the rules need special treatment because they overlap.
    # This happens when:
    # - Rule A is subsumed by Rule B, rule A has no backward links and Rule B appears in the same layer as rule A, or in a layer before
    # - Rule A is subsumed by rule B and both rule A and rule B have backward links and Rule A appears in the same layer as rule B
    # returns a list of pairs of rules for which combinators need to be built for
    def get_rules_needing_overlap_treatment(self, has_backward_links):
        rules_needing_overlap_treatment = {}
        for rule in sorted(self.rules.keys()):
            subsuming_rules = self.get_subsuming_rules(rule)

            rule_has_bl = has_backward_links[rule]

            for s_rule in subsuming_rules:
                s_rule_has_bl = has_backward_links[s_rule]

                #                 print("---------------------------------")
                #                 print("Rule: " + str(rule))
                # #                 print "Has backward links: " + str(rule_has_bl)
                # #                 print "Position: " + str(self.layer_rule_occurs_in(rule))
                #                 print("Subsuming Rule: " + str(s_rule))
                # #                 print "Has backward links: " + str(s_rule_has_bl)
                # #                 print "Position: " + str(self.layer_rule_occurs_in(s_rule))
                #                 print("---------------------------------")

                try:
                    if (not rule_has_bl and not s_rule_has_bl) or \
                            (not rule_has_bl and s_rule_has_bl):
                        if self.layer_rule_occurs_in(rule) >= self.layer_rule_occurs_in(s_rule):
                            if rule in rules_needing_overlap_treatment.keys():
                                rules_needing_overlap_treatment[rule].append(s_rule)
                            else:
                                rules_needing_overlap_treatment[rule] = [s_rule]

                    elif rule_has_bl and s_rule_has_bl:
                        if self.layer_rule_occurs_in(rule) == self.layer_rule_occurs_in(s_rule):
                            if rule in rules_needing_overlap_treatment.keys():
                                rules_needing_overlap_treatment[rule].append(s_rule)
                            else:
                                rules_needing_overlap_treatment[rule] = [s_rule]
                except Exception:
                    print("ERROR in rules_needing_overlap_treatment()")
                    tb = traceback.format_exc()
                    print(tb)

        return rules_needing_overlap_treatment




    def remove_subsumption_between_rules(self, ruleSubsumption, has_backward_links):
        # remove from the subsumption relation subsumption between a rule in a layer and a rule in a layer appearing before
        # TODO: this should be replaced by layer ordering to avoid tests all the time during PC construction
        try:
            for rule in sorted(ruleSubsumption.keys()):
                rulesToDelete = []
                for subsumedRule in ruleSubsumption[rule]:
                    if self.layer_rule_occurs_in(rule) > self.layer_rule_occurs_in(subsumedRule) or \
                            (self.layer_rule_occurs_in(rule) < self.layer_rule_occurs_in(subsumedRule) and
                                 has_backward_links[rule] and has_backward_links[subsumedRule]):
                        rulesToDelete.append(subsumedRule)
                ruleSubsumption[rule] = [r for r in ruleSubsumption[rule] if r not in rulesToDelete]
            # now remove empty dictionary entries
            ruleSubsumption = dict((k, v) for k, v in ruleSubsumption.items() if v)

            print("Subsumption")
            print(ruleSubsumption)

            self.ruleSubsumption = ruleSubsumption

            return ruleSubsumption
        except Exception as e:
            print(e)
            raise Exception("Error in subsuming rules")

    # # remove loops in the subsumption relation by defining only one subsumption direction between rules that subsume each other.
    #     # remove all upward subsumption relations for any but the top rule in the rules that subsume each other.
    #     # remove all downward subsumption relations for any but the bottom rule in the rules that subsume each other.
    #def removeLoops(self):


    def cleanLoopingRuleSubsumption(self):
        # remove from loopingRuleSubsumption relation rules that completeley overlap but belong to different layers, as they
        # will be treated by the total combinators. If rules belonging to more than one layer exist keep them only if two or
        # more belong to the same layer, otherwise discard

        newLoopingRuleSubsumption = []

        for loopingRules in self.loopingRuleSubsumption:
            loopDict = {}
            for rule in loopingRules:
                rule_layer = self.layer_rule_occurs_in(rule)
                if rule_layer not in loopDict:
                    loopDict[rule_layer] = [rule]
                else:
                    loopDict[rule_layer].append(rule)

            # keep entries that only have more than one rule
            for layer in loopDict.keys():
                if len(loopDict[layer]) > 1:
                    newLoopingRuleSubsumption.append(loopDict[layer])

        self.loopingRuleSubsumption = newLoopingRuleSubsumption

        return self.loopingRuleSubsumption
