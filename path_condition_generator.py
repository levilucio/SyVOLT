
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
from core.himesis_utils import set_do_pickle
from core.himesis_utils import set_compression

from core.himesis_plus import *

#from core.himesis import Himesis

import math
import time

#from PCDict import PCDict

from copy import deepcopy

#from solver.prolog_attribute_equation_evaluator import PrologAttributeEquationEvaluator
from solver.simple_attribute_equation_evaluator import SimpleAttributeEquationEvaluator

from PyRamify import PyRamify
from PropertyProverTester import PropertyProverTester

import multiprocessing
from multiprocessing import Manager, Queue
from path_condition_generator_worker import *

from random import shuffle

from profiler import *


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
    def __init__(self, transformation, targetMM, ruleCombinators, ruleTraceCheckers, matchRulePatterns, overlappingRules, subsumption, loopingRuleSubsumption, args):

        # the empty path condition

        self.draw_svg = args.draw_svg
        self.run_tests = args.run_tests

        self.do_parallel = args.do_parallel

        set_do_pickle(args.do_pickle)
        set_compression(args.compression)

        self.transformation = transformation
        self.targetMM = targetMM
        self.ruleCombinators = ruleCombinators
        self.ruleTraceCheckers = ruleTraceCheckers
        self.matchRulePatterns = matchRulePatterns
        self.overlappingRules = overlappingRules
        self.subsumption = subsumption
        self.loopingRuleSubsumption = loopingRuleSubsumption
        
        self.rulesRequiringDisambiguation = {}

        self.ruleContainment = []

        self.verbosity = args.verbosity
        
        self.attributeEquationEvaluator = SimpleAttributeEquationEvaluator(self.verbosity)

        #with PyCallGraph(output=GraphvizOutput()):
        self._pre_process()

        self.debug()


    def print_transformation(self):
        for layer in self.transformation:
            for rule in layer:
                graph_to_dot("rule_" + str(self.rule_names[rule.name]), rule)
                self.rules.append(rule.name)

    def print_ruleCombinators(self):
        for key in self.rules:

            if not self.ruleCombinators[key]:
                continue

            value = self.ruleCombinators[key]
            for (m, r) in value:
                graph_to_dot("ruleCombinator_match_" + str(m.condition.name), m.condition)
                graph_to_dot("ruleCombinator_rewrite_" + str(r.condition.name), r.condition)

                if len(m.condition.NACs) > 0:
                    graph_to_dot("ruleCombinator_NAC_" + str(m.condition.name), m.condition.NACs[0])


    def print_ruleTraceCheckers(self):
        for key in self.rules:
            if self.ruleTraceCheckers[key] is None:
                continue

            tc = self.ruleTraceCheckers[key]
            graph_to_dot("traceChecker_" + str(tc.condition.name), tc.condition)

    def print_matchRulePatterns(self):
        for key in self.rules:
            if self.matchRulePatterns[key] is None:
                continue

            matcher, rewriter = self.matchRulePatterns[key]
            graph_to_dot("matchPattern_matcher_" + str(matcher.condition.name), matcher.condition)
            graph_to_dot("matchPattern_rewriter_" + str(rewriter.condition.name), rewriter.condition)


    def debug(self):         

        if self.draw_svg:
            print("Drawing svgs...")
            self.rules = []
            self.print_transformation()
            self.print_ruleCombinators()
            self.print_ruleTraceCheckers()
            self.print_matchRulePatterns()

        if self.run_tests:
            ppt = PropertyProverTester()
            ppt.set_artifacts(self.transformation, self.ruleTraceCheckers, self.matchRulePatterns, self.ruleCombinators, self.rule_names)
 
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

        if self.verbosity >= 1:
            print("----------------Start pre-process")
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

                            
        # TODO: now traceability is being built for all rules. We only need traceability for the rules that have no dependencies, 
        # as the others are built by the combinators associated to the rule

        if self.verbosity >= 1:
            print("Start building traceability for rules")
        # transformation to built traceability for rules
        from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import \
            HBuildTraceabilityForRuleLHS
        from property_prover_rules.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import \
            HBuildTraceabilityForRuleRHS

        build_traceability_for_rule = ARule(clean_graph(HBuildTraceabilityForRuleLHS()), clean_graph(HBuildTraceabilityForRuleRHS()))

        for layerIndex in range(0, len(self.transformation)):
            for ruleIndex in range(0, len(self.transformation[layerIndex])):
                while True:
                    p = Packet()
                    p.graph = self.transformation[layerIndex][ruleIndex]
                    p = build_traceability_for_rule.packet_in(p)
                    if not build_traceability_for_rule.is_success:
                        break


                self.transformation[layerIndex][ruleIndex] = clean_graph(p.graph)

