

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMapECU2FiveElements(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapECU2FiveElements.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapECU2FiveElements, self).__init__(name='HMapECU2FiveElements', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(6, 11), (11, 7), (7, 12), (12, 1), (4, 19), (19, 2), (4, 20), (20, 8), (4, 21), (21, 5), (4, 22), (22, 10), (4, 23), (23, 0), (15, 0), (18, 1), (2, 13), (2, 15), (9, 3), (3, 4), (13, 8), (8, 14), (14, 5), (16, 6), (17, 7), (9, 16), (9, 17), (9, 18)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """MapECU2FiveElements"""
        self["GUID__"] = UUID('dde0672d-e2fa-472f-a64b-45015182f1aa')
        
        # Set the node attributes
        self.vs[0]["name"] = """sysmap1"""
        self.vs[0]["classtype"] = """SystemMapping"""
        self.vs[0]["mm__"] = """SystemMapping"""
        self.vs[0]["cardinality"] = """1"""
        self.vs[0]["GUID__"] = UUID('e3b4eb5c-49c5-4a31-b090-3a0d50f7d66e')
        self.vs[1]["name"] = """dist1"""
        self.vs[1]["classtype"] = """Distributable"""
        self.vs[1]["mm__"] = """Distributable"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('67c59f13-88cb-4dbf-9389-1a040e65d429')
        self.vs[2]["name"] = """sys1"""
        self.vs[2]["classtype"] = """System"""
        self.vs[2]["mm__"] = """System"""
        self.vs[2]["cardinality"] = """1"""
        self.vs[2]["GUID__"] = UUID('c615651a-147d-4922-b097-db637189a742')
        self.vs[3]["mm__"] = """paired_with"""
        self.vs[3]["GUID__"] = UUID('4ce09d40-29bf-4988-a894-e46587719188')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('22967a9f-7c55-4a4b-8f8c-6012d9a77ba5')
        self.vs[5]["name"] = """composty1"""
        self.vs[5]["classtype"] = """CompositionType"""
        self.vs[5]["mm__"] = """CompositionType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = UUID('0014d3aa-0eff-482e-9485-9d93f8b277a9')
        self.vs[6]["name"] = """ecu1"""
        self.vs[6]["classtype"] = """ECU"""
        self.vs[6]["mm__"] = """ECU"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('637c789b-6775-48a5-b351-99c2f1a0fdf1')
        self.vs[7]["name"] = """vd1"""
        self.vs[7]["classtype"] = """VirtualDevice"""
        self.vs[7]["mm__"] = """VirtualDevice"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('977b0c98-b786-4a62-bebf-37af4fda18e8')
        self.vs[8]["name"] = """swcompos1"""
        self.vs[8]["classtype"] = """SoftwareComposition"""
        self.vs[8]["mm__"] = """SoftwareComposition"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = UUID('f4e5950a-29eb-4815-97e5-b46fffa02bea')
        self.vs[9]["mm__"] = """MatchModel"""
        self.vs[9]["GUID__"] = UUID('5b83274c-ed6f-4e41-825d-3fa61327df85')
        self.vs[10]["name"] = """ecuinst1"""
        self.vs[10]["classtype"] = """EcuInstance"""
        self.vs[10]["mm__"] = """EcuInstance"""
        self.vs[10]["cardinality"] = """1"""
        self.vs[10]["GUID__"] = UUID('30b3cecd-8212-4696-81cc-e726143bdf0a')
        self.vs[11]["associationType"] = """virtualDevice"""
        self.vs[11]["mm__"] = """directLink_S"""
        self.vs[11]["GUID__"] = UUID('f9ddbb4d-8d94-4cc2-8de5-98bb186b39a1')
        self.vs[12]["associationType"] = """distributable"""
        self.vs[12]["mm__"] = """directLink_S"""
        self.vs[12]["GUID__"] = UUID('a95215b9-ed36-490a-8e9b-22a85b912e1f')
        self.vs[13]["associationType"] = """softwareComposition"""
        self.vs[13]["mm__"] = """directLink_T"""
        self.vs[13]["GUID__"] = UUID('deac04bb-0b30-4eec-82c8-4d54b4feccef')
        self.vs[14]["associationType"] = """softwareComposition"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = UUID('43348d09-c69b-40a3-b57a-d3feeec7adb2')
        self.vs[15]["associationType"] = """mapping"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = UUID('56f8b9a3-d0c8-4f7e-8de4-8c910fa89036')
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = UUID('317c56c0-a0a8-4739-9138-4f03b8ebd2c5')
        self.vs[17]["mm__"] = """match_contains"""
        self.vs[17]["GUID__"] = UUID('7c5896ab-9e32-437a-a2f3-0d9c98753bfa')
        self.vs[18]["mm__"] = """match_contains"""
        self.vs[18]["GUID__"] = UUID('678c88de-02b9-4c5b-8c83-264d90047cc7')
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = UUID('7f243209-6695-413a-bff4-6f46f1f1c485')
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = UUID('98af4346-74eb-46df-8c0e-eaa0bf80fdab')
        self.vs[21]["mm__"] = """apply_contains"""
        self.vs[21]["GUID__"] = UUID('5e0cab53-f22c-4aca-8129-aeabab7783a2')
        self.vs[22]["mm__"] = """apply_contains"""
        self.vs[22]["GUID__"] = UUID('559a4ca3-0996-4098-87de-80ffaa043830')
        self.vs[23]["mm__"] = """apply_contains"""
        self.vs[23]["GUID__"] = UUID('78841fa1-4341-4764-bf05-9611703cf257')

