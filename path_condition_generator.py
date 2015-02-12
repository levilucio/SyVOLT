from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.iterator import Iterator

from t_core.tc_python.srule import SRule
from t_core.tc_python.frule import FRule

from itertools import permutations

from himesis_utils import disjoint_model_union
from himesis_utils import graph_to_dot
from himesis_utils import print_graph

from copy import deepcopy

from solver.prolog_attribute_equation_evaluator import PrologAttributeEquationEvaluator

from PyRamify import PyRamify
from PropertyProverTester import PropertyProverTester

# the empty path condition
from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition

# transformation to forward the cardinalities to the apply models
from property_prover_rules.cardinality_resolution.Himesis.HForwardCardinalitiesToApplyModelLHS import HForwardCardinalitiesToApplyModelLHS
from property_prover_rules.cardinality_resolution.Himesis.HForwardCardinalitiesToApplyModelRHS import HForwardCardinalitiesToApplyModelRHS

# transformation to built traceability for rules
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS

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


class PathConditionGenerator():
    """
    Builds the set of path conditions for a transformation
    
    Attributes:
        - rules: all the rules in the transformation, accessible by name, in a dictionary
        - transformation: an array containing the rules, with one subarray per layer
        - ruleCombinators: dictionary containing as key the rule name and as element for each key the array of matcher/rewriter pairs containing the rules necessary
                           to combine the rule with path conditions.
                           Each pair contains a partial or total possibility of matching of the rule on top of the path condition.
                           The first pair in the list entry for a rule key is always the one where only the backward links exist and no other match parts of the rule.
        - ruleTraceCheckers: dictionary containing a matcher for each set of backward links existing for each rule.
        - matchRulePatterns: dictionary containing matchers for the match part of each rule. Needed in case the match parts of the rules overlap.
        - pathConditionSet: holds the set of path conditions. Starts off with the empty path condition.
        - ruleContainment: holds for each layer a lattice representing which match patterns for rules are included in those of other rules
        - verbosity: verbosity level (0 - no verbosity / 1 - verbose / 2 - debug)                          
    """

    def __init__(self, transformation, ruleCombinators, ruleTraceCheckers, matchRulePatterns, verbosity):
        self.transformation = transformation
        self.ruleCombinators = ruleCombinators
        self.ruleTraceCheckers = ruleTraceCheckers
        self.matchRulePatterns = matchRulePatterns

        self.ruleContainment = []

        self.verbosity = verbosity
#         self.outputStates = outputStates

      
        # the path condition set starts with only the empty (None) path condition inside
        self.pathConditionSet = [HEmptyPathCondition()]        
        self.attributeEquationEvaluator = PrologAttributeEquationEvaluator(verbosity) 
#        self.mergeInterLayerFactory = MergeInterLayerFactory(verbosity)

        self._pre_process()

        if verbosity >= 2:
            self.debug()

    def print_transformation(self):
        for layer in self.transformation:
            for rule in layer:
                graph_to_dot("rule_" + str(rule['name']), rule)

    def print_ruleCombinators(self):
        for key in self.ruleCombinators.keys():
            value = self.ruleCombinators[key]

            if value is not None:
                for (m, r) in value:
                    graph_to_dot("ruleCombinator_match_" + str(m.condition.name), m.condition)
                    graph_to_dot("ruleCombinator_rewrite_" + str(r.condition.name), r.condition)

                    if len(m.condition.NACs) > 0:
                        graph_to_dot("ruleCombinator_NAC_" + str(m.condition.name), m.condition.NACs[0])


    def print_ruleTraceCheckers(self):
        for key in self.ruleTraceCheckers.keys():
            tc = self.ruleTraceCheckers[key]
            if tc is not None:
                graph_to_dot("traceChecker_" + str(tc.condition.name), tc.condition)

    def print_matchRulePatterns(self):
        for matchRulePattern in sorted(self.matchRulePatterns.keys()):
            matcher, rewriter = self.matchRulePatterns[matchRulePattern]
            graph_to_dot("matchPattern_matcher_" + str(matchRulePattern), matcher.condition)
            graph_to_dot("matchPattern_rewriter_" + str(matchRulePattern), rewriter.condition)


    def debug(self):
        self.print_transformation()
        self.print_ruleCombinators()
        self.print_ruleTraceCheckers()
        self.print_matchRulePatterns()

        ppt = PropertyProverTester()
        ppt.set_artifacts(self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)

        ppt.test_matchRulePatterns()
        ppt.test_ruleTraceCheckers()
        ppt.test_ruleCombinators()


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
        print("merge rules of the same layer that share common match patterns over those match patterns   ")
        for layer in range(0,len(self.transformation)):
            print(layer)
            # loop until all the rules in the layer have been treated
            merged_layer = []
            while self.transformation[layer] != []:
                # compare the first rule to the remaining ones
                mergeResult = self.transformation[layer][0]
                markedForRemoval = [self.transformation[layer][0]]
                   
                matchPatternCurrentRule = self.matchRulePatterns[self.transformation[layer][0].name][0]
  
