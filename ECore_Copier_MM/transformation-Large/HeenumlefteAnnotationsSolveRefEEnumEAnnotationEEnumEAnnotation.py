

from core.himesis import Himesis

class HeenumlefteAnnotationsSolveRefEEnumEAnnotationEEnumEAnnotation(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HeenumlefteAnnotationsSolveRefEEnumEAnnotationEEnumEAnnotation.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HeenumlefteAnnotationsSolveRefEEnumEAnnotationEEnumEAnnotation, self).__init__(name='HeenumlefteAnnotationsSolveRefEEnumEAnnotationEEnumEAnnotation', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """eenumlefteAnnotationsSolveRefEEnumEAnnotationEEnumEAnnotation"""
        self["GUID__"] = 8788987425808097391
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 3640420995561889919
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 771573141089772354
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6655167031377833847
        self.vs[3]["associationType"] = """eAnnotations"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 2928529216783636284
        self.vs[4]["associationType"] = """eAnnotations"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3608206538963831963
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """EEnum"""
        self.vs[5]["mm__"] = """EEnum"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 465143393671246670
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 4655273607873685023
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EAnnotation"""
        self.vs[7]["mm__"] = """EAnnotation"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 5821445526799249065
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 5137886651335340190
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """EEnum"""
        self.vs[9]["mm__"] = """EEnum"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 3813526525300675943
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 8345617604570598872
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EAnnotation"""
        self.vs[11]["mm__"] = """EAnnotation"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 6005443664246838022
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6280482860996558131
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 5346223879731953350
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 6889150385656325932
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 7171759430044761664
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3190540703124904348
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3590389766655131006
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2697717284668357581
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8135854866417770005
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 1615344990473796893
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 5518049740885737345
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 3364968200735265920
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3024132758616005627
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 3770346266661855318
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 7000876397900255354
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 1275809918140950100

