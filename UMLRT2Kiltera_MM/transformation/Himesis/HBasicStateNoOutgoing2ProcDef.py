

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
        self["GUID__"] = UUID('ac701ece-046c-490f-93dd-692568fec361')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """p"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('38fea26e-58f8-4008-894b-7edf54ee5490')
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('b15e8d2c-ab1a-439d-bae5-b501ccd00b1e')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('d56845e1-c440-4b59-bb7f-46e8169f49d0')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('6e8b148c-70f5-4c0a-8111-e88ee7433bf3')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('1e52e718-b19c-4aa1-97e6-1c036b937a1b')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('72138778-a27d-430c-a091-9cea362418f1')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('7743998b-abb0-40d0-b55c-65b00a37fee7')
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('450485d1-48ee-449f-be22-8993a1fa3431')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('bcd00c6b-6530-410c-8801-e273577b079e')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('cb639448-398e-4d36-8c1f-9cf7b375d903')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('7205aa2c-67c8-4cc1-8627-8e17a65d5e8b')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('3713f991-ad4a-4205-9fe8-f89d3c3b483c')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('9ee82b05-1d40-48b3-acb6-5fe94e5989ef')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('03e8b04a-39cb-4dd8-86fd-a44422f44e29')
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = UUID('b06b3c5e-4012-42a9-8378-06380231949e')
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = UUID('01ff1095-5dcc-478b-bbc8-0d83d684548c')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('82d4d2e7-741c-4bd0-b41c-8bf99ed35ab1')
        self.vs[17]["name"] = """eq1"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('193d7043-7a34-481f-a23e-e942c419d99b')
        self.vs[18]["name"] = """eq2"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('d98fdaa7-f04b-4b2a-b792-b89aa5c2aac1')
        self.vs[19]["name"] = """eq3"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = UUID('0a56ecca-943e-4c51-932b-1c5a25c1623e')
        self.vs[20]["name"] = """isComposite"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'Bool'"""
        self.vs[20]["GUID__"] = UUID('fa04135f-e9ed-4cec-8765-e28fed584b0c')
        self.vs[21]["name"] = """hasOutgoingTransitions"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'Bool'"""
        self.vs[21]["GUID__"] = UUID('b1744bd4-b59b-445e-a308-08c3bf13a34c')
        self.vs[22]["name"] = """pivot"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = UUID('dfb0626f-a677-4f4b-a3ed-5d8147a60679')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('c0e40998-a409-4afc-8d93-8df2885666fd')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('57f049ac-e3f0-459e-ae03-ddcaa9cd0ec9')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('09d4b90d-c314-4d07-8171-7ff4be9167cc')
        self.vs[26]["name"] = """false"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'Bool'"""
        self.vs[26]["GUID__"] = UUID('111b9e8a-4819-4602-9b22-df6bf5ecd17d')
        self.vs[27]["name"] = """false"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["Type"] = """'Bool'"""
        self.vs[27]["GUID__"] = UUID('1b2ed0f1-1cbb-41ed-8308-167ab4ad3d3c')
        self.vs[28]["name"] = """procdef"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('938a581e-5c10-446a-b14b-fe8d8da67ebb')

