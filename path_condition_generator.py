
from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.iterator import Iterator

from t_core.tc_python.arule import ARule
from t_core.tc_python.frule import FRule

from itertools import permutations

from core.himesis_utils import disjoint_model_union
from core.himesis_utils import graph_to_dot
from core.himesis_utils import clean_graph
from core.himesis_utils import print_graph

from PCDict import PCDict

from copy import deepcopy

from solver.prolog_attribute_equation_evaluator import PrologAttributeEquationEvaluator
from solver.simple_attribute_equation_evaluator import SimpleAttributeEquationEvaluator

from PyRamify import PyRamify
from PropertyProverTester import PropertyProverTester


from multiprocessing import Pool, Manager, Process

from path_condition_generator_worker import *

#profile memory
global global_profile_memory
global global_hp

global_profile_memory= False

if global_profile_memory:
 
    #import heapy
    from guppy import hpy
 
    #create the heapy object
    global_hp = hpy()


#set up cProfile
#and the do_cprofile wrapper
import cProfile
import pstats
import StringIO
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            if global_profile_memory:
                global_hp.setref()

            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:


            print("\nFunction: " + str(func.__name__))

            if global_profile_memory:
                h = global_hp.heap()
                print("\nMemory usage:")
                print(h)

                print("\nBy id:")
                print(h.byid)
                print(h.byvia)
                print(h.byrcs)
                print(h.referents)

                print("\nreferents[0]:")
                print(h.referents[0].byid)
                print(h.referents[0].byvia)
                print(h.referents[0].byrcs)
                print(h.referents[0].referents)



            s = StringIO.StringIO()
            sortby = 'time'
            ps = pstats.Stats(profile, stream = s).sort_stats(sortby)
            ps.print_stats()

            print("Time usage:")
            time_table = str(s.getvalue()).split("\n")
            for i in range(25):
                if i >= len(time_table):
                    break

                if time_table[i].strip() == "":
                    continue

                print(time_table[i])




            print("")
    return profiled_func






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




class PathConditionGenerator(object):
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

    #@do_cprofile
    def __init__(self, transformation, ruleCombinators, ruleTraceCheckers, matchRulePatterns, verbosity, draw_svg = True, run_tests=True):
        # the empty path condition

        self.transformation = transformation
        self.ruleCombinators = ruleCombinators
        self.ruleTraceCheckers = ruleTraceCheckers
        self.matchRulePatterns = matchRulePatterns

        self.draw_svg = draw_svg

        self.run_tests = run_tests

        self.ruleContainment = []

        self.verbosity = verbosity
#         self.outputStates = outputStates

      
        # the path condition set starts with only the empty (None) path condition inside

        self.attributeEquationEvaluator = SimpleAttributeEquationEvaluator(verbosity) 

        self._pre_process()

        self.debug()


    def print_transformation(self):
        for layer in self.transformation:
            for rule in layer:
                graph_to_dot("rule_" + str(self.rule_names[rule.name]), rule)

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
            graph_to_dot("matchPattern_matcher_" + str(matcher.condition.name), matcher.condition)
            graph_to_dot("matchPattern_rewriter_" + str(rewriter.condition.name), rewriter.condition)


    def debug(self):         

        if self.draw_svg:
            print("Drawing svgs...")
            self.print_transformation()
            self.print_ruleCombinators()
            self.print_ruleTraceCheckers()
            self.print_matchRulePatterns()

        if self.run_tests:
            ppt = PropertyProverTester()
            ppt.set_artifacts(self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators)
 
            ppt.test_matchRulePatterns()
            ppt.test_ruleTraceCheckers()
            ppt.test_ruleCombinators()


    #@do_cprofile
    def _pre_process(self):
        """
        1) Forward the cardinalities to the apply part of the rules
        2) Merge rules of the same layer that share common match patterns over those match patterns (G- while merging their cardinalities too using cardinality algebra ?)
        3) G - Build traceability links for merged rules
        """

        # transformation to forward the cardinalities to the apply models
        # from property_prover_rules.cardinality_resolution.Himesis.HForwardCardinalitiesToApplyModelLHS import \
        #    HForwardCardinalitiesToApplyModelLHS
        #from property_prover_rules.cardinality_resolution.Himesis.HForwardCardinalitiesToApplyModelRHS import \
        #    HForwardCardinalitiesToApplyModelRHS
        # declare the necessary T-Core rules
        # self.forward_cardinalities_to_apply = SRule(HForwardCardinalitiesToApplyModelLHS(),
        # HForwardCardinalitiesToApplyModelRHS())

