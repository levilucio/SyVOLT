'''
Created on 2013-08-17

@author: bentley
'''

from t_core.messages import Packet
from t_core.matcher import Matcher

from PropertyVerification.v2.contract import Contract

from core.himesis_utils import graph_to_dot
from core.himesis_plus import look_for_attached

from core.match_algo import HimesisMatcher

from copy import deepcopy

from util.decompose_graph import decompose_graph, match_links


class AtomicContract(Contract):
    '''
    classdocs
    '''
    def __init__(self, isolated, connected, complete):
        '''
        Constructor
        '''
        #print ("Initializing an AtomicStateProp Object")

        #StateProperty.__init__(self)

        super(AtomicContract, self).__init__()

        self.isolated = isolated
        self.connected = connected
        self.complete = complete

        self.isolated_matcher = Matcher(isolated)
        self.connected_matcher = Matcher(connected)
        self.complete_matcher = Matcher(complete)



        try:
            self.contract_mms = [mm.replace("MT_pre__", "") for mm in self.complete.vs["mm__"]]
        except KeyError:
            self.contract_mms = []

        #graph_to_dot(self.complete.name, self.complete)

        self.connected_data = {}
        self.connected_data["direct_links"], self.connected_data["backward_links"],\
        self.connected_data["match_elements"], self.connected_data["isolated_match_elements"],\
        self.connected_data["apply_elements"] = decompose_graph(self.connected)

        self.complete_data = {}
        self.complete_data["direct_links"], self.complete_data["backward_links"],\
        self.complete_data["match_elements"], self.complete_data["isolated_match_elements"],\
        self.complete_data["apply_elements"] = decompose_graph(self.complete)

        #self.connected_data = self.get_data(self.connected)
        #self.complete_data = self.get_data(self.complete)

        #print("Connected Data: " + str(self.connected_data))
        #print("Complete Data: " + str(self.complete_data))


    def check_isolated(self, pc):

        p = Packet()
        p.graph = pc

        self.isolated_matcher.packet_in(p)

        if self.isolated_matcher.is_success:
            return self.ISOLATED
        else:
            return self.NO_ISOLATED


        # pc_mms = pc.vs["mm__"]
        #
        # self.contract_mms = [mm.replace("MT_pre__", "") for mm in self.isolated.vs["mm__"]]
        #
        # #print("Contract MMs: " + str(self.contract_mms))
        # #print("PC MMs: " + str(pc_mms))
        #
        # for mm in self.contract_mms:
        #     if mm not in pc_mms:
        #         #print("Fail on " + mm)
        #         return self.NO_ISOLATED

        # return self.ISOLATED


    def check(self, pc, verbosity=0):

        self.verbosity = verbosity

        self.pc_data = {}
        self.pc_data["direct_links"], self.pc_data["backward_links"],\
        self.pc_data["match_elements"], self.pc_data["isolated_match_elements"],\
        self.pc_data["apply_elements"] = decompose_graph(pc)

        if self.match(self.connected, self.connected_data, pc):
            pass
            #print("Connected")
        else:
            #print("No connected")
            return self.NO_CONNECTED

        if self.match(self.complete, self.complete_data, pc):
            #print("Complete")
            return self.COMPLETE_FOUND
        else:
            #print("No complete")
            return self.NO_COMPLETE


    def match(self, contract, contract_data, pc):

        #print("Contract data: " + str(contract_data))
        #print("PC data: " + str(self.pc_data))

        matcher = HimesisMatcher(pc, contract)

        if not match_links(matcher, contract, contract_data["direct_links"], pc, self.pc_data["direct_links"], verbosity=0, match_all = True):
            return False

        if not match_links(matcher, contract, contract_data["backward_links"], pc, self.pc_data["backward_links"], verbosity=0, match_all = True):
            return False

        return True