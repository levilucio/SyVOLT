

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HMapECU2FiveElementsFAULTY(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapECU2FiveElementsFAULTY.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapECU2FiveElementsFAULTY, self).__init__(name='HMapECU2FiveElementsFAULTY', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([(3, 13), (13, 1), (3, 14), (14, 7), (3, 15), (15, 4), (3, 16), (16, 9), (3, 17), (17, 0), (12, 0), (1, 10), (1, 12), (8, 2), (2, 3), (10, 7), (7, 11), (11, 4), (6, 5), (8, 6)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """MapECU2FiveElementsFAULTY"""
        self["GUID__"] = UUID('0189de79-ad80-46fe-8cdf-3c9660fbf97e')
        
        # Set the node attributes
        self.vs[0]["name"] = """sysmap1"""
        self.vs[0]["classtype"] = """SystemMapping"""
        self.vs[0]["mm__"] = """SystemMapping"""
        self.vs[0]["cardinality"] = """1"""
        self.vs[0]["GUID__"] = UUID('687562be-821e-439c-9fce-47ae11467678')
        self.vs[1]["name"] = """sys1"""
        self.vs[1]["classtype"] = """System"""
        self.vs[1]["mm__"] = """System"""
        self.vs[1]["cardinality"] = """1"""
        self.vs[1]["GUID__"] = UUID('cb8878f4-a1b3-4cdf-a2b5-8bf8eecca0ea')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('51d63a65-6b5a-496c-a8fb-98c920c282be')
        self.vs[3]["mm__"] = """ApplyModel"""
        self.vs[3]["GUID__"] = UUID('32133fc6-bfe9-4d0f-b977-b65d0d69dc98')
        self.vs[4]["name"] = """composty1"""
        self.vs[4]["classtype"] = """CompositionType"""
        self.vs[4]["mm__"] = """CompositionType"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = UUID('2a964067-cba1-4116-a309-e5c4d13df67c')
        self.vs[5]["name"] = """ecu1"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = UUID('8062ce53-a751-45a1-a8c7-47d36f8c9b87')
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = UUID('bfcf68b6-5aac-4559-b6c8-86b0bcc5f0d9')
        self.vs[7]["name"] = """swcompos1"""
        self.vs[7]["classtype"] = """SoftwareComposition"""
        self.vs[7]["mm__"] = """SoftwareComposition"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = UUID('7cd536cf-f1c8-4844-8c89-7320c3a6730d')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('566adad0-f3dc-4fbc-8197-9f20cee7ccaf')
        self.vs[9]["name"] = """ecuinst1"""
        self.vs[9]["classtype"] = """EcuInstance"""
        self.vs[9]["mm__"] = """EcuInstance"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = UUID('0d4bd38e-7980-46b7-b3ce-4723c7627f58')
        self.vs[10]["associationType"] = """softwareComposition"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = UUID('cb60b658-71b9-4680-a88b-61ba26893333')
        self.vs[11]["associationType"] = """softwareComposition"""
        self.vs[11]["mm__"] = """directLink_T"""
        self.vs[11]["GUID__"] = UUID('a930e9c7-cdba-4195-b662-100b250272e0')
        self.vs[12]["associationType"] = """mapping"""
        self.vs[12]["mm__"] = """directLink_T"""
        self.vs[12]["GUID__"] = UUID('ce06fc71-7463-4e49-a3eb-dc4b30f89824')
        self.vs[13]["mm__"] = """apply_contains"""
        self.vs[13]["GUID__"] = UUID('e4027808-1037-46b9-9997-195ded70a1bf')
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = UUID('d052adaa-a524-46bb-9708-315a14a45626')
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = UUID('5f608be9-21c5-413c-94ce-3dc98a9fc201')
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = UUID('67fad7b9-cb7f-4e84-9f7c-9026d0bdb3c7')
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = UUID('ff30d629-25ca-4e1f-8872-49684b5b4d9f')