#         print("----------------Start pre-process")
#         # forward the cardinalities to the apply part of the rules
#         for layer in self.transformation:
#             for rule in layer:
#                 p = Packet()
#                 p.graph = rule
#                 p = self.forward_cardinalities_to_apply.packet_in(p)
#                 rule = p.graph
#                 print(rule.name)
#                 print(rule)

                #print('\n')

#        self.debug()

        #merge rules of the same layer that share common match patterns over those match patterns   
        for layerIndex in range(0,len(self.transformation)):
            # loop until all the rules in the layer have been treated
            merged_layer = []
            while self.transformation[layerIndex] != []:
                # compare the first rule to the remaining ones
                mergedResult = deepcopy(self.transformation[layerIndex][0])

                markedForRemoval = [self.transformation[layerIndex][0]]
                    
                matchPatternCurrentRule = self.matchRulePatterns[self.transformation[layerIndex][0].name][0]
   
#                 print("MPCR: ")
#                 print_graph(matchPatternCurrentRule.condition)
#                 for r in self.transformation[layer]:
#                     print(r)
                for candidateToMerge in range(1,len(self.transformation[layerIndex])):
                    matchPatternCandidateRule = self.matchRulePatterns[self.transformation[layerIndex][candidateToMerge].name][0]
#                     print("MPCRNAme: " + self.transformation[layer][candidateToMerge].name)
                    # check whether the rules can be merged, if both have the same match pattern
                    # check if the current rule's (first rule) match is a subset of the candidate's rule match
                    p = Packet()
                    p.graph = self.transformation[layerIndex][candidateToMerge]
