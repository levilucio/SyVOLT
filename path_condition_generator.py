from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.iterator import Iterator

from t_core.tc_python.srule import SRule
from t_core.tc_python.frule import FRule

from itertools import permutations
from itertools import combinations
from itertools import chain

from himesis_utils import disjoint_model_union
from himesis_utils import graph_to_dot
from himesis_utils import print_graph

from copy import deepcopy
from collapse import CollapseFactory
from merge_preprocess import MergePreprocessFactory
from merge_inter_layer import MergeInterLayerFactory

import sys
import time
import copy

import subprocess

# the empty path condition
from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition

# transformation to forward the cardinalities to the apply models
from property_prover_rules.cardinality_resolution.Himesis.HForwardCardinalitiesToApplyModelLHS import HForwardCardinalitiesToApplyModelLHS
from property_prover_rules.cardinality_resolution.Himesis.HForwardCardinalitiesToApplyModelRHS import HForwardCardinalitiesToApplyModelRHS

# transformation to built traceability for rules
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS

# check for the existence of backward links is rules
from property_prover_rules.backward_link_test.Himesis.HCheckForNoBackwardLinksLHS import HCheckForNoBackwardLinksLHS

##Backward Matchers -start
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectPPortPrototype_Back_CompositionType2ECULHS import HConnectPPortPrototype_Back_CompositionType2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnectRPortPrototype_Back_CompositionType2ECULHS import HConnectRPortPrototype_Back_CompositionType2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_EcuInst2ECULHS import HConnECU2VirtualDevice_Back_EcuInst2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS import HConnECU2VirtualDevice_Back_STEM2VirtualDeviceLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnECU2VirtualDevice_Back_SystemMapping2ECULHS import HConnECU2VirtualDevice_Back_SystemMapping2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS import HConnVirtualDevice2Distributable_Back_ComponentPrototype2DistributableLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS import HConnVirtualDevice2Distributable_Back_CompositionType2ECULHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS import HConnVirtualDevice2Distributable_Back_SCTEMc2DistributableLHS
# from GM2AUTOSAR_MM.backward_matchers.Himesis.HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS import HConnVirtualDevice2Distributable_Back_STEM2VirtualDeviceLHS
##Backward Matchers -end

# declare the necessary T-Core rules
forward_cardinalities_to_apply = SRule(HForwardCardinalitiesToApplyModelLHS(), HForwardCardinalitiesToApplyModelRHS())
build_traceability_for_rule = FRule(HBuildTraceabilityForRuleLHS(), HBuildTraceabilityForRuleRHS())
check_for_no_backward_links = Matcher(HCheckForNoBackwardLinksLHS())


class PathConditionGenerator():
    """
    Builds the set of path conditions for a transformation
    
    Attributes:
        - rules: all the rules in the transformation, accessible by name, in a dictionary
        - transformation: an array containing the rules, with one subarray per layer
        - ruleCombinators: a dictionary containing as key the rule name and as element for each key the array of matcher/rewriter pairs containing the rules necessary
                           to combine the rule with path conditions.
                           Each pair contains a partial or total possibility of matching of the rule on top of the path condition.
                           The first pair in the list entry for a rule key is always the one where only the backward links exist and no other match parts of the rule.
        - backwardPatternsComplete: dictionary holding for each rule the complete set of linked connected graphs involving the
                                    match elements that are backward linked plus the match elements connected to them
        - matchRulePatterns: dictionary containing matchers for the match part of each rule. Needed in case the match parts of the rules overlap.
        - symbStateSpace: holds the state space itself. The state space is a list of lists of rules, obtained by going through
                          each layer, calculating its powerset and for each state in that powerset merging it will all states
                          found in previous layers. A merge can only be achieved if all the backward linked graphs in the
                          new state exist the previous state.
        - backwardMergeCache: holds the cache for rules for layer l+1 merged with rules of layer l-n.
        - backwardMatchCache: holds a dictionary cache that allows checking whether a backward link pattern matches a rule
                              key: concatenation of the backward link pattern name and the rule name
                              value: True, False, meaning the backward links patterns matches or does not match.
        - verifiedStateCache (deprecated): holds all the verified states during a property check, along with the number of times the 
                              individual elements rules matched. --> This attribute is deprecated and is now an attribute of AtomicStateProperty 
        - collapseFactory: holds the object that allows performing collapses. The object contains a cache of its own to handle
                           duplicate collapses resulting from multiple collapses of the same rules.
        - mergeFactory: holds the object that allows performing merges. The object contains a cache of its own to handle
                     duplicate merges resulting from multiple collapses of the same rules.
        - ruleOrder: holds for each layer a lattice representing which match patterns for rules are included in those of other rules
        - verbosity: verbosity level (0 - no verbosity / 1 - verbose / 2 - debug)
        - outputStates: True - output all the produced states, including collapsed one, in svg format
                          
    """

    def __init__(self, transformation, ruleCombinators, ruleTraceCheckers, matchRulePatterns, verbosity):
        self.transformation = transformation
        self.ruleCombinators = ruleCombinators
        self.ruleTraceCheckers = ruleTraceCheckers

        self.print_transformation()
        self.print_ruleCombinators()
        self.print_ruleTraceCheckers()

