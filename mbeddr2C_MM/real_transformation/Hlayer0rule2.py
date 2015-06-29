

from core.himesis import Himesis

class Hlayer0rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer0rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer0rule2, self).__init__(name='Hlayer0rule2', num_nodes=20, edges=[])
        
        # Add the edges
        self.add_edges([[0, 14], [14, 3], [0, 15], [15, 4], [1, 16], [16, 5], [1, 17], [17, 6], [4, 7], [7, 3], [5, 8], [8, 6], [3, 9], [9, 18], [5, 10], [10, 19], [11, 12], [12, 19], [11, 13], [13, 18], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer0rule2"""
        self["GUID__"] = 7998824052048558747
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 7494554117155975158
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 4035857492401530802
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 4360260994451656452
        self.vs[3]["name"] = """layer0rule2class0"""
        self.vs[3]["classtype"] = """Operation"""
        self.vs[3]["mm__"] = """Operation"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 1332719044466526519
        self.vs[4]["name"] = """layer0rule2class1"""
        self.vs[4]["classtype"] = """ClientServerInterface"""
        self.vs[4]["mm__"] = """ClientServerInterface"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 3878457496669103000
        self.vs[5]["name"] = """layer0rule2class2"""
        self.vs[5]["classtype"] = """CFunctionPointerStructMember"""
        self.vs[5]["mm__"] = """CFunctionPointerStructMember"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 9097275559522579509
        self.vs[6]["name"] = """layer0rule2class3"""
        self.vs[6]["classtype"] = """FunctionRefType"""
        self.vs[6]["mm__"] = """FunctionRefType"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 7579864285335767538
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 4764179013616017091
        self.vs[8]["associationType"] = """type"""
        self.vs[8]["mm__"] = """directLink_T"""
        self.vs[8]["GUID__"] = 7657124168606544162
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 8220723227164516443
        self.vs[10]["mm__"] = """hasAttribute_T"""
        self.vs[10]["GUID__"] = 5576314549654769687
        self.vs[11]["name"] = """eq_"""
        self.vs[11]["mm__"] = """Equation"""
        self.vs[11]["GUID__"] = 2527084059105533838
        self.vs[12]["mm__"] = """leftExpr"""
        self.vs[12]["GUID__"] = 3421022542997168895
        self.vs[13]["mm__"] = """rightExpr"""
        self.vs[13]["GUID__"] = 454239012213455629
        self.vs[14]["mm__"] = """match_contains"""
        self.vs[14]["GUID__"] = 7867560488060098998
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 2182449887010454264
        self.vs[16]["mm__"] = """apply_contains"""
        self.vs[16]["GUID__"] = 3095223427275868466
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 3203935587889065283
        self.vs[18]["name"] = """name"""
        self.vs[18]["mm__"] = """Attribute"""
        self.vs[18]["Type"] = """'String'"""
        self.vs[18]["GUID__"] = 1021140744041383833
        self.vs[19]["name"] = """name"""
        self.vs[19]["mm__"] = """Attribute"""
        self.vs[19]["Type"] = """'String'"""
        self.vs[19]["GUID__"] = 783473854610542157