#         print("----------------------------")
#         print("Rule Combinators: ")
#         print(self.ruleCombinators.keys())
#         print("----------------------------")
# 
#         print("----------------------------")
#         print("Rule Trace Checkers: ")
#         print(self.ruleTraceCheckers.keys())
#         print("----------------------------"  )
                    
        if self.verbosity >= 1:
            print("Start changing rule names")
            
        self.rule_names = {"HEmpty":"HEmptyPathCondition"}
        # keep the original names around 
        self.rule_originalnames = {"HEmpty":"HEmptyPathCondition"}
        # change rules names to be shorter   
        for layer in range(len(self.transformation)):
            i = 0
            subsumedRulesInLayer = []
            subsumingRulesInLayer = []
            for rule in self.transformation[layer]:
 
                new_name = "L" + str(layer) + "R" + str(i)
                                         
                i += 1
                self.rule_names[new_name] = rule.name
   
                self.ruleCombinators[new_name] = self.ruleCombinators[rule.name]
                del self.ruleCombinators[rule.name]
   
                self.ruleTraceCheckers[new_name] = self.ruleTraceCheckers[rule.name]
                del self.ruleTraceCheckers[rule.name]
   
                self.matchRulePatterns[new_name] = self.matchRulePatterns[rule.name]
                del self.matchRulePatterns[rule.name]
                
                if rule.name in self.overlappingRules.keys():
                    self.overlappingRules[new_name] = self.overlappingRules[rule.name]
                    del self.overlappingRules[rule.name]
                    subsumedRulesInLayer.append(new_name)
                
                #remove this when layer is ordered
                if rule.name in self.subsumption.keys():
                    self.subsumption[new_name] = self.subsumption[rule.name]
                    del self.subsumption[rule.name]
                    subsumingRulesInLayer.append(new_name)
                   
                rule.name = new_name
                
            # now that the layer renaming is complete, change the names of the subsuming rules for rules that need overlap treatment

            for subsumedRule in subsumedRulesInLayer:
                for subsumingRuleIndex in range(len(self.overlappingRules[subsumedRule])):
                    ruleName = self.overlappingRules[subsumedRule][subsumingRuleIndex]
                    newRuleName = None
                    for newRuleNameIter in self.rule_names.keys():
                        if ruleName == self.rule_names[newRuleNameIter]:
                            newRuleName = newRuleNameIter
                            break
                    self.overlappingRules[subsumedRule][subsumingRuleIndex] = newRuleName
            
            # remove this when layer is ordered        
            for subsumedRule in subsumingRulesInLayer:
                for subsumingRuleIndex in range(len(self.subsumption[subsumedRule])):
                    ruleName = self.subsumption[subsumedRule][subsumingRuleIndex]
                    newRuleName = None
                    for newRuleNameIter in self.rule_names.keys():
                        if ruleName == self.rule_names[newRuleNameIter]:
                            newRuleName = newRuleNameIter
                            break
                    self.subsumption[subsumedRule][subsumingRuleIndex] = newRuleName

                    
        # change the names of the rules in a subsumption loop

        for loop in self.loopingRuleSubsumption:
            for ruleIndex in range(len(loop)):
                newRuleName = None
                for newRuleNameIter in self.rule_names.keys():
                    if loop[ruleIndex] == self.rule_names[newRuleNameIter]:
                        newRuleName = newRuleNameIter
                        break
                loop[ruleIndex] = newRuleName
                    
