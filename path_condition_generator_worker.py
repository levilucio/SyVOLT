
from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.iterator import Iterator

from t_core.tc_python.srule import SRule
from t_core.tc_python.frule import FRule

import time

from multiprocessing import Process
from core.himesis_utils import expand_graph, shrink_graph, delete_graph, disjoint_model_union, print_graph, graph_to_dot, get_preds_and_succs

from copy import deepcopy

from solver.simple_attribute_equation_evaluator import SimpleAttributeEquationEvaluator
from solver.simple_attribute_equation_evaluator import is_consistent

import numpy.random as nprnd

from profiler import *
from util.progress import ProgressBar

from PCDict import PCDict

#needed to use kernprof
class DummyProcess:
    def join(self):
        pass

    def start(self):
        self.run()

class path_condition_generator_worker(Process):

    def __init__(self, transformation, pruner, layer, num, report_progress, verbosity):
        super(path_condition_generator_worker, self).__init__()
        self.transformation = transformation
        self.layer = layer
        self.num = num
        self.currentPathConditionSet = None
        self.results_queue = None
        self.verbosity = verbosity

        #self.attributeEquationEvaluator = SimpleAttributeEquationEvaluator(verbosity)

        nprnd.seed(num)

        self.report_progress = report_progress
        
        self.pruner = pruner
        
        self.pruning = True

        self.pc_dict = None



    def load_pc_dict(self, pcs):

        #print("PC length: " + str(len(pcs)))

        self.pc_dict = PCDict(pcs)
        
        
    def getRuleNamesInPathCondition(self, pcName):
        ruleNames = []
        for token in pcName.split("_"):
            if token == 'HEmpty':
                pass
            else:
                rulename = token.split("-")[0]
                ruleNames.append(rulename) 
        
        return ruleNames
        

    #@do_cprofile
    #@profile
    def run(self):

        start_time = time.time()

        #print("Running thread")

        pathConSetLength = len(self.currentPathConditionSet)

        newPathConditionSet = []
        new_pc_dict = {}

        name_dict = {}
        reverse_name_dict = {}

        ruleNamesInLayer = [rule.name for rule in self.transformation[self.layer]]
        rulesForSecondPhase = sorted(set(self.overlappingRules.keys()).intersection(ruleNamesInLayer))

        rulesToTreat = []
        if self.pruning:
            # build the set of rules that remains to be executed
            for l in range(self.layer + 1, len(self.transformation)):
                for r in self.transformation[l]:
                    rulesToTreat.append(r.name)

            rulesToTreat += list(rulesForSecondPhase)


        progress_bar = None
        if self.report_progress:
            progress_bar = ProgressBar(pathConSetLength)

        pcs_to_prune = []

        for pathConditionIndex in range(pathConSetLength):

            pc_name = self.currentPathConditionSet[pathConditionIndex]

            if self.report_progress:
                progress_bar.update_progress(pathConditionIndex)


            pc = self.pc_dict[pc_name]

            #store the preds and succs of the pc graph if needed
            pc_preds = []
            pc_succs = []

            childrenPathConditions = [pc_name]

            # produce a fresh copy of the path condition in pc_dict, associated with the name of the path condition.
            # this frees up the original parent path condition that will not be changed throughout the execution of
            # the rules in the layer, while its copy will. This will avoid matching over a rewritten parent path condition.
            #self.pc_dict[pc_name] = shrink_graph(deepcopy(pc))

            ###########################################################################
            # Run first phase: run all rules without any overlaps with subsuming rules
            ###########################################################################
            
            for rule in self.transformation[self.layer]:

                rule_name = rule.name

                if self.verbosity >= 2:
                    print("--------------------------------------")
                    print("Treating rule: " + self.rule_names[rule_name])
                    print("Combining with:")
                    print("Path Condition:" + pc_name)
                #if self.verbosity >= 1:
                    #print "Layer: " + str(self.layer+1)
                    #print "Number of Path Conditions generated so far: " +  str(len(self.currentPathConditionSet))
                    #print "Number of Path Conditions Percentage: " +  str(int(pathConditionIndex / float(pathConSetLength) * 100))




                # possible cases of rule combination

                ######################################
                # Case 1: Rule has no dependencies
                ######################################

                # the rule is disjointly added to the path condition
                if len(self.ruleCombinators[rule_name]) == 1:
                    if self.verbosity >= 2 : print("Case 1: Rule has no dependencies")
                    
                    # The rule only gets ran in the first phase if it does not overlap with any other rule.
                    
                    # check if any of the subsuming rules exists in the path condition
                    
                    localPathConditionLayerAccumulator = []
                    
                    subsumingRules = None
                    if rule_name in self.overlappingRules.keys():
                        subsumingRules = self.overlappingRules[rule_name]
                        
                    subsumedRules = None
                    if rule_name in self.subsumption.keys():
                        subsumedRules = self.subsumption[rule_name]
                        
                    # calculate if the rule is in a subsuming loop and has a subsuming parent
                    ruleInLoopAndHasSubsumingParent = False
                    for loop in self.loopingRuleSubsumption:
                        if rule_name in loop and loop[0] != rule_name:
                            ruleInLoopAndHasSubsumingParent = True                            
                           
                    for child_pc_index in range(len(childrenPathConditions)):

                        child_pc_name = childrenPathConditions[child_pc_index]
                        
                        subsumingRulesinPC = False
                        
                        if subsumingRules != None:
                            for sRule in subsumingRules:
                                if sRule in child_pc_name:
                                    subsumingRulesinPC = True
                                    break     
                                
                        subsumedRulesinPC = False
                        
                        if subsumedRules != None:
                            for sRule in subsumedRules:
                                if sRule in child_pc_name:
                                    subsumedRulesinPC = True
                                    break              
                        
    #                     if not (rule_name in self.overlappingRules.keys() or\
    #                             (rule_name in self.overlappingRules.keys() and subsumedRulesinPC)):
                            
                        # can symbolically execute only if the path condition contains no rule that subsumes
                        # the rule being executed or rule subsumed by the rule being executed.
                        # in this way we guarantee that all rules in a partial order get executed
                        # at least once (when the larger rules don't execute), and overlaps are
                        # dealt with during the second phase - i.e. all rules that execute and subsume
                        # others have to get their subsumed rules executed too.   
                        
                        if not (subsumingRulesinPC or subsumedRulesinPC or ruleInLoopAndHasSubsumingParent):

                            cpc = self.pc_dict[child_pc_name]

                            #take off the num of nodes in the name
                            cpc_name = cpc.name.split(".")[0]

                            new_name = cpc_name + '_' + rule_name + "-0"
    
                            # create a new path condition which is the result of combining the rule with the current path condition being examined
                            newPathCond = cpc.copy()
                            newPathCond = disjoint_model_union(newPathCond,rule)

                            new_name += "." + str(newPathCond.vcount())
                                
                            # name the new path condition as the combination of the previous path condition and the rule    
                            newPathCond.name = new_name

                            if not self.pruning or self.pruner.isPathConditionStillFeasible(newPathCond, rulesToTreat):
                                shrunk_newCond = shrink_graph(newPathCond)
                                self.pc_dict[new_name] = shrunk_newCond
                                new_pc_dict[new_name] = shrunk_newCond

                                if self.verbosity >= 2 : print("Created path condition with name: " + newPathCond.name)
                                localPathConditionLayerAccumulator.append(new_name)

                                #print_graph(newPathCond)

                                # store the newly created path condition as a child
                                childrenPathConditions.append(new_name)
                                    

                    newPathConditionSet.extend(localPathConditionLayerAccumulator)


                else:

                    #########################################################################
                    # Case 2: Rule has dependencies but cannot execute because
                    #         not all the backward links can be found in the path condition
                    #########################################################################

                    # gather the matcher for only the backward links in the rule being combined.
                    # it is the first matcher (LHS) of the combinators in the list.

                    ruleBackwardLinksMatcher = self.ruleTraceCheckers[rule_name]

                    # check if the backward links cannot be found by matching them on the path condition

                    # if not pc_preds or not pc_succs:
                    #     pc_preds, pc_succs = get_preds_and_succs(pc)
                        #pc_preds = [(len(tmp), tmp) for tmp in pc.get_adjlist(mode=2)]
                        #pc_succs = [(len(tmp), tmp) for tmp in pc.get_adjlist(mode=1)]


                    p = Packet()
                    p.graph = pc
                    ruleBackwardLinksMatcher.packet_in(p, preds=pc_preds, succs=pc_succs)
                    if not ruleBackwardLinksMatcher.is_success:
                        if self.verbosity >= 2 : print("Case 2: Rule has dependencies but cannot execute")


                    else:
                        #graph_to_dot(pc.name + "_par", pc)
                        #########################################################################
                        # Case 3: Rule has dependencies that may or will execute
                        #########################################################################

                        if self.verbosity >= 2 : print("Case 3: Rule has dependencies that may or will execute")

                        # go through the partial and the total rule combinators
                        for combinator in range(2):

                            combinatorMatcher = self.ruleCombinators[rule_name][combinator][0]

                            if self.verbosity >= 2 : print("Combinator: " + combinatorMatcher.condition.name)

                            # check whether we are dealing with a partial or a total combinator

                            isTotalCombinator = False

                            #if combinator == len(self.ruleCombinators[rule_name]) - 1:
                            if combinator == 1:
                                isTotalCombinator = True

                            # find all the matches of the rule combinator in the path condition that the rule combines with

                            p = Packet()
                            p.graph = pc

                            #print_graph(p.graph)

                            combinatorMatcher.packet_in(p, preds=pc_preds, succs=pc_succs)
                            

                            # if self.rule_names[rule.name] == "HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier":
                            #     graph_to_dot("pathCondition_par_" + pc.name, pc)
                            #graph_to_dot("combinator_par_" + combinatorMatcher.condition.name, combinatorMatcher.condition)

                            #print_graph(combinatorMatcher.condition)
                            #print_graph(pc)

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
                                
                                subsumingRules = None
                                if rule_name in self.overlappingRules.keys():
                                    subsumingRules = self.overlappingRules[rule_name]
                                   
                                subsumedRules = None
                                if rule_name in self.subsumption.keys():  
                                    subsumedRules = self.subsumption[rule_name]
                                    
                                # calculate if the rule is in a subsuming loop and has a subsuming parent
                                ruleInLoopAndHasSubsumingParent = False
                                for loop in self.loopingRuleSubsumption:
                                    if rule_name in loop and loop[0] != rule_name:
                                        ruleInLoopAndHasSubsumingParent = True    
                                                                    
                                # now combine the rule with the newly created path condition using the current combinator
                                # in all the places where the rule matched on top of the path condition
                                i = Iterator()
                                #p_copy = deepcopy(p)
                                #p_copy = i.packet_in(p_copy)
                                p = i.packet_in(p)

                                pathCondSubnum = 0

                                while i.is_success and pathCondSubnum < 1:

                                    #go through all the children of this path condition

                                    for child_pc_index in range(len(childrenPathConditions)):

                                        #get the name of the child
                                        child_pc_name = childrenPathConditions[child_pc_index]
 
                                        subsumingRulesinPC = False
                                        
                                        if subsumingRules != None:
                                            for sRule in subsumingRules:
                                                if sRule in child_pc_name:
                                                    subsumingRulesinPC = True
                                                    break     
                                                
                                        subsumedRulesinPC = False
                                 
                                        #print(".......... Child PC name: " + child_pc_name)
                                        #print(".......... Subsumed Rules: " + str(subsumedRules))                                        
                                        
                                        if subsumedRules != None:
                                            for sRule in subsumedRules:
                                                if sRule in child_pc_name:
                                                    subsumedRulesinPC = True
                                                    break              
                                                
                                        #print("----------------> RuleInLoopAndHasSubsumingParent: " + str(ruleInLoopAndHasSubsumingParent))
                                        #print("----------------> subsumingRulesinPC: " + str(subsumingRulesinPC))         
                                        #print("----------------> subsumedRulesinPC: " + str(subsumedRulesinPC))                                                  
                                        #print("----------------> Going to execute: " + str(not (subsumingRulesinPC or subsumedRulesinPC or ruleInLoopAndHasSubsumingParent)))
                            
                                        if not (subsumingRulesinPC or subsumedRulesinPC or ruleInLoopAndHasSubsumingParent):

                                            if self.verbosity >= 2 :
                                                print("--> Combining with path condition: " + child_pc_name)
    
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
                                            cpc = self.pc_dict[child_pc_name]
    
                                            # if the combinator is not the total one, make a copy of the path condition in the set
                                            # of combinations generated so far.
                                            # the total combinator is always the one at the end of the combinator list for the rule.
    
                                            # name the new path condition as the combination of the previous path condition and the rule
                                            newPathCondName = cpc.name.split(".")[0] + "_" + rule.name
    
                                            p_copy = deepcopy(p)
                                            newPathCond = cpc.copy()
                                            p_copy.graph = newPathCond
    
                                            rewriter = self.ruleCombinators[rule.name][combinator][1]
                                            p_copy = rewriter.packet_in(p_copy)
                                                                                              
                                            newPathCond = p_copy.graph

    
                                            # check if the equations on the attributes of the newly created path condition are satisfied
    
                                            #if not is_consistent(newPathCond):
                                            if not rewriter.is_success:
                                                if self.verbosity >= 2:
                                                    print("Path Condition: " + newPathCondName + " has inconsistent equations")

                                            # elif self.pruning and not self.pruner.isPathConditionStillFeasible(newPathCond,
                                            #                                                                 rulesToTreat):
                                            #     if self.verbosity >= 2:
                                            #         print("Path Condition: " + newPathCondName + " was pruned")
                                            else:

                                                valid = True
                                                if isTotalCombinator:
    
                                                    #print("Going to write a total: " + newPathCondName)
    
                                                    newPathCondName = newPathCondName +"-T" + str(pathCondSubnum)

                                                    newPathCondName += "." + str(len(newPathCond.vs))
                                                    newPathCond.name = newPathCondName

                                                    if self.pruning and not self.pruner.isPathConditionStillFeasible(
                                                            newPathCond, rulesToTreat):
                                                        valid = False

                                                    if self.verbosity >= 2:
                                                        print("Total: Possible PC: " + newPathCondName + " valid?: " + str(valid))
                                                                                                        
                                                    # because the rule combines totally with a path condition in the accumulator we just copy it
                                                    # directly on top of the accumulated path condition
    
                                                    # several totals my exist, so the original PC may be rewritten multiple times
    
                                                    previousTotalPC = None                                                    
                                                    writeOverPreviousTotalPC = False

                                                    if valid:
                                                        try:
                                                            reverse_name = reverse_name_dict[cpc.name]
                                                            name_dict[reverse_name] = newPathCondName
                                                            reverse_name_dict[newPathCondName] = reverse_name
                                                        except KeyError:
                                                            name_dict[cpc.name] = newPathCondName
                                                            reverse_name_dict[newPathCondName] = cpc.name

                                                        
                                                    #change the child's name in the child's array
                                                    childrenPathConditions[child_pc_index] = newPathCondName
    
                                                else:
    
                                                    #print("Going to write a partial: " + newPathCondName)
    
                                                    newPathCondName = newPathCondName +"-P" + str(pathCondSubnum)
                                                    newPathCondName += "." + str(len(newPathCond.vs))
                                                    newPathCond.name = newPathCondName
                                                    
                                                    # we are dealing with a partial combination of the rule.
                                                    # create a copy of the path condition in the accumulator because this match of the rule is partial.

                                                    if self.pruning and not self.pruner.isPathConditionStillFeasible(
                                                            newPathCond, rulesToTreat):
                                                        valid = False
                                                    else:
                                                        # add the result to the local accumulator
                                                        partialTotalPathCondLayerAccumulator.append(newPathCond.name)
                                                    if self.verbosity >= 2:
                                                        print("Partial: Possible PC: " + newPathCondName + " valid?: " + str(valid))

                                                    # store the parent of the newly created path condition
                                                    childrenPathConditions.append(newPathCond.name)

                                                if self.verbosity >= 2:
                                                    print("Created path condition with name: " + newPathCondName)


                                                # store the new path condition
                                                shrunk_newCond = shrink_graph(newPathCond)
                                                self.pc_dict[newPathCondName] = shrunk_newCond

                                                if valid:
                                                    new_pc_dict[newPathCondName] = shrunk_newCond
                                                else:
                                                    pcs_to_prune.append(newPathCondName)

                                    p = i.next_in(p)
                                    pathCondSubnum += 1
                                    

                                newPathConditionSet.extend(partialTotalPathCondLayerAccumulator)
                                
            ###########################################################################
            # Run second phase: run all rules with any overlaps with subsuming rules on 
            # path conditions generated during the first phase
            ###########################################################################
            

