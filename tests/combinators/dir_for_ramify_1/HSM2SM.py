

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM, self).__init__(name='HSM2SM', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(2, 9), (9, 5), (2, 10), (10, 6), (5, 0), (0, 6), (7, 1), (1, 2), (5, 11), (11, 4), (6, 12), (12, 8), (4, 3), (3, 8), (13, 4), (7, 13), (7, 14), (14, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM"""
        self["GUID__"] = UUID('cc3fd644-21a1-43df-95a2-f34c25051124')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('c4f54adc-3964-4242-91ed-93fde08e8626')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('7c20ebc9-4d36-4356-a007-6c833b607cab')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('5b77f4a3-f504-491a-a1be-194064a9bb67')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('3998c665-525c-412f-b3ea-10756dddd288')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """1"""
        self.vs[4]["mm__"] = """Station_S"""
        self.vs[4]["cardinality"] = """s_"""
        self.vs[4]["GUID__"] = UUID('1eb29cc0-6f72-4fbd-b452-b1992a41f473')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('269ae635-3c89-4bf7-8d0f-8f75c71893e0')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Male_T"""
        self.vs[6]["GUID__"] = UUID('8861e26f-a52d-4731-ab78-b2d1de7e7020')
        self.vs[7]["mm__"] = """MatchModel"""
        self.vs[7]["GUID__"] = UUID('a5e2b7af-8114-4e3a-a68e-4e68dfc9a5a6')
        self.vs[8]["name"] = """s_"""
        self.vs[8]["classtype"] = """1"""
        self.vs[8]["mm__"] = """Male_S"""
        self.vs[8]["cardinality"] = """s_"""
        self.vs[8]["GUID__"] = UUID('e7e201bc-0566-49ad-be9a-3258fc2f2b01')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('13069109-6b89-4fc0-b888-ad547a1ec750')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('a295144a-2b00-487a-8e5d-4e71b793cdc3')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('d7c197b3-4bca-4aa7-ad07-f2871a497999')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('49384bb0-96aa-4187-ae2b-8a79a5bb538f')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('52f2b274-98c0-4df6-bc76-736dd527123c')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('325d1843-cc4b-46c5-9dc4-fee1071ba6a3')