#         # calculate the set of rules the require disambiguation.
#         # these are the rules that have elements in the match part connected to two or more backward links.
#         # keep in the dictionary the name of the rule and the element(s) that require disambiguation
# 
#         for layerIndex in range(len(self.transformation)):
#             for ruleIndex in range(len(self.transformation[layerIndex])):
#                 rule = self.transformation[layerIndex][ruleIndex]
#                 matchContainsNodes = find_nodes_with_mm(rule, ["match_contains"])
#                 matchNodes = [rule.neighbors(node,"out")[0] for node in matchContainsNodes]
#                 
#                 for mNode in matchNodes:
#                     matchOutgoingNodes = rule.neighbors(rule.vs[mNode],"in")                    
#                     backLinks = [node for node in matchOutgoingNodes if rule.vs[node]["mm__"] == "backward_link"]
#                     
#                     if len(backLinks) > 1:
#                         if rule.name not in self.rulesRequiringDisambiguation.keys():
#                             self.rulesRequiringDisambiguation[rule.name] = [rule.vs[mNode]["mm__"]]
#                         else:
#                             self.rulesRequiringDisambiguation[rule.name].append(rule.vs[mNode]["mm__"])
                            
#         print("Rules requiring disambiguation:" + str(self.rulesRequiringDisambiguation))
#         print("\n")
        

        if self.verbosity >= 2:                
            print("------------------------------------")
            print("Transformation: " )
            for l in range(len(self.transformation)):
                print("Layer " + str(l))
                for r in self.transformation[l]:
                    print("  " + self.rule_names[r.name])
            print("------------------------------------")
            print("\n")


#         print("------------------------------------")
#         print("Transformation: " )
#         print(self.rule_names)
#         print("------------------------------------")

            
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


    def chunks(self, l, n):
        n = max(1, n)
        return [l[i:i+n] for i in range(0, len(l), n)]

    #@do_cprofile
    #@profile
    def build_path_conditions(self):     
        """
        Build the set of path conditions by combining rules of a given layer with the
        path conditions of the previous layer. The complete algorithm is described in:
        
        http://msdl.cs.mcgill.ca/people/levi/30_publications/files/A_Technique_for_Symbolically_Verifying_Properties_of_Model_Transf.pdf
        """


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



        manager = Manager()
        cpu_count = multiprocessing.cpu_count()
