'''
Created on 2013-09-21

@author: gehan
'''
from abc import ABCMeta, abstractmethod
from .property import Property
import os
#from atomic_state_property import AtomicStateProperty

from disambiguate import Disambiguator
from core.himesis_utils import disjoint_model_union
from copy import deepcopy
from core.himesis_utils import graph_to_dot
from core.himesis_utils import load_class

from t_core.messages import Packet
from t_core.matcher import Matcher

import time
import PropertyVerification

from profiler import *

class StateProperty(Property):
    '''
    classdocs
    '''
    __metaclass__=ABCMeta
    hasDefaultVerifResult=None
    verifResult=None

    def __init__(self):
        Property.__init__(self)
        self.counterexamples = []


        self.NOT_CHECKED = "Not checked"
        self.NO_ISOLATED = "Isolated did not match"
        self.NO_CONNECTED = "Connected did not match"
        self.NO_COMPLETE = "Complete did not match"
        self.COMPLETE_FOUND = "The complete property was found"

        #detail the status of the property
        self.status = self.NOT_CHECKED

        self.disambig = Disambiguator(0)

    def SETverifResult (self, boolres):
        self.hasDefaultVerifResult= True
        self.verifResult=boolres
        
    def GETverifResult(self):
        return self.verifResult
    
    def GEThasDefaultVerifResult (self):
        return self.hasDefaultVerifResult
    
    def resetVerifResultToFalse (self):
        self.verifResult=False
        self.hasDefaultVerifResult=False

    def verify (self, state, StateSpace=None):
        #I added a second parameter with a default value of none because 
        #   the only subclass of StateProperty that will need this second parameter is AtomicStateProperty
        #   (its verify method will need StateSpace.verbosity and StateSpace.verifiedStateCache)
        pass
    
    @staticmethod
    def parseStateName2RuleNames (stateName):
        result=stateName.split('_')
        return result[1:]
      
    @staticmethod    
    def checkRuleReachability (ruleName2Check, StateSpace):

        ts0 = time.time()
        reachable=False
        for pathCond in StateSpace.get_path_conditions():
            rulesInPathCond=StateProperty.parseStateName2RuleNames(pathCond.name)
            if ruleName2Check in rulesInPathCond:
                reachable= True
                break
        ts1 = time.time()
        if reachable:
            print("\nRule "+ruleName2Check+ " is reachable through at least one path condition !")
        else:
            print("\nRule "+ruleName2Check+ " is not reachable through any path condition !")
        print("Time to verify reachability: " + str(ts1 - ts0))
        return reachable
        
    @staticmethod
    def getAllAtomicStatePropsInStateProp (sprop, listResult):
        result=listResult
        if isinstance(sprop, PropertyVerification.atomic_state_property.AtomicStateProperty) :
            result.append(sprop)
        else :
            operands= sprop.getAllOperands() #gets all operands, even if they are duplicates
            #AndStateProperty(AndStateProperty(atomic1,atomic2),atomic1).getAllOperands() returns a list of size 2 with an AndStateProperty and an AtomicStateProperty
            for op in operands:
                StateProperty.getAllAtomicStatePropsInStateProp(op,result)
        return result
    
    @staticmethod
    def twoOrMoreAtomicPropsAreTrue (atomicProps):
        if (len(atomicProps)>1):
            ctr=0
            for prop in atomicProps:
                if (prop.GETverifResult()==True) and (prop.GEThasDefaultVerifResult()==True) and (len(prop.get_matchesOfTotal())>0):
                    ctr=ctr+1
                    if (ctr == 2):
                        return True
        return False
    
    @staticmethod
    def CheckConsistencyFunc (atomicProps):
        listOfListsOfMatches=[]
        for prop in atomicProps:
            if ((len(prop.get_matchesOfTotal())>0) and (prop.GEThasDefaultVerifResult()==True) and (prop.GETverifResult()==True)):
                curlist=[]
                for dict1 in prop.get_matchesOfTotal():
                    curlist.append(dict1.values())
                listOfListsOfMatches.append(curlist)
        
        for atpropindex in range(len(listOfListsOfMatches)):
                curmatches = listOfListsOfMatches[atpropindex]
                for match in curmatches:
                    for anotherAtPropIndex in range(len(listOfListsOfMatches)):
                        if anotherAtPropIndex==atpropindex :
                            continue
                        foundoverlap=False
                        curMatchesInAnotherAtProp = listOfListsOfMatches[anotherAtPropIndex]
                        for matchInAnotherAtProp in curMatchesInAnotherAtProp:
                            if (len(set(match).intersection(set(matchInAnotherAtProp)))>0):
                                foundoverlap=True
                                break
                        if foundoverlap==False:
                            print('Pivots of the state property are not consistent :(')
                            return False    
        #print('Pivots of the state property are consistent :)')
        return True
    
    @staticmethod      
    def break_down_pc_name(pcName):
        nameList = []
        for token in pcName.split("_"):
            token = token.split("-")[0]
            nameList.append(token)
        return nameList


    #@do_cprofile
    def verifyCompositeStateProperty(self, StateSpace, stateprop):
        """
        Inputs: 
        1- StateSpace: the complete state space to be iterated
        2- stateprop: the StateProperty that we'd like to prove "for all" states, 
                    i.e., proving that its true per state and that t its true for all states
        
        Steps performed by function:
        1- Gets all the composite AtomicStateProperties in stateprop.
        2- build the united graph from the symbolic state
        2- iterates on each state of StateSpace, & for each state the following steps are done:
            a- Build cacheIsolatedPatternMatches which is a lookup cache containing the name of each AtomiStateProperty retrieved from step 1, and whether or not their isolated patterns have a match in the current state or not.
            b- While building cacheIsolatedPatternMatches, set the default verification result of AtomicStateProperties in the verifiedStateCache or those that have no matches for their isolated patterns to true, 
                i.e. their verification result will be set to true without having to check their connected and complete patterns.
            c- After building cacheIsolatedPatternMatches, if non of the cache keys has a 'true' (i.e. non of the composite AtomicStateProperties have a match for their Isolated patterns), then do not collapse the state and call stateprop.verify function on the uncollapsed state. (For efficiency & because collapsing is expensive, we collapse the current state only if a match for IsolatedLHS exists for at least one of the composite AtomicStateProperties)
            d-     ...else, collapse the state into a resultant set of collapsed states. For each collapsed state in the resultant set of states, call stateprop.verify on the collapsed state. This time the verify function will match the connected pattern then the complete pattern.
            e- If the compositeStatePattern does not hold for one state then return false. Else, return true
        """        
        AtomicStatePropsInStateProp=StateProperty.getAllAtomicStatePropsInStateProp(stateprop,[])
        #print ("Started running function verifyCompositeStateProperty of class StateProperty")
        state_index = 0
        found_counterexample=False
        curVerifResult=False

        pcs_failed = []

        self.disambig.set_property(stateprop)

        #ensure that the property's precondition matched at least one path condition
        #otherwise, there is an issue (different metamodels, ...)
        property_isolated_matched = False
        
        for state in StateSpace.get_path_conditions():
            if state is ():
                continue

            #print("PC: " + state.name)
            
            stateRuleNames = StateProperty.break_down_pc_name(state.name)

            #if (state_index)==2:
            #    print ("Start debugging here")
            #Initially, merged_state has the first rule of the the current state being examined in the SymbolicStateSpace
            #merged_state = deepcopy(state[0])
            merged_state = deepcopy(state)
            #rule_index = 1
            numberOfIsolatedMatchesForAllAtomicStateProperties=[]

            # Go through all the rules in the layer and merge them in one graph
            # Merged state will finally have the merged (disjoint union) state corresponding to the state we are checking in SymbolicStateSpace
            #while rule_index < len(state):
            #    merged_state = disjoint_model_union(merged_state, state[rule_index])
            #    rule_index += 1

            cacheIsolatedPatternMatches=[]
            for atomicStatePropIndex in range(len(AtomicStatePropsInStateProp)):
                isolated = AtomicStatePropsInStateProp[atomicStatePropIndex].isolated_matcher
                s = Packet()
                s.graph = deepcopy(merged_state)

                #if StateSpace.draw_svg:
                #    graph_to_dot('out' + str(state_index), s.graph)

                isolated.packet_in(s)
                if isolated.is_success:
                    property_isolated_matched = True
                    if StateSpace.verbosity >= 1:
                        print('State ' + str(state_index) + ": " + state.name)
                        print('    Isolated pattern matched')

                    # find first how many matches of the isolated elements of the property (if any) were found
                    numberOfIsolatedMatches = len(s.match_sets[s.current].matches)
                    numberOfIsolatedMatchesForAllAtomicStateProperties.append(numberOfIsolatedMatches)
                    # check whether there exists in the already verified state cache a state which is smaller (can be fully covered)
                    # by the current state and has the same amount of isolated matches as the current state. If so there's no need to
                    # verify the current state as the property holds in it

                    smallerStateWithSameRulesExists = False
                    rulecounter=0
