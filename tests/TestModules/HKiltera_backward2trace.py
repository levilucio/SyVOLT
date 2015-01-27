

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HKiltera_backward2trace(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HKiltera_backward2trace.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HKiltera_backward2trace, self).__init__(name='HKiltera_backward2trace', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(2, 0), (0, 6), (5, 1), (1, 3), (5, 2), (6, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """kiltera_backward2trace"""
        self["GUID__"] = UUID('a5977678-6a03-4d9d-976f-8336bc943153')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """ApplyModel"""
        self.vs[0]["GUID__"] = UUID('dfd55c68-c635-4531-b9ac-eff589b84950')
        self.vs[1]["mm__"] = """match_contains"""
        self.vs[1]["GUID__"] = UUID('f6343ebe-3b98-42f7-a5ff-0d1a21557e14')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('e68925a6-430c-40c8-92ae-b8ee0fa0c10e')
        self.vs[3]["mm__"] = """Trigger_S"""
        self.vs[3]["classtype"] = """t_"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["name"] = """s_"""
        self.vs[3]["GUID__"] = UUID('2dc18245-24ce-48fd-b382-df132dee5221')
        self.vs[4]["mm__"] = """Trigger_T"""
        self.vs[4]["classtype"] = """t_"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["name"] = """s_"""
        self.vs[4]["GUID__"] = UUID('c711dbae-ac10-423d-8b95-54ae165bb043')
        self.vs[5]["mm__"] = """MatchModel"""
        self.vs[5]["GUID__"] = UUID('73609a8c-95dc-42e6-8eb6-f3a9f3be7971')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('c6d47377-73c8-46ca-b81d-65f27f2b6b39')

