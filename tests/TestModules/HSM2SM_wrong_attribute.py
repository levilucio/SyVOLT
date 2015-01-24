

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_wrong_attribute(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_wrong_attribute.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_wrong_attribute, self).__init__(name='HSM2SM_wrong_attribute', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([(2, 8), (8, 4), (2, 9), (9, 5), (4, 0), (0, 5), (6, 1), (1, 2), (3, 10), (10, 14), (7, 11), (11, 15), (12, 3), (16, 3), (4, 16), (6, 12), (6, 13), (13, 7), (5, 17), (17, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_wrong_attribute"""
        self["GUID__"] = UUID('f3b1a9a8-956b-4159-afbe-e121b69f0797')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('8fd8fa8d-8670-4a04-88aa-42a1a3cf1d70')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('072ee440-375d-452d-8b70-d0c61930a9d0')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('ef53e34b-8515-4257-9bdc-e74dc758cd5c')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """1"""
        self.vs[3]["mm__"] = """Station_S"""
        self.vs[3]["cardinality"] = """s_"""
        self.vs[3]["GUID__"] = UUID('9ba87971-0635-4348-b4b8-8f720d8c360b')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """t_"""
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["GUID__"] = UUID('66cab380-409f-44e8-8fb2-8317fff0699c')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["GUID__"] = UUID('12f0b162-29e4-49d9-b329-3e5c55360e73')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('1ac9f864-60e6-4539-b641-6c2df35bc755')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["mm__"] = """Male_S"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["GUID__"] = UUID('75e72cc2-f8bc-4d51-90a5-f612e8239525')
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = UUID('f9e75659-8bca-40d9-ae6f-ef808a3eb5c8')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('e7182470-6ba7-492b-84ef-1b6eba1aab76')
        self.vs[10]["mm__"] = """hasAttr_S"""
        self.vs[10]["GUID__"] = UUID('2478d3fa-1868-49cd-86f6-1c8ab8b4f9f9')
        self.vs[11]["mm__"] = """hasAttr_S"""
        self.vs[11]["GUID__"] = UUID('33902066-05f4-4c70-b6f8-213141d5dbe9')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('592a2c9b-4f7c-45ae-aa24-15e20f310a1c')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('a67d9313-f337-4a66-a4c8-f7f5d03134d1')
        self.vs[14]["name"] = """othername"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["GUID__"] = UUID('c45ba735-d5a1-4320-8781-b86d18242075')
        self.vs[15]["name"] = """yetanothername"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["GUID__"] = UUID('0e8fe610-c908-4ec4-b60a-cb384d9e115a')
        self.vs[16]["mm__"] = """trace_link"""
        self.vs[16]["GUID__"] = UUID('40e841c7-e927-476b-a49f-5dbf73eff68f')
        self.vs[17]["mm__"] = """trace_link"""
        self.vs[17]["GUID__"] = UUID('34a42d37-3faa-437d-bcb3-c1fb30f8c7b0')