#                     print("First name: " + p.graph.name)
                    p = matchPatternCurrentRule.packet_in(p)
                    # now check if the candidate rule's match is a subset of the current rule's match
                    p = Packet()
                    p.graph = mergedResult
                    p = matchPatternCandidateRule.packet_in(p)
                    
                    # check if the rules share the same match pattern such that we can merge them
                    if matchPatternCurrentRule.is_success and matchPatternCandidateRule.is_success:
                                                
                        # merge the rules by copying the candidate to merge on top of the results of merging
                        # all rules so far with the same matcher
                        i = Iterator()
                        p = i.packet_in(p)
                        p = self.matchRulePatterns[self.transformation[layerIndex][candidateToMerge].name][1].packet_in(p)
                        mergedResultBeforeEquationEval = p.graph
                        
                        # check the result of merging the rules for consistency of equations over the attribute
                        if self.attributeEquationEvaluator(mergedResultBeforeEquationEval):
                        
                            mergedResult = mergedResultBeforeEquationEval
                            mergedResult.name = mergedResult.name + self.transformation[layerIndex][candidateToMerge].name                                                  
                            # mark the rule for removal
                            markedForRemoval.append(self.transformation[layerIndex][candidateToMerge])
   
                # copy the result of the merged or the unmerged rule to the merged layer              
                
                merged_layer.append(mergedResult)

                # merge backwardPatterns matchers for the merged rules
                # gather all the backwardPattern matchers from the rules that got merged
                # and are to be removed, only if any rule got merged during this pass
                   
                if len(markedForRemoval) > 1:                  
                    # rebuild the auxiliary structures
                    # matchRulePatterns
                    #self.matchRulePatterns[mergedResult.name] = self.matchRulePatterns[markedForRemoval[0].name]
                     
                    # rebuild the rule combinators and the matchers for the merged rule
                    pyramify = PyRamify(draw_svg=False)
                    
                    ruleToCreateMatcher = deepcopy(mergedResult)
                    self.matchRulePatterns.update(pyramify.get_match_pattern({ruleToCreateMatcher.name : ruleToCreateMatcher}))
                     
                    ruleToCreateCombinator = deepcopy(mergedResult)
                    self.ruleCombinators.update(pyramify.get_rule_combinators({ruleToCreateCombinator.name : ruleToCreateCombinator}))

                    ruleToCreateTraceChecker = deepcopy(mergedResult)
                    self.ruleTraceCheckers.update(pyramify.get_backward_patterns({ruleToCreateTraceChecker.name : ruleToCreateTraceChecker})[0])
                                      
                    # remove from the backwardPatterns dictionary the references to rules that got merged
                    for rule in markedForRemoval:
                        del self.matchRulePatterns[rule.name]
                        del self.ruleCombinators[rule.name]
                        del self.ruleTraceCheckers[rule.name]
 
                # remove the rules that got merged during the previous pass
                self.transformation[layerIndex] = [rule for rule in self.transformation[layerIndex] if rule not in markedForRemoval]                          
            # the layer has been treated and can be put back into the transformation               
            self.transformation[layerIndex] = merged_layer
        
        # now build the partial order of rules as a dictionary per layer
        # the keys are rules that are larger than the elements in the order

        layerpairs = []

        for layerIndex in range(0,len(self.transformation)):
            layerpairs.append(list(permutations(self.transformation[layerIndex],2)))
               
        ruleContainment = []
         
        for layerIndex in range(0,len(layerpairs)):
            ruleContainment.append({})
            for pair in layerpairs[layerIndex]:
                p = Packet()
                p.graph = pair[1]
                p = self.matchRulePatterns[pair[0].name][0].packet_in(p)
                if self.matchRulePatterns[pair[0].name][0].is_success:
                    # the partial order may branch, so we need lists to store the smaller elements
                    if pair[1] not in ruleContainment[layerIndex].keys():
                        ruleContainment[layerIndex][pair[1]] = [pair[0]]
                    else:
                        ruleContainment[layerIndex][pair[1]].append(pair[0])                     

        self.ruleContainment = ruleContainment
        
        if self.verbosity >= 2:
            print "Subsumption order between rules for all layers:"                   
            print self.ruleContainment
            print "\n"

        def get_subsumed_rules(rules, layer):
            requiredRules = []
            for rule in rules:
                if rule in set(self.ruleContainment[layer].keys()):
                    requiredRules = self.ruleContainment[layer][rule]
                    requiredRules.extend(get_subsumed_rules(self.ruleContainment[layer][rule], layer))
            return requiredRules
        
        # now go through all the layers and merge rules with all the rules that they subsume.
        # rules that subsume others become combined with them and their names have to be combined too, separated by underscores.
        # new combinators for each of the combined rules have to be created.
        # building the correct combination of rules in the layer is then done by the path condition construction algorithm.
        # TODO: this only solves overlaps between rules of the same layer. Overlaps between rules of different layers can
        # be achieved by reordering the rules in the transformation.
        

