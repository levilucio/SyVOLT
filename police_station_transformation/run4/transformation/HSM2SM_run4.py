

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_run4, self).__init__(name='HSM2SM_run4', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 7), (5, 11), (11, 6), (7, 12), (12, 4), (5, 0), (0, 7), (8, 1), (2, 8), (2, 13), (2, 14), (6, 3), (3, 4), (13, 6), (14, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_run4"""
        self["GUID__"] = UUID('3e18639c-188b-4ab4-a740-1825966ed360')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('a87d8423-8010-4435-a8ee-40ca6b2e7edd')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('084473c0-f8d1-4f48-a4c7-fa054f0ee855')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('01521908-a967-49aa-bb4f-7c6d31b68d56')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('a43e5dba-399c-47ad-bd84-b2d4d23609a2')
        self.vs[4]["name"] = """m"""
        self.vs[4]["classtype"] = """male4"""
        self.vs[4]["mm__"] = """Male_S"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('71434dbc-611e-4d85-81b7-e1855855f082')
        self.vs[5]["name"] = """s"""
        self.vs[5]["classtype"] = """station4"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('3cf8f632-c636-4619-80e4-84d797e9b96e')
        self.vs[6]["name"] = """s"""
        self.vs[6]["classtype"] = """station4"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('d4013029-ee1e-4a28-9bd4-4d0647bc56b1')
        self.vs[7]["name"] = """m"""
        self.vs[7]["classtype"] = """male4"""
        self.vs[7]["mm__"] = """Male_T"""
        self.vs[7]["GUID__"] = UUID('62161e56-0ecb-4c3b-aa55-3399cef06770')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('e1b04536-b2bd-4ec3-925f-ee35fcf8115d')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('12810c77-9216-43f5-9cd5-0454fc3e518a')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('e45cfa03-ce83-403d-8563-53363340de93')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('60e9961d-41ad-4cf4-8121-dd6e710ba5a7')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('944a6903-6036-465e-8a3e-bd669241cc7d')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('c288db3c-ee34-4a8a-938f-2755bed2cddd')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('718c60e8-5015-457a-ad20-24a3a8ed8dfa')

