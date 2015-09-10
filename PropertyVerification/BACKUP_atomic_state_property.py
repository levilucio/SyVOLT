'''
Created on 2013-08-17

@author: gehan
'''
from .state_property import StateProperty

from t_core.messages import Packet
from t_core.matcher import Matcher

#from himesis_utils import merge_models
from core.himesis_utils import disjoint_model_union
from core.himesis_utils import graph_to_dot
from copy import deepcopy

import time

class BKUPAtomicStateProperty(StateProperty):
    '''
    classdocs
    '''
    Isolated=None
    Connected=None
    CompleteQuantified=None

    def __init__(self, isolated, connected, completeQuantified):
        '''
        Constructor
        '''
        print ("Initializing an AtomicStateProp Object")
        self.Isolated=isolated
        self.Connected=connected
        self.CompleteQuantified=completeQuantified
        
    def verify(self,StateSpace):
        """
        check a property in the state space
        1) build the united graph from the symbolic state
        G-- then check if Isolated exists, if it does -> do the next step
        2) build all collapsed graph from the initial graph
        g-- then check if connected -> complete exists
        3) check that if the precondition of the property holds in any of the collapsed graphs,
           then the postcondition also hold. If it is not the case for one graph then return false. Else return true.
        For efficiency, and because collapsing is expensive, do a preprocessing step that only collapses a state if all
        elements included in the property are also included in the state (G-- i.e. if IsolatedLHS exists)  
        
        Parameters:
            propIsolatedElems: query that matches in a state just the match elements in the property
            propMatchPattern: query that matches in a state the match pattern in the property
            propTotal: query that matches in a state the whole property
        """

        isolated = Matcher(self.Isolated)
        match = Matcher(self.Connected)
        total = Matcher(self.CompleteQuantified)
        print ("Started running function verify of Class AtomicStateProp")
        state_index = 0
        
        found_counterexample = False
        
        for state in StateSpace.symbStateSpace:
            if state != ():
                #G- initially, merged_state has the first rule of the the current state being examined in the SymbolicStateSpace
                merged_state = deepcopy(state[0])
                rule_index = 1
                
                # go through all the rules in the layer and merge them in one graph
                #G- go thr all rules in state, and merge them
                #G- merged state will finally have the merged (disjoint union) state corresponding to the state we are checking in SymbolicStateSpace
                while rule_index < len(state):
                    #merged_state = merge_models(merged_state, state[rule_index])
                    merged_state = disjoint_model_union(merged_state, state[rule_index])
                    rule_index += 1
            
                s = Packet()
                s.graph = deepcopy(merged_state)
                
                if StateSpace.outputStates:
                    graph_to_dot('out' + str(state_index), s.graph)                
                
                isolated.packet_in(s)
                                       
                if isolated.is_success:
                    if StateSpace.verbosity >= 1:
                        print('State ' + str(state_index))
                        print(StateSpace._pretty_print_state(state))
                        print('    Found Property Elements')
                        
                    # find first how many matches of the isolated elements of the property (if any) were found
                    numberOfIsolatedMatches = len(s.match_sets[s.current].matches)
                                    
                    # check whether there exists in the already verified state cache a state which is smaller (can be fully covered)
                    # by the current state and has the same amount of isolated matches as the current state. If so there's no need to
                    # verify the current state as the property holds in it
                
                    smallerStateWithSameRulesExists = False
                
                    for alreadyVerifiedState in StateSpace.verifiedStateCache:
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
                        StateSpace.verifiedStateCache.append((state,numberOfIsolatedMatches))
         
                        # build set of collapsed states to analyse
                        #G- states_to_analyze will contain merged state (containing disjoint union of its composite rules), and all recursively, collapsed versions of the (composite rules of the) state
                        states_to_analyse = [merged_state]               
        
                        if StateSpace.verbosity >= 1: t0 = time.time()                
                        states_to_analyse.extend(StateSpace.collapseFactory.collapse(state))
                        if StateSpace.verbosity >= 1: t1 = time.time()
                        if StateSpace.verbosity >= 1: print('Time to collapse state: ' + str(t1-t0))
         
                        if StateSpace.verbosity >= 1: print('    Number of states to analyse: ' + str(len(states_to_analyse)))
                        
                        #if len(states_to_analyse) > self.maxdepth: self.maxdepth = len(states_to_analyse)
                        
                        for collapsed_state in range(len(states_to_analyse)):
                            
                            s = Packet()
                            s.graph = states_to_analyse[collapsed_state]
                                
                            if StateSpace.outputStates:
                                graph_to_dot('out' + str(state_index) + '.' + str(collapsed_state), s.graph)
                                
                            match.packet_in(s)
        
                            if StateSpace.verbosity >= 1: print('    Collapsed state ' + str(collapsed_state) )
                            # if the match was found, try to find the whole property
                            if match.is_success:
                                if StateSpace.verbosity >= 1: print('        Found Match!')
                                total.packet_in(s)
                                if total.is_success:
                                    if StateSpace.verbosity >= 1: print('        Found Apply!')
                                else:
                                    if StateSpace.verbosity >= 1: print('        Could not find Apply!')
                                    found_counterexample = True
                                    # match part of the property was found, but apply not, thus we found a counterexample
                                    break
                            else:
                                if StateSpace.verbosity >= 1:  print('        Could not find Match!')
                                
                    else:
                        if StateSpace.verbosity >= 1: print('        Will not check state, property holds...')
                        #Question- if  smallerStateWithSameRulesExists=true means property holds ? how come? U only add to the cache the entry after isolated elements of the match pattern match, not after matching the whole property                 
                            
                else:
                    if StateSpace.verbosity >= 1: 
                        print('State ' + str(state_index))
                        print(StateSpace._pretty_print_state(state))
                        print('    Property Elements not found'    )
            
                if found_counterexample == True:
                    break
                state_index += 1
                
        if StateSpace.verbosity >= 1: 
            print('\n')
        if found_counterexample == True:
            if StateSpace.verbosity >= 1: print('AtomicStateProp does not Hold!!!')

        else:
            #question - if found_counterexample= false, couldnt it be property not provable as suggested in ur paper, i.e. match pattern was never found hence, u cant determine if property will hold or not
            if StateSpace.verbosity >= 1: print('AtomicStateProp Holds!!!')
        
        # cleanup the already verified state cache
        StateSpace.verifiedStateCache = [] 
        return not(found_counterexample)