#         for layerIndex in range(len(self.transformation)):
#             rulesToAdd = []
#             matchRulePatternsToAdd = {}
#             combinatorsToAdd = {}
#             ruleTraceCheckersToAdd = {}
#             rulesToDelete = []
# 
#             for ruleIndex in range(len(self.transformation[layerIndex])):
#                 rule = self.transformation[layerIndex][ruleIndex]
#                 subsumedRules = get_subsumed_rules([self.transformation[layerIndex][ruleIndex]], layerIndex)
#                 
# #                 print "Rule: " + rule.name
# #                 print "Subsumed rules:"
# #                 print subsumedRules
#                 
#                 if subsumedRules != []:
#                     # combine the rule with all the rules it subsumes
#                     mergedResult = deepcopy(rule)
#                     for subRule in subsumedRules:                                                
#                         ruleMergerMatcher = self.matchRulePatterns[subRule.name][0]
#                         ruleMergerRewriter = self.matchRulePatterns[subRule.name][1]                        
#                         p = Packet()
#                         p.graph = mergedResult
#                         p = ruleMergerMatcher.packet_in(p)
#                         i = Iterator()
#                         p = i.packet_in(p)
#                         p = ruleMergerRewriter.packet_in(p)
#                         mergedResult.name += "_" + subRule.name
# 
#                     # now build the new combinator for the rule combined with the rules it subsumes
#                     pyramify = PyRamify(draw_svg=False)
# 
#                     ruleToCreateMatcher = deepcopy(mergedResult)
#                     matchRulePatternsToAdd.update(pyramify.get_match_pattern({ruleToCreateMatcher.name : ruleToCreateMatcher}))
# 
#                     ruleToCreateCombinator = deepcopy(mergedResult)
#                     combinatorsToAdd.update(pyramify.get_rule_combinators({ruleToCreateCombinator.name : ruleToCreateCombinator}))
#                     
#                     ruleToCreateTraceChecker = deepcopy(mergedResult)
#                     ruleTraceCheckersToAdd.update(pyramify.get_backward_patterns({ruleToCreateTraceChecker.name : ruleToCreateTraceChecker})[0]) 
#                     
#                     rulesToAdd.append(mergedResult)
#                     # store the original rules to delete and combinators to delete
#                     #combinatorsToDelete.append(rule.name)
#                     rulesToDelete.append(rule)      
#                     
#             # remove the rules that got merged from the layer
#             self.transformation[layerIndex] = [rule for rule in self.transformation[layerIndex] if rule not in rulesToDelete]               
#             # remove the combinators and the trace checkers for the rules that got merged from the layer
#             for rule in rulesToDelete:
#                 del self.matchRulePatterns[rule.name]
#                 del self.ruleCombinators[rule.name]
#                 del self.ruleTraceCheckers[rule.name]                    
#             
#             # now add to the layer the combined rules
#             self.transformation[layerIndex].extend(rulesToAdd)
#             # and the new match rule patterns
#             self.matchRulePatterns.update(matchRulePatternsToAdd)                
#             # and the new combinators
#             self.ruleCombinators.update(combinatorsToAdd)
#             # and the new trace checkers                  
#             self.ruleTraceCheckers.update(ruleTraceCheckersToAdd)
#             # reset the rules to delete for the next layer
#             rulesToDelete = []
#             # reset the combinators and the trace checkers to add for the next layer
#             combinatorsToAdd = {}
#             ruleTraceCheckersToAdd = {}

                            
        # TODO: now traceability is being built for all rules. We only need traceability for the rules that have no dependencies, 
        # as the others are built by the combinators associated to the rule

        # transformation to built traceability for rules
        from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import \
            HBuildTraceabilityForRuleLHS
        from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import \
            HBuildTraceabilityForRuleRHS

        build_traceability_for_rule = FRule(clean_graph(HBuildTraceabilityForRuleLHS()), clean_graph(HBuildTraceabilityForRuleRHS()))

        for layerIndex in range(0, len(self.transformation)):
            for ruleIndex in range(0, len(self.transformation[layerIndex])):
                p = Packet()
                p.graph = self.transformation[layerIndex][ruleIndex]
#                p = build_traceability_no_backward.packet_in(p)
#                p = build_traceability_with_backward.packet_in(p)
                p = build_traceability_for_rule.packet_in(p)


                self.transformation[layerIndex][ruleIndex] = clean_graph(p.graph)

                if self.draw_svg:
                    graph_to_dot("traced_" + self.transformation[layerIndex][ruleIndex].name , self.transformation[layerIndex][ruleIndex])

