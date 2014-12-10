

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HExample_model(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExample_model.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExample_model, self).__init__(name='HExample_model', num_nodes=8, edges=[])
        
        # Add the edges
        self.add_edges([(1, 6), (6, 2), (4, 7), (7, 0), (5, 0), (2, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """example_model"""
        self["GUID__"] = UUID('e9c19091-08a9-4340-b314-29411f06a394')
        
        # Set the node attributes
        self.vs[0]["name"] = """s_"""
        self.vs[0]["classtype"] = """1"""
        self.vs[0]["mm__"] = """Male_S"""
        self.vs[0]["cardinality"] = """s_"""
        self.vs[0]["GUID__"] = UUID('479e4dc3-85cf-4876-817f-624128caf201')
        self.vs[1]["name"] = """s_"""
        self.vs[1]["classtype"] = """t_"""
        self.vs[1]["mm__"] = """Station_T"""
        self.vs[1]["GUID__"] = UUID('665717af-fef8-4c40-a106-8e353ddad551')
        self.vs[2]["name"] = """s_"""
        self.vs[2]["classtype"] = """1"""
        self.vs[2]["mm__"] = """Station_S"""
        self.vs[2]["cardinality"] = """s_"""
        self.vs[2]["GUID__"] = UUID('4a68a359-fcb8-4618-a805-c4f767447ade')
        self.vs[3]["name"] = """s_"""
        self.vs[3]["classtype"] = """1"""
        self.vs[3]["mm__"] = """Female_S"""
        self.vs[3]["cardinality"] = """s_"""
        self.vs[3]["GUID__"] = UUID('0d7432cd-bd78-4e8d-aa12-61948ce0ee15')
        self.vs[4]["name"] = """s_"""
        self.vs[4]["classtype"] = """t_"""
        self.vs[4]["mm__"] = """Male_T"""
        self.vs[4]["GUID__"] = UUID('09b60957-c440-4df4-b8e2-09349a252d81')
        self.vs[5]["associationType"] = """t_"""
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = UUID('91895446-c16e-4530-a940-87af5188a4cf')
        self.vs[6]["mm__"] = """backward_link"""
        self.vs[6]["GUID__"] = UUID('5f47bb76-a271-49c9-8a68-d407eaf0ffa3')
        self.vs[7]["mm__"] = """backward_link"""
        self.vs[7]["GUID__"] = UUID('e9d32fca-f740-44ec-8eec-f917de1f6633')