#         self.backwardPatternsComplete = backwardPatternsComplete
        self.matchRulePatterns = matchRulePatterns
        self.verbosity = verbosity
#         self.outputStates = outputStates

        # output suffix for graph files
#        self.output_suffix = output_suffix
      
        # the path condition set starts with only the empty (None) path condition inside
        self.pathConditionSet = [HEmptyPathCondition()]        
#        self.verifiedStateCache = []
        self.collapseFactory = CollapseFactory(verbosity)
        self.mergePreprocessFactory = MergePreprocessFactory(verbosity)
#        self.mergeInterLayerFactory = MergeInterLayerFactory(verbosity)

        self._pre_process()

    def print_transformation(self):
        for layer in self.transformation:
            for rule in layer:
                graph_to_dot("rule_" + str(rule['name']), rule)

    def print_ruleCombinators(self):
        print("RuleCombinators")
        for key in self.ruleCombinators.keys():
            value = self.ruleCombinators[key]

            if value is not None:
                #print("Value")
                #print(value)

                for (m, r) in value:
                    #print("Name: " + str(m.condition.name))

                    #print(m)

                    graph_to_dot("ruleCombinator_match_" + str(m.condition.name), m.condition)
                    graph_to_dot("ruleCombinator_rewrite_" + str(r.condition.name), r.condition)

    def print_ruleTraceCheckers(self):
        for key in self.ruleTraceCheckers.keys():

            tc = self.ruleTraceCheckers[key]
            if tc is not None:
                graph_to_dot("traceChecker_" + str(tc.condition.name), tc.condition)

#    def print_backwardPatternsComplete(self):
#        print("\n===\nbackwardPatternsComplete:")
#         for backwardPatternsCompleteKey in sorted(self.backwardPatternsComplete.keys()):
#             print("Key: " + str(backwardPatternsCompleteKey))
#             val = self.backwardPatternsComplete[backwardPatternsCompleteKey]
#             if val is None:
#                 print("Val is None")
#                 continue
#             elif val ==[]:
#                 print("Val is []")
#                 continue
#             for v in val:
#                 print_graph(v.condition)
#                 graph_to_dot("backComplete_" + str(backwardPatternsCompleteKey) + self.output_suffix, v.condition)

#    def print_matchRulePatterns(self):
#        print("\n===\nmatchRulePatterns:")
#         for matchRulePattern in sorted(self.matchRulePatterns.keys()):
#             print("\nKey: " + str(matchRulePattern))
#             print("\nValue: ")
#             print_graph(self.matchRulePatterns[matchRulePattern].condition)
#             graph_to_dot("matchPattern_" + str(matchRulePattern) + self.output_suffix, self.matchRulePatterns[matchRulePattern].condition)

    def _pre_process(self):
        """
        1) Forward the cardinalities to the apply part of the rules
        2) Merge rules of the same layer that share common match patterns over those match patterns (G- while merging their cardinalities too using cardinality algebra ?)
        3) G - Build traceability links for merged rules
        """

#         print("----------------Start pre-process")
#         # forward the cardinalities to the apply part of the rules
#         for layer in self.transformation:
#             for rule in layer:
#                 p = Packet()
#                 p.graph = rule
#                 p = forward_cardinalities_to_apply.packet_in(p)
#                 rule = p.graph
#                 print(rule.name)
#                 print(rule)
#         
        # merge rules of the same layer that share common match patterns over those match patterns   
