

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HExample_model2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HExample_model2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HExample_model2, self).__init__(name='HExample_model2', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([(1, 4), (4, 2), (3, 5), (5, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """example_model2"""
        self["GUID__"] = UUID('1fdb2463-fec0-4ec2-8387-20869b0af2e7')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """Male_S"""
        self.vs[0]["classtype"] = """1"""
        self.vs[0]["cardinality"] = """s_"""
        self.vs[0]["name"] = """s_"""
        self.vs[0]["GUID__"] = UUID('5eb40092-b0b5-4254-9fd5-fbe182b19ce9')
        self.vs[1]["mm__"] = """Station_T"""
        self.vs[1]["classtype"] = """t_"""
        self.vs[1]["name"] = """s_"""
        self.vs[1]["GUID__"] = UUID('058d1fe7-eb4e-48bd-86e0-e63b7a14d982')
        self.vs[2]["mm__"] = """Station_S"""
        self.vs[2]["classtype"] = """1"""
        self.vs[2]["cardinality"] = """s_"""
        self.vs[2]["name"] = """s_"""
        self.vs[2]["GUID__"] = UUID('3376e0ba-2d7a-400b-b347-342e7215b57f')
        self.vs[3]["mm__"] = """Male_T"""
        self.vs[3]["classtype"] = """t_"""
        self.vs[3]["name"] = """s_"""
        self.vs[3]["GUID__"] = UUID('e63553c6-baa8-4c6a-a237-cec7b0b5543e')
        self.vs[4]["mm__"] = """backward_link"""
        self.vs[4]["GUID__"] = UUID('074cacec-9ddc-4dc2-946a-9b49116c8883')
        self.vs[5]["mm__"] = """backward_link"""
        self.vs[5]["GUID__"] = UUID('8772c71b-1b78-4046-8282-a9142567802c')