#             print("--------------------------------")
#             print("overlapping rules: " + str(self.overlappingRules.keys()))
#             print("rules in layer: " + str(ruleNamesInLayer))
#             print("Rules for second phase: " + str(rulesForSecondPhase))

                
            for pathConditionIndex in range(len(childrenPathConditions)):
                
                for rule_name in rulesForSecondPhase:
                    ruleNamesInPC = []
                    for token in childrenPathConditions[pathConditionIndex].split("_"):
                        ruleNamesInPC.append(token.split("-")[0])
                        
#                     print("Rule names in PC: " + str(ruleNamesInPC))
#                     print("Overlaps looked for: " + str(self.overlappingRules[rule_name]))                 
#                     print("Intersection: " + str(set(self.overlappingRules[rule_name]).intersection(set(ruleNamesInPC))))
                    
                    # check if any of the subsuming rules exists in the path condition's name,
                    # otherwise don't even try to apply the rule.
                    # check also if the rules has not been previously executed as a rule with no dependencies
                    if set(self.overlappingRules[rule_name]).intersection(set(ruleNamesInPC)) != set() and\
                        rule_name not in childrenPathConditions[pathConditionIndex]:
                        
                        if self.verbosity >= 2 : print("Executing rule " + self.rule_names[rule_name] + " in second phase for overlaps.")
                        
                        combinatorMatcher = None
                        combinatorRewriter = None
                        
                        if len(self.ruleCombinators[rule_name]) == 1:
                            # Case 1: Rule has no dependencies
                            
                            combinatorMatcher = self.ruleCombinators[rule_name][0][0]     
                            combinatorRewriter = self.ruleCombinators[rule_name][0][1]
                        else:
                            # Case 3: Rule has dependencies that may or will execute
                            combinatorMatcher = self.ruleCombinators[rule_name][2][0]     
                            combinatorRewriter = self.ruleCombinators[rule_name][2][1]
                            
                        # execute the rule

                        p = Packet()
                        cpc = self.pc_dict[childrenPathConditions[pathConditionIndex]]
                        p.graph = cpc
                        p = combinatorMatcher.packet_in(p)
