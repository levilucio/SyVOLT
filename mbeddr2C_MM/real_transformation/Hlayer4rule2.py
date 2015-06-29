

from core.himesis import Himesis

class Hlayer4rule2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer4rule2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule2, self).__init__(name='Hlayer4rule2', num_nodes=36, edges=[])
        
        # Add the edges
        self.add_edges([[0, 15], [15, 14], [0, 16], [16, 3], [1, 28], [28, 17], [1, 29], [29, 4], [1, 30], [30, 5], [1, 31], [31, 6], [14, 7], [7, 3], [17, 22], [22, 4], [4, 23], [23, 5], [4, 24], [24, 6], [17, 8], [8, 14], [14, 18], [18, 25], [3, 19], [19, 26], [4, 9], [9, 27], [10, 11], [11, 27], [10, 12], [21, 34], [34, 13], [21, 35], [35, 26], [20, 32], [32, 25], [20, 33], [33, 21], [12, 20], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer4rule2"""
        self["GUID__"] = 198730979079575755
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 19386418164737106
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 3249096190590936580
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 6885191321276432342
        self.vs[3]["name"] = """layer4rule2class1"""
        self.vs[3]["classtype"] = """TestCase"""
        self.vs[3]["mm__"] = """TestCase"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4706268672668916700
        self.vs[4]["name"] = """layer4rule2class3"""
        self.vs[4]["classtype"] = """Function"""
        self.vs[4]["mm__"] = """Function"""
        self.vs[4]["cardinality"] = """1"""
        self.vs[4]["GUID__"] = 3317105054865609890
        self.vs[5]["name"] = """layer4rule2class4"""
        self.vs[5]["classtype"] = """VoidType"""
        self.vs[5]["mm__"] = """VoidType"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 3684838187513647098
        self.vs[6]["name"] = """layer4rule2class5"""
        self.vs[6]["classtype"] = """StatementList"""
        self.vs[6]["mm__"] = """StatementList"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 1114265513377399037
        self.vs[7]["associationType"] = """contents"""
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = 8093474108074597776
        self.vs[8]["mm__"] = """backward_link"""
        self.vs[8]["type"] = """ruleDef"""
        self.vs[8]["GUID__"] = 4636623350140959775
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 602599557998628086
        self.vs[10]["name"] = """eq_"""
        self.vs[10]["mm__"] = """Equation"""
        self.vs[10]["GUID__"] = 5920964122368675317
        self.vs[11]["mm__"] = """leftExpr"""
        self.vs[11]["GUID__"] = 4866904122860331274
        self.vs[12]["mm__"] = """rightExpr"""
        self.vs[12]["GUID__"] = 829832256075424307
        self.vs[13]["name"] = """_"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["mm__"] = """Constant"""
        self.vs[13]["GUID__"] = 9147691479212860383
        self.vs[14]["name"] = """layer4rule2class0"""
        self.vs[14]["classtype"] = """ImplementationModule"""
        self.vs[14]["mm__"] = """ImplementationModule"""
        self.vs[14]["cardinality"] = """+"""
        self.vs[14]["GUID__"] = 4347489372748796583
        self.vs[15]["mm__"] = """match_contains"""
        self.vs[15]["GUID__"] = 5540593405740686634
        self.vs[16]["mm__"] = """match_contains"""
        self.vs[16]["GUID__"] = 1921301452509021129
        self.vs[17]["name"] = """layer4rule2class2"""
        self.vs[17]["classtype"] = """ImplementationModule"""
        self.vs[17]["mm__"] = """ImplementationModule"""
        self.vs[17]["cardinality"] = """1"""
        self.vs[17]["GUID__"] = 7072793579505573793
        self.vs[18]["mm__"] = """hasAttribute_S"""
        self.vs[18]["GUID__"] = 290650960373940552
        self.vs[19]["mm__"] = """hasAttribute_S"""
        self.vs[19]["GUID__"] = 1095744968468209172
        self.vs[20]["name"] = """Concatlayer4rule2class3attribute029"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Concat"""
        self.vs[20]["GUID__"] = 8312824583314495154
        self.vs[21]["name"] = """Concatlayer4rule2class3attribute032"""
        self.vs[21]["Type"] = """'String'"""
        self.vs[21]["mm__"] = """Concat"""
        self.vs[21]["GUID__"] = 9062469116663340065
        self.vs[22]["associationType"] = """contents"""
        self.vs[22]["mm__"] = """directLink_T"""
        self.vs[22]["GUID__"] = 3700332857859829907
        self.vs[23]["associationType"] = """type"""
        self.vs[23]["mm__"] = """directLink_T"""
        self.vs[23]["GUID__"] = 9220431187133756405
        self.vs[24]["associationType"] = """body"""
        self.vs[24]["mm__"] = """directLink_T"""
        self.vs[24]["GUID__"] = 5894890208510734250
        self.vs[25]["name"] = """name"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["GUID__"] = 4945584151114515054
        self.vs[26]["name"] = """name"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = 4359313495745559007
        self.vs[27]["name"] = """name"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Attribute"""
        self.vs[27]["GUID__"] = 6661060068241580979
        self.vs[28]["mm__"] = """apply_contains"""
        self.vs[28]["GUID__"] = 5319981296882898515
        self.vs[29]["mm__"] = """apply_contains"""
        self.vs[29]["GUID__"] = 6868060744173284125
        self.vs[30]["mm__"] = """apply_contains"""
        self.vs[30]["GUID__"] = 5828419405532065709
        self.vs[31]["mm__"] = """apply_contains"""
        self.vs[31]["GUID__"] = 4884374855072157011
        self.vs[32]["mm__"] = """hasArgs"""
        self.vs[32]["GUID__"] = 4029970864770720768
        self.vs[33]["mm__"] = """hasArgs"""
        self.vs[33]["GUID__"] = 7264780234815387182
        self.vs[34]["mm__"] = """hasArgs"""
        self.vs[34]["GUID__"] = 8056841654637055949
        self.vs[35]["mm__"] = """hasArgs"""
        self.vs[35]["GUID__"] = 768977864390049094

