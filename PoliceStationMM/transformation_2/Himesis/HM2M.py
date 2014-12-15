

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HM2M(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM2M.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM2M, self).__init__(name='HM2M', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 7), (5, 1), (1, 11), (10, 2), (2, 4), (12, 3), (3, 11), (5, 9), (10, 6), (6, 12), (9, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """M2M"""
        self["GUID__"] = UUID('488fe13e-6fdc-459b-89f9-960f35a91db9')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('1307eaa9-46ef-47ce-b9a6-475443ae1156')
        self.vs[1]["mm__"] = """leftExpr"""
        self.vs[1]["GUID__"] = UUID('46b81ca5-57bc-48a9-a61c-f6c4af0a9254')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('76594ba3-6bb9-4d15-aa63-586fd724e8ee')
        self.vs[3]["mm__"] = """hasAttr_S"""
        self.vs[3]["GUID__"] = UUID('b1daa623-a7ca-48d8-ac47-fa6b0ce631cb')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('2a99e217-4977-4c3a-97be-4ced917fccfb')
        self.vs[5]["mm__"] = """Equation"""
        self.vs[5]["GUID__"] = UUID('abd209f8-1cfb-4f3c-a323-8ea876ed3b37')
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = UUID('65de52a0-4e64-4a91-a889-acee82b10f13')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """t_"""
        self.vs[7]["mm__"] = """Male_T"""
        self.vs[7]["GUID__"] = UUID('ad7d29fe-fa59-49bf-99dd-dc27dc54d9cc')
        self.vs[8]["value"] = """somestation"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["GUID__"] = UUID('d8892b62-1144-4ec9-a752-921959b0ef63')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('291e78de-83de-4848-8250-4c484568d063')
        self.vs[10]["mm__"] = """MatchModel"""
        self.vs[10]["GUID__"] = UUID('3f96302a-6828-4955-879b-9160224d05d1')
        self.vs[11]["name"] = """name"""
        self.vs[11]["mm__"] = """Attribute"""
        self.vs[11]["GUID__"] = UUID('c175068b-8802-4a03-ac69-c17178fbd978')
        self.vs[12]["name"] = """s_"""
        self.vs[12]["classtype"] = """1"""
        self.vs[12]["mm__"] = """Male_S"""
        self.vs[12]["cardinality"] = """s_"""
        self.vs[12]["GUID__"] = UUID('7df2b031-7117-46e8-b62d-4e5718cc5922')

