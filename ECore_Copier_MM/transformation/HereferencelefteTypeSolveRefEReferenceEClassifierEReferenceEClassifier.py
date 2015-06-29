

from core.himesis import Himesis

class HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier, self).__init__(name='HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier"""
        self["GUID__"] = 8388354868321727385
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 4315431827204934593
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 5026486399361471097
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8685365752270342664
        self.vs[3]["associationType"] = """eType"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5246899585925216901
        self.vs[4]["associationType"] = """eType"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3358827495053816494
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1725714861469303290
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4150534864595693760
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClassifier"""
        self.vs[7]["mm__"] = """EClassifier"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 1051673698251842261
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 593385027574381439
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 7658881861131814006
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 7607197329358787645
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EClassifier"""
        self.vs[11]["mm__"] = """EClassifier"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 3743879246502372451
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 1868470406873287971
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 1795326848453104661
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 2198797314964058149
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 8823035535294854034
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 2713237288631924314
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 2639140290888557574
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 6307938896322078256
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 3001984895254458476
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 5610355998032210743
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 1946847198550333075
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 8994804203094622190
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3596271218406592702
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 2403908328850657322
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7645311829399308125
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 6067335351160745107

