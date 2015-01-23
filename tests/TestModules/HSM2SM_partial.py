

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_partial(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_partial.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_partial, self).__init__(name='HSM2SM_partial', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([(2, 8), (8, 4), (2, 9), (9, 5), (4, 0), (0, 5), (6, 1), (1, 2), (4, 10), (10, 3), (5, 11), (11, 7), (3, 12), (12, 16), (7, 13), (13, 17), (14, 3), (6, 14), (6, 15), (15, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_partial"""
        self["GUID__"] = UUID('05d103f4-7b67-4968-8906-d0dbd4886f17')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('8f20ed0f-c647-4838-ac5c-5fd8317fbcda')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('4bc7f8b5-3caf-469f-b54a-f4945ff24c31')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('cf1f4896-1d1d-49ae-ac4f-50c2a0b0f167')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """1"""
        self.vs[3]["mm__"] = """Station_S"""
        self.vs[3]["cardinality"] = """s_"""
        self.vs[3]["GUID__"] = UUID('a2930c9e-5c94-41d9-8099-6ee2e22a48d5')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """t_"""
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["GUID__"] = UUID('d9ea3c38-c924-4b1d-bea0-9b48429c61de')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["GUID__"] = UUID('27ae1efc-ad10-4cdd-81c3-7aae052b0a90')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('590043d7-5915-4853-8c46-28cae15a6a50')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["mm__"] = """Male_S"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["GUID__"] = UUID('713e044d-7c74-4cba-8784-c73d11a1ccf1')
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = UUID('d4af14d8-0594-4c92-9dc5-6d75c4db7049')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('41cb7a73-1e24-4056-9836-3defe142c47e')
        self.vs[10]["mm__"] = """backward_link"""
        self.vs[10]["GUID__"] = UUID('1db8d605-fe56-48bc-b431-1dbac83a09ef')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('97010236-c89d-4227-b2d2-6b7c1d480770')
        self.vs[12]["mm__"] = """hasAttr_S"""
        self.vs[12]["GUID__"] = UUID('fde8bdc2-9dfb-4057-b708-a43683ef08f9')
        self.vs[13]["mm__"] = """hasAttr_S"""
        self.vs[13]["GUID__"] = UUID('0b31e99a-3fac-4721-b405-09c8aa1d3c90')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('08472018-509f-4b66-a533-ca3a4e238aba')
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = UUID('866e4392-cbe0-4fae-a08a-e111bff7fe3b')
        self.vs[16]["name"] = """name"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = UUID('5292e597-9fa5-4b8e-b987-f182dcf1d95f')
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["GUID__"] = UUID('df9502e1-6096-4792-9fa7-acd4d2cd6043')

