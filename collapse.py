'''
Created on 2013-02-04
'''

import pydot
from itertools import combinations
import time

from t_core.tc_python.arule import ARule
from t_core.tc_python.frule import FRule

from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator
from t_core.rollbacker import Rollbacker


from himesis_utils import disjoint_model_union
from himesis_utils import print_graph
from himesis_utils import graph_to_dot

# collapse elements from match and apply model

from GM2AUTOSAR_MM.collapse_rules.Himesis.HStripMatchModelLHS import HStripMatchModelLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HStripMatchModelRHS import HStripMatchModelRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HStripApplyModelLHS import HStripApplyModelLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HStripApplyModelRHS import HStripApplyModelRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HStripRemoveMatchApplyModelsLHS import HStripRemoveMatchApplyModelsLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HStripRemoveMatchApplyModelsRHS import HStripRemoveMatchApplyModelsRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HFindTwoMatchElementsSameTypeDiffRulesLHS import HFindTwoMatchElementsSameTypeDiffRulesLHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HFindTwoApplyElementsWithBackwardLHS import HFindTwoApplyElementsWithBackwardLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HFindTwoApplyElementsWithBackwardRHS import HFindTwoApplyElementsWithBackwardRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMergeCardinalitiesMatchDiffRulesLHS import HMergeCardinalitiesMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMergeCardinalitiesMatchDiffRulesRHS import HMergeCardinalitiesMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputDirectMatchDiffRulesLHS import HMoveOneInputDirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputDirectMatchDiffRulesRHS import HMoveOneInputDirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputRepeatedDirectMatchDiffRulesLHS import HMoveOneInputRepeatedDirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputRepeatedDirectMatchDiffRulesRHS import HMoveOneInputRepeatedDirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputIndirectMatchDiffRulesLHS import HMoveOneInputIndirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputIndirectMatchDiffRulesRHS import HMoveOneInputIndirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputRepeatedIndirectMatchDiffRulesLHS import HMoveOneInputRepeatedIndirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputRepeatedIndirectMatchDiffRulesRHS import HMoveOneInputRepeatedIndirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputDirectMatchDiffRulesLHS import HMoveOneOutputDirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputDirectMatchDiffRulesRHS import HMoveOneOutputDirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputRepeatedDirectMatchDiffRulesLHS import HMoveOneOutputRepeatedDirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputRepeatedDirectMatchDiffRulesRHS import HMoveOneOutputRepeatedDirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputIndirectMatchDiffRulesLHS import HMoveOneOutputIndirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputIndirectMatchDiffRulesRHS import HMoveOneOutputIndirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputRepeatedIndirectMatchDiffRulesLHS import HMoveOneOutputRepeatedIndirectMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputRepeatedIndirectMatchDiffRulesRHS import HMoveOneOutputRepeatedIndirectMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputDirectApplyDiffRulesLHS import HMoveOneInputDirectApplyDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputDirectApplyDiffRulesRHS import HMoveOneInputDirectApplyDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputRepeatedDirectApplyDiffRulesLHS import HMoveOneInputRepeatedDirectApplyDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneInputRepeatedDirectApplyDiffRulesRHS import HMoveOneInputRepeatedDirectApplyDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputDirectApplyDiffRulesLHS import HMoveOneOutputDirectApplyDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputDirectApplyDiffRulesRHS import HMoveOneOutputDirectApplyDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputRepeatedDirectApplyDiffRulesLHS import HMoveOneOutputRepeatedDirectApplyDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneOutputRepeatedDirectApplyDiffRulesRHS import HMoveOneOutputRepeatedDirectApplyDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneBackwardLinkDiffRulesLHS import HMoveOneBackwardLinkDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HMoveOneBackwardLinkDiffRulesRHS import HMoveOneBackwardLinkDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HDeleteUncollapsedElementMatchDiffRulesLHS import HDeleteUncollapsedElementMatchDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HDeleteUncollapsedElementMatchDiffRulesRHS import HDeleteUncollapsedElementMatchDiffRulesRHS

from GM2AUTOSAR_MM.collapse_rules.Himesis.HDeleteUncollapsedElementApplyDiffRulesLHS import HDeleteUncollapsedElementApplyDiffRulesLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HDeleteUncollapsedElementApplyDiffRulesRHS import HDeleteUncollapsedElementApplyDiffRulesRHS

