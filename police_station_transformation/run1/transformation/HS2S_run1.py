

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HS2S_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S_run1, self).__init__(name='HS2S_run1', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 4), (6, 1), (2, 6), (2, 3), (3, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """S2S_run1"""
        self["GUID__"] = UUID('cd3b5027-894d-459c-9c3c-2ed8ddc42890')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('622ee346-e49c-4783-8f91-c4b068dcbe1c')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('429aa85f-f8fd-4c51-b33f-ee0d838e46a1')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('caf57fd5-d50d-4e28-b5e8-0734056fd61c')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('6c258b32-787f-48df-90f6-81580fe11961')
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["classtype"] = """station1"""
        self.vs[4]["name"] = """1.s"""
        self.vs[4]["GUID__"] = UUID('3da55aa5-4e5c-4668-849c-ae51fae14835')
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["classtype"] = """station1"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """1.s"""
        self.vs[5]["GUID__"] = UUID('07b4d7e7-eaa9-4c35-a8f5-0c7a1f4ec3ac')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('b36853d2-5b68-412b-8b53-ca1f8027f424')

