

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
        self["GUID__"] = UUID('08346ac3-1a47-4fed-a83e-4b403ea6994d')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """p"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('58ab6e87-4551-443e-bfff-63fbaec4aece')
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('9fb62753-1769-4343-a251-1e39317acbe9')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('d972c3f8-f639-4f7c-84ff-8363453a522d')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('5f94aced-772a-4fb2-bfc5-9814cf857f1d')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('c6922e5f-99ee-4364-a792-6c57221d528a')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('8ce1a5f1-3270-49b7-9a0f-7d0d26f809f7')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('4420071f-e83a-4268-8800-632cf7217570')
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('126a0f48-d3d4-418e-99cc-119845c0824b')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('9233ea41-f0ba-46a2-9cf5-1afcc0e29357')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('ec016c81-d5de-4142-be2b-a2c199b4bd4d')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('08746aa3-1cce-4d1b-836a-a4a32027579c')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('c044e48e-3dbf-4672-a699-664c44b592ea')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('c3bea447-16d5-4b5f-b46c-04410400b949')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('32976621-348e-41b9-9d9e-0e5cc18f7983')
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = UUID('2084dd88-dcc6-4cc4-bf73-4e6ba642889d')
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = UUID('5f6be339-0999-4fd7-9e9d-eb543ad11b08')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('0db1fbd6-cb67-4813-963f-9e0c55025b24')
        self.vs[17]["name"] = """eq1"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('8b49bbf3-1bf9-428d-84ed-d98e720da5d5')
        self.vs[18]["name"] = """eq2"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('97df9a79-4269-4dfe-8196-a03ec0a36eca')
        self.vs[19]["name"] = """eq3"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = UUID('7d22d7b5-ae26-4fae-8ca0-6ac250ed9d1b')
        self.vs[20]["name"] = """isComposite"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'Bool'"""
        self.vs[20]["GUID__"] = UUID('a9c9e9b8-d009-40a7-a9ea-df0fc913200d')
        self.vs[21]["name"] = """hasOutgoingTransitions"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'Bool'"""
        self.vs[21]["GUID__"] = UUID('afd9794f-4f68-4d05-94ab-d63985935fce')
        self.vs[22]["name"] = """pivotin"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = UUID('ab7d9cc5-6f6b-496b-a28b-9f5d80992d12')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('f76659f6-1300-451e-91d1-41677c07802c')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('d6d9217b-413d-485e-92b7-714d2727a400')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('6c08f50c-fa5f-417e-ae40-7d2964489148')
        self.vs[26]["name"] = """false"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'Bool'"""
        self.vs[26]["GUID__"] = UUID('780ccb04-ca3a-4391-a999-828acfbc3691')
        self.vs[27]["name"] = """false"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["Type"] = """'Bool'"""
        self.vs[27]["GUID__"] = UUID('4ebd2dfc-60e3-47f5-ac8a-395158a30a95')
        self.vs[28]["name"] = """procdef"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('e1138885-34ab-4053-98d8-8006df3406f3')

