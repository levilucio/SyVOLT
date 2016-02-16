
from itertools import permutations
from t_core.messages import Packet

class SubsumptionHandler:

    def __init__(self, rules):
        self.rules = rules

        self.loopingRuleSubsumption = []

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

        return ruleSubsumption