#         print("merge rules of the same layer that share common match patterns over those match patterns   ")
#         for layer in range(0,len(self.transformation)):
#             print(layer)
#             # loop until all the rules in the layer have been treated
#             merged_layer = []
#             while self.transformation[layer] != []:
#                 # compare the first rule to the remaining ones
#                 mergeResult = self.transformation[layer][0]
#                 markedForRemoval = [self.transformation[layer][0]]
#                   
#                 matchPatternCurrentRule = self.matchRulePatterns[self.transformation[layer][0].name]
#  
#                 print("MPCR: ")
#                 print_graph(matchPatternCurrentRule.condition)
#                 for r in self.transformation[layer]:
#                     print(r)
#                 for candidateToMerge in range(1,len(self.transformation[layer])):
#                     matchPatternCandidateRule = self.matchRulePatterns[self.transformation[layer][candidateToMerge].name]
#                     print("MPCRNAme: " + self.transformation[layer][candidateToMerge].name)
#                     # check whether the rules can be merged, if both have the same match pattern
#                     # check if the current rule's (first rule) match is a subset of the candidate's rule match
#                     p = Packet()
#                     p.graph = self.transformation[layer][candidateToMerge]
#                     print("First name: " + p.graph.name)
#                     matchPatternCurrentRule.packet_in(p)
#                     # now check if the candidate rule's match is a subset of the current rule's match
#                     p = Packet()
#                     p.graph = self.transformation[layer][0]
#                     print("Other name: " + p.graph.name)
#                     matchPatternCandidateRule.packet_in(p)                           
#                     # check if the rules share the same match pattern such that we can merge them
#                     print("matchPatternCurrentRule.is_success: " + str(matchPatternCurrentRule.is_success))
#                     print("matchPatternCandidateRule.is_success: " + str(matchPatternCandidateRule.is_success))
#                     if matchPatternCurrentRule.is_success and matchPatternCandidateRule.is_success:
#  
#                         mergeResult = self.mergePreprocessFactory.merge_two_rules_preprocess(mergeResult, self.transformation[layer][candidateToMerge])
#                         # mark the rule for removal
#                         markedForRemoval.append(self.transformation[layer][candidateToMerge])
#  
#                 # copy the result of the merge to the merged layer
#                 merged_layer.append(mergeResult)
#                 # merge backwardPatterns matchers for the merged rules
#                 # gather all the backwardPattern matchers from the rules that got merged
#                 # and are to be removed, only if any rule got merged during this pass
#                  
#                 if len(markedForRemoval) > 1:                  
#                     # rebuild the auxiliary structures
#                     # rules
#                     self.rules[mergeResult.name] = mergeResult
#                     # rulesIncludingBackwardLinks
#                     for rule in markedForRemoval:
#                         if rule in set(self.rulesIncludingBackwardLinks[layer]):
#                             self.rulesIncludingBackwardLinks[layer].append(mergeResult)
#                             break
#                     # backwardPatterns
#                     newBackwardPattern = []
#                     for rule in markedForRemoval:
#                         if self.backwardPatterns[rule.name] != []:
#                             print("Rule name: " + str(rule.name))
#                             newBackwardPattern.extend(self.backwardPatterns[rule.name])
#                     self.backwardPatterns[mergeResult.name] = newBackwardPattern
#                     # backwardPatterns2Rules
#                     for backPattern in self.backwardPatterns2Rules.keys():
#                         if self.rules[self.backwardPatterns2Rules[backPattern]] in set(markedForRemoval):
#                             self.backwardPatterns2Rules[backPattern] = mergeResult.name
#                     # backwardPatternsComplete
#                     self.backwardPatternsComplete[mergeResult.name] = self.[markedForRemoval[0].name]  
#                     # matchRulePatterns
#                     self.matchRulePatterns[mergeResult.name] = self.matchRulePatterns[markedForRemoval[0].name]
#                                     
#                     # remove from the backwardPatterns dictionary the references to rules that got merged
#                     for rule in markedForRemoval:
#                         del self.rules[rule.name]
#                         del self.backwardPatterns[rule.name]
#                         del self.backwardPatternsComplete[rule.name]
#                         del self.matchRulePatterns[rule.name]
#                         self.rulesIncludingBackwardLinks[layer] = [rule for rule in self.rulesIncludingBackwardLinks[layer] if rule not in markedForRemoval]
#                 # remove the rules that got merged (marked None) during the previous pass
#                 self.transformation[layer] = [rule for rule in self.transformation[layer] if rule not in markedForRemoval]               
#             # the layer has been treated and can be put back into the transformation               
#             self.transformation[layer] = merged_layer
#             
#        print 'Transformation:'
#        for layer in range(0,len(self.transformation)):
#            print 'Layer ' + str(layer)
#            for rule in self.transformation[layer]:
#                print rule
#
#        print '\nRules:'
#        print self.rules
#        
#        print '\nRules Including Backward Links:'
#        for layer in range(0,len(self.rulesIncludingBackwardLinks)):
#            print 'Layer: ' + str(layer)
#            for rule in self.rulesIncludingBackwardLinks[layer]:
#                print rule
#              
#        print '\nBackward Pattern Matchers:'
#        print self.backwardPatterns
#        
#        print '\nBackward Pattern 2 Rules Matchers:'
#        print self.backwardPatterns2Rules             
#        
#        print '\nBackward Complete Matchers:'
#        print self.backwardPatternsComplete
#        
#        print '\nMatch Rule Patterns:'
#        print self.matchRulePatterns
            

#         print 'Buiding traceability---------------------'
#         for layerIndex in range(0,len(self.transformation)):
#             p = Packet()
#             p.graph = self.transformation[layerIndex][0]
#             p = build_traceability_for_rule.packet_in(p)
#             print build_traceability_for_rule.is_success
#             self.transformation[layerIndex][0] =  p.graph
#         print '------------------------------------------'

        # build traceability links-for each rule that got merged it produces traceability between them
        # to know which apply elems came from which match elems   
        
        # TODO: now traceability is being built for all rules. We only need traceability for the rules that have no dependencies, 
        # as the others are built by the combinators associated to the rule      
        
        for layerIndex in range(0, len(self.transformation)):
            for ruleIndex in range(0, len(self.transformation[layerIndex])):
                p = Packet()
                p.graph = self.transformation[layerIndex][ruleIndex]