#         print "----------------------------"
#         print "Rule Combinators: "
#         print self.ruleCombinators.keys()
#         print "----------------------------"
# 
#         print "----------------------------"
#         print "Rule Trace Checkers: "
#         print self.ruleTraceCheckers.keys()
#         print "----------------------------"  
                    
        self.rule_names = {"HEmpty":"HEmptyPathCondition"}
        # keep the original names around 
        self.rule_originalnames = {"HEmpty":"HEmptyPathCondition"}
        # change rules names to be shorter
  
        for layer in range(len(self.transformation)):
            i = 0
            for rule in self.transformation[layer]:
                
#                 subsumedRuleNames = (rule.name.split("_"))
#                 beforeMergeName = subsumedRuleNames.pop(0) 
#                 new_name = "L" + str(layer) + "R" + str(i)
#                 original_new_name = new_name
#                 self.rule_originalnames[new_name] = beforeMergeName       
#                 for subName in subsumedRuleNames:
#                     print "----------> " + subName
#                     for subNewName in self.rule_names.keys():
#                         if self.rule_names[subNewName] == subName:
#                             new_name += "_" + subNewName

                new_name = "L" + str(layer) + "R" + str(i)
                                        
                i += 1
                self.rule_names[new_name] = rule.name
  
                self.ruleCombinators[new_name] = self.ruleCombinators[rule.name]
                del self.ruleCombinators[rule.name]
  
                self.ruleTraceCheckers[new_name] = self.ruleTraceCheckers[rule.name]
                del self.ruleTraceCheckers[rule.name]
  
                self.matchRulePatterns[new_name] = self.matchRulePatterns[rule.name]
                del self.matchRulePatterns[rule.name]
  
                rule.name = new_name

        if self.verbosity >= 2:                
            print "------------------------------------"
            print "Transformation: " 
            for l in range(len(self.transformation)):
                print "Layer " + str(l)
                for r in self.transformation[l]:
                    print "  " + self.rule_names[r.name]
            print "------------------------------------"
            print "\n"


#         print "------------------------------------"
#         print "Transformation: " 
#         print self.rule_names
#         print "------------------------------------"

            
#             # auxiliary function to order the nodes recursively, starting from the top nodes
#             def _build_ordered_rules(topRules):
#                 newTopRules = []
#                 for rule in topRules:
#                     if rule in set(self.partialOrder.keys()):
#                         newTopRules.extend(self.partialOrder[rule])
#                         orderedRules.extend(self.partialOrder[rule])
#                 
#                 if newTopRules != [] : _build_ordered_rules(newTopRules)
#             
#             # continue adding nodes as we go down the tree
#             _build_ordered_rules(topRules)

