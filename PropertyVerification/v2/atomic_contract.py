'''
Created on 2013-08-17

@author: bentley
'''

from t_core.messages import Packet
from t_core.matcher import Matcher

from core.himesis_utils import graph_to_dot
from core.himesis_plus import look_for_attached

from core.match_algo import HimesisMatcher

from copy import deepcopy

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
        self.pc_data = self.get_data(pc)

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


    def get_data(self, graph):
        directLinks = []
        traceLinks = []

        mms = [mm.replace("MT_pre__", "") for mm in graph.vs["mm__"]]

        for i in range(len(graph.vs)):
            node = graph.vs[i]

            mm = node["mm__"]

            if "directLink" in mm:
                neighbours = look_for_attached(i, graph)

                dl = []
                for n in neighbours:
                    dl.append(n)

                directLinks.append(dl)
                #directLinks.append(neighbours)
            elif "trace_link" in mm:
                neighbours = look_for_attached(i, graph)

                traceLinks.append(neighbours)


        #print("Contract directLinks: " + graph.name + str(directLinks))

        return [directLinks, traceLinks]

    def match_nodes(self, pc, src_node, contract, patt_node):
        sourceMM = pc.vs[src_node]["mm__"]
        targetMM = contract.vs[patt_node]["mm__"][8:]

        if sourceMM != targetMM:

            #print("Source MM: " + sourceMM)
            #print("Target MM: " + targetMM)

            superclasses_dict = contract["superclasses_dict"]
            #print("Superclasses: " + str(superclasses_dict))
            
            if not superclasses_dict[sourceMM] or targetMM not in superclasses_dict[sourceMM]:
                return False

        return self.matcher.are_semantically_feasible(src_node, patt_node)


    def match(self, contract, contract_data, pc):

        #print("Contract data: " + str(contract_data))
        #print("PC data: " + str(self.pc_data))

        self.matcher = HimesisMatcher(pc, contract)


        b_links = contract_data[1]
        pc_back_links = deepcopy(self.pc_data[1])

        for n0_n, n1_n, link_n in b_links:

            found_match = False


            for pc_n0_n, pc_n1_n, pc_link_n in pc_back_links:

                # print()
                # print(pc.vs[pc_n0_n]["mm__"])
                # print(pc.vs[pc_n1_n]["mm__"])
                # print(pc.vs[pc_link_n]["mm__"])

                #nodes_match = True

                nodes_match = (self.match_nodes(pc, pc_n0_n, contract, n0_n) and self.match_nodes(pc, pc_n1_n, contract, n1_n))\
                    or\
                               (self.match_nodes(pc, pc_n1_n, contract, n0_n) and self.match_nodes(pc, pc_n0_n, contract, n1_n))
                # if nodes_match:
                #     print("Success matching on " + pc.vs[pc_n0_n]["mm__"] + " vs " + contract.vs[n0_n]["mm__"])
                # else:
                #     print("Failure matching on " + pc.vs[pc_n0_n]["mm__"] + " vs " + contract.vs[n0_n]["mm__"])

                # if nodes_match:
                #     print("Success matching on " + pc.vs[pc_n1_n]["mm__"] + " vs " + contract.vs[n1_n]["mm__"])
                # else:
                #     print("Failure matching on " + pc.vs[pc_n1_n]["mm__"] + " vs " + contract.vs[n1_n]["mm__"])

                nodes_match = nodes_match and self.match_nodes(pc, pc_link_n, contract, link_n)

                # if nodes_match:
                #     print("Success matching on " + pc.vs[pc_link_n]["mm__"] + " vs " + contract.vs[link_n]["mm__"])
                # else:
                #     print("Failure matching on " + pc.vs[pc_link_n]["mm__"] + " vs " + contract.vs[link_n]["mm__"])

                if nodes_match:
                    found_match = True
                    pc_back_links.remove([pc_n0_n, pc_n1_n, pc_link_n])

                    break


            if not found_match:

                if self.verbosity > 1:
                    print("No backward matches found")
                    print("Couldn't find:")
                    print(contract.vs[n0_n]["mm__"])
                    print(contract.vs[n1_n]["mm__"])
                    print(contract.vs[link_n]["mm__"])



                return False





        d_links = contract_data[0]
        pc_direct_links = deepcopy(self.pc_data[0])
        for n0_n, n1_n, link_n in d_links:


            found_match = False

            for pc_n0_n, pc_n1_n, pc_link_n in pc_direct_links:


                nodes_match = (self.match_nodes(pc, pc_n0_n, contract, n0_n) and self.match_nodes(pc, pc_n1_n, contract, n1_n)) \
                or \
                              (self.match_nodes(pc, pc_n1_n, contract, n0_n) and self.match_nodes(pc, pc_n0_n, contract, n1_n))

                # if not nodes_match:
                #     print("Failure matching on " + pc.vs[pc_n0_n]["mm__"] + " vs " + contract.vs[n0_n]["mm__"])

                # if not nodes_match:
                #     print("Failure matching on " + pc.vs[pc_n1_n]["mm__"] + " vs " + contract.vs[n1_n]["mm__"])

                nodes_match = nodes_match and self.match_nodes(pc, pc_link_n, contract, link_n)


                if nodes_match:
                    found_match = True
                    pc_direct_links.remove([pc_n0_n, pc_n1_n, pc_link_n])
                    break
                else:
                    if self.verbosity > 1:
                        print("Not match on:")
                        print(pc.vs[pc_n0_n]["mm__"])
                        print(pc.vs[pc_n1_n]["mm__"])
                        print(pc.vs[pc_link_n]["mm__"])
                        print()

            if not found_match:
                if self.verbosity > 1:
                    print("No direct link matches found")
                    print("Couldn't find:")
                    print(contract.vs[n0_n]["mm__"])
                    print(contract.vs[n1_n]["mm__"])
                    print(contract.vs[link_n]["mm__"])
                    print()
                return False

        return True