

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HF2F_run4(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HF2F_run4.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HF2F_run4, self).__init__(name='HF2F_run4', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 3), (6, 1), (2, 6), (2, 4), (4, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'PoliceStationMM'
p2
a.""")
        self["name"] = """F2F_run4"""
        self["GUID__"] = UUID('b1adaa34-8447-4ac4-a93e-6d874db5734e')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """apply_contains"""
        self.vs[0]["GUID__"] = UUID('b041381b-c367-4dbc-9d5f-bed6b8fdc11b')
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = UUID('4b41673b-b545-45e9-945e-7a2af3680d26')
        self.vs[2]["mm__"] = """MatchModel"""
        self.vs[2]["GUID__"] = UUID('d76f9d77-68cc-4669-87f0-d42e9ca4a05e')
        self.vs[3]["mm__"] = """Female_T"""
        self.vs[3]["classtype"] = """female4"""
        self.vs[3]["name"] = """f"""
        self.vs[3]["GUID__"] = UUID('b2640011-17a4-4618-b251-130672b5080f')
        self.vs[4]["mm__"] = """match_contains"""
        self.vs[4]["GUID__"] = UUID('f23289f1-92f6-4574-b9b4-ab58acc09488')
        self.vs[5]["mm__"] = """Female_S"""
        self.vs[5]["classtype"] = """female4"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """f"""
        self.vs[5]["GUID__"] = UUID('19cfe6ab-6891-4b11-a26a-d573689a1b93')
        self.vs[6]["mm__"] = """paired_with"""
        self.vs[6]["GUID__"] = UUID('0ad1bb92-038e-46a0-b6ac-ebe2a7f0f7e7')