#             # remove from the layer the rules that need to be ordered
#             self.transformation[layerIndex] = list(set(self.transformation[layerIndex]) - set(orderedRules))   
#             # now place the reordered rules back in the layer, at the end
#             self.transformation[layerIndex].extend(list(reversed(orderedRules)))



    # @do_cprofile
    def build_path_conditions(self):     
        """
        Build the set of path conditions by combining rules of a given layer with the
        path conditions of the previous layer. The complete algorithm is described in:
        
        http://msdl.cs.mcgill.ca/people/levi/30_publications/files/A_Technique_for_Symbolically_Verifying_Properties_of_Model_Transf.pdf
        """


        pool = Pool()
        print("Pool: " + str(pool))


        self.num_path_conditions = 0

        from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition

        HEmptyPathCondition = clean_graph(HEmptyPathCondition())
        HEmptyPathCondition.name = "HEmpty"

        currentpathConditionSet = [HEmptyPathCondition.name]

        # start with a set (list) of path conditions containing only the empty path condition (declared in the constructor)
        # a path condition is a list of where the elements are rules (or combinations of rules) with traceability information

        if self.verbosity >= 1 : print("Start building path conditions")


        # store a dictionary from pc name to pc
        #pc_dict = {HEmptyPathCondition.name:HEmptyPathCondition}

        #global_hp.setref()

        pc_dict = PCDict(1000)

        #manager = Manager()
        #pc_dict = manager.dict()
        pc_dict[HEmptyPathCondition.name] = HEmptyPathCondition
        
        # now go through the layers one-by-one

        for layer in range(len(self.transformation)):

            # for each path condition built so far, combine it with each of the rules from the current layer

            #store the old length
            pathConSetLength = len(currentpathConditionSet)

            # the path condition set generated for the layer being treated starts off with the set of path
            # conditions generated for the previous layer
            
            # build a dictionary to remember which path condition in the current layer is built from
            # which path condition from the previous layer
            # This is needed because the layerPathCondAccumulator set keeps all path conditions generated
            # for the current layer, starting from the same set as the ones accumulated for the previous layer.
            # for every rule pass we need to know which path conditions for the current layer were built
            # from which path condition from the previous layer, since they are all in a vector.
            # this can be optimized by having a dictionary for each rule from the previous layer containing
            # the path conditions generated for it, instead of going though the whole vector each time.

            childrenPathConditions = {}
            for pc_name in currentpathConditionSet:
                childrenPathConditions[pc_name] = [pc_name]
            
            for pathConditionIndex in range(pathConSetLength):

                # for each rule in the current layer, combine it with the path condition.
                # start with the local path condition set with just a copy of the path condition being combined.

                pathCondition_name = currentpathConditionSet[pathConditionIndex]

                if not isinstance(pathCondition_name, str):
                    raise Exception("Not string")

                pathCondition = pc_dict[pathCondition_name]

#                 pathConditionCopy = deepcopy(self.pathConditionSet[pathCondition])
#                 pathCondAndRuleCombAccumulator = [pathConditionCopy]

                # hold the changes done to the original path condition through total matches of the rule, if any.
                # note that the original path condition being matched by the rules can never be changed as long as the rules in the layer are being matched on it
                changedPathCondition = deepcopy(pathCondition)
                
                for rule in self.transformation[layer]:
                    
                    if self.verbosity >= 2:
                        print "--------------------------------------"
                        print "Treating rule:"
                        print self.rule_names[rule.name]
                        print "Combining with:"
                        print "Path Condition:" + self.expand_pc_name(pathCondition.name)
                    if self.verbosity >= 1:
                        print "Number of Path Conditions generated so far: " +  str(len(currentpathConditionSet))
                        print "Number of Path Conditions to go in this layer: " +  str(pathConSetLength - pathConditionIndex)
                        
                    # first check if the rule requires any other rules to execute with it,
                    # in case of rule overlapping. If all the rules that are required to execute
                    # are already present in the path condition, then the rule executes.
                    # If they are not, then the combination is not possible and we can skip it.
                    
                    # function to return all the rules that have to execute if the current rule executes.
#                    requiredRules = self.calc_required([rule], layer)
                    
                    # now check if all the required rules exist in the path condition
                    # by checking the path condition's name. Note that "_" (underscore) is
                    # the rule name separator, so rules names cannot have underscores
                   
#                     combinationIsPossible = True                
#                     if requiredRules is not []:
#                         namesOfRulesinPathCond = pathCondition.name.split("_")
#                         for rule in requiredRules:
#                             if rule.name not in set(namesOfRulesinPathCond):
#                                 combinationIsPossible = False
#                     
#                     if not combinationIsPossible:
#                         if self.verbosity >= 2:
#                             print "Cannot combine: missing required rules that should have executed\
#                                     because they are subsumed by the executed rule!"                      
#                         continue                   


                    # possible cases of rule combination                    

                    ######################################
                    # Case 1: Rule has no dependencies
                    ######################################
                    
                    # the rule is disjointly added to the path condition
                    if self.ruleCombinators[rule.name] is None:
                        if self.verbosity >= 2 : print "Case 1: Rule has no dependencies"
                        
                        localPathConditionLayerAccumulator = []


                        num = 0
                        for child_pc_index in range(len(childrenPathConditions[pathCondition.name])):

                            child_pc_name = childrenPathConditions[pathCondition.name][child_pc_index]
                            
