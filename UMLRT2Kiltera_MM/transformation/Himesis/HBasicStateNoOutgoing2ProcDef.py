

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HBasicStateNoOutgoing2ProcDef(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HBasicStateNoOutgoing2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HBasicStateNoOutgoing2ProcDef, self).__init__(name='HBasicStateNoOutgoing2ProcDef', num_nodes=29, edges=[])
        
        # Add the edges
        self.add_edges([(8, 0), (0, 7), (18, 14), (14, 27), (17, 15), (15, 26), (19, 16), (16, 28), (8, 1), (1, 22), (5, 2), (2, 12), (2, 13), (6, 3), (3, 4), (4, 10), (10, 20), (4, 11), (11, 21), (9, 4), (6, 5), (17, 23), (18, 24), (19, 25), (13, 7), (12, 8), (8, 9), (23, 20), (24, 21), (25, 22)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'UMLRT2Kiltera_MM'
p2
a.""")
        self["name"] = """BasicStateNoOutgoing2ProcDef"""
        self["GUID__"] = UUID('0cfb4ea5-8a37-4a38-a0ba-32ee1b74936e')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """p"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('32378e6b-02aa-475f-ae65-f4c6503fd8c3')
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('dc47ee44-f153-49da-b3b0-ec43e910458f')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('be95dd13-afe0-4389-a4d4-9a7b4e6cdef4')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('a592e72a-f5a0-49b9-9114-b5e24094a5cb')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('f0657732-76e5-411e-a552-05e6aa38a9b3')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('2e35e7c6-d6f4-461b-a70e-8b93f6df3a5f')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('ca8082f3-69b8-4888-a0b6-7df6c6de7115')
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('fd7cd17d-46bd-4cf5-8326-e56a9a4a4a9a')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('0c4a2235-ed3f-433e-8484-9071e14eab5d')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('98cbba6a-278b-4897-b28a-db7d7a7e469a')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('ef63ea8b-9584-4d7f-8da6-df8f0e07b4ca')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('2f638222-de05-4b09-99e8-174e139d8d7a')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('2671906b-31d8-40a7-aec0-03b6aed22f2d')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('d503e0be-b39a-4c10-859d-f75016475450')
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = UUID('6a7428d1-7543-47c5-a50a-dee1791ffbb7')
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = UUID('b07207de-f84d-4fce-9cf5-ce943917986b')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('9e85ad68-4b6e-4b23-bdaa-9f752857df43')
        self.vs[17]["name"] = """eq1"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('24e32ec5-a0fa-4def-986f-72a9fc85f00f')
        self.vs[18]["name"] = """eq2"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('84854393-0ea2-43d7-a14e-ea677cca1e15')
        self.vs[19]["name"] = """eq3"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = UUID('788f9eee-2017-4a10-a4fb-6b901a877d0e')
        self.vs[20]["name"] = """isComposite"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'Bool'"""
        self.vs[20]["GUID__"] = UUID('35e3ea2b-77b4-4a4f-b9b0-382615a06c0b')
        self.vs[21]["name"] = """hasOutgoingTransitions"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'Bool'"""
        self.vs[21]["GUID__"] = UUID('841fe2de-bf60-4ab7-b9ea-4e08a641973e')
        self.vs[22]["name"] = """pivot"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = UUID('47062edf-5037-4929-8c5d-d337413c2f83')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('5fee2295-76f9-45e2-bea6-ec4070de01f3')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('5e6c6417-52c3-4e30-984b-753521511f18')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('10937beb-00fe-4ffb-a803-821511585ee9')
        self.vs[26]["name"] = """false"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'Bool'"""
        self.vs[26]["GUID__"] = UUID('30e0d5a5-50e1-44d3-ae11-3c3f29cd215f')
        self.vs[27]["name"] = """false"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["Type"] = """'Bool'"""
        self.vs[27]["GUID__"] = UUID('0307d08d-2a42-4b85-9c1a-a13ad4e88b66')
        self.vs[28]["name"] = """procdef"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('65f3a414-b3fc-4f42-a91d-b1fb063042fd')

