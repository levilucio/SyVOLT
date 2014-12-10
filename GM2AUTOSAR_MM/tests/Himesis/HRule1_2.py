

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HRule1_2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRule1_2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HRule1_2, self).__init__(name='HRule1_2', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(5, 0), (0, 6), (4, 9), (9, 1), (4, 10), (10, 7), (1, 3), (1, 11), (8, 2), (2, 4), (11, 5), (7, 12), (12, 6), (3, 7), (13, 5), (14, 6), (8, 13), (8, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'GM2AUTOSAR_MM'
p2
a.""")
        self["name"] = """rule1_2"""
        self["GUID__"] = UUID('9cb6f28b-ae7b-4f8e-aa88-6b745f5ff4a7')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """virtualDevice"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = UUID('4d5bd1cb-e269-48fe-a903-32f371376c17')
        self.vs[1]["name"] = """s2"""
        self.vs[1]["classtype"] = """System"""
        self.vs[1]["mm__"] = """System"""
        self.vs[1]["cardinality"] = """+"""
        self.vs[1]["GUID__"] = UUID('707b7323-3e2e-4731-b997-9ce9090c6aa5')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('e0d8abdb-3b78-4a97-b5e6-fc2337d72fb8')
        self.vs[3]["associationType"] = """softwareComposition"""
        self.vs[3]["mm__"] = """directLink_T"""
        self.vs[3]["GUID__"] = UUID('beabed3e-4a58-4e01-9651-6603447292f5')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('8b849a79-d984-4b3e-ba17-cf9332264560')
        self.vs[5]["name"] = """ecu2"""
        self.vs[5]["classtype"] = """ECU"""
        self.vs[5]["mm__"] = """ECU"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = UUID('dc22f920-b805-4cdd-be14-922cb7389072')
        self.vs[6]["name"] = """vd2"""
        self.vs[6]["classtype"] = """VirtualDevice"""
        self.vs[6]["mm__"] = """VirtualDevice"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('68a7a8a6-ae0f-44a5-8e34-22297cbbcbfd')
        self.vs[7]["name"] = """sc2"""
        self.vs[7]["classtype"] = """SoftwareComposition"""
        self.vs[7]["mm__"] = """SoftwareComposition"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('85fad338-921c-473b-8a8f-902796b2e804')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('521c6578-7c39-4875-824a-5421b58c91c0')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('363d8862-43fb-4f3f-8d52-215c27943925')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('ee9fe33b-fa56-46b4-af52-39cf08d289d4')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = UUID('33e70e74-4dbf-4370-83a3-c94317e56cea')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = UUID('f9a7bb00-05f6-402d-9007-562d7215bba5')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('74385cbd-e6b4-4500-8cd4-cdd7930046e7')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('c68a907c-c51e-4f77-929a-c0e3813fe387')