#                p = build_traceability_no_backward.packet_in(p)
#                p = build_traceability_with_backward.packet_in(p)
                p = build_traceability_for_rule.packet_in(p)                
                self.transformation[layerIndex][ruleIndex] =  p.graph

            
        # calculate the partial order containing the containment order between the match patterns of the rules
        # first calculate all the pairs according to the layers of the transformation
        layerpairs = []
        for layerIndex in range(0,len(self.transformation)):
            layerpairs.append(list(permutations(self.transformation[layerIndex],2)))
             
        # now build the partial order of rules as a dictionary per layer
        # the keys are rules that are larger than the elements in the order 
        ruleOrder = []
        
        for layerIndex in range(0,len(layerpairs)):
            ruleOrder.append({})
            for pair in layerpairs[layerIndex]:
                p = Packet()
                p.graph = pair[1]
                p = self.matchRulePatterns[pair[0].name][0].packet_in(p)
                if self.matchRulePatterns[pair[0].name][0].is_success:
                    # Test for the satisfaction of the attribute equations when the two rules combine.
                    # If the attribute equations are satisfied for at least one of the combination of the two rules, 
                    # then the two rules are dependent, otherwise they are not dependent
                    
                    dependentRules = False
                    
                    i = Iterator()
                    p = i.packet_in(p)
                    while i.is_success:
                        p.graph = pair[0]
                        p = self.matchRulePatterns[pair[0].name][1].packet_in(p)
                        if self.evaluate_attribute_equations(p.graph):
                            dependentRules = True
                            break
                        p = i.next_in(p)                                                                   
                    
                    if dependentRules:
                        # the partial order may branch, so we need lists to store the smaller elements
                        if pair[1] not in ruleOrder[layerIndex].keys():
                            ruleOrder[layerIndex][pair[1]] = [pair[0]]
                        else:
                            ruleOrder[layerIndex][pair[1]].append(pair[0])

        if self.verbosity >= 2:
            print 'Subsumption order between rules for all layers:'                    
            print ruleOrder
        
        # now reorder the rules within each layer of the transformation such that the rules that are
        # contained in others always appear first. This makes it possible to make it such that when
        # rules are symbolically executed to build the path conditions, we can force subsumed rules
        # to executed with the rules that subsume them.
             
        
        for layerIndex in range(0,len(self.transformation)):

            # first find all the top nodes
            topNodes = []

            for node in ruleOrder[layerIndex].keys():
                topnode = True
                for nodepass in ruleOrder.keys():
                    if node in set(ruleOrder[nodepass]):
                        topnode = False
                if topnode: topNodes.append(node)

            orderedNodes = []            
            orderedNodes.extend(topNodes)
            
            # auxiliary function to order the nodes recursively, starting from the top nodes
            def build_ordered_nodes(topNodes):
                newTopNodes = []
                for node in topNodes:
                    if node in set(self.partialOrder.keys()):
                        newTopNodes.extend(self.partialOrder[node])
                        orderedNodes.extend(self.partialOrder[node])
                
                if newTopNodes != [] : self.build_ordered_nodes(newTopNodes)
            
            print "---------------- before"
            print orderedNodes
            
            # continue adding nodes as we go down the tree
            build_ordered_nodes(topNodes)
            
            print orderedNodes
            print "---------------- after"

            # remove from the layer the rules that need to be ordered
            self.transformation[layerIndex] = list(set(self.transformation[layerIndex]) - set(orderedNodes))   
            # now place the reordered rules back in the layer, at the end
            
            print list(reversed(orderedNodes))
            
            print self.transformation[layerIndex] 
            
            self.transformation[layerIndex] = self.transformation[layerIndex]#.extend(list(reversed(orderedNodes)))
            
            print self.transformation[layerIndex] 
                       


    def build_path_conditions(self):     
        """
        Build the set of path conditions by combining rules of a given layer with the
        path conditions of the previous layer. The complete algorithm is described in:
        
        http://msdl.cs.mcgill.ca/people/levi/30_publications/files/A_Technique_for_Symbolically_Verifying_Properties_of_Model_Transf.pdf
        """

        # start with a set (list) of path conditions containing only the empty path condition (declared in the constructor)
        # a path condition is a list of where the elements are rules (or combinations of rules) with traceability information

        if self.verbosity >= 1 : print("Start building path conditions")

        # now go through the layers one-by-one

        for layer in range(len(self.transformation)):
            
            # for each path condition built so far, combine it with each of the rules from the current layer
           
            # the path condition set generated for the layer being treated starts off with the set of path
            # conditions generated for the previous layer
            layerPathCondAccumulator = deepcopy(self.pathConditionSet)
            
            # build a dictionary to remember which path condition in the current layer is built from
            # which path condition from the previous layer
            
            parentPathCondition = {}
            for pc in layerPathCondAccumulator:
                parentPathCondition[pc] = pc.name
            
            for pathCondition in range(len(self.pathConditionSet)):

                # for each rule in the current layer, combine it with the path condition.
                # start with the local path condition set with just a copy of the path condition being combined.
                
