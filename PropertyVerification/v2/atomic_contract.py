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

        self.isolated_matcher = Matcher(isolated, disambig_matching = True)
        self.connected_matcher = Matcher(connected, disambig_matching = True)
        self.complete_matcher = Matcher(complete, disambig_matching = True)

        self.last_packet = None

        self.verbosity = 0

        try:
            self.contract_mms = [mm.replace("MT_pre__", "") for mm in self.complete.vs["mm__"]]
        except KeyError:
            self.contract_mms = []

        #graph_to_dot(self.complete.name, self.complete)

        #self.connected_data = decompose_graph(self.connected)

        #self.complete_data = decompose_graph(self.complete)

        #self.connected_data = self.get_data(self.connected)
        #self.complete_data = self.get_data(self.complete)

        #print("Connected Data: " + str(self.connected_data))
        #print("Complete Data: " + str(self.complete_data))

    def draw(self):
        contract_name = self.isolated.name.replace("_Isolated", "")
        graph_to_dot("contract_isolated_" + contract_name, self.isolated)
        graph_to_dot("contract_connected_" + contract_name, self.connected)
        graph_to_dot("contract_complete_" + contract_name, self.complete)

    def get_pivots(self):
        if len(self.last_packet.match_sets) == 0:
            #matching failed, so don't bother returning anything
            return {}

        matches = list(self.last_packet.match_sets.values())[0].matches[0]

        eqs = self.complete["equations"]
        pivots = {}
        for eq in eqs:
            (node_num, attr), (typ, value) = eq
            if attr != "pivot" or typ != "constant":
                continue
            label = self.complete.vs[node_num]["MT_label__"]

            #lookup the GUID that got matched to the label
            pivots[value] = matches[label]

        return pivots


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

        #self.pc_data = decompose_graph(pc)

        # if self.match(self.connected, self.connected_data, pc):
        #     pass
        #     #print("Connected")
        # else:
        #     #print("No connected")
        #     return self.NO_CONNECTED
        #
        # if self.match(self.complete, self.complete_data, pc):
        #     #print("Complete")
        #     return self.COMPLETE_FOUND
        # else:
        #     #print("No complete")
        #     return self.NO_COMPLETE

        p = Packet()
        p.graph = pc

        self.connected_matcher.packet_in(p)

        if not self.connected_matcher.is_success:
            return self.NO_CONNECTED

        p = Packet()
        p.graph = pc

        self.complete_matcher.packet_in(p)

        self.last_packet = p

        if self.complete_matcher.is_success:
            return self.COMPLETE_FOUND
        else:
            return self.NO_COMPLETE

    # def match(self, contract, contract_data, pc):
    #
    #     #print("Contract data: " + str(contract_data))
    #     #print("PC data: " + str(self.pc_data))
    #
    #     matcher = HimesisMatcher(pc, contract, disambig_matching = True)
    #
    #     if not match_links(matcher, contract, contract_data["direct_links"], pc, self.pc_data["direct_links"], verbosity=self.verbosity, match_all = True):
    #         return False
    #
    #     if not match_links(matcher, contract, contract_data["backward_links"], pc, self.pc_data["backward_links"], verbosity=self.verbosity, match_all = True):
    #         return False
    #
    #     return True