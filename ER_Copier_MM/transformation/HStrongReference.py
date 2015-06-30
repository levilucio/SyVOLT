

from core.himesis import Himesis

class HStrongReference(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HStrongReference.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HStrongReference, self).__init__(name='HStrongReference', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 7], [1, 4], [4, 8], [7, 5], [5, 17], [8, 9], [9, 18], [10, 11], [11, 18], [10, 12], [12, 17], [8, 13], [13, 19], [14, 15], [15, 19], [14, 16], [16, 6], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """StrongReference"""
        self["GUID__"] = 7607505855784937967
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5779182832684694727
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4439173739649219989
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 318214662816307773
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 7266391706852440631
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 3118127023479334668
        self.vs[5]["mm__"] = """hasAttribute_S"""
        self.vs[5]["GUID__"] = 5006354795003185966
        self.vs[6]["name"] = """solveRef"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Type"] = """'String'"""
        self.vs[6]["GUID__"] = 4300650762447879728
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """StrongReference"""
        self.vs[7]["mm__"] = """StrongReference"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2091721814895722432
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """StrongReference"""
        self.vs[8]["mm__"] = """StrongReference"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 8572740810756804112
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 8100571557044138732
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 3901028009018375833
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 4422744497776058125
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 8600975732530936185
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 3024146977829022094
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 4086686441975403575
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 1309883089728549566
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 5599472733327381857
        self.vs[17]["name"] = """name"""
        self.vs[17]["mm__"] = """Attribute"""
        self.vs[17]["Type"] = """'String'"""
        self.vs[17]["GUID__"] = 1165287500042232225
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 1906527204588346210
        self.vs[19]["name"] = """ApplyAttribute"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 4150362521604040097