# eliminate repeated matchmodels and applymodels after two rules collapsed

from GM2AUTOSAR_MM.collapse_rules.Himesis.HReconnectMatchElementsLHS import HReconnectMatchElementsLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HReconnectMatchElementsRHS import HReconnectMatchElementsRHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HReconnectApplyElementsLHS import HReconnectApplyElementsLHS
from GM2AUTOSAR_MM.collapse_rules.Himesis.HReconnectApplyElementsRHS import HReconnectApplyElementsRHS

from copy import deepcopy


# declare all the needed TCore rules

strip_matchmodel = FRule(HStripMatchModelLHS(), HStripMatchModelRHS())
strip_applymodel = FRule(HStripApplyModelLHS(), HStripApplyModelRHS())

strip_match_applymodels = ARule(HStripRemoveMatchApplyModelsLHS(), HStripRemoveMatchApplyModelsRHS())

find_elements_collapse_match = Matcher(HFindTwoMatchElementsSameTypeDiffRulesLHS())       

find_elements_collapse_apply = Matcher(HFindTwoApplyElementsWithBackwardLHS())

merge_cardinalities_matchmodel = ARule(HMergeCardinalitiesMatchDiffRulesLHS(), HMergeCardinalitiesMatchDiffRulesRHS())

move_input_direct_matchmodel = FRule(HMoveOneInputDirectMatchDiffRulesLHS(), HMoveOneInputDirectMatchDiffRulesRHS())
move_input_repeated_direct_matchmodel = FRule(HMoveOneInputRepeatedDirectMatchDiffRulesLHS(), HMoveOneInputRepeatedDirectMatchDiffRulesRHS())
move_output_direct_matchmodel = FRule(HMoveOneOutputDirectMatchDiffRulesLHS(), HMoveOneOutputDirectMatchDiffRulesRHS())
move_output_repeated_direct_matchmodel = FRule(HMoveOneOutputRepeatedDirectMatchDiffRulesLHS(), HMoveOneOutputRepeatedDirectMatchDiffRulesRHS())

move_input_indirect_matchmodel = FRule(HMoveOneInputIndirectMatchDiffRulesLHS(), HMoveOneInputIndirectMatchDiffRulesRHS())
move_input_repeated_indirect_matchmodel = FRule(HMoveOneInputRepeatedIndirectMatchDiffRulesLHS(), HMoveOneInputRepeatedIndirectMatchDiffRulesRHS())
move_output_indirect_matchmodel = FRule(HMoveOneOutputIndirectMatchDiffRulesLHS(), HMoveOneOutputIndirectMatchDiffRulesRHS())
move_output_repeated_indirect_matchmodel = FRule(HMoveOneOutputRepeatedIndirectMatchDiffRulesLHS(), HMoveOneOutputRepeatedIndirectMatchDiffRulesRHS())

move_input_direct_applymodel = FRule(HMoveOneInputDirectApplyDiffRulesLHS(), HMoveOneInputDirectApplyDiffRulesRHS())
move_input_repeated_direct_applymodel = FRule(HMoveOneInputRepeatedDirectApplyDiffRulesLHS(), HMoveOneInputRepeatedDirectApplyDiffRulesRHS())
move_output_direct_applymodel = FRule(HMoveOneOutputDirectApplyDiffRulesLHS(), HMoveOneOutputDirectApplyDiffRulesRHS())
move_output_repeated_direct_applymodel = FRule(HMoveOneOutputRepeatedDirectApplyDiffRulesLHS(), HMoveOneOutputRepeatedDirectApplyDiffRulesRHS())

move_backwardlink = FRule(HMoveOneBackwardLinkDiffRulesLHS(), HMoveOneBackwardLinkDiffRulesRHS())

delete_uncollapsed_element_match = FRule(HDeleteUncollapsedElementMatchDiffRulesLHS(), HDeleteUncollapsedElementMatchDiffRulesRHS())
delete_uncollapsed_element_apply = FRule(HDeleteUncollapsedElementApplyDiffRulesLHS(), HDeleteUncollapsedElementApplyDiffRulesRHS())
delete_uncollapsed_element_backward = Rewriter(HFindTwoApplyElementsWithBackwardRHS())

