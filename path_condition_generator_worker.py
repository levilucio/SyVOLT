
from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.iterator import Iterator

from t_core.tc_python.srule import SRule
from t_core.tc_python.frule import FRule

import time

from multiprocessing import Process
from core.himesis_utils import expand_graph, shrink_graph, disjoint_model_union, print_graph, graph_to_dot

from copy import deepcopy

from solver.simple_attribute_equation_evaluator import SimpleAttributeEquationEvaluator

import numpy.random as nprnd

from profile import *

class path_condition_generator_worker(Process):


    def __init__(self, verbosity, num):
        super(path_condition_generator_worker, self).__init__()
        self.num = num
        self.currentPathConditionSet = None
        self.results_queue = None

        self.verbosity = verbosity

        #self.attributeEquationEvaluator = SimpleAttributeEquationEvaluator(verbosity)

        nprnd.seed(num)

    #@do_cprofile
    def run(self):

        #print("Running thread")

        pathConSetLength = len(self.currentPathConditionSet)

        newPathConditionSet = []
        new_pc_dict = {}

        name_dict = {}

        for pathConditionIndex in xrange(pathConSetLength):
        #while True:

            pc_name = self.currentPathConditionSet[pathConditionIndex]


            #newPathConditionSet.append(pc_name)

            pc = expand_graph(self.pc_dict[pc_name])
            #print_graph(pc)

            childrenPathConditions = [pc_name]

            # produce a fresh copy of the path condition in pc_dict, associated with the name of the path condition.
            # this frees up the original parent path condition that will not be changed throughout the execution of
            # the rules in the layer, while its copy will. This will avoid matching over a rewritten parent path condition.
            #self.pc_dict[pc_name] = shrink_graph(deepcopy(pc))

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
                if self.ruleCombinators[rule_name] is None:
                    if self.verbosity >= 2 : print("Case 1: Rule has no dependencies")

                    localPathConditionLayerAccumulator = []


                    num = 0
                    for child_pc_index in xrange(len(childrenPathConditions)):

                        child_pc_name = childrenPathConditions[child_pc_index]

                        cpc = expand_graph(self.pc_dict[child_pc_name])
                        new_name = cpc.name + '_' + rule_name + "-" + str(num)

                        # create a new path condition which is the result of combining the rule with the current path condition being examined
                        #newPathCond = deepcopy(cpc)
                        newPathCond = disjoint_model_union(cpc,rule)
                        # name the new path condition as the combination of the previous path condition and the rule


                        newPathCond.name = new_name
                        num += 1

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

                    p = Packet()
                    p.graph = pc
                    ruleBackwardLinksMatcher.packet_in(p)
                    if not ruleBackwardLinksMatcher.is_success:
                        if self.verbosity >= 2 : print("Case 2: Rule has dependencies but cannot execute")


                    else:
                        #graph_to_dot(pc.name + "_par", pc)
                        #########################################################################
                        # Case 3: Rule has dependencies that may or will execute
                        #########################################################################

                        if self.verbosity >= 2 : print("Case 3: Rule has dependencies that may or will execute")

                        # go through all LHS (matchers) in rule combinators
                        for combinator in xrange(len(self.ruleCombinators[rule_name])):

                            combinatorMatcher = self.ruleCombinators[rule_name][combinator][0]

                            if self.verbosity >= 2 : print("Combinator: " + combinatorMatcher.condition.name)

                            # check whether we are dealing with a partial or a total combinator

                            isTotalCombinator = False

                            if combinator == len(self.ruleCombinators[rule_name]) - 1:
                                isTotalCombinator = True

                            # find all the matches of the rule combinator in the path condition that the rule combines with

                            p = Packet()
                            p.graph = pc

                            #print_graph(p.graph)

                            combinatorMatcher.packet_in(p)

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

                                #go through all the children of this path condition
                                num = 0
                                for child_pc_index in xrange(len(childrenPathConditions)):

                                    #get the name of the child
                                    child_pc_name = childrenPathConditions[child_pc_index]

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
                                    cpc = expand_graph(self.pc_dict[child_pc_name])
                                    cpc_name = cpc.name

                                    # if the combinator is not the total one, make a copy of the path condition in the set
                                    # of combinations generated so far.
                                    # the total combinator is always the one at the end of the combinator list for the rule.

                                    # name the new path condition as the combination of the previous path condition and the rule
                                    newPathCondName = cpc_name + "_" + rule_name + "-" + str(num)
                                    num += 1

                                    #print("CPC name")
                                    #print(cpc.name)
                                    # print_graph(cpc)

                                    #newPathCond = deepcopy(cpc)
                                    newPathCond = cpc

                                    # now combine the rule with the newly created path condition using the current combinator
                                    # in all the places where the rule matched on top of the path condition
                                    i = Iterator()
                                    p_copy = deepcopy(p)
                                    p_copy.graph = newPathCond
                                    #print_graph(p_copy.graph)

                                    p_copy = i.packet_in(p_copy)



                                    while i.is_success:
                                        #print("Rewriting")
                                        #print_graph(self.ruleCombinators[rule.name][combinator][1].condition)
                                        p_copy = self.ruleCombinators[rule_name][combinator][1].packet_in(p_copy)
                                        p_copy = i.next_in(p_copy)

                                    newPathCond = p_copy.graph
                                    #print_graph(p_copy.graph)

                                    newPathCond.name = newPathCondName

                                    #graph_to_dot("produced_" + newPathCond.name + "_par", newPathCond)

                                    # check if the equations on the attributes of the newly created path condition are satisfied

                                    if self.attributeEquationEvaluator(newPathCond):

                                    #if True:

                                        if isTotalCombinator:

                                            # because the rule combines totally with a path condition in the accumulator we just copy it
                                            # directly on top of the accumulated path condition

                                            #find the path condition and change its name
                                            #TODO: Make this faster
                                            # for pathConditionIndex in range(len(self.currentPathConditionSet)):
                                            #     if self.currentPathConditionSet[pathConditionIndex] == cpc.name:
                                            #         self.currentPathConditionSet[pathConditionIndex] = newPathCond.name
                                            #         print("Changed " + cpc.name + " to " + newPathCond.name)

                                            name_dict[cpc_name] = newPathCondName

                                            #change the child's name in the child's array
                                            childrenPathConditions[child_pc_index] = newPathCondName

                                        else:
                                            # we are dealing with a partial combination of the rule.
                                            # create a copy of the path condition in the accumulator because this match of the rule is partial.

                                            # add the result to the local accumulator
                                            partialTotalPathCondLayerAccumulator.append(newPathCondName)

                                            # store the parent of the newly created path condition
                                            childrenPathConditions.append(newPathCondName)

                                        # store the new path condition
                                        shrunk_newCond = shrink_graph(newPathCond)
                                        self.pc_dict[newPathCondName] = shrunk_newCond
                                        new_pc_dict[newPathCondName] = shrunk_newCond

    #                                                 print "----------------------"
    #                                                 print "Adding: " + newPathCond.name
    #                                                 print "Parent is: " + parentPathCondition[layerPathCondAccumulator[currentPathCondition]]
    #                                                 print "----------------------"

                                        if self.verbosity >= 2:
                                            print("Created path condition with name: " + newPathCondName)

                                newPathConditionSet.extend(partialTotalPathCondLayerAccumulator)


        #print("newPathConditionSet: " + str(newPathConditionSet))
        #print("currentPathConditionSet: " + str(self.currentPathConditionSet))

        print("Thread finished")

        self.currentPathConditionSet.extend(newPathConditionSet)
        self.results_queue.put((self.currentPathConditionSet, new_pc_dict, name_dict))






















