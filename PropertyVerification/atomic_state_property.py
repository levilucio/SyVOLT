'''
Created on 2013-08-17

@author: gehan
'''
from .state_property import StateProperty

from t_core.messages import Packet
from t_core.matcher import Matcher

from core.himesis_utils import graph_to_dot

class AtomicStateProperty(StateProperty):
    '''
    classdocs
    '''
    Isolated=None
    Connected=None
    CompleteQuantified=None
    verifiedStateCache = None
    propFalseForAtleastOneCollapsedState=None
    NumberOfTimesPropWasChecked=None
    NumberOfTimesFoundMatch=None
    matchesOfTotal=None
    #"propFalseForAtleastOneCollapsedState" is added as a flag to know whether or not the last record in an AtomiStateProperty's verifiedStateCache needs to be removed, if the atomicStateProperty's complete pattern had no match for one of the collapsed states of the current state being checked

    def __init__(self, isolated, connected, completeQuantified): #isolated was the first param after self
        '''
        Constructor
        '''
        #print ("Initializing an AtomicStateProp Object")

        StateProperty.__init__(self)

        self.Isolated=isolated
        self.Connected=connected
        self.CompleteQuantified=completeQuantified

        self.isolated_matcher = Matcher(isolated)
        self.match = Matcher(connected)
        self.total = Matcher(completeQuantified)


        self.resetVerifResultToFalse()
        self.verifiedStateCache = []
        self.propFalseForAtleastOneCollapsedState=False
        self.NumberOfTimesPropWasChecked=0
        self.NumberOfTimesFoundMatch=0
        self.matchesOfTotal=[]
        #In AtomicStateProperty, we added the attribute "NumberOfTimesPropWasChecked" to be used when adding entries to the AtomicStateProperty's verifiedStateCache
        #i.e., sometimes if you are verifying an AndStateProperty, if the first atomicStateProperty evaluates to False, then the second AtomicStateProperty is not evaluated at all..
        #In that case, you cannot add an entry to the verifiedStateCache of the second AtomicStateProperty since that AtomicStateProperty was not even evaluated for all the collapsed state of that merged state...
        #So we added an attribute "NumberOfTimesPropWasChecked" which increments by 1 each time the atomicStateProperty is evaluated. Before adding an entry to its verifiedStateCache we check that propFalseForAtleastOneCollapsedState==False and that the number of collapsed states == NumberOfTimesPropWasChecked (i.e., AtomicStateProperty was checked for all collapsed states of the current merged state)

    def incrementNumberOfTimesPropWasChecked(self):
        self.NumberOfTimesPropWasChecked+=1
             
    def incrementNumberOfTimesFoundMatch(self):
        self.NumberOfTimesFoundMatch+=1
    
    def resetNumberOfTimesFoundMatch(self):
        self.NumberOfTimesFoundMatch=0
                   
    def resetNumberOfTimesPropWasChecked(self):
        self.NumberOfTimesPropWasChecked=0
        
    def resetpropFalseForAtleastOneCollapsedState(self):
        self.propFalseForAtleastOneCollapsedState=False
    
    def reset_matchesOfTotal(self):
        self.matchesOfTotal=[]
        
    def set_matchesOfTotal(self,inputmatches):
        self.matchesOfTotal=inputmatches 
        
    def get_matchesOfTotal(self):
        return self.matchesOfTotal  
    
    
    def verify(self,inputstate, StateSpace=None, verbosity = 0):
        #Check if the AtomicStateProp verification result was preset to some value. 
        ###### If yes, return that value. 
        ###### If no, match the connected pattern then the complete pattern on the input state and return the resultant verification result of the two matches performed

        if StateSpace.verbosity > verbosity:
            verbosity = StateSpace.verbosity

        if verbosity >= 1: print ("Verifying on: " + inputstate.name)

        if True:#self.GEThasDefaultVerifResult()==False:
            """
            check a property on a specific state in the state space
            1) Check if connected exists 
            2) Check if complete exists

            Parameters:
                inputstate: i.e. state on which we would like to check if the AtomicStateProperty holds or not
                StateSpace which contains inputstate: we will only be using StateSpace.verifiedStateCache and StateSpace.verbosity 
            """



            found_counterexample = False
                             
            s = Packet()
            s.graph = inputstate         
            self.match.packet_in(s)
                              
            # if the match was found, try to find the whole property
            if self.match.is_success:
                if verbosity >= 1: print('        Found Match! (Connected)')
                
                #if verbosity >= 1: graph_to_dot("found_connected_" + s.graph.name, s.graph)

                s = Packet()
                s.graph = inputstate                   
                self.total.packet_in(s)
                if self.total.is_success:
                    self.status = self.COMPLETE_FOUND
                    #self.verifiedStateCache.append((inputstate,numberOfIsolatedMatches))
                    self.incrementNumberOfTimesFoundMatch()
                    if verbosity >= 1: print('        Found Apply! (Complete)')
                    self.set_matchesOfTotal(s.match_sets[s.current].matches)
                    #debug1 is a dictionary structure
                    #str(debug1['1']) ... u can find a function that returns all keys of a dictionary
                    #then iterate on all the keys and convert them to string to use them for cross matching
                    #print (str(len(s.match_sets[s.current].matches)))
                else:
                    self.status = self.NO_COMPLETE

                    #if verbosity >= 1: graph_to_dot(s.graph.name + "_not_complete", s.graph)
                    if verbosity >= 1: print('        Could not find Apply! (Complete)')

                    #self.counterexamples.append(s.graph)

                    found_counterexample = True
                    self.set_matchesOfTotal([])
                    # match part of the property was found, but apply not, thus we found a counterexample
            else:
                self.status = self.NO_CONNECTED
                if verbosity >= 1: print("Couldn't find connected: " + s.graph.name)
                if verbosity >= 1:  print('        Could not find Match! (Connected)')
        
                
            if verbosity >= 1:
                print('\n')
            # if found_counterexample == True:
            #     if StateSpace.verbosity >= 1: print 'AtomicStateProp does not Hold for the current state!!!'
            #
            # else:
            #     if StateSpace.verbosity >= 1: print 'AtomicStateProp Holds for the current state!!!'
            #
            # cleanup the already verified state cache
            #StateSpace.verifiedStateCache = []
            self.SETverifResult(not(found_counterexample)) 
            
        self.incrementNumberOfTimesPropWasChecked()
        return self.GETverifResult()