#                 print("MPCR: ")
#                 print_graph(matchPatternCurrentRule.condition)
#                 for r in self.transformation[layer]:
#                     print(r)
                for candidateToMerge in range(1,len(self.transformation[layer])):
                    matchPatternCandidateRule = self.matchRulePatterns[self.transformation[layer][candidateToMerge].name][0]
#                     print("MPCRNAme: " + self.transformation[layer][candidateToMerge].name)
                    # check whether the rules can be merged, if both have the same match pattern
                    # check if the current rule's (first rule) match is a subset of the candidate's rule match
                    p = Packet()
                    p.graph = self.transformation[layer][candidateToMerge]
#                     print("First name: " + p.graph.name)
                    matchPatternCurrentRule.packet_in(p)
                    # now check if the candidate rule's match is a subset of the current rule's match
                    p = Packet()
                    p.graph = self.transformation[layer][0]
                    matchPatternCandidateRule.packet_in(p)                           

                    # check if the rules share the same match pattern such that we can merge them
                    if matchPatternCurrentRule.is_success and matchPatternCandidateRule.is_success:
                        
                        # merge the rules by copying the candidate to merge on top of the results of merging
                        # all rules so far with the same matcher
                        mergeResultNameBefore = mergeResult.name
                        p = Packet()
                        p.graph = mergeResult
                        p = self.matchRulePatterns[self.transformation[layer][candidateToMerge].name][1].packet_in(p)
                        mergeResult = p.graph
                        mergeResult.name = mergeResult + self.transformation[layer][candidateToMerge].name
                        
                        # mark the rule for removal
                        markedForRemoval.append(self.transformation[layer][candidateToMerge])
  
                # copy the result of the merge or the unmerged rule to the merged layer
                merged_layer.append(mergeResult)
                # merge backwardPatterns matchers for the merged rules
                # gather all the backwardPattern matchers from the rules that got merged
                # and are to be removed, only if any rule got merged during this pass
                  
                if len(markedForRemoval) > 1:                  
                    # rebuild the auxiliary structures
                    # matchRulePatterns
                    self.matchRulePatterns[mergeResult.name] = self.matchRulePatterns[markedForRemoval[0].name]
                    
                    # rebuild the rule combinators for the merged rule
