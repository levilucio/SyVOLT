

from core.himesis import Himesis

class HereferencelefteKeysSolveRefEReferenceEAttributeEReferenceEAttribute(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HereferencelefteKeysSolveRefEReferenceEAttributeEReferenceEAttribute.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HereferencelefteKeysSolveRefEReferenceEAttributeEReferenceEAttribute, self).__init__(name='HereferencelefteKeysSolveRefEReferenceEAttributeEReferenceEAttribute', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """ereferencelefteKeysSolveRefEReferenceEAttributeEReferenceEAttribute"""
        self["GUID__"] = 1610401918581494585
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7290202723213402962
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8953952500153800519
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 1745716098265147040
        self.vs[3]["associationType"] = """eKeys"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2904352035897882136
        self.vs[4]["associationType"] = """eKeys"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 1337209911478187474
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EReference"""
        self.vs[5]["mm__"] = """EReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 1985188787676880826
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 5721665388393063575
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAttribute"""
        self.vs[7]["mm__"] = """EAttribute"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 3636244732691836956
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3490226096630323899
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EReference"""
        self.vs[9]["mm__"] = """EReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 3012210182481766512
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 3999656875255371340
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAttribute"""
        self.vs[11]["mm__"] = """EAttribute"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 7586195251368743384
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 5895831786013361896
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 3399022517610121958
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 5325410611170697635
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 2250946392043885196
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 7647605021470081956
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 6848563336108743285
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 883029134286577054
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8709845223847329484
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 6004463022576365293
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3426334626304334646
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 2629784837212259493
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 7318224309665074938
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 6866117516012243145
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7095119573367224665
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 8057146403300436678

