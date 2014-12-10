

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HFF2FF_run1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_run1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_run1, self).__init__(name='HFF2FF_run1', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 9), (1, 6), (6, 10), (9, 7), (7, 13), (10, 8), (8, 14), (9, 0), (0, 10), (4, 1), (2, 4), (2, 11), (2, 12), (13, 3), (3, 14), (11, 13), (12, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """FF2FF_run1"""
        self["GUID__"] = UUID('760af717-9b9e-4b21-bd88-a2c6005f1c0d')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """f2f"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('c1d63bf1-7c9a-4c46-9455-1a5247b0fe7f')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('38fc2676-41ef-4824-936e-5be1accbdb58')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('e29b0d01-a473-468e-8ad6-d4a49a68f4f3')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('16b2cd2a-0530-4e54-8c8e-d23207890a04')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('cfe61358-562b-4d0c-a67d-0141fe1f4697')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('88f889a2-05c1-42e0-8d83-ed0fd8990132')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('fcd36a82-ddc4-483c-8d4c-8003b125eb6a')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('dc880e03-28eb-435e-8209-bcdf75d113b1')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('64efb0fe-6a92-44ef-845b-38b0d92ccc89')
        self.vs[9]["name"] = """7.f1"""
        self.vs[9]["classtype"] = """female1"""
        self.vs[9]["mm__"] = """Female_T"""
        self.vs[9]["GUID__"] = UUID('5bf2bd4c-25d4-4a52-b119-cd2cace01618')
        self.vs[10]["name"] = """7.f2"""
        self.vs[10]["classtype"] = """female1"""
        self.vs[10]["mm__"] = """Female_T"""
        self.vs[10]["GUID__"] = UUID('12df362b-2368-479b-a653-6a431dbe1d91')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('8e25a830-7b84-40f6-8928-77725b0d84ec')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('e735c7e5-92e1-4007-80f2-21de87f62bad')
        self.vs[13]["name"] = """7.f1"""
        self.vs[13]["classtype"] = """female1"""
        self.vs[13]["mm__"] = """Female_S"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('645c435e-ce2f-415b-b7a5-b67705a0a6e0')
        self.vs[14]["name"] = """7.f2"""
        self.vs[14]["classtype"] = """female1"""
        self.vs[14]["mm__"] = """Female_S"""
        self.vs[14]["cardinality"] = """+"""
        self.vs[14]["GUID__"] = UUID('a227ef0d-ba57-4638-8121-faabd9c9e029')

