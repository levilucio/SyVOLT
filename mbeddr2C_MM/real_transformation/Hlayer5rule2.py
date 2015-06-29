

from core.himesis import Himesis

class Hlayer5rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer5rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer5rule2, self).__init__(name='Hlayer5rule2', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 17], [17, 5], [1, 18], [18, 6], [1, 19], [19, 7], [1, 20], [20, 8], [3, 9], [9, 4], [5, 14], [14, 7], [7, 15], [15, 8], [8, 16], [16, 6], [5, 12], [12, 3], [6, 13], [13, 4], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer5rule2"""
        self["GUID__"] = 2113155702694132287
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4744454053314561271
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2749424729347042536
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5557579439377465840
        self.vs[3]["name"] = """layer5rule2class0"""
        self.vs[3]["classtype"] = """InstanceConfiguration"""
        self.vs[3]["mm__"] = """InstanceConfiguration"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 9145507115859204508
        self.vs[4]["name"] = """layer5rule2class1"""
        self.vs[4]["classtype"] = """ComponentInstance"""
        self.vs[4]["mm__"] = """ComponentInstance"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4119299872654686795
        self.vs[5]["name"] = """layer5rule2class2"""
        self.vs[5]["classtype"] = """StatementList"""
        self.vs[5]["mm__"] = """StatementList"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5497314343734903939
        self.vs[6]["name"] = """layer5rule2class3"""
        self.vs[6]["classtype"] = """FunctionPrototype"""
        self.vs[6]["mm__"] = """FunctionPrototype"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 4039157419151244346
        self.vs[7]["name"] = """layer5rule2class4"""
        self.vs[7]["classtype"] = """ExpressionStatement"""
        self.vs[7]["mm__"] = """ExpressionStatement"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 4531684624366496070
        self.vs[8]["name"] = """layer5rule2class5"""
        self.vs[8]["classtype"] = """FunctionCall"""
        self.vs[8]["mm__"] = """FunctionCall"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 5370270807863900637
        self.vs[9]["associationType"] = """contents"""
        self.vs[9]["mm__"] = """directLink_S"""
        self.vs[9]["GUID__"] = 4833335131602466516
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 7439912846033980042
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 4300419083112571523
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = 2251451306357905006
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 8595240904373005212
        self.vs[14]["associationType"] = """statements"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = 5710736237852540798
        self.vs[15]["associationType"] = """expr"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = 4297842251989930908
        self.vs[16]["associationType"] = """function"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 2384784618709460087
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 4670404447877262802
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 2297595049584875913
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 2877127992762052413
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 4107882124100567444

