

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMapVirtualDeviceFAULTY(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapVirtualDeviceFAULTY.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapVirtualDeviceFAULTY, self).__init__(name='HMapVirtualDeviceFAULTY', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(2, 0), (0, 3), (6, 1), (1, 2), (5, 4), (6, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """MapVirtualDeviceFAULTY"""
        self["GUID__"] = UUID('95aaacf6-a957-4e2f-986e-9e069a7a09f2')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('e77d3d09-327b-4795-acca-0599901f5c7d')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('5548eeef-cfd5-4dec-9a4b-af74be724585')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('4e2ecd2a-ba0e-4be1-807e-1c6fd2bd60d5')
        self.vs[3]["mm__"] = """SwcToEcuMapping"""
        self.vs[3]["classtype"] = """SwcToEcuMapping"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["name"] = """stem1"""
        self.vs[3]["GUID__"] = UUID('011a86fc-fe0c-4653-9254-e4e8201cb258')
        self.vs[4]["mm__"] = """VirtualDevice"""
        self.vs[4]["classtype"] = """VirtualDevice"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["name"] = """vd1"""
        self.vs[4]["GUID__"] = UUID('0c032feb-653f-4d67-b722-bd6bb18c8093')
        self.vs[5]["mm__"] = """match_contains"""
        self.vs[5]["GUID__"] = UUID('58031c66-4dde-4ac7-aa57-b996e24d2ed8')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('be81108d-1238-41de-962b-176da604ca4b')

