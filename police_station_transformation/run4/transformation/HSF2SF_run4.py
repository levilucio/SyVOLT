

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HSF2SF_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSF2SF_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSF2SF_run4, self).__init__(name='HSF2SF_run4', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (9, 5), (1, 10), (10, 3), (5, 11), (11, 6), (3, 12), (12, 7), (5, 0), (0, 3), (8, 1), (2, 8), (2, 13), (2, 14), (6, 4), (4, 7), (13, 6), (14, 7)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """SF2SF_run4"""
        self["GUID__"] = UUID('82e533ed-4d5c-46a5-8577-f862a076ef9e')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('a445d69b-9ea0-4f93-b0cf-d0e02510d43b')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('dcc04053-3733-4899-b7c4-2637c91f0056')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('a6cbfcdd-a543-441b-ae9f-c33c0cf3ecb5')
        self.vs[3]["name"] = """f"""
        self.vs[3]["classtype"] = """female4"""
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["GUID__"] = UUID('bd1244e0-9e39-4d63-a92d-d862603c45ba')
        self.vs[4]["mm__"] = """indirectLink_S"""
        self.vs[4]["GUID__"] = UUID('a4ae493e-3138-4de6-8d62-c06aa928c603')
        self.vs[5]["name"] = """s"""
        self.vs[5]["classtype"] = """station4"""
        self.vs[5]["mm__"] = """Station_T"""
        self.vs[5]["GUID__"] = UUID('1371a243-edbf-4d1f-a630-442949b8e844')
        self.vs[6]["name"] = """s"""
        self.vs[6]["classtype"] = """station4"""
        self.vs[6]["mm__"] = """Station_S"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = UUID('67544367-c463-4696-a76f-05baa8150d0d')
        self.vs[7]["name"] = """f"""
        self.vs[7]["classtype"] = """female4"""
        self.vs[7]["mm__"] = """Female_S"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = UUID('ba81859b-21ed-44f8-9553-b86e3c38aacb')
        self.vs[8]["mm__"] = """paired_with"""
        self.vs[8]["GUID__"] = UUID('b0047ee0-5848-4c97-94a2-0bba310d7629')
        self.vs[9]["mm__"] = """apply_contains"""
        self.vs[9]["GUID__"] = UUID('01f9d0b3-9d16-4bb9-a96e-8ded3e133acf')
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = UUID('6fa29e96-14c5-4222-9273-37864d98d2a7')
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["GUID__"] = UUID('1c8969aa-6417-468d-ab1f-d8f49eb7a6a8')
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["GUID__"] = UUID('3bdc37c8-c7d4-43ed-8fe1-b9ff888cd67b')
        self.vs[13]["mm__"] = """match_contains"""
        self.vs[13]["GUID__"] = UUID('063706bc-6050-49bf-95c9-b39cbaa5e2f9')
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = UUID('a9616ac6-c83c-46a3-b386-eeab2708e1ab')

