

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HS2S(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HS2S.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HS2S, self).__init__(name='HS2S', num_nodes=13, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (0, 6), (7, 1), (1, 12), (11, 2), (2, 4), (5, 3), (3, 12), (8, 5), (7, 10), (11, 8), (10, 9)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """S2S"""
        self["GUID__"] = UUID('fa1d212b-8b66-414a-add3-7e486b23f5c7')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('d82869f8-cee0-4eb1-b6b9-f958d1c97e55')
        self.vs[1]["mm__"] = """leftExpr"""
        self.vs[1]["GUID__"] = UUID('1adddf34-27c0-4e4a-b14b-584e658a5f35')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('6ca50e51-9441-43fb-ab88-dbc6f13f5982')
        self.vs[3]["mm__"] = """hasAttribute_S"""
        self.vs[3]["GUID__"] = UUID('2628ac14-c717-42e5-a517-51709611aed4')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('e5536838-ff23-46e8-9d43-7345c115f357')
        self.vs[5]["name"] = """s_"""
        self.vs[5]["classtype"] = """1"""
        self.vs[5]["mm__"] = """Station_S"""
        self.vs[5]["cardinality"] = """s_"""
        self.vs[5]["GUID__"] = UUID('fefb6b14-63cb-48d8-82b9-20e325ca6f6b')
        self.vs[6]["name"] = """s_"""
        self.vs[6]["classtype"] = """t_"""
        self.vs[6]["mm__"] = """Station_T"""
        self.vs[6]["GUID__"] = UUID('faff3d34-e023-48d1-ae5d-96cc87d99a93')
        self.vs[7]["mm__"] = """Equation"""
        self.vs[7]["GUID__"] = UUID('739071de-2bbc-427c-989d-f903906871b3')
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = UUID('90a0ecdc-03af-4eb8-86da-2699eb9504b3')
        self.vs[9]["name"] = """somestation"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["GUID__"] = UUID('0197e56c-8c0a-4fcf-a68d-a8f042c82fcb')
        self.vs[10]["mm__"] = """rightExpr"""
        self.vs[10]["GUID__"] = UUID('aead3e35-a195-44a0-94de-7eda181250eb')
        self.vs[11]["mm__"] = """MatchModel"""
        self.vs[11]["GUID__"] = UUID('6d92dd6d-7d67-46dc-8355-b08c224f8a1d')
        self.vs[12]["name"] = """name"""
        self.vs[12]["mm__"] = """Attribute"""
        self.vs[12]["GUID__"] = UUID('e794b05b-48f2-4a11-a8c2-5a4954f093c6')

