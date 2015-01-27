

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
        self["GUID__"] = UUID('9c676da8-6b0d-4b3f-a898-236ea9e186e1')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """p"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('dfb30889-33fd-4132-8b1e-047682551b1b')
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('738a3785-937f-4e1d-afb9-29abdce82422')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('2a13808c-f431-49d9-9858-e5cd58442baa')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('a1dba4ad-b4b2-47d9-b1e1-1d431188654f')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('c052cfe1-8904-465b-b9a3-d85ad852ff73')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('def59445-56e5-4784-83ee-0d1a7aaef28c')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('c3e0fd4c-8e8e-4716-880e-fc762adfe80c')
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('828f3777-4f40-4cdb-b8a1-e25e5b0a7ec7')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('7706080f-bd96-4014-9aa2-ba61b3e54553')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('608fe1cb-a297-4e8d-ab53-4447b20cda71')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('6450ed6b-6cee-4520-8603-5faaa6b3844a')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('49d2cf75-ddb8-4257-9a7d-416202297a3e')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('5f2c6dd2-a54f-4872-ae3e-bc077199d1ba')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('ca112930-e3a3-4a54-ba65-8285a7cc90b0')
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = UUID('d792f537-305e-4068-aedd-78b23d2176dd')
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = UUID('4f1cb3e9-794f-437f-9231-a8b126e12bd3')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('ff05c2cb-6c72-46aa-bf4e-4c48d23d5f29')
        self.vs[17]["name"] = """eq1"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('a178e944-5e87-4342-bc8b-3bb501bbaa9c')
        self.vs[18]["name"] = """eq2"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('0b283fa4-29bc-4d1a-848d-fa453891f35e')
        self.vs[19]["name"] = """eq3"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = UUID('12576e47-3145-4384-83f0-27b6aa438613')
        self.vs[20]["name"] = """isComposite"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'Bool'"""
        self.vs[20]["GUID__"] = UUID('2f4b8933-73e0-4672-bb02-35d0dda935a4')
        self.vs[21]["name"] = """hasOutgoingTransitions"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'Bool'"""
        self.vs[21]["GUID__"] = UUID('9e03d897-0c08-43b5-8576-4b0419220f3f')
        self.vs[22]["name"] = """pivotin"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = UUID('6521737c-99b5-41ba-a243-3c0b46eea24d')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('8e36e4a2-0623-49a0-9302-3184c72c5c9c')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('76d4909b-d446-44e4-82b9-ade0b9015aca')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('4726d9d3-ffc9-485c-a1c4-02fb4d8fc68b')
        self.vs[26]["name"] = """false"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'Bool'"""
        self.vs[26]["GUID__"] = UUID('fc84419c-a439-4db5-96e2-b6d76a08fc4d')
        self.vs[27]["name"] = """false"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["Type"] = """'Bool'"""
        self.vs[27]["GUID__"] = UUID('e7c3a397-2a0c-42cc-bd4d-338eba0fc124')
        self.vs[28]["name"] = """procdef"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('f5feefe5-78e2-45d3-8b36-da100cc0b9f9')