#                     pyramify = PyRamify()
#                     self.ruleCombinators = pyramify.get_rule_combinators(mergeResult)
                                     
                    # remove from the backwardPatterns dictionary the references to rules that got merged
                    for rule in markedForRemoval:
                        del self.matchRulePatterns[rule.name]

                # remove the rules that got merged during the previous pass
                self.transformation[layer] = [rule for rule in self.transformation[layer] if rule not in markedForRemoval]               
            # the layer has been treated and can be put back into the transformation               
            self.transformation[layer] = merged_layer
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
        
            
        # calculate the partial order containing the containment order between the match patterns of the rules
        # first calculate all the pairs according to the layers of the transformation
        layerpairs = []
        for layerIndex in range(0,len(self.transformation)):
            layerpairs.append(list(permutations(self.transformation[layerIndex],2)))
             
        # now build the partial order of rules as a dictionary per layer
        # the keys are rules that are larger than the elements in the order 
        ruleContainment = []
        
        for layerIndex in range(0,len(layerpairs)):
            ruleContainment.append({})
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
                        if pair[1] not in ruleContainment[layerIndex].keys():
                            ruleContainment[layerIndex][pair[1]] = [pair[0]]
                        else:
                            ruleContainment[layerIndex][pair[1]].append(pair[0])
                            
        self.ruleContainment = ruleContainment

        if self.verbosity >= 2:
            print 'Subsumption order between rules for all layers:'                    
            print ruleContainment
        
        # now reorder the rules within each layer of the transformation such that the rules that are
        # contained in others always appear first. This makes it possible to make it such that when
        # rules are symbolically executed to build the path conditions, we can force subsumed rules
        # to executed with the rules that subsume them.
                     
        for layerIndex in range(0,len(self.transformation)):

            # first find all the top nodes
            topRules = []

            for rule in ruleContainment[layerIndex].keys():
                toprule = True
                for rulepass in ruleContainment.keys():
                    if rule in set(ruleContainment[rulepass]):
                        toprule = False
                if toprule: topRules.append(rule)

            orderedRules = []            
            orderedRules.extend(topRules)
            
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
                graph_to_dot("traced_" + self.transformation[layerIndex][ruleIndex].name , self.transformation[layerIndex][ruleIndex])

            
            # auxiliary function to order the nodes recursively, starting from the top nodes
            def _build_ordered_rules(topRules):
                newTopRules = []
                for rule in topRules:
                    if rule in set(self.partialOrder.keys()):
                        newTopRules.extend(self.partialOrder[rule])
                        orderedRules.extend(self.partialOrder[rule])
                
                if newTopRules != [] : _build_ordered_rules(newTopRules)
            
            # continue adding nodes as we go down the tree
            _build_ordered_rules(topRules)

            # remove from the layer the rules that need to be ordered
            self.transformation[layerIndex] = list(set(self.transformation[layerIndex]) - set(orderedRules))   
            # now place the reordered rules back in the layer, at the end
            self.transformation[layerIndex].extend(list(reversed(orderedRules)))



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
            # This is needed because the layerPathCondAccumulator set keeps all path conditions generated
            # for the current layer, starting from the same set as the ones accumulated for the previous layer.
            # for every rule pass we need to know which path conditions for the current layer were built
            # from which path condition from the previous layer, since they are all in a vector.
            # this can be optimized by having a dictionary for each rule from the previous layer containing
            # the path conditions generated for it, instead of going though the whole vector each time.
            
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
                        
                    # first check if the rule requires any other rules to execute with it,
                    # in case of rule overlapping. If all the rules that are required to execute
                    # are already present in the path condition, then the rule executes.
                    # If they are not, then the combination is not possible and we can skip it.
                    
                    # function to return all the rules that have to execute if the current rule executes.
                    
                    def calc_required(rules):
                        requiredRules = []
                        for rule in rules:
                            if rule in set(self.ruleContainment[layer].keys()):
                                requiredRules = self.ruleContainment[layer][rule]
                                requiredRules.extend(self.calc_required(self.ruleContainment[layer][rule]))
                        return requiredRules
                    
                    
                    requiredRules = calc_required([rule])
                    
                    # now check if all the required rules exist in the path condition
                    # by checking the path condition's name. Note that "_" (underscore) is
                    # the rule name separator, so rules names cannot have underscores
                   
                    combinationIsPossible = True                
                    if requiredRules != []:
                        namesOfRulesinPathCond = pathCondition.name.split("_")
                        for rule in requiredRules:
                            if rule.name not in set(namesOfRulesinPathCond):
                                combinationIsPossible = False
                    
                    if not combinationIsPossible:
                        if self.verbosity >= 2:
                            print "Cannot combine: missing required rules that should have executed\
                                    because they are subsumed by the executed rule!"                      
                        continue                   

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
                                p.graph = self.pathConditionSet[pathCondition]
                                
                                combinatorMatcher.packet_in(p)
                                                                
                                # now go through the path conditions resulting from combination of the rule and the
                                # path condition from the previous layer currently being treated in order to apply
                                # the combinator's RHS to every possibility of match of the combinator's LHS

                                if self.verbosity >= 2 :
                                    if combinatorMatcher.is_success:
                                        print("Matching was successful")
                                    else:
                                        print("Matching was not successful")



                                if combinatorMatcher.is_success:  

                                    # holds the result of combining the path conditions generated so far when combining
                                    # the rule with the path condition using the multiple combinators
                     
                                    partialTotalPathCondLayerAccumulator = []             
        
                                    for currentPathCondition in range(len(layerPathCondAccumulator)):  
                                        
