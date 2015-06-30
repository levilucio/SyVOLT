

from core.himesis import Himesis

class HEClass_Copy(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEClass_Copy.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEClass_Copy, self).__init__(name='HEClass_Copy', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([[0, 3], [3, 6], [1, 4], [4, 7], [6, 8], [8, 37], [6, 9], [9, 38], [6, 10], [10, 39], [6, 11], [11, 40], [6, 12], [12, 41], [7, 13], [13, 42], [14, 15], [15, 42], [14, 16], [16, 37], [7, 17], [17, 43], [18, 19], [19, 43], [18, 20], [20, 38], [7, 21], [21, 44], [22, 23], [23, 44], [22, 24], [24, 39], [7, 25], [25, 45], [26, 27], [27, 45], [26, 28], [28, 40], [7, 29], [29, 46], [30, 31], [31, 46], [30, 32], [32, 41], [7, 33], [33, 47], [34, 35], [35, 47], [34, 36], [36, 5], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """EClass_Copy"""
        self["GUID__"] = 2715072377568590185
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5327814319267194359
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2070637516319446111
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 5857524026069646317
        self.vs[3]["mm__"] = """match_contains"""
        self.vs[3]["GUID__"] = 974435305006421843
        self.vs[4]["mm__"] = """apply_contains"""
        self.vs[4]["GUID__"] = 8171407524798820343
        self.vs[5]["name"] = """solveRef"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Type"] = """'String'"""
        self.vs[5]["GUID__"] = 5102194526507375479
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """EClass"""
        self.vs[6]["mm__"] = """EClass"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 5474742946891799389
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """EClass"""
        self.vs[7]["mm__"] = """EClass"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 3921902937370184129
        self.vs[8]["mm__"] = """hasAttribute_S"""
        self.vs[8]["GUID__"] = 8124714632685028758
        self.vs[9]["mm__"] = """hasAttribute_S"""
        self.vs[9]["GUID__"] = 7193206616672473102
        self.vs[10]["mm__"] = """hasAttribute_S"""
        self.vs[10]["GUID__"] = 4034493108132359899
        self.vs[11]["mm__"] = """hasAttribute_S"""
        self.vs[11]["GUID__"] = 3000071399092577681
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 8321176195089554785
        self.vs[13]["mm__"] = """hasAttribute_T"""
        self.vs[13]["GUID__"] = 2884503289384741749
        self.vs[14]["name"] = """eq_"""
        self.vs[14]["mm__"] = """Equation"""
        self.vs[14]["GUID__"] = 7640968134017524035
        self.vs[15]["mm__"] = """leftExpr"""
        self.vs[15]["GUID__"] = 5761268900010165423
        self.vs[16]["mm__"] = """rightExpr"""
        self.vs[16]["GUID__"] = 4899411837257535198
        self.vs[17]["mm__"] = """hasAttribute_T"""
        self.vs[17]["GUID__"] = 333506335933976939
        self.vs[18]["name"] = """eq_"""
        self.vs[18]["mm__"] = """Equation"""
        self.vs[18]["GUID__"] = 8274910277604621633
        self.vs[19]["mm__"] = """leftExpr"""
        self.vs[19]["GUID__"] = 702124374654398481
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 8862080798562733297
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 442924605266138773
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 8312541115985810368
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 3096386338828190725
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 3252310092941037304
        self.vs[25]["mm__"] = """hasAttribute_T"""
        self.vs[25]["GUID__"] = 5192918988801075228
        self.vs[26]["name"] = """eq_"""
        self.vs[26]["mm__"] = """Equation"""
        self.vs[26]["GUID__"] = 6596528990791338581
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 7919531433784025661
        self.vs[28]["mm__"] = """rightExpr"""
        self.vs[28]["GUID__"] = 3652775308162357255
        self.vs[29]["mm__"] = """hasAttribute_T"""
        self.vs[29]["GUID__"] = 2469379221974035338
        self.vs[30]["name"] = """eq_"""
        self.vs[30]["mm__"] = """Equation"""
        self.vs[30]["GUID__"] = 6266012022170793579
        self.vs[31]["mm__"] = """leftExpr"""
        self.vs[31]["GUID__"] = 7472819675457523462
        self.vs[32]["mm__"] = """rightExpr"""
        self.vs[32]["GUID__"] = 71344449243340450
        self.vs[33]["mm__"] = """hasAttribute_T"""
        self.vs[33]["GUID__"] = 3676323838989821207
        self.vs[34]["name"] = """eq_"""
        self.vs[34]["mm__"] = """Equation"""
        self.vs[34]["GUID__"] = 377240367032333907
        self.vs[35]["mm__"] = """leftExpr"""
        self.vs[35]["GUID__"] = 5605900689509448612
        self.vs[36]["mm__"] = """rightExpr"""
        self.vs[36]["GUID__"] = 4696235209156110593
        self.vs[37]["name"] = """name"""
        self.vs[37]["mm__"] = """Attribute"""
        self.vs[37]["Type"] = """'String'"""
        self.vs[37]["GUID__"] = 6612524532967001787
        self.vs[38]["name"] = """instanceClassName"""
        self.vs[38]["mm__"] = """Attribute"""
        self.vs[38]["Type"] = """'String'"""
        self.vs[38]["GUID__"] = 6088922433115202171
        self.vs[39]["name"] = """instanceTypeName"""
        self.vs[39]["mm__"] = """Attribute"""
        self.vs[39]["Type"] = """'String'"""
        self.vs[39]["GUID__"] = 2809878293921024445
        self.vs[40]["name"] = """abstract"""
        self.vs[40]["mm__"] = """Attribute"""
        self.vs[40]["Type"] = """'String'"""
        self.vs[40]["GUID__"] = 2383952144371312194
        self.vs[41]["name"] = """interface"""
        self.vs[41]["mm__"] = """Attribute"""
        self.vs[41]["Type"] = """'String'"""
        self.vs[41]["GUID__"] = 827890523350434617
        self.vs[42]["name"] = """name"""
        self.vs[42]["mm__"] = """Attribute"""
        self.vs[42]["Type"] = """'String'"""
        self.vs[42]["GUID__"] = 6695211539908034989
        self.vs[43]["name"] = """instanceClassName"""
        self.vs[43]["mm__"] = """Attribute"""
        self.vs[43]["Type"] = """'String'"""
        self.vs[43]["GUID__"] = 5766441553637667654
        self.vs[44]["name"] = """instanceTypeName"""
        self.vs[44]["mm__"] = """Attribute"""
        self.vs[44]["Type"] = """'String'"""
        self.vs[44]["GUID__"] = 2631648284645663935
        self.vs[45]["name"] = """abstract"""
        self.vs[45]["mm__"] = """Attribute"""
        self.vs[45]["Type"] = """'String'"""
        self.vs[45]["GUID__"] = 6111423040766287194
        self.vs[46]["name"] = """interface"""
        self.vs[46]["mm__"] = """Attribute"""
        self.vs[46]["Type"] = """'String'"""
        self.vs[46]["GUID__"] = 1477595216414802
        self.vs[47]["name"] = """ApplyAttribute"""
        self.vs[47]["mm__"] = """Attribute"""
        self.vs[47]["Type"] = """'String'"""
        self.vs[47]["GUID__"] = 4381099568667487930

