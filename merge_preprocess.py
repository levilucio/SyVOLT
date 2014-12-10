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

# merge elements from match and apply model

from property_prover_rules.merge_preprocess_rules.Himesis.HStripMatchModelLHS import HStripMatchModelLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HStripMatchModelRHS import HStripMatchModelRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HStripApplyModelLHS import HStripApplyModelLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HStripApplyModelRHS import HStripApplyModelRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HStripRemoveMatchApplyModelsLHS import HStripRemoveMatchApplyModelsLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HStripRemoveMatchApplyModelsRHS import HStripRemoveMatchApplyModelsRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HFindTwoMatchElementsSameTypeDiffRulesLHS import HFindTwoMatchElementsSameTypeDiffRulesLHS

from property_prover_rules.merge_preprocess_rules.Himesis.HFindTwoApplyElementsWithBackwardLHS import HFindTwoApplyElementsWithBackwardLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HFindTwoApplyElementsWithBackwardRHS import HFindTwoApplyElementsWithBackwardRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMergeCardinalitiesMatchDiffRulesLHS import HMergeCardinalitiesMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMergeCardinalitiesMatchDiffRulesRHS import HMergeCardinalitiesMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputDirectMatchDiffRulesLHS import HMoveOneInputDirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputDirectMatchDiffRulesRHS import HMoveOneInputDirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputRepeatedDirectMatchDiffRulesLHS import HMoveOneInputRepeatedDirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputRepeatedDirectMatchDiffRulesRHS import HMoveOneInputRepeatedDirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputIndirectMatchDiffRulesLHS import HMoveOneInputIndirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputIndirectMatchDiffRulesRHS import HMoveOneInputIndirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputRepeatedIndirectMatchDiffRulesLHS import HMoveOneInputRepeatedIndirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputRepeatedIndirectMatchDiffRulesRHS import HMoveOneInputRepeatedIndirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputDirectMatchDiffRulesLHS import HMoveOneOutputDirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputDirectMatchDiffRulesRHS import HMoveOneOutputDirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputRepeatedDirectMatchDiffRulesLHS import HMoveOneOutputRepeatedDirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputRepeatedDirectMatchDiffRulesRHS import HMoveOneOutputRepeatedDirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputIndirectMatchDiffRulesLHS import HMoveOneOutputIndirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputIndirectMatchDiffRulesRHS import HMoveOneOutputIndirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputRepeatedIndirectMatchDiffRulesLHS import HMoveOneOutputRepeatedIndirectMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputRepeatedIndirectMatchDiffRulesRHS import HMoveOneOutputRepeatedIndirectMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputDirectApplyDiffRulesLHS import HMoveOneInputDirectApplyDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputDirectApplyDiffRulesRHS import HMoveOneInputDirectApplyDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputRepeatedDirectApplyDiffRulesLHS import HMoveOneInputRepeatedDirectApplyDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputRepeatedDirectApplyDiffRulesRHS import HMoveOneInputRepeatedDirectApplyDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputDirectApplyDiffRulesLHS import HMoveOneOutputDirectApplyDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputDirectApplyDiffRulesRHS import HMoveOneOutputDirectApplyDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputRepeatedDirectApplyDiffRulesLHS import HMoveOneOutputRepeatedDirectApplyDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneOutputRepeatedDirectApplyDiffRulesRHS import HMoveOneOutputRepeatedDirectApplyDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneBackwardLinkDiffRulesLHS import HMoveOneBackwardLinkDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneBackwardLinkDiffRulesRHS import HMoveOneBackwardLinkDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputTraceLinkLHS import HMoveOneInputTraceLinkLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HMoveOneInputTraceLinkRHS import HMoveOneInputTraceLinkRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HDeleteUncollapsedElementMatchDiffRulesLHS import HDeleteUncollapsedElementMatchDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HDeleteUncollapsedElementMatchDiffRulesRHS import HDeleteUncollapsedElementMatchDiffRulesRHS

from property_prover_rules.merge_preprocess_rules.Himesis.HDeleteUncollapsedElementApplyDiffRulesLHS import HDeleteUncollapsedElementApplyDiffRulesLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HDeleteUncollapsedElementApplyDiffRulesRHS import HDeleteUncollapsedElementApplyDiffRulesRHS

# eliminate repeated matchmodels and applymodels after two rules merged

from property_prover_rules.merge_preprocess_rules.Himesis.HReconnectMatchElementsLHS import HReconnectMatchElementsLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HReconnectMatchElementsRHS import HReconnectMatchElementsRHS
from property_prover_rules.merge_preprocess_rules.Himesis.HReconnectApplyElementsLHS import HReconnectApplyElementsLHS
from property_prover_rules.merge_preprocess_rules.Himesis.HReconnectApplyElementsRHS import HReconnectApplyElementsRHS

