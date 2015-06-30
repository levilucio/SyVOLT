

from core.himesis import Himesis

class HermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType, self).__init__(name='HermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType"""
        self["GUID__"] = 1991836424006426669
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 9121061616443645593
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2972682726713347653
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 9190584009775141581
        self.vs[3]["associationType"] = """entities"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 4434396024254041021
        self.vs[4]["associationType"] = """entities"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 387360420461980985
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ERModel"""
        self.vs[5]["mm__"] = """ERModel"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 2054852957009375038
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 225639720357013166
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EntityType"""
        self.vs[7]["mm__"] = """EntityType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 173213547489842326
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 506491327113408309
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """ERModel"""
        self.vs[9]["mm__"] = """ERModel"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 8048539632479317484
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 3763306692563537994
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EntityType"""
        self.vs[11]["mm__"] = """EntityType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 8474576540119115137
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 118429709941025324
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 6448589974746704304
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 7122587554012258876
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 121405169741651887
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 7791086169515764479
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 1056497912090921308
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 1116317438146549856
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 5667165791481401678
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 6269794049915120823
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3748810656320640254
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 6231245939434503442
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 6332943465905808784
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3105285962512299323
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 914091837803350910
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 487063481478742822

