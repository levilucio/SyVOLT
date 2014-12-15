

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSF2SF(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF, self).__init__(name='HSF2SF', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 6), (2, 10), (10, 3), (6, 0), (0, 3), (8, 1), (1, 2), (6, 11), (11, 5), (3, 12), (12, 7), (5, 4), (4, 7), (13, 5), (14, 7), (8, 13), (8, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SF2SF"""
        self["GUID__"] = UUID('340caab3-bf42-4d48-a221-0fde1989a5e5')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('6725f782-0a3d-42a4-9d1c-6e61c462a85f')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('d2863d70-7e13-41fa-9cc4-92beac5bebac')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('508ec2b3-1466-4966-a378-1c739c60ef43')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """t_"""
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["GUID__"] = UUID('ca29863c-d63e-48c1-bfaa-69ae58b31b80')
        self.vs[4]["mm__"] = """indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('44a81247-25fa-47d9-a21b-14da925a500f')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """1"""
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["cardinality"] = """s_"""
        self.vs[5]["GUID__"] = UUID('0164d0c3-6f5a-4221-bfc2-48992a04def8')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Station_T"""
        self.vs[6]["GUID__"] = UUID('9c9491e7-3572-42a5-bebf-7d2ce3719e3c')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["GUID__"] = UUID('655f179c-24de-49f9-b91c-4f9238eea279')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('680e205b-4b27-4c02-bf11-45dc01418dbb')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('a785d407-76bb-4732-a3c1-8ca40cb8313f')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('50a83d15-a809-4cef-9626-38b6e5237ba1')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('cdeb65d6-aff4-4b8f-9549-af9660ddda55')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('9e9e357d-093a-4ffa-bd7a-b7ebc8660ab9')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('367275bd-694a-486a-89c5-c9bf5d5ad106')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('15d3d2fc-5b39-413b-a7d5-13bfeda9a591')