#                             # TODO: delete this when the overlapping is finished with the new algorithm
#                             # Check if the child being treated already contains the rule.
#                             # This happens if the match of a rule contains the match of another rule, in which case they need to execute together.
#                             # During the Pre-Process step rules are merged with rules they subsume to deal with this joint execution.
#                             # In the path condition construction algorithm this has to be taken into consideration by preventing path conditions
#                             # where a rule B subsumed by a rule A has already executed (meaning A merged with B already exists in the path condition),
#                             # that rule B executes again (or vice-versa)).
#                             # This is achieved by looking at whether the name of the path condition already includes the rule being executed now,
#                             # in which case the rule does not get executed over the path condition. Note that the rule executed may subsume others, in
#                             # which case all the names of subsumed rules have to be checked in the path condition name. 
#                             
#                             # get all the rule names in the name of the rule being executed (can be merged with subsumed rules).
#                             # also get the rule names of all rules already present in the path condition

#                             ruleNamesInRule = rule.name.split("_")
#                             ruleNamesInPC = child_pc_name.split("_")
#                             # cleanup the dashes from the rule names in the path condition
#                             for nameIndex in range(len(ruleNamesInPC)):
#                                 ruleNamesInPC[nameIndex] = ruleNamesInPC[nameIndex].split("-")[0]
                                                        
                            cpc = pc_dict[child_pc_name]

                            # create a new path condition which is the result of combining the rule with the current path condition being examined
                            newPathCond = deepcopy(cpc)
                            newPathCond = disjoint_model_union(newPathCond,rule)
                            # name the new path condition as the combination of the previous path condition and the rule
                            newPathCond.name = cpc.name + '_' + rule.name + "-" + str(num)
                            num += 1

                            pc_dict[newPathCond.name] = newPathCond

                            if self.verbosity >= 2 : print "Created path condition with name: " + newPathCond.name
                            localPathConditionLayerAccumulator.append(newPathCond.name)

                            # store the newly created path condition as a child
                            childrenPathConditions[pathCondition.name].append(newPathCond.name)

                        currentpathConditionSet.extend(localPathConditionLayerAccumulator)
                    
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
                        p.graph = pathCondition
                        ruleBackwardLinksMatcher.packet_in(p)
                        if not ruleBackwardLinksMatcher.is_success:
                            if self.verbosity >= 2 : print "Case 2: Rule has dependencies but cannot execute"

                        else:

                            #########################################################################
                            # Case 3: Rule has dependencies that may or will execute
                            #########################################################################

                            if self.verbosity >= 2 : print "Case 3: Rule has dependencies that may or will execute"

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
                                p.graph = pathCondition

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

                                    #go through all the children of this path condition
                                    num = 0
                                    for child_pc_index in range(len(childrenPathConditions[pathCondition.name])):

                                        #get the name of the child
                                        child_pc_name = childrenPathConditions[pathCondition.name][child_pc_index]

                                        if self.verbosity >= 2 :
                                            print "--> Combining with path condition: " + self.expand_pc_name(child_pc_name)

