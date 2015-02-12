

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
        self["GUID__"] = UUID('ca24643e-e458-42e4-9856-0246a6bae4d1')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('099b47c1-4397-490e-befc-d1a76831905e')
        self.vs[1]["mm__"] = """leftExpr"""
        self.vs[1]["GUID__"] = UUID('67f0f790-8d38-4b9a-82d7-db14f0287cd3')
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = UUID('8011f6d6-de53-45c1-8b3f-dcb843d31118')
        self.vs[3]["mm__"] = """hasAttribute_S"""
        self.vs[3]["GUID__"] = UUID('cb7b48c2-69c9-410d-85f9-346868d28f50')
        self.vs[4]["mm__"] = """ApplyModel"""
        self.vs[4]["GUID__"] = UUID('43202232-75b2-45ab-883d-e9fc0a93eefb')
        self.vs[5]["mm__"] = """Equation"""
        self.vs[5]["GUID__"] = UUID('9ef058ad-729d-46f2-a64c-8a778bc8137c')
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = UUID('aca44d3c-8f72-4dbd-be7e-d9dfab37576b')
        self.vs[7]["name"] = """s_"""
        self.vs[7]["classtype"] = """t_"""
        self.vs[7]["mm__"] = """Male_T"""
        self.vs[7]["GUID__"] = UUID('86512c60-3b61-4f1b-ac81-248b82d4415f')
        self.vs[8]["name"] = """somemale"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["GUID__"] = UUID('7eed3de6-e3da-4488-adce-c1bd0fafc57f')
        self.vs[9]["mm__"] = """rightExpr"""
        self.vs[9]["GUID__"] = UUID('16f023d2-c317-4279-af01-10536a0c8b61')
        self.vs[10]["mm__"] = """MatchModel"""
        self.vs[10]["GUID__"] = UUID('965f9cd8-f62c-43d4-85b9-785243039284')
        self.vs[11]["name"] = """name"""
        self.vs[11]["mm__"] = """Attribute"""
        self.vs[11]["GUID__"] = UUID('b5b0c4e8-3bd0-4303-9b92-ad62abd03140')
        self.vs[12]["name"] = """s_"""
        self.vs[12]["classtype"] = """1"""
        self.vs[12]["mm__"] = """Male_S"""
        self.vs[12]["cardinality"] = """s_"""
        self.vs[12]["GUID__"] = UUID('3613d8cd-bc61-4989-b6b9-fd1a0f87fd87')

