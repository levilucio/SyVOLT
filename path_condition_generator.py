

from core.himesis_utils import clean_graph
from core.himesis_utils import set_do_pickle
from core.himesis_utils import set_compression
from core.himesis_utils import build_traceability

import math
import time

from util.Tester import Tester

import multiprocessing
from multiprocessing import Manager
from path_condition_generator_worker import *

from pruner.pruner import Pruner

from random import shuffle

from profiler import *
from string import ascii_uppercase

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
        - pathConditionSet: holds the set of path conditions. Starts off with the empty path condition.
        - ruleContainment: holds for each layer a lattice representing which match patterns for rules are included in those of other rules
        - verbosity: verbosity level (0 - no verbosity / 1 - verbose / 2 - debug)                          
    """

    #@do_cprofile
    def __init__(self, transformation, targetMM, ruleCombinators, ruleTraceCheckers, overlappingRules, subsumption, loopingRuleSubsumption, args):

        self.print_memory_usage = True


        self.do_parallel = args.do_parallel
        self.num_threads = args.num_threads

        set_do_pickle(args.do_pickle)
        set_compression(args.compression)

        from core.new_match_algo import NewHimesisMatcher
        NewHimesisMatcher.use_old_match_gen = args.old_match_gen


        self.transformation = transformation
        self.targetMM = targetMM
        self.ruleCombinators = ruleCombinators
        self.ruleTraceCheckers = ruleTraceCheckers
        self.overlappingRules = overlappingRules
        self.subsumption = subsumption
        self.loopingRuleSubsumption = loopingRuleSubsumption 
        
        self.rulesRequiringDisambiguation = {}

        self.ruleContainment = []

        self.pc_dict = {}
        self.currentpathConditionSet = []
        self.num_path_conditions = 0

        self.verbosity = args.verbosity

        self.show_progress_bar = args.show_progress_bar

        #with PyCallGraph(output=GraphvizOutput()):
        self._pre_process()

        self.prunner = Pruner(args.do_pruning, self.targetMM, self.transformation, self.rule_names, self.rules_in_pc_name)

        self.tester = Tester(args)
        self.tester.set_artifacts(self.transformation, self.ruleTraceCheckers, self.ruleCombinators,
                                  self.rule_names)

        self.tester.debug()

        self.use_bin_packing = not args.shuffle

        self.max_chunk_size = args.max_chunk_size
        self.min_chunk_size = args.min_chunk_size

    def generate_letters(self, i):

        if i <= 25:
            return ascii_uppercase[i]
        else:
            i -= 26
            return self.generate_letters(int(i%26)) + str(int(i/26))



    #@do_cprofile
    def _pre_process(self):
        """
        1) Forward the cardinalities to the apply part of the rules
        2) Merge rules of the same layer that share common match patterns over those match patterns (G- while merging their cardinalities too using cardinality algebra ?)
        3) G - Build traceability links for merged rules
        """



        if self.verbosity >= 1:
            print("----------------Start pre-process")

        #remove empty layers
        new_transformation = []
        for layer in range(len(self.transformation)):
            new_layer = [rule for rule in self.transformation[layer]]
            if new_layer:
                new_transformation.append(new_layer)
        self.transformation = new_transformation



                            
        # now traceability is being built for all rules. We only need traceability for the rules that have no dependencies,
        # as the others are built by the combinators associated to the rule

        if self.verbosity >= 1:
            print("Start building traceability for rules")
        # transformation to built traceability for rules


        for layerIndex in range(0, len(self.transformation)):
            for ruleIndex in range(0, len(self.transformation[layerIndex])):
                self.transformation[layerIndex][ruleIndex] = build_traceability(self.transformation[layerIndex][ruleIndex])


        if self.verbosity >= 1:
            print("Start changing rule names")
            
        self.rule_names = {"Em":"HEmptyPathCondition"}
        # keep the original names around 
        self.shortened_rule_names = {"HEmptyPathCondition":"Em"}
        # change rules names to be shorter

        rule_num = 0

        for layer in range(len(self.transformation)):
            i = 0
            subsumedRulesInLayer = []
            subsumingRulesInLayer = []

            for rule in self.transformation[layer]:
 
                new_name = "" + str(layer) + "R" + str(i)

                #new_name = str(self.generate_letters(rule_num))

                rule_num += 1

                i += 1
                self.rule_names[new_name] = rule.name
                self.shortened_rule_names[rule.name] = new_name
   
                self.ruleCombinators[new_name] = self.ruleCombinators[rule.name]
                del self.ruleCombinators[rule.name]
   
                self.ruleTraceCheckers[new_name] = self.ruleTraceCheckers[rule.name]
                del self.ruleTraceCheckers[rule.name]
                
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
                    short_rule_name = self.shortened_rule_names[ruleName]
                    self.overlappingRules[subsumedRule][subsumingRuleIndex] = short_rule_name
            
            # remove this when layer is ordered        
            for subsumedRule in subsumingRulesInLayer:
                for subsumingRuleIndex in range(len(self.subsumption[subsumedRule])):
                    ruleName = self.subsumption[subsumedRule][subsumingRuleIndex]
                    try:
                        short_rule_name = self.shortened_rule_names[ruleName]
                    except:
                        #TODO: Fix this Exception
                        short_rule_name = ruleName
                    self.subsumption[subsumedRule][subsumingRuleIndex] = short_rule_name

                    
        # change the names of the rules in a subsumption loop

        for loop in self.loopingRuleSubsumption:
            for ruleIndex in range(len(loop)):
                newRuleName = None
                for newRuleNameIter in self.rule_names.keys():
                    if loop[ruleIndex] == self.rule_names[newRuleNameIter]:
                        newRuleName = newRuleNameIter
                        break
                loop[ruleIndex] = newRuleName


        if self.verbosity >= 2:                
            print("------------------------------------")
            print("Transformation: " )
            for l in range(len(self.transformation)):
                print("Layer " + str(l))
                for r in self.transformation[l]:
                    print("  " + self.rule_names[r.name])
            print("------------------------------------")
            print("\n")


    def get_artifacts_for_layer(self, artifact_dict, rules_in_layer, do_deletion = True):
        return_dict = {}
        found_rules = []
        for rule, rcs in artifact_dict.items():
            if rule in rules_in_layer:
                return_dict[rule] = rcs
                found_rules.append(rule)
        if do_deletion:
            for rule in found_rules:
                del artifact_dict[rule]
        return return_dict

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
        HEmptyPathCondition.name = "Em.0"

        currentpathConditionSet = [HEmptyPathCondition.name]

        # store a dictionary from pc name to pc
        pc_dict = {HEmptyPathCondition.name : shrink_graph(HEmptyPathCondition)}

        # start with a set (list) of path conditions containing only the empty path condition (declared in the constructor)
        # a path condition is a list of where the elements are rules (or combinations of rules) with traceability information


        if self.verbosity >= 1 : print("Start building path conditions")


        if not self.do_parallel:
            print("Restricting to one thread")
            cpu_count = 1
        else:
            if self.num_threads > 0:
                cpu_count = self.num_threads
            else:
                cpu_count = multiprocessing.cpu_count()
            print("CPU Count: " + str(cpu_count))

        try:
            import psutil as psutil
        except ImportError:
            print("Warning: psutil not found")
            self.print_memory_usage = False
            psutil = None

        manager = Manager()

        # now go through the layers one-by-one

        start_time = time.time()

        pc_divide_time = 0

        for layer in range(len(self.transformation)):
            print("Layer: " + str(layer + 1) + "/" + str(len(self.transformation)) + " at time " + str(time.time() - start_time))

            #store the old length
            pathConSetLength = len(currentpathConditionSet)

            name_dict = {}

            chunkSize = int(math.ceil(pathConSetLength / float(cpu_count)))

            print("Path Cond Set Size: " + str(pathConSetLength))

            #layer_start_time = time.time()

            if self.use_bin_packing:
                pc_divide_start_time = time.time()

                if not self.do_parallel:
                    number_of_bins = 1
                    chunkSize = pathConSetLength
                elif chunkSize < self.min_chunk_size:
                    number_of_bins = int(math.ceil(pathConSetLength / float(self.min_chunk_size)))
                    chunkSize = self.min_chunk_size
                elif chunkSize > self.max_chunk_size:
                    number_of_bins = int(math.ceil(pathConSetLength / float(self.max_chunk_size)))
                    chunkSize = self.max_chunk_size
                else:
                    number_of_bins = cpu_count

                pc_chunks = [[] for _ in range(number_of_bins)]
                pc_count = [0] * number_of_bins

                pc_with_weights = [[pc, int(pc.split(".")[1])] for pc in currentpathConditionSet]

                pc_with_weights.sort(key=lambda x: x[1])

                for pc, weight in pc_with_weights:

                    min_index = pc_count.index(min(pc_count))

                    pc_chunks[min_index].append(pc)
                    pc_count[min_index] += weight

                pc_chunks = [sorted(chunk) for chunk in pc_chunks if chunk]
                #print(pc_chunks)

                pc_divide_time += time.time() - pc_divide_start_time
            else:
                # divide the path conditions up into little pieces
                pc_divide_start_time = time.time()
                shuffle(currentpathConditionSet)
                pc_chunks = self.chunks(currentpathConditionSet, chunkSize)
                pc_divide_time += time.time() - pc_divide_start_time

            #only give the workers exactly the artifacts they need

            layer_rules = self.transformation[layer]

            rules_in_layer = [rule.name for rule in self.transformation[layer]]

            layer_rule_combinators = self.get_artifacts_for_layer(self.ruleCombinators, rules_in_layer)
            layer_rule_trace_checkers = self.get_artifacts_for_layer(self.ruleTraceCheckers, rules_in_layer)
            layer_rule_overlapping_rules = self.get_artifacts_for_layer(self.overlappingRules, rules_in_layer, do_deletion = False)

            #calculate the overlapping rules for this layer
            ruleNamesInLayer = [rule.name for rule in self.transformation[layer]]
            rulesForSecondPhase = sorted(set(self.overlappingRules.keys()).intersection(ruleNamesInLayer))

            # print("Rules for Second Phase:")
            # print(rulesForSecondPhase)

            rulesToTreat = []

            # build the set of rules that remains to be executed
            for l in range(layer + 1, len(self.transformation)):
                for r in self.transformation[l]:
                    rulesToTreat.append(r.name)

            rulesToTreat += list(rulesForSecondPhase)



            print("Starting " + str(len(pc_chunks)) + " workers with chunk size: " + str(chunkSize))

            workers = []
            worker_result_list = []

            #initialize the workers
            for i in range(len(pc_chunks)):#range(cpu_count):


                #print("Chunk size: " + str(len(pc_chunks[i])))
                
                new_worker = path_condition_generator_worker(layer_rules, rulesToTreat, rulesForSecondPhase, self.prunner, layer, layer * 1000 + i,
                                                             False, self.verbosity)

                new_worker.daemon = True

                new_worker.currentPathConditionSet = pc_chunks[i]#pc_queue

                #print("Size of chunk: " + str(len(pc_chunks[i])))

                worker_list = manager.list([None, None, None])
                worker_result_list.append(worker_list)
                new_worker.worker_list = worker_list

                new_worker.load_pc_dict(pc_dict)


                new_worker.rule_names = self.rule_names


                new_worker.ruleCombinators = layer_rule_combinators
                new_worker.ruleTraceCheckers =  layer_rule_trace_checkers
                new_worker.overlappingRules = layer_rule_overlapping_rules
                new_worker.subsumption = self.subsumption
                new_worker.loopingRuleSubsumption = self.loopingRuleSubsumption

                workers.append(new_worker)


            worker_chunks = self.chunks(workers, cpu_count)
            total_rounds = len(worker_chunks) - 1
            for curr_round, ws in enumerate(worker_chunks):
                for i, worker in enumerate(ws):
                    if i == 0 and self.show_progress_bar:
                        worker.report_progress = True
                    worker.start()

                #print("Time to start layer: " + str(time.time() - layer_start_time))

                round_start_time = time.time()
                for worker in ws:
                    worker.join()
                round_time = time.time() - round_start_time

                rounds_remaining = total_rounds - curr_round
                print("Round " + str(curr_round + 1) + "/" + str(total_rounds + 1) + " took {:.2f} seconds".format(round_time))

                if rounds_remaining > 0 and round_time > 0:
                    layer_time = round_time * rounds_remaining
                    print("Time remaining in layer " + str(layer + 1) + "/" + str(len(self.transformation)) + ": {:.2f}".format(layer_time) + " seconds = {:.2f} minutes".format(layer_time/60))

                if self.print_memory_usage:
                    memory_percent = psutil.virtual_memory()[2]
                    print("Memory usage percent: {:.2f} %".format(memory_percent))

            layer_finish_time = time.time()

            currentpathConditionSet = []

            for worker_list in worker_result_list:
                r = worker_list
                currentpathConditionSet.extend(r[0])

                pc_dict.update(r[1])

                name_dict.update(r[2])

            currentpathConditionSet.sort()


            if len(name_dict) > 0:
                for i in range(len(currentpathConditionSet)):
                    try:
                        pc_name = currentpathConditionSet[i]
                        currentpathConditionSet[i] = name_dict[pc_name]

                        delete_graph(pc_name)

                        #print("Changed " + pc_name + " to " + name_dict[pc_name])

                    except KeyError:
                        pass

            self.currentpathConditionSet = currentpathConditionSet
            self.pc_dict = pc_dict
            self.tester.check_rule_reachability(self, layer)

            #print(asizeof.asized(self.pc_dict, detail = 4).format())

            print("Time to finish layer: " + str(time.time() - layer_finish_time))
            print("========================\n")

        # h = global_hp.heap()
        # print("\nMemory usage:")
        # print(h)

        self.pc_dict = pc_dict
        self.currentpathConditionSet = currentpathConditionSet
        self.num_path_conditions = len(currentpathConditionSet)

        print("Time taken for: -Dividing pcs- " + str(pc_divide_time) + " seconds")
        #print("Time taken for: -Pruning pcs- " + str(self.prunner.pruning_time) + " seconds")

    #clean up
    def __del__(self):
        #print("Destructor")

        # import os
        # d = "./pickle"
        # size = sum(os.path.getsize(d+"/"+f) for f in os.listdir(d))
        # print("Size of pickle dir: " + str(size/1000000) + "MB")

        #TODO: Make cleanup argument for test script
        pass
        # for pc_name in self.currentpathConditionSet:
        #     delete_graph(pc_name)

        # size = sum(os.path.getsize(d + "/" + f) for f in os.listdir(d))
        # print("Size of pickle dir: " + str(size / 1000000) + "MB")

        # for f in os.listdir(d):
        #     graph = expand_graph(f)
        #     print(graph.name)

    def load_saved_pcs(self, new_pc_dict):

        self.pc_dict = new_pc_dict
        self.currentpathConditionSet = list(sorted(new_pc_dict.keys()))
        self.num_path_conditions = len(self.currentpathConditionSet)


    def get_all_path_conditions(self):
        path_conditions = []
        for pc in self.get_path_conditions():
            path_conditions.append(pc)
        return path_conditions

    def get_path_conditions(self, expand=True, get_pretty_name = True):

        for pc_name in sorted(self.currentpathConditionSet):
            pc = self.pc_dict[pc_name]

            if expand:
                pc = expand_graph(pc)

            if get_pretty_name:
                pc_name = self.expand_pc_name_with_multiple_applications(pc_name)
        
            yield pc, pc_name


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

    def rules_in_pc_real_name(self, name):
        return [self.rule_names[n] for n in self.rules_in_pc_name(name)]


    def rules_in_pc_name(self, name):
        rules = []
        name = name.split(".")[0]
        for token in name.split("_"):
            if "-" in token:
                rulename = token.split("-")[0]
                rules.append(rulename)
            else:
                rules.append(token)
        return rules

    def expand_pc_name_with_multiple_applications(self, name):
        new_name = ""
        name = name.split(".")[0]
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
        name = name.split(".")[0]
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
        print("Drawing path conditions:")
        for pathCond, name in self.get_path_conditions():
            try:
                
                graph_to_dot(name, pathCond)
                #i=i+1
            except IOError:
                print("Graph name is too long: " + name)
                

                    
                
