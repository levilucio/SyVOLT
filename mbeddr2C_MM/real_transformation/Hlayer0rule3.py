

from core.himesis import Himesis

class Hlayer0rule3(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule3.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule3, self).__init__(name='Hlayer0rule3', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 5], [1, 4], [4, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule3"""
        self["GUID__"] = 3376982168922358405
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2738274392421964779
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 9061671787737637659
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2826873630220895546
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 6820670477679581495
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 4519327719651968463
        self.vs[5]["mm__"] = """StringType"""
        self.vs[5]["classtype"] = """StringType"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["name"] = """layer0rule3class0"""
        self.vs[5]["GUID__"] = 7549063420161515755
        self.vs[6]["mm__"] = """StringType"""
        self.vs[6]["classtype"] = """StringType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["name"] = """layer0rule3class1"""
        self.vs[6]["GUID__"] = 7053750179173031227