#                 pathConditionCopy = deepcopy(self.pathConditionSet[pathCondition])
#                 pathCondAndRuleCombAccumulator = [pathConditionCopy]
                
                for rule in self.transformation[layer]:
                    
                    if self.verbosity >= 2:
                        print "--------------------------------------"
                        print "Treating rule:"
                        print rule.name
                        print "Combining with:"
                        print "Path Condition:" + self.pathConditionSet[pathCondition].name           

                    # possible cases of rule combination                    

                    ######################################
                    # Case 1: Rule has no dependencies
                    ######################################
                    
                    # the rule is disjointly added to the path condition
                    if self.ruleCombinators[rule.name] == None:
                        if self.verbosity >= 1 : print "Case 1: Rule has no dependencies"
                        
                        localPathConditionLayerAccumulator = []
                        
                        for currentPathCondition in range(len(layerPathCondAccumulator)):

                            # look for the right path conditions
                            if parentPathCondition[layerPathCondAccumulator[currentPathCondition]] == self.pathConditionSet[pathCondition].name:                          
                                # create a new path condition which is the result of combining the rule with the current path condition being examined
                                newPathCond = deepcopy(layerPathCondAccumulator[currentPathCondition])
                                newPathCond = disjoint_model_union(newPathCond,rule)
                                # name the new path condition as the combination of the previous path condition and the rule               
                                newPathCond.name = layerPathCondAccumulator[currentPathCondition].name + '_' + rule.name
                                if self.verbosity >= 2 : print "Created path condition with name: " + newPathCond.name
                                localPathConditionLayerAccumulator.append(newPathCond)
                                
                                # store the parent of the newly created path condition
                                parentPathCondition[newPathCond] = parentPathCondition[layerPathCondAccumulator[currentPathCondition]]
                            
                        layerPathCondAccumulator.extend(localPathConditionLayerAccumulator)
                    
                    else:
                    
                        #########################################################################
                        # Case 2: Rule has dependencies but cannot execute because 
                        #         not all the backward links can be found in the path condition
                        #########################################################################
                        
                        # gather the matcher for only the backward links in the rule being combined.
                        # it is the first matcher (LHS) of the combinators in the list.

                        ruleBackwardLinksMatcher = self.ruleTraceCheckers[rule.name]

                        # check if the backward links cannot be found by matching them on the path condition
                        
                        p = Packet()
                        p.graph = self.pathConditionSet[pathCondition]  
                        ruleBackwardLinksMatcher.packet_in(p)
                        if not ruleBackwardLinksMatcher.is_success:
                            if self.verbosity >= 1 : print "Case 2: Rule has dependencies but cannot execute"
                    
                        else:

                            #########################################################################
                            # Case 3: Rule has dependencies that may or will execute     
                            ######################################################################### 
        
                            if self.verbosity >= 1 : print "Case 3: Rule has dependencies that may or will execute"
                            
                            # go through all LHS (matchers) in rule combinators
                            for combinator in range(len(self.ruleCombinators[rule.name])):
                                
                                combinatorMatcher = self.ruleCombinators[rule.name][combinator][0]
                                
                                if self.verbosity >= 2 : print "Combinator: " + combinatorMatcher.condition.name
                                
                                # check whether we are dealing with a partial or a total combinator
                                
                                isTotalCombinator = False
                                
                                if combinator == len(self.ruleCombinators[rule.name]) - 1:
                                    isTotalCombinator = True
                                
                                # find all the matches of the rule combinator in the path condition that the rule combines with
                                
                                p = Packet()
                                i = Iterator()
                                p.graph = self.pathConditionSet[pathCondition]
                                combinatorMatcher.packet_in(p)
                                
                                # now go through the path conditions resulting from combination of the rule and the
                                # path condition from the previous layer currently being treated in order to apply
                                # the combinator's RHS to every possibility of match of the combinator's LHS
                                
                                if combinatorMatcher.is_success:  
                                    
                                    # TODO: go through all the matches in the iterator, now we're only going through
                                    # the first one
                                    p = i.packet_in(p)
                                    
                                    # holds the result of combining the path conditions generated so far when combining
                                    # the rule with the path condition using the multiple combinators
                     
                                    partialTotalPathCondLayerAccumulator = []             
        
                                    for currentPathCondition in range(len(layerPathCondAccumulator)):  
                                        
                                        if self.verbosity >= 2 :
                                            print "--> Combining with path condition: " + layerPathCondAccumulator[currentPathCondition].name
                                        
                                        # only combine if the path condition in the accumulator currently being treated (currentPathCondition)
                                        # includes all the rules from the path condition of the previous layer the rule is being executed
                                        # against (pathCondition) and if the rule hasn't executed yet on that path condition
                                        
                                        if parentPathCondition[layerPathCondAccumulator[currentPathCondition]] == self.pathConditionSet[pathCondition].name:
                                                                     
                                            # if the combinator is not the total one, make a copy of the path condition in the set 
                                            # of combinations generated so far.
                                            # the total combinator is always the one at the end of the combinator list for the rule.
                                            
                                            # name the new path condition as the combination of the previous path condition and the rule
                                            newPathCondName = layerPathCondAccumulator[currentPathCondition].name + "_" + rule.name
                                            
                                            newPathCond = deepcopy(layerPathCondAccumulator[currentPathCondition])                               
        
                                            # now combine the rule with the newly created path condition using the current combinator
                                            p_copy = deepcopy(p)
                                            p_copy.graph = newPathCond 
                                            p_copy = self.ruleCombinators[rule.name][combinator][1].packet_in(p_copy)
                                            
                                            newPathCond = p_copy.graph
                                            newPathCond.name = newPathCondName
                                            
                                            # check if the equations on the attributes of the newly created path condition are satisfied
                                            
                                            # if self.evaluate_attribute_equations(newPathCond):
                                            
                                            if True:
                                            
                                                if isTotalCombinator:
                                                    # because the rule combines totally with a path condition in the accumulator we just copy it 
                                                    # directly on top of the accumulated path condition
                                                    layerPathCondAccumulator[currentPathCondition] = newPathCond
                                                                                 
                                                else:
                                                    # we are dealing with a partial combination of the rule.
                                                    # create a copy of the path condition in the accumulator because this match of the rule is partial.           
                                                   
                                                    # add the result to the local accumulator
                                                    partialTotalPathCondLayerAccumulator.append(newPathCond)  
                                                    
                                                    # store the parent of the newly created path condition
                                                    parentPathCondition[newPathCond] = parentPathCondition[layerPathCondAccumulator[currentPathCondition]]
                                             
                                                    
                                                if self.verbosity >= 2: print "Created path condition with name: " + newPathCond.name                                          
                                            
                                    layerPathCondAccumulator.extend(partialTotalPathCondLayerAccumulator)
                           
                
            # when the layer treatment is finished the set of path conditions for the transformation can receive the
            # accumulated path condition set for the layer

            self.pathConditionSet = layerPathCondAccumulator
                


