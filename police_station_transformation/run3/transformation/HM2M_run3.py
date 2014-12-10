

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HM2M_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M_run3, self).__init__(name='HM2M_run3', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 5), (6, 1), (2, 6), (2, 3), (3, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """M2M_run3"""
        self["GUID__"] = UUID('1208be92-fdbc-489f-856c-cbfa9a12fda5')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('072af5cf-7b65-4aa3-a8a1-9edb7062aa23')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('deb68af0-082e-4a5b-bcfa-f4d7632b53bc')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('ada25b8e-6142-461a-9c41-a06c318af909')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('8061d323-5488-40e2-b65f-bcbb968ab11c')
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["classtype"] = """male3"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["name"] = """m"""
        self.vs[4]["GUID__"] = UUID('74e5e67b-adcd-4593-bd00-d14215b86b51')
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["classtype"] = """male3"""
        self.vs[5]["name"] = """m"""
        self.vs[5]["GUID__"] = UUID('c6bcc4a7-e381-4ca6-acb5-90c6be4975f5')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('332ec032-dca7-426f-9f08-a6cec4b2799c')

