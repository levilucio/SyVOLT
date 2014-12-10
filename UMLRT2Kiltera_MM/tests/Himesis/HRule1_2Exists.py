

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HRule1_2Exists(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRule1_2Exists.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRule1_2Exists, self).__init__(name='HRule1_2Exists', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 6), (4, 9), (9, 1), (4, 10), (10, 7), (1, 3), (1, 11), (8, 2), (2, 4), (11, 5), (7, 12), (12, 6), (3, 7), (13, 5), (14, 6), (8, 13), (8, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """rule1_2Exists"""
        self["GUID__"] = UUID('633187c2-1966-4648-82e0-17db446e9ac0')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """virtualDevice"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('8d07a36a-afd9-4eef-b5a9-39b3fb535f8a')
        self.vs[1]["name"] = """s2"""
        self.vs[1]["classtype"] = """System"""
        self.vs[1]["mm__"] = """System"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('e176785d-8e2a-4c6e-9d46-961b199025cb')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('ee5441cb-dbf3-4b6c-9b5f-0472a2b7f4bf')
        self.vs[3]["associationType"] = """softwareComposition"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = UUID('1942a54f-6db1-422f-810c-e6724a1d6fdd')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('2f9c4487-4a3e-42aa-b317-157be9b2b9e5')
        self.vs[5]["name"] = """ecu2"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('b06f6897-039a-4d1d-ae42-22f1dd7135e2')
        self.vs[6]["name"] = """vd2"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = UUID('209b3005-d2e6-48b4-a17b-6e71a164b66c')
        self.vs[7]["name"] = """sc2"""
        self.vs[7]["classtype"] = """SoftwareComposition"""
        self.vs[7]["mm__"] = """SoftwareComposition"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('01e33d16-c257-43fb-860c-9e7f08965bf2')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('aa12ffde-8959-415d-9db4-6d7933d00897')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('0fbc80b4-5cdb-4758-b18d-d6288a8d91ee')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('823eeb99-d3aa-4fbc-ad03-171941d7ed96')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = UUID('1416e2d7-0144-4a95-a440-dffe17d9e93e')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = UUID('69aa1edd-82ac-4118-beb8-99bee1d23bfe')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('744e9050-d8ac-4542-ba1d-cd027d0fcb40')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('a1501e2b-33cc-44fd-b44a-8053c0671e86')