#        cpu_count = 1
        print("CPU Count: " + str(cpu_count))


        pc_dict = {}#manager.dict()





        #pc_dict = PCDict(1000)

        pc_dict[HEmptyPathCondition.name] = shrink_graph(HEmptyPathCondition)
        
        # now go through the layers one-by-one

        start_time = time.time()

        for layer in range(len(self.transformation)):
            if self.verbosity > 0:
                print("Layer: " + str(layer + 1) + " at time " + str(time.time() - start_time))

            # for each path condition built so far, combine it with each of the rules from the current layer

            #store the old length
            pathConSetLength = len(currentpathConditionSet)

            name_dict = {}

            chunkSize = int(math.ceil(pathConSetLength / float(cpu_count)))                             

            print("Path Cond Set Size: " + str(pathConSetLength))
            print("Chunksize: " + str(chunkSize))


            use_bin_packing = True
            sort_time = time.time()

            if use_bin_packing:
                pc_chunks = [[] for i in range(cpu_count)]
                pc_count = [0] * cpu_count

                for pc in currentpathConditionSet:
                    weight = len(pc)

                    min_index = pc_count.index(min(pc_count))

                    pc_chunks[min_index].append(pc)
                    pc_count[min_index] += weight
            else:
                shuffle(currentpathConditionSet)
                pc_chunks = self.chunks(currentpathConditionSet, chunkSize)


            print("Time to sort: " + str(time.time() - sort_time))
            #name_dict = manager.dict()

            #print("After ceil: " + str(math.ceil(pathConSetLength / float(cpu_count))))


            workers = []

            #chunk_time = time.time()
            #divide the path conditions up into little pieces


            #print("Time to chunk: " + str(time.time() - chunk_time))

            results_queue = manager.Queue()


            #initialize the workers
            for i in range(len(pc_chunks)):#range(cpu_count):
                #worker_time = time.time()

                #only one thread should print a progress bar
                if i == 0:
                    report_progress = True
                else:
                    report_progress = False

                #print("Chunk size: " + str(len(pc_chunks[i])))
                
                
                
                new_worker = path_condition_generator_worker(self.transformation, self.targetMM, layer,\
                                                             layer*1000+i, report_progress, self.verbosity)
                new_worker.currentPathConditionSet = pc_chunks[i]#pc_queue
                new_worker.attributeEquationEvaluator = self.attributeEquationEvaluator

                #print("Size of chunk: " + str(len(pc_chunks[i])))

                new_worker.results_queue = results_queue

                new_worker.pc_dict = pc_dict

                #new_worker.verbosity = self.verbosity
                #new_worker.layer = layer
                #new_worker.transformation = self.transformation

                new_worker.rule_names = self.rule_names


                #new_worker.name_dict = name_dict


                new_worker.ruleCombinators = self.ruleCombinators
                new_worker.ruleTraceCheckers =  self.ruleTraceCheckers
                new_worker.overlappingRules = self.overlappingRules
                new_worker.subsumption = self.subsumption
                new_worker.loopingRuleSubsumption = self.loopingRuleSubsumption



                workers.append(new_worker)

                #print("Time to initialize worker: " + str(time.time() - worker_time))


            #worker_start_time = time.time()
            for worker in workers:
                worker.start()

            #print("Time to start workers: " + str(time.time() - worker_start_time))


            for worker in workers:
                worker.join()


            #result_time = time.time()

            currentpathConditionSet = []

            for worker in workers:
                r = results_queue.get()
                currentpathConditionSet.extend(r[0])

                pc_dict.update(r[1])

                name_dict.update(r[2])

            #print("Time to collect results: " + str(time.time() - result_time ))

            #change_names_time = time.time()
            if len(name_dict.keys()) > 0:
                for i in range(len(currentpathConditionSet)):
                    try:
                        pc_name = currentpathConditionSet[i]
                        currentpathConditionSet[i] = name_dict[pc_name]
                        #print("Changed " + pc_name + " to " + name_dict[pc_name])

                    except KeyError:
                        pass


            #print("PC Dict Keys: " + str(pc_dict.keys()))
            #print("Time to change names: " + str(time.time() - change_names_time))
            #print("PC Length: " + str(len(currentpathConditionSet)))



        # h = global_hp.heap()
        # print("\nMemory usage:")
        # print(h)

        cleanup_time = time.time()
        self.pc_dict = pc_dict
        self.currentpathConditionSet = currentpathConditionSet
        self.num_path_conditions = len(currentpathConditionSet)

        print("Time to finish up: " + str(time.time() - cleanup_time))


    def get_all_path_conditions(self):
        path_conditions = []
        for pc in self.get_path_conditions():
            path_conditions.append(pc)
        return path_conditions

    def get_path_conditions(self):

        for pc_name in sorted(self.currentpathConditionSet):
            
            #print("-> " + pc_name)
            
            pc = expand_graph(self.pc_dict[pc_name])
            pc.name = self.expand_pc_name_with_multiple_applications(pc_name)
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

    def expand_pc_name_with_multiple_applications(self, name):
        new_name = ""
        for token in name.split("_"):
            if "-" in token:
                rulename = token.split("-")[0]
                number = token.split("-")[1]
                new_name += self.rule_names[rulename] + "-" + str(number) + "_"
            else:
                new_name = self.rule_names[token] + "_"
        new_name = new_name[:-1]
        return new_name

    def expand_pc_name(self, name):
        new_name = ""
        for token in name.split("_"):
            token = token.split("-")[0]
            new_name += self.rule_names[token] + "_"
        new_name = new_name[:-1]
        return new_name

    def print_path_conditions_screen(self):
        pathCondNames = [self.expand_pc_name_with_multiple_applications(pathCondName) for pathCondName in self.currentpathConditionSet]
        for pathCondName in sorted(pathCondNames):
            print("----------")
            print(pathCondName)
            
    def print_path_conditions_screen_real_name(self):
        for pathCondName in self.currentpathConditionSet:
            print("----------")
            print(pathCondName)


    def print_path_conditions_file(self):
        print("Printing path conditions:")
        for pathCondName in self.currentpathConditionSet:
            name = pathCondName.translate(None, '-')
            try:
                
                graph_to_dot(name, expand_graph(self.pc_dict[pathCondName]))
                #i=i+1
            except IOError:
                print("Graph name is too long: " + pathCondName)
                
    def check_rule_reachability(self):
        print("Checking Reachability: ")
        for layer in self.transformation:
            for rule in layer:
                ruleNotFound = True
                for pc_name in sorted(self.currentpathConditionSet):

                    if rule.name in pc_name:
                        print("Found: " + rule.name + " (" + self.rule_names[rule.name] + ")")
                        ruleNotFound = False
                        break
                if ruleNotFound: 
                    print("Could not find: " + rule.name + " (" + self.rule_names[rule.name] + ")")
                
                    
                
