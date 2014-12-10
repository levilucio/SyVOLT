

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HConnectRPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HConnectRPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectRPortPrototype, self).__init__(name='HConnectRPortPrototype', num_nodes=23, edges=[])
        
        # Add the edges
        self.add_edges([(6, 14), (14, 7), (7, 15), (15, 0), (0, 16), (16, 8), (8, 17), (17, 9), (4, 12), (12, 5), (4, 13), (13, 11), (20, 0), (10, 1), (1, 4), (5, 2), (2, 6), (5, 3), (3, 11), (18, 6), (19, 7), (21, 8), (22, 9), (10, 18), (10, 19), (10, 20), (10, 21), (10, 22)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """ConnectRPortPrototype"""
        self["GUID__"] = UUID('a56bd140-5b4a-43ff-8bf5-fdd465e15e43')
        
        # Set the node attributes
        self.vs[0]["name"] = """dist1"""
        self.vs[0]["classtype"] = """Distributable"""
        self.vs[0]["mm__"] = """Distributable"""
        self.vs[0]["cardinality"] = """+"""
        self.vs[0]["GUID__"] = UUID('905cde79-1996-4901-9b34-158528ec1708')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('27d72a45-84ee-44ca-bad3-b871954201fe')
        self.vs[2]["mm__"] = """backward_link"""
        self.vs[2]["type"] = """ruleDef"""
        self.vs[2]["GUID__"] = UUID('2f4b3983-2524-4234-8d52-cc4a523abc90')
        self.vs[3]["associationType"] = """port"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = UUID('cd0dd0be-0a0e-4b9f-9d46-c983da5fa79a')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('6054104a-89bd-4b3a-ac46-031961dc69c1')
        self.vs[5]["name"] = """composty1"""
        self.vs[5]["classtype"] = """CompositionType"""
        self.vs[5]["mm__"] = """CompositionType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('2d5e1d2f-1f02-4915-923a-89865e69d6f7')
        self.vs[6]["name"] = """ecu1"""
        self.vs[6]["classtype"] = """ECU"""
        self.vs[6]["mm__"] = """ECU"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('69b8c1b1-91b1-4a38-8a51-cfc228787e74')
        self.vs[7]["name"] = """vd1"""
        self.vs[7]["classtype"] = """VirtualDevice"""
        self.vs[7]["mm__"] = """VirtualDevice"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('b5dfbf0c-3d9e-46dc-b691-81f96ba415ce')
        self.vs[8]["name"] = """ef1"""
        self.vs[8]["classtype"] = """ExecFrame"""
        self.vs[8]["mm__"] = """ExecFrame"""
        self.vs[8]["cardinality"] = """+"""
        self.vs[8]["GUID__"] = UUID('f4d1d4fb-6e36-4059-96aa-8cdb9a71cef2')
        self.vs[9]["name"] = """sig1"""
        self.vs[9]["classtype"] = """Signal"""
        self.vs[9]["mm__"] = """Signal"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('4187dced-b7e4-4a4d-bac2-05c335db5faf')
        self.vs[10]["mm__"] = """MatchModel"""
        self.vs[10]["GUID__"] = UUID('58006b86-3615-45ac-a9bb-3800cc549cd3')
        self.vs[11]["name"] = """rport1"""
        self.vs[11]["classtype"] = """RPortPrototype"""
        self.vs[11]["mm__"] = """RPortPrototype"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = UUID('a674e4da-bf71-4cdd-a495-2940ec7c69a3')
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = UUID('fefcd754-a93b-41fa-a87a-c1e0da9d2717')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('e1e2c0cf-d386-4b60-8457-99be5f650e62')
        self.vs[14]["associationType"] = """virtualDevice"""
        self.vs[14]["mm__"] = """directLink_S"""
        self.vs[14]["GUID__"] = UUID('be15f4ea-65f8-47ce-9795-2c41cdad897e')
        self.vs[15]["associationType"] = """distributable"""
        self.vs[15]["mm__"] = """directLink_S"""
        self.vs[15]["GUID__"] = UUID('a6dc00a0-4ab7-4c1b-98f8-1b3f700b6286')
        self.vs[16]["associationType"] = """execFrame"""
        self.vs[16]["mm__"] = """directLink_S"""
        self.vs[16]["GUID__"] = UUID('fda28a45-cbb0-48de-8bed-9baf3012f227')
        self.vs[17]["associationType"] = """required"""
        self.vs[17]["mm__"] = """directLink_S"""
        self.vs[17]["GUID__"] = UUID('20cd4479-c663-4d09-b9ca-9e15fecf5c89')
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = UUID('97dbd320-e564-4af2-bc7c-efa0578b5de5')
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = UUID('573dd05f-befb-447b-9070-9d207ab03dc9')
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = UUID('39921227-19fe-4bb5-957b-91191a63a082')
        self.vs[21]["mm__"] = """match_contains"""
        self.vs[21]["GUID__"] = UUID('926d7f23-8536-4fe7-9bd8-aae9f51678c8')
        self.vs[22]["mm__"] = """match_contains"""
        self.vs[22]["GUID__"] = UUID('d8ef6c6d-7d11-4f5c-bfea-4398c3eb346a')