#                                         # only combine if the rule hasn't executed yet on that path condition
#                                                                     
#                                         # get all the rule names in the name of the rule being executed (can be merged with subsumed rules).
#                                         # also get the rule names of all rules already present in the path condition
#                                         ruleNamesInRule = rule.name.split("_")
#                                         ruleNamesInPC = child_pc_name.split("_")
#                                         # cleanup the dashes from the rule names in the path condition
#                                         for nameIndex in range(len(ruleNamesInPC)):
#                                             ruleNamesInPC[nameIndex] = ruleNamesInPC[nameIndex].split("-")[0]


                                        #get the path condition from the dictionary
                                        cpc = pc_dict[child_pc_name]

                                        # if the combinator is not the total one, make a copy of the path condition in the set
                                        # of combinations generated so far.
                                        # the total combinator is always the one at the end of the combinator list for the rule.

                                        # name the new path condition as the combination of the previous path condition and the rule
                                        newPathCondName = cpc.name + "_" + rule.name + "-" + str(num)
                                        num += 1

                                        newPathCond = deepcopy(cpc)

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

                                        if self.attributeEquationEvaluator(newPathCond):

                                        #if True:

                                            if isTotalCombinator:
                                                
                                                # because the rule combines totally with a path condition in the accumulator we just copy it
                                                # directly on top of the accumulated path condition

                                                #find the path condition and change its name
                                                #TODO: Make this faster
                                                for pathConditionIndex in range(len(currentpathConditionSet)):
                                                    if currentpathConditionSet[pathConditionIndex] == cpc.name:
                                                        currentpathConditionSet[pathConditionIndex] = newPathCond.name
     
                                                #change the child's name in the parent's array
                                                childrenPathConditions[pathCondition.name][child_pc_index] = newPathCond.name

                                            else:
                                                # we are dealing with a partial combination of the rule.
                                                # create a copy of the path condition in the accumulator because this match of the rule is partial.

                                                # add the result to the local accumulator
                                                partialTotalPathCondLayerAccumulator.append(newPathCond.name)

                                                # store the parent of the newly created path condition
                                                childrenPathConditions[pathCondition.name].append(newPathCond.name)

                                            # store the new path condition
                                            pc_dict[newPathCond.name] = newPathCond

#                                                 print "----------------------"
#                                                 print "Adding: " + newPathCond.name
#                                                 print "Parent is: " + parentPathCondition[layerPathCondAccumulator[currentPathCondition]]
#                                                 print "----------------------"

                                            if self.verbosity >= 2:
                                                print "Created path condition with name: " + self.expand_pc_name(newPathCond.name)

                                    currentpathConditionSet.extend(partialTotalPathCondLayerAccumulator)


            # when the layer treatment is finished the set of path conditions for the transformation can receive the
            # accumulated path condition set for the layer

        # h = global_hp.heap()
        # print("\nMemory usage:")
        # print(h)

        self.pc_dict = pc_dict
        self.currentpathConditionSet = currentpathConditionSet
        self.num_path_conditions = len(currentpathConditionSet)


    def get_all_path_conditions(self):
        path_conditions = []
        for pc in self.get_path_conditions():
            path_conditions.append(pc)
        return path_conditions

    def get_path_conditions(self):

        for pc_name in self.currentpathConditionSet:
            pc = self.pc_dict[pc_name]

            pc.name = self.expand_pc_name(pc_name)
            yield pc

    #@do_cprofile
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

    def expand_pc_name(self, name):
        new_name = ""
        for token in name.split("_"):
            token = token.split("-")[0]
            new_name += self.rule_names[token] + "_"
        new_name = new_name[:-1]
        return new_name

    def print_path_conditions_screen(self):
        for pathCondName in self.currentpathConditionSet:
            print("----------")
            print(self.expand_pc_name(pathCondName))
            
    def print_path_conditions_screen_real_name(self):
        for pathCondName in self.currentpathConditionSet:
            print("----------")
            print(pathCondName)


    def print_path_conditions_file(self):
        if self.draw_svg:
            i=0
            for pathCond in self.get_path_conditions():
                try:
                    print  ( str(i)+"---"+pathCond.name)
                    print  ( " ")
                    opname="pc"+str(i)
                    graph_to_dot(opname, pathCond, 1)
                    i=i+1
                except IOError:
                    print("Graph name is too long: " + pathCond.name)