#                                         if self.verbosity >= 2 :
#                                             print "--> Combining with path condition: " + layerPathCondAccumulator[currentPathCondition].name
                                        
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
                                            # in all the places where the rule matched on top of the path condition
                                            i = Iterator()
                                            p_copy = deepcopy(p)
                                            p_copy.graph = newPathCond
                                            p_copy = i.packet_in(p_copy)
                                                                    
                                            while i.is_success:
                                                p_copy = self.ruleCombinators[rule.name][combinator][1].packet_in(p_copy)
                                                p_copy = i.next_in(p_copy)
                                                
                                            newPathCond = p_copy.graph
                                            newPathCond.name = newPathCondName
                                            
                                            # check if the equations on the attributes of the newly created path condition are satisfied
                                        
                                            graph_to_dot("evaluating", newPathCond)
                                        
                                            if self.attributeEquationEvaluator(newPathCond):
                                       
                                            #if True:
                                            
                                                if isTotalCombinator:
                                                    # because the rule combines totally with a path condition in the accumulator we just copy it 
                                                    # directly on top of the accumulated path condition
                                                    
                                                    parentPathCondition[newPathCond] = parentPathCondition[layerPathCondAccumulator[currentPathCondition]]

                                                    layerPathCondAccumulator[currentPathCondition] = newPathCond
                                                                                 
                                                else:
                                                    # we are dealing with a partial combination of the rule.
                                                    # create a copy of the path condition in the accumulator because this match of the rule is partial.           
                                                   
                                                    # add the result to the local accumulator
                                                    partialTotalPathCondLayerAccumulator.append(newPathCond)  
                                                    
                                                    # store the parent of the newly created path condition
                                                    parentPathCondition[newPathCond] = parentPathCondition[layerPathCondAccumulator[currentPathCondition]]
                                         
#                                                 print "----------------------"
#                                                 print "Adding: " + newPathCond.name
#                                                 print "Parent is: " + parentPathCondition[layerPathCondAccumulator[currentPathCondition]]
#                                                 print "----------------------"
                                                    
                                                if self.verbosity >= 2: print "Created path condition with name: " + newPathCond.name                                          
                                            
                                    layerPathCondAccumulator.extend(partialTotalPathCondLayerAccumulator)
                           
                
            # when the layer treatment is finished the set of path conditions for the transformation can receive the
            # accumulated path condition set for the layer

            self.pathConditionSet = layerPathCondAccumulator
                

        
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
    

#     def _buildBackLinksCacheKeys(self,backLinkMatchers,pathCondition):
#         """
#         build a set of cache keys by concatenating the name of the backward link matcher with a fragment of the path condition to check.
#         The cache keys are organized in sublists, one per backward link matcher.
#         Each key is a pair, containing the string with the concatenation of names and the fragment of the path condition it refers to.
#         """     
#         backLinksCacheKeys = []
#         for backMatcherPosition in range(len(backLinkMatchers)):
#             backLinksCacheKeys.append([])
#             for fragment in pathCondition:
#                 backLinksCacheKeys[backMatcherPosition].append((backLinkMatchers[backMatcherPosition].condition.name + fragment.name, fragment))
#         return backLinksCacheKeys
    

    def print_path_conditions_screen(self):
        for pathCond in self.pathConditionSet:
            print "----------"
            print pathCond.name


    def print_path_conditions_file(self):
        for pathCond in self.pathConditionSet:
            graph_to_dot(pathCond.name, pathCond, 1)