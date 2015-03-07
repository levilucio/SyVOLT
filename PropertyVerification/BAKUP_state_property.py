'''
Created on 2013-09-21

@author: gehan
'''
#Until this backup, if a record is in and AtomicStateProperty's verifiedStateCache, then the property was true for that state
#This is WRONG.. A record is added to verifiedStateCache only after the Isolated pattern has been matched. This does not necessarily mean that the complete pattern has been matched and evaluated to true.
#Until this backup, this error was not fixed yet. In the new state_property file, this error has been fixed
#The fix is commented with the following 
#"Remove from an AtomicStateProperty's verifiedStateCache the last tuple of (state,#ofmatches), if the complete pattern had no match"
#for this fix, the class AtomicStateProperty had a new attribute added, too. ("propFalseForAtleastOneCollapsedState"). This property was initialized to False in the constructor of AtomicStateProperty
from abc import ABCMeta, abstractmethod
from property import Property
#from atomic_state_property import AtomicStateProperty

from core.himesis_utils import disjoint_model_union
from copy import deepcopy
from core.himesis_utils import graph_to_dot
from t_core.messages import Packet
from t_core.matcher import Matcher

import time
import PropertyVerification

class StateProperty(Property):
    '''
    classdocs
    '''
    __metaclass__=ABCMeta
    hasDefaultVerifResult=None
    verifResult=None
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
        
    @abstractmethod 
    def verify (self, state, StateSpace=None):
        #I added a second parameter with a default value of none because 
        #   the only subclass of StateProperty that will need this second parameter is AtomicStateProperty
        #   (its verify method will need StateSpace.verbosity and StateSpace.verifiedStateCache)
        pass
    
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
    def verifyCompositeStateProperty(StateSpace, stateprop):
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
        AtomicStatesInStateProp=StateProperty.getAllAtomicStatePropsInStateProp(stateprop,[])
        print ("Started running function verifyCompositeStateProperty of class StateProperty")
        state_index = 0
        
        for state in StateSpace.symbStateSpace:
            if state != ():
                #Initially, merged_state has the first rule of the the current state being examined in the SymbolicStateSpace
                merged_state = deepcopy(state[0])
                rule_index = 1
                
                # Go through all the rules in the layer and merge them in one graph
                # Merged state will finally have the merged (disjoint union) state corresponding to the state we are checking in SymbolicStateSpace
                while rule_index < len(state):
                    merged_state = disjoint_model_union(merged_state, state[rule_index])
                    rule_index += 1
            
                cacheIsolatedPatternMatches=[]
                for atomicStateIndex in range(len(AtomicStatesInStateProp)):
                    isolated = Matcher(AtomicStatesInStateProp[atomicStateIndex].Isolated)
                    s = Packet()
                    s.graph = deepcopy(merged_state)
                
                    if StateSpace.outputStates:
                        graph_to_dot('out' + str(state_index), s.graph)                
                
                    isolated.packet_in(s)
                    if isolated.is_success:
                        if StateSpace.verbosity >= 1:
                            print 'State ' + str(state_index)
                            print StateSpace._pretty_print_state(state)
                            print '    Found Property Elements'
                        
                        # find first how many matches of the isolated elements of the property (if any) were found
                        numberOfIsolatedMatches = len(s.match_sets[s.current].matches)
                                    
                        # check whether there exists in the already verified state cache a state which is smaller (can be fully covered)
                        # by the current state and has the same amount of isolated matches as the current state. If so there's no need to
                        # verify the current state as the property holds in it
                
                        smallerStateWithSameRulesExists = False
                
                        for alreadyVerifiedState in AtomicStatesInStateProp[atomicStateIndex].verifiedStateCache:
                            if len(set(state) - set(alreadyVerifiedState[0])) == len(set(state)) - len(set(alreadyVerifiedState[0]))\
                            and numberOfIsolatedMatches == alreadyVerifiedState[1]:
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
                            AtomicStatesInStateProp[atomicStateIndex].verifiedStateCache.append((state,numberOfIsolatedMatches))
                            cacheIsolatedPatternMatches.append(True)
                        else:
                            #if StateSpace.verbosity >= 1: print '        Will not check state, property holds...'
                            #cacheIsolatedPatternMatches.append(False)
                            #AtomicStatesInStateProp[atomicStateIndex].SETverifResult(True)
                            if StateSpace.verbosity >= 1: print '        Will not check state, property holds...'
                            cacheIsolatedPatternMatches.append(False)
                            AtomicStatesInStateProp[atomicStateIndex].SETverifResult(True)
                    else: # did not succeed in matching isolated
                        if StateSpace.verbosity >= 1: 
                            print 'State ' + str(state_index)
                            print StateSpace._pretty_print_state(state)
                            print '    Property Elements not found'            
                        cacheIsolatedPatternMatches.append(False)
                        AtomicStatesInStateProp[atomicStateIndex].SETverifResult(True)
             
                collapseFlag=False          
                for foundIsolated in cacheIsolatedPatternMatches:
                    collapseFlag=collapseFlag or foundIsolated
                if collapseFlag==True:
                    # build set of collapsed states to analyse
                    #G- states_to_analyze will contain merged state (containing disjoint union of its composite rules), and all recursively, collapsed versions of the (composite rules of the) state
                    states_to_analyse = [merged_state]               
                    if StateSpace.verbosity >= 1: t0 = time.time()                
                    states_to_analyse.extend(StateSpace.collapseFactory.collapse(state))
                    if StateSpace.verbosity >= 1: t1 = time.time()
                    if StateSpace.verbosity >= 1: print 'Time to collapse state: ' + str(t1-t0)
                    if StateSpace.verbosity >= 1: print '    Number of states to analyse: ' + str(len(states_to_analyse))
                       
                    for collapsed_state in range(len(states_to_analyse)):
                        if StateSpace.outputStates:
                            s = Packet()
                            s.graph = states_to_analyse[collapsed_state]
                            graph_to_dot('out' + str(state_index) + '.' + str(collapsed_state), s.graph)
                        if StateSpace.verbosity >= 1: print '    Collapsed state ' + str(collapsed_state)
                        curVerifResult=stateprop.verify(states_to_analyse[collapsed_state],StateSpace)
                        #Next, if for any atomicProperty it was evaluated to false, then remove the last entry added to THE AtomicStateProperty's verifiedStateCache
                        #for curprop in AtomicStatesInStateProp:
                        #    if curprop.GETverifResult()==False:
                        #        curprop.verifiedStateCache.pop()
                        
                        #Should the results of atomicProperties be reset here or not 
                        if curVerifResult==False: break
                    
                    ###############
                else:
                    curVerifResult=stateprop.verify(merged_state, StateSpace)
                found_counterexample=not(curVerifResult)
                
                #if the composite state property does not hold for atleast one state, break out of the loop 
                if found_counterexample == True:
                    break
                                
                #reset verification result of all atomicStateProperties in the compositeStateProperty to false, so that they can be refilled when checking the compositeStateProperty for the next state
                for curatomicprop in AtomicStatesInStateProp:
                    curatomicprop.resetVerifResultToFalse()
                state_index += 1
        if StateSpace.verbosity >= 1: 
            print '\n'
        if found_counterexample == True:
            if StateSpace.verbosity >= 1: print 'Composite StateProperty does not Hold for all states!!!'

        else:
            #question - if found_counterexample= false, couldnt it be property not provable as suggested in ur paper, i.e. match pattern was never found hence, u cant determine if property will hold or not
            if StateSpace.verbosity >= 1: print 'Composite StateProperty Holds for all states!!!'
        
        # cleanup the already verified state cache
        #StateSpace.verifiedStateCache = []
        for stateProp in AtomicStatesInStateProp:
            stateProp.verifiedStateCache=[]
             
        return not(found_counterexample)                