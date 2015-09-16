'''
Created on 2013-08-17

@author: bentley
'''

from t_core.messages import Packet
from t_core.matcher import Matcher

from core.himesis_utils import graph_to_dot
from core.himesis_plus import look_for_attached

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

        self.contract_mms = [mm.replace("MT_pre__", "") for mm in self.complete.vs["mm__"]]

        #graph_to_dot(self.complete.name, self.complete)


        self.connected_data = self.get_data(self.connected)
        self.complete_data = self.get_data(self.complete)

        #print("Connected Data: " + str(self.connected_data))
        #print("Complete Data: " + str(self.complete_data))


    def check_isolated(self, pc):

        pc_mms = pc.vs["mm__"]

        #print("Contract MMs: " + str(self.contract_mms))
        #print("PC MMs: " + str(pc_mms))

        for mm in self.contract_mms:
            if mm not in pc_mms:
                #print("Fail on " + mm)
                return self.NO_ISOLATED

        return self.ISOLATED


    def check(self, pc):

        self.pc_data = self.get_data(pc)

        if self.match(self.connected, self.connected_data, pc):
            print("Connected")
        else:
            return self.NO_CONNECTED

        if self.match(self.complete, self.complete_data, pc):
            print("Complete")
            return self.COMPLETE_FOUND
        else:
            return self.NO_COMPLETE


    def get_data(self, graph):
        directLinks = []
        mms = [mm.replace("MT_pre__", "") for mm in graph.vs["mm__"]]

        for i in range(len(graph.vs)):
            node = graph.vs[i]

            mm = node["mm__"]

            if "directLink" in mm:
                neighbours = look_for_attached(i, graph)

                directLinks.append(neighbours)

        #print("Contract directLinks: " + graph.name + str(directLinks))

        return [directLinks]

    def match(self, contract, contract_data, pc):

        print("Contract data: " + str(contract_data))
        print("PC data: " + str(self.pc_data))

        d_links = contract_data[0]
        for n0, n1, link in d_links:

            # print(contract.vs[n0]["mm__"])
            # print(contract.vs[n1]["mm__"])
            # print(contract.vs[link]["mm__"])

            if [n0, n1, link] not in self.pc_data:
                return False

        return True