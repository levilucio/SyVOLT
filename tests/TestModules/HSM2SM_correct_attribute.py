

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSM2SM_correct_attribute(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSM2SM_correct_attribute.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSM2SM_correct_attribute, self).__init__(name='HSM2SM_correct_attribute', num_nodes=18, edges=[])
        
        # Add the edges
        self.add_edges([(2, 8), (8, 4), (2, 9), (9, 5), (4, 0), (0, 5), (6, 1), (1, 2), (3, 10), (10, 14), (7, 11), (11, 15), (12, 3), (16, 3), (4, 16), (6, 12), (6, 13), (13, 7), (5, 17), (17, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SM2SM_correct_attribute"""
        self["GUID__"] = UUID('a409faf9-99ed-4019-914d-bcdf17efad66')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('afa75e56-ecc7-420d-92a4-c6b10c246681')
        self.vs[1]["mm__"] = """paired_with"""
        self.vs[1]["GUID__"] = UUID('1a246efa-0648-4a60-9bd3-ceb5ca069047')
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = UUID('a939367e-f57b-493f-9036-819c4a38e2a7')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """1"""
        self.vs[3]["mm__"] = """Station_S"""
        self.vs[3]["cardinality"] = """s_"""
        self.vs[3]["GUID__"] = UUID('7eb7c10e-ccab-451c-ad60-897696d0118a')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """t_"""
        self.vs[4]["mm__"] = """Station_T"""
        self.vs[4]["GUID__"] = UUID('affefa23-ed97-432c-98e2-3b7450897892')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """t_"""
        self.vs[5]["mm__"] = """Male_T"""
        self.vs[5]["GUID__"] = UUID('7812f7fd-c40b-4a54-8e9c-4385a1717fe5')
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = UUID('39588145-c71f-4afa-99f7-a5dc9c6f6d21')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """1"""
        self.vs[7]["mm__"] = """Male_S"""
        self.vs[7]["cardinality"] = """s_"""
        self.vs[7]["GUID__"] = UUID('d7c5f938-2665-4d31-a373-9c7c6584e667')
        self.vs[8]["mm__"] = """apply_contains"""
        self.vs[8]["GUID__"] = UUID('ffa7fb8f-44d0-45fd-9559-45bbdb09731c')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('2974add4-735f-4d45-8e8f-7f6ff534e576')
        self.vs[10]["mm__"] = """hasAttr_S"""
        self.vs[10]["GUID__"] = UUID('471605b9-4e1c-455f-8f63-bb46a3d08f7e')
        self.vs[11]["mm__"] = """hasAttr_S"""
        self.vs[11]["GUID__"] = UUID('b7cf39bb-2ebb-43bf-94be-dd780b1bad11')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('bd2293e1-11b4-4563-aac5-fb01e890d29a')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('de31f917-00f8-4286-955a-979d487341e9')
        self.vs[14]["name"] = """name"""
        self.vs[14]["mm__"] = """Attribute"""
        self.vs[14]["GUID__"] = UUID('d17ace3d-2df3-41b5-939f-38b8662e8e0c')
        self.vs[15]["name"] = """name"""
        self.vs[15]["mm__"] = """Attribute"""
        self.vs[15]["GUID__"] = UUID('d0832294-ea32-4b99-aace-9b64b2a2b80e')
        self.vs[16]["mm__"] = """trace_link"""
        self.vs[16]["GUID__"] = UUID('93f0927f-9a43-4a15-b244-c73da13331f9')
        self.vs[17]["mm__"] = """trace_link"""
        self.vs[17]["GUID__"] = UUID('42fbd3c8-b693-401d-a7df-b8e9bb6d483b')

