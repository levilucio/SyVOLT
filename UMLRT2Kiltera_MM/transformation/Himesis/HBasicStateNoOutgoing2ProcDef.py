

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
        self["GUID__"] = UUID('cf50ec15-675a-4bdb-b8e5-dd5a28c1eba7')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """p"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('f6a842c7-3d2b-4210-91ac-ffc996d61a02')
        self.vs[1]["mm__"] = """hasAttribute_T"""
        self.vs[1]["GUID__"] = UUID('2c28ab14-8e1e-4d2a-b80c-acdab2e0fc41')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('d5f99b76-8c52-4ece-8521-b75c9573f61c')
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = UUID('c5101b6a-1e2b-44a0-9190-b1964eebceb9')
        self.vs[4]["name"] = """state1"""
        self.vs[4]["classtype"] = """State"""
        self.vs[4]["mm__"] = """State"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = UUID('4c742c56-fe4f-4adc-a910-2ee2b81cb17b')
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = UUID('b4a3aaa2-e84b-4d52-8781-0824de608300')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('2cf99bbc-c4a2-4163-8301-b3cbfc25a6e3')
        self.vs[7]["name"] = """null1"""
        self.vs[7]["classtype"] = """Null"""
        self.vs[7]["mm__"] = """Null"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('7fc265e4-6e5d-4b20-919a-a1152c4711bb')
        self.vs[8]["name"] = """procdef1"""
        self.vs[8]["classtype"] = """ProcDef"""
        self.vs[8]["mm__"] = """ProcDef"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('e9a7acdd-1d7f-42c5-8ae5-f674285a4d3e')
        self.vs[9]["type"] = """ruleDef"""
        self.vs[9]["mm__"] = """backward_link"""
        self.vs[9]["GUID__"] = UUID('18ed52a6-95cc-4bce-9c6d-4bb0d781632c')
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = UUID('797f9b10-72b3-492c-92b4-2974e943e208')
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = UUID('309bfd00-cd27-488f-8c12-44d9f9e86916')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('f01be0e3-14e4-4eb9-ac0c-21a552fc53c8')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('40075334-2c88-4966-94b0-0758ba528b2e')
        self.vs[14]["mm__"] = """rightExpr"""
        self.vs[14]["GUID__"] = UUID('20c4b111-d2af-4118-a01e-c7a2d1c2d876')
        self.vs[15]["mm__"] = """rightExpr"""
        self.vs[15]["GUID__"] = UUID('5760b586-b2f2-4b05-984f-6e4542e5e54d')
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = UUID('2b3c9d45-4732-4124-b4da-a1002b90a75f')
        self.vs[17]["name"] = """eq1"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('b77545e4-6394-4ee1-8ebd-22fdebe134d5')
        self.vs[18]["name"] = """eq2"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('7fd746d4-6008-4cac-bcad-802886c27206')
        self.vs[19]["name"] = """eq3"""
        self.vs[19]["mm__"] = """Equation"""
        self.vs[19]["GUID__"] = UUID('8449bf42-9aee-471b-9d4f-b8e3b0f3afe7')
        self.vs[20]["name"] = """isComposite"""
        self.vs[20]["mm__"] = """Attribute"""
        self.vs[20]["Type"] = """'Bool'"""
        self.vs[20]["GUID__"] = UUID('1caf6137-588f-4627-bcc3-ffd6fc554986')
        self.vs[21]["name"] = """hasOutgoingTransitions"""
        self.vs[21]["mm__"] = """Attribute"""
        self.vs[21]["Type"] = """'Bool'"""
        self.vs[21]["GUID__"] = UUID('9fa66109-ddbd-4e5a-a1a0-575eb4b23989')
        self.vs[22]["name"] = """pivotin"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["GUID__"] = UUID('efe20919-c600-48c0-9782-be8ffbd3bbcb')
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = UUID('64b6310c-a831-43fb-8463-24beb278e7a0')
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = UUID('2a84eba3-0d1c-4453-8ab0-e8cc0eb41b75')
        self.vs[25]["mm__"] = """leftExpr"""
        self.vs[25]["GUID__"] = UUID('ed9be5aa-73b5-4329-bbcf-55d855e8f372')
        self.vs[26]["name"] = """false"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["Type"] = """'Bool'"""
        self.vs[26]["GUID__"] = UUID('6552e90c-103e-4764-a5e6-33715d38a69d')
        self.vs[27]["name"] = """false"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["Type"] = """'Bool'"""
        self.vs[27]["GUID__"] = UUID('c92ab1d2-3af9-465d-bd96-026a858c2a80')
        self.vs[28]["name"] = """procdef"""
        self.vs[28]["mm__"] = """Constant"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["GUID__"] = UUID('0dcaaea1-9925-4f93-b29d-66dc8dcaf52a')

