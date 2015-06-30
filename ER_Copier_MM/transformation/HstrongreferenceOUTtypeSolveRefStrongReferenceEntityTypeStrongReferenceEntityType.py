

from core.himesis import Himesis

class HstrongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HstrongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HstrongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType, self).__init__(name='HstrongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType', num_nodes=27, edges=[])
        
        # Add the edges
        self.add_edges([[0, 6], [6, 5], [0, 8], [8, 7], [1, 10], [10, 9], [1, 12], [12, 11], [5, 3], [3, 7], [9, 4], [4, 11], [9, 13], [13, 5], [11, 14], [14, 7], [9, 15], [15, 16], [17, 18], [18, 16], [17, 19], [19, 20], [11, 21], [21, 22], [23, 24], [24, 22], [23, 25], [25, 26], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """strongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType"""
        self["GUID__"] = 2156072848312600704
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 216788228956971873
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 8603545377374615816
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4170304251365617583
        self.vs[3]["associationType"] = """type"""
        self.vs[3]["mm__"] = """directLink_S"""
        self.vs[3]["GUID__"] = 5212052876877625892
        self.vs[4]["associationType"] = """type"""
        self.vs[4]["mm__"] = """directLink_T"""
        self.vs[4]["GUID__"] = 3484258345446711486
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """StrongReference"""
        self.vs[5]["mm__"] = """StrongReference"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 7089155900368380249
        self.vs[6]["mm__"] = """match_contains"""
        self.vs[6]["GUID__"] = 6904012166523919533
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EntityType"""
        self.vs[7]["mm__"] = """EntityType"""
        self.vs[7]["cardinality"] = """+"""
        self.vs[7]["GUID__"] = 2211024366594620586
        self.vs[8]["mm__"] = """match_contains"""
        self.vs[8]["GUID__"] = 3666826788776086812
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """StrongReference"""
        self.vs[9]["mm__"] = """StrongReference"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2646884695933293549
        self.vs[10]["mm__"] = """apply_contains"""
        self.vs[10]["GUID__"] = 1265723398759900028
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """EntityType"""
        self.vs[11]["mm__"] = """EntityType"""
        self.vs[11]["cardinality"] = """1"""
        self.vs[11]["GUID__"] = 2684669373592136115
        self.vs[12]["mm__"] = """apply_contains"""
        self.vs[12]["GUID__"] = 6188467550478779182
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 4161735840896215595
        self.vs[14]["mm__"] = """backward_link"""
        self.vs[14]["type"] = """ruleDef"""
        self.vs[14]["GUID__"] = 4210070091256964459
        self.vs[15]["mm__"] = """hasAttribute_T"""
        self.vs[15]["GUID__"] = 3821848612217110480
        self.vs[16]["name"] = """ApplyAttribute"""
        self.vs[16]["Type"] = """'String'"""
        self.vs[16]["mm__"] = """Attribute"""
        self.vs[16]["GUID__"] = 3468554602334192614
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 1458620341211361972
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 8259608185404971083
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 8056417178411742521
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 1155598866128533011
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 2604576007144458992
        self.vs[22]["name"] = """ApplyAttribute"""
        self.vs[22]["Type"] = """'String'"""
        self.vs[22]["mm__"] = """Attribute"""
        self.vs[22]["GUID__"] = 884458949677739545
        self.vs[23]["name"] = """eq_"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 3130970771640425867
        self.vs[24]["mm__"] = """leftExpr"""
        self.vs[24]["GUID__"] = 8867138172547843414
        self.vs[25]["mm__"] = """rightExpr"""
        self.vs[25]["GUID__"] = 8647935607854252182
        self.vs[26]["name"] = """solveRef"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Constant"""
        self.vs[26]["GUID__"] = 4132133430912085748

