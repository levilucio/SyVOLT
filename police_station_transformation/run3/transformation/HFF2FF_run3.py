

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HFF2FF_run3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFF2FF_run3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFF2FF_run3, self).__init__(name='HFF2FF_run3', num_nodes=15, edges=[])
        
        # Add the edges
        self.add_edges([(1, 5), (5, 9), (1, 6), (6, 10), (9, 7), (7, 13), (10, 8), (8, 14), (9, 0), (0, 10), (4, 1), (2, 4), (2, 11), (2, 12), (13, 3), (3, 14), (11, 13), (12, 14)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """FF2FF_run3"""
        self["GUID__"] = UUID('b8f28896-9586-495a-a36f-ae4bc359989b')
        
        # Set the node attributes
        self.vs[0]["associationType"] = """t_"""
        self.vs[0]["mm__"] = """directLink_T"""
        self.vs[0]["GUID__"] = UUID('cacc39c4-c865-4c7c-979c-05048e3a629d')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('d80b0843-844c-438e-a1b0-a4bbca031f06')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('c2eb47a9-2c70-459a-a49b-36e3978957f8')
        self.vs[3]["mm__"] = """indirectLink_S"""
        self.vs[3]["GUID__"] = UUID('6a9e4988-2fe6-4ef5-b424-ebcabbce545f')
        self.vs[4]["mm__"] = """paired_with"""
        self.vs[4]["GUID__"] = UUID('42f7a550-3aa7-44ec-9198-3a3c0116e1bc')
        self.vs[5]["mm__"] = """apply_contains"""
        self.vs[5]["GUID__"] = UUID('ebebe7d3-5208-42e1-aa07-faad59c14e56')
        self.vs[6]["mm__"] = """apply_contains"""
        self.vs[6]["GUID__"] = UUID('ae810911-3ef4-4739-b3a3-d144726ecb8b')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('5b86af15-c1ac-4a46-a6af-b9a598c12926')
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["GUID__"] = UUID('2b51505a-4545-458c-900a-244b90c37e74')
        self.vs[9]["name"] = """f1"""
        self.vs[9]["classtype"] = """female3"""
        self.vs[9]["mm__"] = """Female_T"""
        self.vs[9]["GUID__"] = UUID('cfa408b1-ee50-4743-b3af-1c392b6147dd')
        self.vs[10]["name"] = """f2"""
        self.vs[10]["classtype"] = """female3"""
        self.vs[10]["mm__"] = """Female_T"""
        self.vs[10]["GUID__"] = UUID('b971743b-8f73-4fee-9082-9d1ba16c8987')
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = UUID('14d3daf4-057d-4db8-89a2-835ed03c2f93')
        self.vs[12]["mm__"] = """match_contains"""
        self.vs[12]["GUID__"] = UUID('5d43d29d-0772-4898-9c43-c2e6a6faab5d')
        self.vs[13]["name"] = """f1"""
        self.vs[13]["classtype"] = """female3"""
        self.vs[13]["mm__"] = """Female_S"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = UUID('f392ea14-a5af-4e23-936c-1a50b2fbec99')
        self.vs[14]["name"] = """f2"""
        self.vs[14]["classtype"] = """female3"""
        self.vs[14]["mm__"] = """Female_S"""
        self.vs[14]["cardinality"] = """+"""
        self.vs[14]["GUID__"] = UUID('cb277fd7-04fc-405b-8893-9d7027b4ba99')

