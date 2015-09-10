'''
Created on 2013-08-17

@author: bentley
'''

from t_core.messages import Packet
from t_core.matcher import Matcher

from core.himesis_utils import graph_to_dot

class AtomicContract():
    '''
    classdocs
    '''
    def __init__(self, isolated, connected, complete):
        '''
        Constructor
        '''
        #print ("Initializing an AtomicStateProp Object")

        #StateProperty.__init__(self)

        self.isolated = isolated
        self.connected = connected
        self.complete = complete

        self.isolated_matcher = Matcher(isolated)
        self.connected_matcher = Matcher(connected)
        self.complete_matcher = Matcher(complete)

        self.NOT_CHECKED = "Not checked"
        self.NO_ISOLATED = "Isolated did not match"
        self.ISOLATED = "Isolated did match"

        self.NO_CONNECTED = "Connected did not match"
        self.NO_COMPLETE = "Complete did not match"
        self.COMPLETE_FOUND = "The complete property was found"

        # detail the status of the property
        self.status = self.NOT_CHECKED


    def check_isolated(self, pc):
        p = Packet()
        p.graph = pc
        self.isolated_matcher.packet_in(p)

        # the isolated was not found
        if self.isolated_matcher.is_success:
            return self.ISOLATED
        else:
            return self.NO_ISOLATED


    def check(self, pc):
        p = Packet()
        p.graph = pc
        self.connected_matcher.packet_in(p)

        # the connected was not found
        # return success
        if not self.connected_matcher.is_success:
            return self.NO_CONNECTED

        p = Packet()
        p.graph = pc
        self.complete_matcher.packet_in(p)

        # the complete was not found
        # return success
        if not self.complete_matcher.is_success:
            return self.NO_COMPLETE
        else:
            print("COMPLETE MATCHED")