#                         #NEW OPTIMIZATION HEURISTIC
#                         # parse name of PC into an ordered set/list - parsedRulesInPC
#                         # if parsedRulesInPC size<2, collapse flag =false in
#                         # if the cache has another PC whose name is a subset of the name of the current PC, then property holds
#                         #check if where verifiedSTatecache was filled needs to be changed
#                         RulesInCurState=StateProperty.parseStateName2RuleNames(state.name) 
#                         for alreadyVerifiedState in AtomicStatePropsInStateProp[atomicStatePropIndex].verifiedStateCache:
#                             if numberOfIsolatedMatches != alreadyVerifiedState[1]:
#                                 continue
#                             rulesInAlreadyVerifiedState= StateProperty.parseStateName2RuleNames(alreadyVerifiedState[0].name)
#                             for rule in rulesInAlreadyVerifiedState:
#                                 if (rule in RulesInCurState)==False:
#                                     break
#                                 else:
#                                     rulecounter=rulecounter+1
#                             if rulecounter==len(rulesInAlreadyVerifiedState):
#                                 smallerStateWithSameRulesExists=True
#                                 break
#                             ####
#                         #NEW OPTIMIZATION HEURISTIC

                        
                    for alreadyVerifiedState in AtomicStatePropsInStateProp[atomicStatePropIndex].verifiedStateCache:
                        # break down the already verified path condition's name in the rules used
                        alreadyVerifiedStateRuleNames =  StateProperty.break_down_pc_name(alreadyVerifiedState[0].name)
                           
                        # if all the rules in the path condition being analyzed exist in a path condition that has been previously analyzed and
                        # the number of isolated matches has not increased, that means that no additional elements that affect the property have
                        # been added in the new path condition and we are sure the property holds for the path condition being analyzed
                        
