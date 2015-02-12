

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSF2SF(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF, self).__init__(name='HSF2SF', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 6), (2, 10), (10, 3), (6, 0), (0, 3), (17, 11), (11, 25), (18, 12), (12, 26), (8, 1), (1, 2), (6, 13), (13, 5), (3, 14), (14, 7), (5, 15), (15, 25), (7, 16), (16, 26), (5, 4), (4, 7), (19, 5), (20, 7), (17, 23), (18, 24), (8, 19), (8, 20), (23, 21), (24, 22)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SF2SF"""
        self["GUID__"] = UUID('5cacf37f-a846-4017-b006-c6fa9826f9bf')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('fbb2711f-5b8f-4650-a539-ea4e2b3952a3')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('ad5d00f6-a468-4284-bfa9-d55151111fb8')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('9b6593cb-83d1-4a52-ad99-40144260a707')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """t_"""
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["GUID__"] = UUID('663fdb60-fce5-44b6-8586-43bc535042e7')
        self.vs[4]["mm__"] = """indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('ba2de2ab-6f00-4543-a3e4-a493ee2463ce')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """1"""
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["cardinality"] = """s_"""
        self.vs[5]["GUID__"] = UUID('ff7eef6c-df41-4d37-8793-f109ebf38ac8')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Station_T"""
        self.vs[6]["GUID__"] = UUID('e196955d-89f6-4c8f-b3e2-a7a1d6745748')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["GUID__"] = UUID('5da3fa50-3b03-47fc-987c-4eb7acd36b86')
        self.vs[8]["mm__"] = """MatchModel"""
        self.vs[8]["GUID__"] = UUID('4f6d5aa2-3642-4241-9e37-1dd3bf61b5dc')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('208f9d6b-e2fc-4d41-bfad-04e5308b8d54')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('d0f89f56-f3a4-40c0-bdbc-58926e820b83')
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = UUID('f5d4fcb7-f3a3-433d-890a-66af91b18cfe')
        self.vs[12]["mm__"] = """leftExpr"""
        self.vs[12]["GUID__"] = UUID('831d82df-45f5-4baa-89ea-4cc43a951796')
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["GUID__"] = UUID('ac66c775-aa97-448a-ab47-b89cef8d0cc3')
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["GUID__"] = UUID('116499e6-be94-4799-a20a-dc6865ff7748')
        self.vs[15]["mm__"] = """hasAttribute_S"""
        self.vs[15]["GUID__"] = UUID('a8082fbe-a552-4b69-be8e-e3e08bcbcbc4')
        self.vs[16]["mm__"] = """hasAttribute_S"""
        self.vs[16]["GUID__"] = UUID('83981992-f4a7-4e40-b52b-f4818e46acfa')
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = UUID('dc5e2f24-662d-4c85-994a-187d60c7f5eb')
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = UUID('cd0a14a7-cb32-42f1-a6e1-f8ee4f935e16')
        self.vs[19]["mm__"] = """match_contains"""
        self.vs[19]["GUID__"] = UUID('e0c5097f-de01-4acc-8f15-4998dd4792ee')
        self.vs[20]["mm__"] = """match_contains"""
        self.vs[20]["GUID__"] = UUID('def95e8e-ee2d-4f94-8dd5-327db1d1d866')
        self.vs[21]["name"] = """somestation"""
        self.vs[21]["mm__"] = """Constant"""
        self.vs[21]["GUID__"] = UUID('27597da0-0589-40b3-96aa-d4dd9ae0d178')
        self.vs[22]["name"] = """otherfemale"""
        self.vs[22]["mm__"] = """Constant"""
        self.vs[22]["GUID__"] = UUID('a4533ef4-6789-42b2-94f9-040ead7453e3')
        self.vs[23]["mm__"] = """rightExpr"""
        self.vs[23]["GUID__"] = UUID('3ea0c455-a6b7-4665-9ba7-ba5cc6495ca2')
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = UUID('93e95d5a-5992-46ad-a0fe-3b651bf42ce5')
        self.vs[25]["name"] = """name"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["GUID__"] = UUID('e3f036d0-985a-4109-9dcd-ec72b2715afd')
        self.vs[26]["name"] = """name"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = UUID('ba113979-0fe1-421a-a2e9-38f5bfb4eb2b')