reconnect_match_elements_merge = FRule(HReconnectMatchElementsLHS(), HReconnectMatchElementsRHS())
reconnect_apply_elements_merge = FRule(HReconnectApplyElementsLHS(), HReconnectApplyElementsRHS())


class CollapseFactory():
    
    def __init__(self, verbosity):
        # dictionary cache to keep the results from performing collapses on multiple rules
        # the dictionary key is the concatenated names of the rules.
        # order does not matter in the application of DSLTrans rules
        # but in the dictionary keys rules should always be ordered in the same way to avoid duplications
        self.ruleCollapseCache = {}
        self.verbosity = verbosity


    def _collapse_two_rules(self, rule1, rule2):
        '''
        Collapse two rules by merging elements of the same type
        1) merge the elements of the match part of the rules and copy all connections from the second element to the first
        2) if two elements merged on the apply are connected to the same element on the source by backward links, merge them too
        The cardinalities of the two elements are merged using a simple cardinality algebra: 1 and + = +; 1 and 1 = 1; + and + = +
        
        TODO: produce multiple results when one element of the first rule can be merged with more one element of the second rule
        right now if this is attempted the result will be wrong  
        
        '''
        
        # start by stripping the second rule from the match and the apply links
        pRule2 = Packet()
        pRule2.graph = deepcopy(rule2)

        pRule2 = strip_matchmodel.packet_in(pRule2)
        pRule2 = strip_applymodel.packet_in(pRule2)
        pRule2 = strip_match_applymodels.packet_in(pRule2)
        
        #build merged graph with the two rules
        p = Packet()
        p.graph = deepcopy(rule1)
        
        p.graph = disjoint_model_union(p.graph, pRule2.graph)
        
        i = Iterator()
        r = Rollbacker(HFindTwoMatchElementsSameTypeDiffRulesLHS())

        p = find_elements_collapse_match.packet_in(p)               
        if self.verbosity >= 2: print 'Found collapsable elements:' + str(find_elements_collapse_match.is_success)
        
        if find_elements_collapse_match.is_success:            
            
            p = i.packet_in(p)
            p = r.packet_in(p)
    
            while True:
                
                print p
                print '---------------------------------------------------'
                
                p = merge_cardinalities_matchmodel.packet_in(p)
                if self.verbosity >= 2: print 'merge_cardinalities_matchmodel:' + str( merge_cardinalities_matchmodel.is_success) 
                        
                p = move_input_repeated_direct_matchmodel.packet_in(p)
                if self.verbosity >= 2: print 'move_input_repeated_direct_matchmodel:' + str(move_input_repeated_direct_matchmodel.is_success)  
                if not move_input_repeated_direct_matchmodel.is_success:
                    p = move_input_direct_matchmodel.packet_in(p) 
                    if self.verbosity >= 2: print 'move_input_direct_matchmodel:' + str(move_input_direct_matchmodel.is_success) 
                      
                p = move_output_repeated_direct_matchmodel.packet_in(p)
                if self.verbosity >= 2: print 'move_output_repeated_direct_matchmodel:' + str(move_output_repeated_direct_matchmodel.is_success)
                if not move_output_repeated_direct_matchmodel.is_success:
                    p = move_output_direct_matchmodel.packet_in(p) 
                    if self.verbosity >= 2: print 'move_output_direct_matchmodel:' + str(move_output_direct_matchmodel.is_success)                
                
                p = move_input_repeated_indirect_matchmodel.packet_in(p) 
                if self.verbosity >= 2: print 'move_input_repeated_indirect_matchmodel:' + str(move_input_repeated_indirect_matchmodel.is_success)  
                if not move_input_repeated_indirect_matchmodel.is_success:
                    p = move_input_indirect_matchmodel.packet_in(p) 
                    if self.verbosity >= 2: print 'move_input_indirect_matchmodel:' + str(move_input_indirect_matchmodel.is_success)
                
                p = move_output_repeated_indirect_matchmodel.packet_in(p)
                if self.verbosity >= 2: print 'move_output_repeated_indirect_matchmodel:' + str(move_output_repeated_indirect_matchmodel.is_success)
                if not move_output_repeated_indirect_matchmodel.is_success:                       
                    p = move_output_indirect_matchmodel.packet_in(p)
                    if self.verbosity >= 2: print 'move_output_indirect_matchmodel:' + str(move_output_indirect_matchmodel.is_success)
                
                p = move_backwardlink.packet_in(p)
                if self.verbosity >= 2: print 'move_backwardlink:' + str(move_backwardlink.is_success)
                  
                p = delete_uncollapsed_element_match.packet_in(p)
                if self.verbosity >= 2: print 'delete_uncollapsed_element_match:' + str(delete_uncollapsed_element_match.is_success) 
                
                p.clear_state()

                # merge apply elements linked to backward links if they have the same type
                # cardinality resolution for the applymodel is done in this rule
                p = find_elements_collapse_apply.packet_in(p)
                if self.verbosity >= 2: print 'Found collapsable apply elements:' + str(find_elements_collapse_apply.is_success)
                        
                i2 = Iterator()
                p = i2.packet_in(p)       
                            
                if find_elements_collapse_apply.is_success:
 
                # collapse all pairs of apply instances of the same type from different rules
                # which are backward linked to the match instance that was collapsed previously
                    while i2.is_success:

                        p = move_input_repeated_direct_applymodel.packet_in(p)
                        if self.verbosity >= 2: print 'move_input_repeated_direct_applymodel:' + str(move_input_repeated_direct_applymodel.is_success)
                        if not move_input_repeated_direct_applymodel.is_success:
                            p = move_input_direct_applymodel.packet_in(p)
                            if self.verbosity >= 2: print 'move_input_direct_applymodel:' + str(move_input_direct_applymodel.is_success) 

                        p = move_output_repeated_direct_applymodel.packet_in(p)
                        if self.verbosity >= 2: print 'move_output_repeated_direct_applymodel:' + str(move_output_repeated_direct_applymodel.is_success) 
                        if not move_output_repeated_direct_applymodel.is_success:   
                            p = move_output_direct_applymodel.packet_in(p)
                            if self.verbosity >= 2: print 'move_output_direct_applymodel:' + str(move_output_direct_applymodel.is_success) 

                        p = delete_uncollapsed_element_backward.packet_in(p)
                        if self.verbosity >= 2: print 'delete_uncollapsed_element_backward:' + str(delete_uncollapsed_element_backward.is_success)
                        p = delete_uncollapsed_element_apply.packet_in(p)                                
                        if self.verbosity >= 2: print 'delete_uncollapsed_element_apply:' + str(delete_uncollapsed_element_apply.is_success)
                        i2.next_in(p)                       

                # restore the original packet where the elements were found and copy the result
                # of the previous collapse into it such that the match set can be reused
                
                # start by creating a copy of the packet collapsed in the previous round
                previousGraph = deepcopy(p.graph)
                p = r.next_in(p)
                # iterate to the next two elements to collapse
                p = i.next_in(p)
 
                # if no more elements can be collapsed
                if not i.is_success:
                    
                    # reconnect disconnected elements from the second rule                 
                    p = reconnect_match_elements_merge.packet_in(p)
                    if self.verbosity >= 2: print 'reconnect_match_elements_merge:' + str(reconnect_match_elements_merge.is_success)
                    p = reconnect_apply_elements_merge.packet_in(p)
                    if self.verbosity >= 2: print 'reconnect_apply_elements_merge:' + str(reconnect_apply_elements_merge.is_success)
                    
                    return p.graph
                
                # if there are more elements to be collapsed copy the packet collapsed
                # in the previous round to the packet holding the match set to continue collapsing                
                p.graph = previousGraph
                
                              
        else:   
            return []
    

    
    def collapse(self, state):
        '''
        build all the states resulting from collapsing elements of rules
        combinations of rules 2-by-2, 3-by-3, ..., n-by-n are built incrementally
        the results of collapsing a combination are put into a cache to avoid multiplying the same collapse operation
        '''
        