#                         print "----> PC Name: " + childrenPathConditions[pathConditionIndex]                         
                        #print ("-----------------------------> Match: " + str(combinatorMatcher.is_success))                                             
                        
                        i = Iterator()
                        p = i.packet_in(p)
                        
#                        print "Match site:"
#                         for matchSite in p.match_sets.keys():
#                             print str(p.match_sets[matchSite])

                        numOfOverlaps = 0

                        while i.is_success:
                            numOfOverlaps = numOfOverlaps + 1
                            beforeOverlappingPC = p.graph.copy()
                            p = combinatorRewriter.packet_in(p)
                            
                            if not combinatorRewriter.is_success:
                                if self.verbosity >= 2:
                                    print("Graph: " + p.graph.name + " has inconsistent equations")
                                    p.graph = beforeOverlappingPC                                    
                            #print("--------------------------------> Rewrite: " + str(combinatorRewriter.is_success))
                            p = i.next_in(p)
                            
                        newPathCond = p.graph
                        newPathCondName = cpc.name.split(".")[0] + "_" + rule_name  + "-OVER" + str(numOfOverlaps)
                        newPathCondName += "." + str(len(newPathCond.vs))
                        
                        # replace the original path condition by the result of overlapping the subsumed rule on it
                  
                        previousTotalPC = None                                                    
                        writeOverPreviousTotalPC = False

                        try:
                            reverse_name = reverse_name_dict[cpc.name]
                            name_dict[reverse_name] = newPathCondName
                            reverse_name_dict[newPathCondName] = reverse_name
                        except KeyError:
                            name_dict[cpc.name] = newPathCondName
                            reverse_name_dict[newPathCondName] = cpc.name

                        # for nameTotalPC in name_dict.keys():
                        #     if name_dict[nameTotalPC] == cpc.name:
                        #         previousTotalPC = nameTotalPC
                        #         writeOverPreviousTotalPC = True
                        #         break
                        #
                        # if not writeOverPreviousTotalPC:
                        #     name_dict[cpc.name] = newPathCondName
                        #     reverse_name_dict[newPathCondName] = cpc.name
                        # else:
                        #     name_dict[previousTotalPC] = newPathCondName
                        #     reverse_name_dict[newPathCondName] = previousTotalPC

                        childrenPathConditions[pathConditionIndex] = newPathCondName

                        if self.verbosity >= 2:
                            print("Second Phase: Created new path condition: " + newPathCondName)
                        
                        newPathCond.name = newPathCondName
                        shrunk_pc = shrink_graph(newPathCond)   
                        self.pc_dict[newPathCondName] = shrunk_pc
                        new_pc_dict[newPathCondName] = shrunk_pc

            if self.pruning and not self.pruner.isPathConditionStillFeasible(pc, rulesToTreat):
                pcs_to_prune.append(pc_name)

        #print("Current length: " + str(len(self.currentPathConditionSet)))
        #print("New length: " + str(len(newPathConditionSet)))

        self.currentPathConditionSet = list(set(self.currentPathConditionSet))


        if self.pruning:

            #pruning_time = time.time()

            for pathCondName in pcs_to_prune:
                #delete_graph(pathCondName)



                # try:
                #     del self.pc_dict[pathCondName]
                # except KeyError:
                #     pass



                try:
                    del new_pc_dict[pathCondName]
                except KeyError:
                    pass

                if pathCondName not in name_dict:
                    try:
                        self.currentPathConditionSet.remove(pathCondName)
                    except ValueError:
                        pass

                try:
                    #delete_graph(name_dict[pathCondName])
                    del name_dict[pathCondName]
                except KeyError:
                    pass

                # for key, value in dict.copy(name_dict).items():
                #     if pathCondName == value:
                #         del name_dict[key]

            #print("Time taken for pruning: " + str(time.time() - pruning_time))

        self.currentPathConditionSet.extend(newPathConditionSet)

        self.currentPathConditionSet = list(set(self.currentPathConditionSet))

        print("Thread finished: Took " + str(time.time() - start_time) + " seconds")

        self.results_queue.put((self.currentPathConditionSet, new_pc_dict, name_dict))






