#                         print "-------------------------------------------------"
#                         print "Rules now: " + str(stateRuleNames)
#                         print "Number of isolated: " + str(numberOfIsolatedMatches)
#                         print "Rules in previous: " + str(alreadyVerifiedStateRuleNames)
#                         print "Number of isolated: " + str(alreadyVerifiedState[1])
#                         print "-------------------------------------------------\n"                       
                        
                        if (set(alreadyVerifiedStateRuleNames) < set(stateRuleNames) and numberOfIsolatedMatches == alreadyVerifiedState[1]):
                            smallerStateWithSameRulesExists = True
                            break

                        # If 2 states, each has 1 different rule, then the first part of the if condition will evaluate to false,
                        # if 2 states, each with 1 same rules, then the first part of the above if condition will evaluate to true
                        # if one state has rules x,y,z and the other state has rule z, then the first part of the above if condition will evaluate to true
                        # if one state has rules x,y,z and the other state has w, then the first part of the above if condition will evaluate to false
                        # i.e. the first part of the above if condition will eval to true iff one state is smaller(fewer number of composite rules) and completely covered (i.e. all rules of the 1st state are in the rules of the 2nd state) by the other state
                        #      or if the two states are the same size(i.e. have the same number of rules), with the same exact composite rules.

                    if not smallerStateWithSameRulesExists:

                        # add to the list of already verified states the new state and how many matches of the
                        # isolated elements of the property were found
                        # collapse must be eventually done in this case

                        #FOLLOWING: Where we used to add entries to an AtomiStateProperty's verified State Cache
                        AtomicStatePropsInStateProp[atomicStatePropIndex].verifiedStateCache.append((state,numberOfIsolatedMatches))
                        cacheIsolatedPatternMatches.append(True)
                    else:
                        #print('        Will not check state, property holds...')
                        cacheIsolatedPatternMatches.append(False)
                        AtomicStatePropsInStateProp[atomicStatePropIndex].SETverifResult(True)
                else: # did not succeed in matching isolated
                    # if StateSpace.verbosity >= 1:
                    #     print('State ' + str(state_index) + ': ' + state.name)
                    #     print('    Isolated pattern not matched')
                    numberOfIsolatedMatchesForAllAtomicStateProperties.append(-1)
                    cacheIsolatedPatternMatches.append(False)
                    AtomicStatePropsInStateProp[atomicStatePropIndex].SETverifResult(True)

            collapseFlag=False
            for foundIsolated in cacheIsolatedPatternMatches:
                collapseFlag=collapseFlag or foundIsolated

            #print("Collapse Flag: " + str(collapseFlag))
            #print("cacheIsolatedPatternMatches: " + str(cacheIsolatedPatternMatches))
            # ****
            if collapseFlag:
                # build set of collapsed states to analyse
                #G- states_to_analyze will contain merged state, and all recursively, collapsed versions of the (composite rules of the) state
                states_to_analyse = [merged_state]
                ###new code -start
                if len(StateProperty.parseStateName2RuleNames(state.name))>1:
                    if StateSpace.verbosity >= 1: t0 = time.time()
                    #disamb=Disambiguator(0)#(StateSpace.verbosity)
                    disambiguated_states = self.disambig.disambiguate(state)
                    #print("Disambiguated size: " + str(len(disambiguated_states)))

                    # for ds in disambiguated_states:
                    #     print("DS: " + ds.name)

                    states_to_analyse.extend(disambiguated_states)
                    ###new code -end
                    if StateSpace.verbosity >= 1: t1 = time.time()
                    if StateSpace.verbosity >= 1: print('Time to collapse state: ' + str(t1-t0))
                else:
                    if StateSpace.verbosity >= 1: print('State contains only one rule; no collapse needed... ')
                if StateSpace.verbosity >= 1: print('    Number of states to analyse: ' + str(len(states_to_analyse)))




                for collapsed_state in range(len(states_to_analyse)):
                    #print("Collapsed State: " + states_to_analyse[collapsed_state].name)

                    #if StateSpace.verbosity >= 1:
                    s = Packet()
                    s.graph = states_to_analyse[collapsed_state]

                        #if StateSpace.draw_svg:
                    #graph_to_dot('out' + str(state_index) + '_' + str(states_to_analyse[collapsed_state].name), s.graph)
                    #if StateSpace.verbosity >= 1: print '    Collapsed state ' + str(collapsed_state)

                    #s.graph.name += str(collapsed_state)

                    #print("Start verify")
                    curVerifResult=stateprop.verify(s.graph,StateSpace)
                    #print(stateprop.status)
                    #print("End verify")

                    if ((curVerifResult==True)) and (StateProperty.twoOrMoreAtomicPropsAreTrue(AtomicStatePropsInStateProp)):
                        curVerifResult=curVerifResult and (StateProperty.CheckConsistencyFunc(AtomicStatePropsInStateProp))

                    if not curVerifResult:
                        pass



                        #break


                    #"Remove from an AtomicStateProperty's verifiedStateCache the last tuple of (state,#ofmatches), if the complete pattern had no match"
                    for curatomicprop in AtomicStatePropsInStateProp:
                        curatomicprop.reset_matchesOfTotal()
                        if ((curatomicprop.propFalseForAtleastOneCollapsedState==False) and (curatomicprop.GEThasDefaultVerifResult()==True) and (curatomicprop.GETverifResult()==False)):
                            curatomicprop.propFalseForAtleastOneCollapsedState= True



                #Add to AtomicStateProperty's verifiedStateCache the tuple (state,#ofmatches), if the complete pattern had a match
                #If the curVerifResult== false, don't make this addition to the verifiedStateCaches of the atomicStateProperties - you won't be using them any more.
                if curVerifResult:
                    for atomicPropIndex in range(len(AtomicStatePropsInStateProp)):
                        if ((AtomicStatePropsInStateProp[atomicPropIndex].propFalseForAtleastOneCollapsedState==False) and (AtomicStatePropsInStateProp[atomicPropIndex].NumberOfTimesPropWasChecked==len(states_to_analyse))and (AtomicStatePropsInStateProp[atomicPropIndex].NumberOfTimesPropWasChecked==AtomicStatePropsInStateProp[atomicPropIndex].NumberOfTimesFoundMatch)):
                            AtomicStatePropsInStateProp[atomicPropIndex].verifiedStateCache.append((state,numberOfIsolatedMatchesForAllAtomicStateProperties[atomicPropIndex]))

            else:
                #print("Other verify start")
                curVerifResult=stateprop.verify(merged_state, StateSpace)
                #print("Other verify end")

                #print(stateprop.status)
                #should I update verified state cache here too ? I think yes
                if curVerifResult and (StateProperty.twoOrMoreAtomicPropsAreTrue(AtomicStatePropsInStateProp)):
                    curVerifResult=curVerifResult and (StateProperty.CheckConsistencyFunc(AtomicStatePropsInStateProp))
                #for curatomicprop in AtomicStatePropsInStateProp:
                #        curatomicprop.reset_matchesOfTotal()
            #if the composite state property does not hold for atleast one state, break out of the loop
            found_counterexample = not curVerifResult
            if found_counterexample:
                pcs_failed.append(state.name)

                try:
                    #graph_to_dot(state.name, state)
                    print("Property: " + stateprop.Connected.name + " failed on path condition: " + state.name)
                    #
                    #graph_to_dot(stateprop.Connected.name + "_failure", stateprop.Connected)
                    #graph_to_dot(stateprop.CompleteQuantified.name + "_failure", stateprop.CompleteQuantified)

                except AttributeError:

                    try:#
                        print("Property: " + stateprop.propArg1.CompleteQuantified.name + " failed on path condition: " + state.name)
                        #graph_to_dot(stateprop.propArg1.CompleteQuantified.name + "_failure", stateprop.propArg1.CompleteQuantified)
                        #graph_to_dot(stateprop.propArg2.CompleteQuantified.name + "_failure", stateprop.propArg2.CompleteQuantified)
                    except:
                        pass
            #    break

            #reset 'propFalseForAtleastOneCollapsedState' & 'verifResult' of all
            #    atomicStateProperties in the compositeStateProperty to false, so that they can be
            #    refilled when checking the compositeStateProperty for the next state

            for curatomicprop in AtomicStatePropsInStateProp:
                curatomicprop.resetpropFalseForAtleastOneCollapsedState()
                curatomicprop.resetVerifResultToFalse()
                curatomicprop.resetNumberOfTimesPropWasChecked()
                curatomicprop.resetNumberOfTimesFoundMatch()
                curatomicprop.reset_matchesOfTotal()
                #In AtomicStateProperty, we added "NumberOfTimesPropWasChecked" to be used when adding entries to the AtomicStateProperty's verifiedStateCache
                #i.e., sometimes if you are verifying an AndStateProperty, if the first atomicStateProperty evaluates to False, then the second AtomicStateProperty is not evaluated at all..
                #In that case, you cannot add an entry to the verifiedStateCache of the second AtomicStateProperty since that AtomicStateProperty was not even evaluated for all the collapsed state of that merged state...
                #So we added an attribute "NumberOfTimesPropWasChecked" which increments by 1 each time the atomicStateProperty is evaluated. Before adding an entry to its verifiedStateCache we check that propFalseForAtleastOneCollapsedState==False and that the number of collapsed states == NumberOfTimesPropWasChecked (i.e., AtomicStateProperty was checked for all collapsed states of the current merged state)


            state_index+=1
        # if StateSpace.verbosity >= 1:
        #     print '\n'
        # if found_counterexample == True:
        #     if StateSpace.verbosity >= 1: print 'Composite StateProperty does not Hold for all path conditions!!!'
        #
        # else:
        #     if StateSpace.verbosity >= 1: print 'Composite StateProperty Holds for all path conditions!!!'
        #
        # cleanup the already verified state cache
        #StateSpace.verifiedStateCache = []
        for curatomicprop in AtomicStatePropsInStateProp:
            curatomicprop.verifiedStateCache=[]

        if not property_isolated_matched:
            print("Error: The property's isolated part did not match on any path condition!")
            print("Recheck the metamodels or the property!")
             
        return pcs_failed