#        print '        Called collapse...'
        
        collapsedResults = []
        previousCombKeys = None

        # build all combinations of rules in the state 2-by-2 through n-by-n
        for n in range(2,len(state)+1):
#        for n in range(2,3):
            ruleCombinations = combinations(state, n)
        
            # build the cache keys to look for
            combKeys = self._build_rule_combination_cache_keys(ruleCombinations)
 
            # go through all combinations n-by-n
            for key in combKeys:
#                print '---------------------------------------'
#                print key
#                print '------'
                
                found = False
                
                # check whether the combination already exists in the cache
                if key[0] not in self.ruleCollapseCache.keys():
                    
                    # assume nothing was found and the combination produces no collapse results
                    # the second argument in the pair is a flag stating whether the collapse results should be used or not for state building
                    # they may not be used if there was no additional collapse possibilities introduced by adding a rule to a smaller combination
                    self.ruleCollapseCache[key[0]] = [[],False]
                    
                    # if combinations of a smaller n have been produced, look for a result that can be used to build the current combination
                    if previousCombKeys != None:
                        for smallerCombKey in previousCombKeys:
                            if self.ruleCollapseCache[smallerCombKey[0]][0] != []:                            
                                # find the intersection between the set of keys we are looking for and the ones in a previous combination
                                remainingRule = set(key[1])-set(smallerCombKey[1])
                                if len(remainingRule) == 1:
