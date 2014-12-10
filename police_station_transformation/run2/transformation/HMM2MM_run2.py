

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMM2MM_run2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMM2MM_run2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMM2MM_run2, self).__init__(name='HMM2MM_run2', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 13), (1, 6), (6, 14), (13, 7), (7, 11), (14, 8), (8, 12), (13, 0), (0, 14), (4, 1), (2, 4), (2, 9), (2, 10), (11, 3), (3, 12), (9, 11), (10, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """MM2MM_run2"""
        self["GUID__"] = UUID('4a6ac55d-90ce-4a49-bc97-d5cab75f9a43')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('204c0626-cd92-4a36-bbde-436d07554e26')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('36d22ad3-4e6d-464a-b5dd-cc121989aed4')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('57e13a8b-40be-443f-a9a5-84ac27f13bcf')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('688cdc2a-ca56-4cf5-996e-bef1627175eb')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('7a4be10c-ca8c-4dad-90f4-0ba12c128e6a')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('dd32a0c6-07f3-4226-acda-eb90f583a290')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('ed80587f-4741-4791-9c7a-19fc45777e75')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('e406f8a2-4131-4ca7-a130-49237d02bcfc')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('d3b6b307-85af-400b-a1f1-c56073825ce1')
        self.vs[9]["mm__"] = """match_contains"""
        self.vs[9]["GUID__"] = UUID('a64d31bf-9391-468a-967d-375d8136fb3d')
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = UUID('e08ca46f-3111-4a90-982a-190d3418c980')
        self.vs[11]["name"] = """m1"""
        self.vs[11]["classtype"] = """male2"""
        self.vs[11]["mm__"] = """Male_S"""
        self.vs[11]["cardinality"] = """+"""
        self.vs[11]["GUID__"] = UUID('ea8af8cd-02b8-41a2-9de7-453b923f07f1')
        self.vs[12]["name"] = """m2"""
        self.vs[12]["classtype"] = """male2"""
        self.vs[12]["mm__"] = """Male_S"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = UUID('23d8f11a-2c00-41ab-8278-b416029a10a1')
        self.vs[13]["name"] = """m"""
        self.vs[13]["classtype"] = """male2"""
        self.vs[13]["mm__"] = """Male_T"""
        self.vs[13]["GUID__"] = UUID('2d23ab6a-53c9-4e52-9ef8-0321adc14acc')
        self.vs[14]["name"] = """m2"""
        self.vs[14]["classtype"] = """male2"""
        self.vs[14]["mm__"] = """Male_T"""
        self.vs[14]["GUID__"] = UUID('7108f209-6628-45c1-908e-69b2691021ee')