from copy import deepcopy


# declare all the needed TCore rules

strip_matchmodel = FRule(HStripMatchModelLHS(), HStripMatchModelRHS())
strip_applymodel = FRule(HStripApplyModelLHS(), HStripApplyModelRHS())

strip_match_applymodels = ARule(HStripRemoveMatchApplyModelsLHS(), HStripRemoveMatchApplyModelsRHS())

find_elements_merge_match = Matcher(HFindTwoMatchElementsSameTypeDiffRulesLHS())       

find_elements_merge_apply = Matcher(HFindTwoApplyElementsWithBackwardLHS())

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

move_input_tracelink = FRule(HMoveOneInputTraceLinkLHS(), HMoveOneInputTraceLinkRHS())

delete_Uncollapsed_element_match = FRule(HDeleteUncollapsedElementMatchDiffRulesLHS(), HDeleteUncollapsedElementMatchDiffRulesRHS())
delete_Uncollapsed_element_apply = FRule(HDeleteUncollapsedElementApplyDiffRulesLHS(), HDeleteUncollapsedElementApplyDiffRulesRHS())
delete_Uncollapsed_element_backward = Rewriter(HFindTwoApplyElementsWithBackwardRHS())

reconnect_match_elements_merge = FRule(HReconnectMatchElementsLHS(), HReconnectMatchElementsRHS())
reconnect_apply_elements_merge = FRule(HReconnectApplyElementsLHS(), HReconnectApplyElementsRHS())


class MergePreprocessFactory():
    
    def __init__(self, verbosity):
        # dictionary cache to keep the results from performing merges on multiple rules
        # the dictionary key is the concatenated names of the rules.
        # order does not matter in the application of DSLTrans rules
        # but in the dictionary keys rules should always be ordered in the same way to avoid duplications
        self.ruleMergeCache = {}
        self.verbosity = verbosity

    def merge_two_rules_preprocess(self, rule1, rule2):
        
        '''
        merge two rules by merging elements of the same type
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

        p = find_elements_merge_match.packet_in(p)               
        if self.verbosity >= 2: print 'Found collapsable elements:' + str(find_elements_merge_match.is_success)
        
        while find_elements_merge_match.is_success:            
            
            p = i.packet_in(p)
            
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
                
            p = move_input_tracelink.packet_in(p)
            if self.verbosity >= 2: print 'move_input_tracelink:' + str(move_input_tracelink.is_success)    
            
            p = move_backwardlink.packet_in(p)
            if self.verbosity >= 2: print 'move_backwardlink:' + str(move_backwardlink.is_success)
              
            p = delete_Uncollapsed_element_match.packet_in(p)
            if self.verbosity >= 2: print 'delete_Uncollapsed_element_match:' + str(delete_Uncollapsed_element_match.is_success) 
            
            p.clear_state()
            
            # merge apply elements linked to backward links if they have the same type
            # cardinality resolution for the applymodel is done in this rule
            p = find_elements_merge_apply.packet_in(p)
            if self.verbosity >= 2: print 'Found collapsable apply elements:' + str(find_elements_merge_apply.is_success)
                    
            i2 = Iterator()
            p = i2.packet_in(p)       
                        
            if find_elements_merge_apply.is_success:
            
            # merge all pairs of apply instances of the same type from different rules
            # which are backward linked to the match instance that was merged previously
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
            
                    p = delete_Uncollapsed_element_backward.packet_in(p)
                    if self.verbosity >= 2: print 'delete_Uncollapsed_element_backward:' + str(delete_Uncollapsed_element_backward.is_success)
                    p = delete_Uncollapsed_element_apply.packet_in(p)                                
                    if self.verbosity >= 2: print 'delete_Uncollapsed_element_apply:' + str(delete_Uncollapsed_element_apply.is_success)
                    i2.next_in(p)                       

            p.clear_state()

            p = find_elements_merge_match.packet_in(p)               
            if self.verbosity >= 2: print 'Found collapsable elements:' + str(find_elements_merge_match.is_success)
            
            # if no more pairs of match elements are found
            if not find_elements_merge_match.is_success:
                
                # reconnect disconnected elements from the second rule                 
                p = reconnect_match_elements_merge.packet_in(p)
                if self.verbosity >= 2: print 'reconnect_match_elements_merge:' + str(reconnect_match_elements_merge.is_success)
                p = reconnect_apply_elements_merge.packet_in(p)
                if self.verbosity >= 2: print 'reconnect_apply_elements_merge:' + str(reconnect_apply_elements_merge.is_success)
                
                return p.graph
                              
        else:   
            return []