#                                    print 'Found: ' + smallerCombKey[0]
                                    mergedCombinations = []
                                    # collapse the results from the smaller combination with the remaining rule 
                                    
                                    # print self.ruleCollapseCache[smallerCombKey[0]]
                                                              
                                    for smallerCollapseResult in self.ruleCollapseCache[smallerCombKey[0]][0]:
                                        remRule,=remainingRule
                                        mergedComb = self._merge_rules([smallerCollapseResult,remRule])
                                        collapseResult = self._collapse_two_rules(mergedComb)
                                        # if the result of the collapse was not empty, then the result can be used in the production of states
                                        if collapseResult != []:
                                            self.ruleCollapseCache[key[0]][0].extend(collapseResult)
                                            self.ruleCollapseCache[key[0]][1] = True
                                        
                                        mergedCombinations.append(mergedComb)
                                   
                                    # in case nothing reusable was found we keep the (non collapsed) merge combinations with the additional rule     
                                    if self.ruleCollapseCache[key[0]][1] == False:
                                        self.ruleCollapseCache[key[0]][0] = mergedCombinations

                                    break

                            
                    else:
                        # no cache result was found, just place the result of collapsing the rule combination in the cache
                        self.ruleCollapseCache[key[0]][0] = (self._collapse_two_rules(key[1][0],key[1][1]))
                        if self.ruleCollapseCache[key[0]][0] != []:
                            self.ruleCollapseCache[key[0]][1] = True
                else:
                    if self.verbosity >= 2: print '          Cache Hit!!!'
   
                # if some collapsed results were found for this key
                if self.ruleCollapseCache[key[0]][1]:
#                    print 'found something......'
                    remainingElements = list(set(state) - set(key[1]))
                    # collect collapsed combination results for this key and merged them with remaining rules
                    for collapsedComb in self.ruleCollapseCache[key[0]][0]:
                        l = [collapsedComb]
                        l.extend(remainingElements)
                        collapsedResults.append(self._merge_rules(l))
                
 #               print self.ruleCollapseCache[key[0]]        
 #               print '---------------------------------------'
            
            # keep a list of all combinations from the previous layer
            # for the current combination of size n, use set subtraction to find the results of collapsing combinations of n-1 elements
            previousCombKeys = combKeys

                   
        return collapsedResults
        

        
            
    def _merge_rules(self, rules):
        '''
        given a list of rules, returns the rule containing their merged result
        '''
        
        mergedRules = deepcopy(rules[0])
        rule_index = 1
        # go through all the rules and merge them in one graph
        while rule_index < len(rules):
            mergedRules = disjoint_model_union(mergedRules, rules[rule_index])
            rule_index += 1

        return mergedRules

    
    def _build_rule_combination_cache_keys(self, ruleCombinations):
        '''
        given a list of rule combinations, return a list with each element being the
        concatenations of the names in each individual concatenation, the rules that lead to that combination
        and a flag allowing or not the combination to be used in the formation of a collapsed state
        '''
        names_combinations = []
        
        for ruleComb in ruleCombinations:
            nameComb = ruleComb[0].name
            for rule in range(1,len(ruleComb)):
                nameComb = nameComb + '-' + ruleComb[rule].name
            names_combinations.append((nameComb,ruleComb))
        
        return names_combinations                                                           