#     def _rulePowerSet(self,rules,layer):
#         """
#         build the powerset of rules in a layer
#         
#         eliminate from the powerset rules that cannot execute alone, because they imply the execution of other rules.
#         this implication is calculated by looking at the partial order implied by containment between the match
#         patterns contained in the self.ruleOrder attribute
#         """
#       
#         rulePowerset = list(chain.from_iterable(combinations(rules, r) for r in range(len(rules)+1)))
#                       
#         # go down all the branches of the partial orders until bottom elements are reached.
#         # when traversing each node branches merge all the rules downtstream from it recursively 
#         # and build new rules from this merging that are put together with the rules of the
#         # transformation, but are only used for the powerset that is returned
#         
#         if self.ruleOrder[layer] != {}:
#             for rule in rules:
#                 branchMergeResult = self._recursiveRuleMerge(rule,layer)
#                 if branchMergeResult != None:          
#                                         
#                     rulePowerset = [comb for comb in rulePowerset if branchMergeResult[1] != set(comb) and set([rule]) != set(comb)]     
#                                       
#                     # add to the powerset the new rule as a member of the set
#                     rulePowerset.append((branchMergeResult[0],))
#                     
#                     # add the new rule to the rules in the layer.
#                     # The rule will be treated as a preprocessed merged rule given it is important to
#                     # know what are the auxiliary structures for it. This treatment cannot be done during the
#                     # preprocess step and needs to be done dynamically because smaller rules in the partial 
#                     # order need to exist both individually in the powerset and also collapsed with larger rules
#                     
#                     # build the auxiliary structures for the newly merged rules
#                     #rules
#                     self.rules[branchMergeResult[0].name] = branchMergeResult[0]
#                     # rulesIncludingBackwardLinks
#                     if set(branchMergeResult[1]).intersection(set(self.rulesIncludingBackwardLinks[layer])) != set([]):
#                         self.rulesIncludingBackwardLinks[layer].append(branchMergeResult[0])
#                     # backwardPatterns
#                     newBackwardPattern = []
#                     for rule in branchMergeResult[1]:
#                         if self.backwardPatterns[rule.name] != []:
#                             for matcher in self.backwardPatterns[rule.name]:
#                                 # build copies of all the matchers such that there is no overlap with the matchers that
#                                 # are used by the smaller rule
#                                 #tmp = getattr(sys.modules[__name__], matcher.condition.name)()
#                                 newMatcher = copy.deepcopy(matcher)#Matcher(tmp)
#                                 #newMatcher = deepcopy(matcher)
#                                 newBackwardPattern.append(newMatcher)
#                                 # add copy of the matcher to the backwardPatterns2Rules structure
#                                 self.backwardPatterns2Rules[newMatcher] = branchMergeResult[0].name               
#                          
#                     self.backwardPatterns[branchMergeResult[0].name] = newBackwardPattern                
#                     # backwardPatternsComplete
#                     self.backwardPatternsComplete[branchMergeResult[0].name] = self.backwardPatternsComplete[rule.name]  
#                     # matchRulePatterns
#                     self.matchRulePatterns[branchMergeResult[0].name] = self.matchRulePatterns[rule.name]
# 
#                     # remove from the powerset path conditions that include rules that form "branches" of the
#                     # partial order, since they are superseded by the merge of the top rule of the partial
#                     # order with all the rules, potentially in branches, under it. Leaf nodes or combinations
#                     # of leaf nodes are not removed.
#             
#                     rulePowerset = [pc for pc in rulePowerset if set(pc).difference(branchMergeResult[1]) != set([]) or\
#                                     set([rule for rule in pc if rule not in self.ruleOrder[layer].keys()]) == set(pc)]
#                     
#             # remove the smallest members of the powerset where all match elements are connected by
#             # backward links. In this case, if a larger (with a larger match patterns) rule merged with
#             # this one executed, then this one had to necessarily execute because all apply elements
#             # backward linked in the smaller rule already exist.
#             # TODO: This assumes that no dead code rules exist that refers to traces that are never
#             # generated by a previous layer.
#             
#             # go through all the smallest members of the partial order and remove their path conditions
#             # from the powerset in all the elements in their match pattern are connected by backward links
#             for rule in rules:
#                 if rule not in self.ruleOrder[layer].keys():
#                     # check if all the elements in their match pattern are connected by backward links
# #                    print 'Rule not in self.ruleOrder:'
# #                    print rule
#                     
#                     p = Packet()
#                     p.graph = rule
#                     check_for_no_backward_links.packet_in(p)
#                     if not check_for_no_backward_links.is_success:
#                         for pathCondition in rulePowerset:
#                             if rule in set(pathCondition) and len(pathCondition) == 1:
#                                 rulePowerset.remove(pathCondition)
#                                 break
#             
# #            print 'Transformation:'
# #            for layer in range(0,len(self.transformation)):
# #                print 'Layer ' + str(layer)
# #                for rule in self.transformation[layer]:
# #                    print rule
# #    
# #            print '\nRules:'
# #            print self.rules
# #            
# #            print '\nRules Including Backward Links:'
# #            for layer in range(0,len(self.rulesIncludingBackwardLinks)):
# #                print 'Layer: ' + str(layer)
# #                for rule in self.rulesIncludingBackwardLinks[layer]:
# #                    print rule
# #                  
# #            print '\nBackward Pattern Matchers:'
# #            print self.backwardPatterns
# #            
# #            print '\nBackward Pattern 2 Rules Matchers:'
# #            print self.backwardPatterns2Rules             
# #            
# #            print '\nBackward Complete Matchers:'
# #            print self.backwardPatternsComplete
# #            
# #            print '\nMatch Rule Patterns:'
# #            print self.matchRulePatterns           
#                 
#         
#         
# #        for pc in rulePowerset:
# #            if pc != ():           
# #                graph_to_dot(pc[0].name, pc[0], 1) 
#    
#         return rulePowerset

        
#     def _recursiveRuleMerge(self,rule,layer):
#         """
#         go down a, potentially branching, partial order (in the self.ruleOrder dictionary) and merge all the rules
#         until bottom elements are reached. Returns the merged rule plus the set of all rules in the partial
#         order under the top element.
#         TODO: can be optimised by starting from the bottom of the branches and building up 
#         """
# 
#         print("_recursiveRuleMerge")
#         print_graph(rule)
#         print(layer)
#         if rule in self.ruleOrder[layer].keys():
#             # accumulate set of treated rules
#             setOfMergedRules = set([rule])
#             # accumulate the result of merging all the rules down the branch
#             mergedResult = deepcopy(rule)  
#             previousRules = self.ruleOrder[layer][rule]
#             for previousRule in previousRules:
#                 print("PreviousRule")
#                 print_graph(previousRule)
#                 branchMergedResult = self._recursiveRuleMerge(previousRule,layer)
#                 if branchMergedResult != None:
#                     mergedResult = self.mergePreprocessFactory.merge_two_rules_preprocess(mergedResult, branchMergedResult[0])
#                     setOfMergedRules.union(branchMergedResult[1])
#                 mergedResult = self.mergePreprocessFactory.merge_two_rules_preprocess(mergedResult, previousRule)
#                 setOfMergedRules.add(previousRule)
#             return (mergedResult, setOfMergedRules)
#         else:
#             return None
        
    def _buildTraceabilityLinks(self,layer):
        """
        build traceability (for the time being apply all rules until exhaustion)
        """
        symbLayer = []
        for rule in layer:
            p = Packet()
            p.graph = rule
            for transf in self.traceBuildTransf:
                p = transf.packet_in(p)
            symbLayer.append(p)
        return symbLayer
    

    def _buildBackLinksCacheKeys(self,backLinkMatchers,pathCondition):
        """
        build a set of cache keys by concatenating the name of the backward link matcher with a fragment of the path condition to check.
        The cache keys are organized in sublists, one per backward link matcher.
        Each key is a pair, containing the string with the concatenation of names and the fragment of the path condition it refers to.
        """     
        backLinksCacheKeys = []
        for backMatcherPosition in range(len(backLinkMatchers)):
            backLinksCacheKeys.append([])
            for fragment in pathCondition:
                backLinksCacheKeys[backMatcherPosition].append((backLinkMatchers[backMatcherPosition].condition.name + fragment.name, fragment))
        return backLinksCacheKeys
    

    def evaluate_attribute_equations(self, pathCondition):
        """
        Build the necessary set of equations to be passed onto Z3 for evaluation (SAT/UNSAT) given a path condition.
        Equations have an abstract syntax tree structure inside the path condition that needs to be parsed.
        Note that some equations share the same variables, and as such those variables have to be given the same identifiers throughout the Z3 expression.
        Evaluate the set of equations using Z3 and return True if there is a solution for them, false otherwise
        """
        
        Z3Input = ""
        variablesInExpression = []
        
        # grab all the equation nodes in the path condition
        equationNodes = self._find_nodes_with_mm(pathCondition, "Equation")
        # now build all the equations
        if equationNodes != []:
            for equationNode in equationNodes:
                # get the left and the right expressions of the equation
                leftExprEdge = [i for i in pathCondition.neighbors(equationNode,1) if pathCondition.vs[i]['mm__'] == 'leftExpr'][0]    
                rightExprEdge = [i for i in pathCondition.neighbors(equationNode,1) if pathCondition.vs[i]['mm__'] == 'rightExpr'][0]

                leftExprNode = pathCondition.neighbors(leftExprEdge,1)[0]
                rightExprNode = pathCondition.neighbors(rightExprEdge,1)[0] 
                
                leftExpr = self._build_equation_expression(leftExprNode, pathCondition, variablesInExpression)
                rightExpr = self._build_equation_expression(rightExprNode, pathCondition, variablesInExpression)  

                Z3Input += "(assert (= " + leftExpr + " " +  rightExpr + ") )\n"
        
        Z3Input = "\n" + Z3Input
        for var in variablesInExpression:
            Z3Input = "(declare-variable " + var + " String)\n" + Z3Input
        Z3Input += "\n(check-sat)"
        
        if self.verbosity >= 2 :
            print "\nChecking with Z3:"
            print "----------------"
            print Z3Input
            print "\n"
         
        # for now write the file with the equation formulas to be caught by the binary
        # TODO: this is WAY TOO SLOW and needs to be done via an API or something faster    
        with open("./tmp/Z3EquationFile", "w") as text_file:
            text_file.write(Z3Input)
             
        # now call the z3-str binary to get the result of checking the formula
        command = 'python /home/levi/z3-str/Z3-str.py -f ./tmp/Z3EquationFile'
        z3_output = subprocess.check_output(command, shell=True)   
         
        if self.verbosity >= 2 :
            print z3_output                                                                                      
        
        if "UNSAT" not in z3_output:   
            return True
        else:
            return False


    def _build_equation_expression(self, node, pathCondition, variablesInExpression):
        """
        helper for building the attribute equations by recursively going through the operations associated
        to the left hand side and to the right hand side of an equation
        """

        # in case it's an attribute, return the object's ID
        if pathCondition.vs[node]['mm__'] == 'Attribute':
            newVar = "a" + str(node)
            if newVar not in set(variablesInExpression):
                variablesInExpression.append(newVar)
            return "a" + str(node)
        # in case it's a constant, return it's value
        elif pathCondition.vs[node]['mm__'] == 'Constant':
            return "\"" + pathCondition.vs[node]['value'] + "\""
        # it's a concat operation
        else:
            # get the arguments of the concat operation
            arg1Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'arg_1'][0]    
            arg2Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'arg_2'][0]
            arg1 = pathCondition.neighbors(arg1Edge,1)[0]
            arg2 = pathCondition.neighbors(arg2Edge,1)[0]

            return "( Concat " + self.build_equation_expression(arg1) + " " + self.build_equation_expression(arg2) + ")"


    #find the nodes with this mm name
    #move this method to the himesis_utils file, together with the one from PyRamify 
    def _find_nodes_with_mm(self, graph, mm_names):
        nodes = []
        for node in graph.vs:
            if node["mm__"] in mm_names:
                nodes.append(node)
        return nodes

    def print_path_conditions_screen(self):
        for pathCond in self.pathConditionSet:
            print "----------"
            print pathCond.name


    def print_path_conditions_file(self):
        for pathCond in self.pathConditionSet:
            graph_to_dot(pathCond.name, pathCond, 1)