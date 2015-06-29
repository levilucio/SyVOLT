

from core.himesis import Himesis

class Hlayer1rule11(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hlayer1rule11.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer1rule11, self).__init__(name='Hlayer1rule11', num_nodes=21, edges=[])
        
        # Add the edges
        self.add_edges([[0, 10], [10, 3], [0, 11], [11, 4], [1, 17], [17, 5], [1, 18], [18, 6], [1, 19], [19, 7], [1, 20], [20, 8], [4, 9], [9, 3], [6, 14], [14, 7], [7, 15], [15, 8], [8, 16], [16, 5], [5, 12], [12, 3], [6, 13], [13, 4], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """layer1rule11"""
        self["GUID__"] = 6446271769502228756
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 2383087138356153593
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 909986318433605956
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 8824925158459629045
        self.vs[3]["name"] = """layer1rule11class0"""
        self.vs[3]["classtype"] = """ClientServerInterface"""
        self.vs[3]["mm__"] = """ClientServerInterface"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 627433440524627589
        self.vs[4]["name"] = """layer1rule11class1"""
        self.vs[4]["classtype"] = """RequiredPort"""
        self.vs[4]["mm__"] = """RequiredPort"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 2222517930569737423
        self.vs[5]["name"] = """layer1rule11class2"""
        self.vs[5]["classtype"] = """TypeDef"""
        self.vs[5]["mm__"] = """TypeDef"""
        self.vs[5]["cardinality"] = """1"""
        self.vs[5]["GUID__"] = 5584521945537438975
        self.vs[6]["name"] = """layer1rule11class3"""
        self.vs[6]["classtype"] = """Member"""
        self.vs[6]["mm__"] = """Member"""
        self.vs[6]["cardinality"] = """1"""
        self.vs[6]["GUID__"] = 3245673813318522973
        self.vs[7]["name"] = """layer1rule11class4"""
        self.vs[7]["classtype"] = """PointerType"""
        self.vs[7]["mm__"] = """PointerType"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 6645784082645385336
        self.vs[8]["name"] = """layer1rule11class5"""
        self.vs[8]["classtype"] = """TypeDefType"""
        self.vs[8]["mm__"] = """TypeDefType"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 6447450585640634293
        self.vs[9]["associationType"] = """intf"""
        self.vs[9]["mm__"] = """directLink_S"""
        self.vs[9]["GUID__"] = 4719343602012171975
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 2998620588873093874
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 4403932952173905252
        self.vs[12]["mm__"] = """backward_link"""
        self.vs[12]["type"] = """ruleDef"""
        self.vs[12]["GUID__"] = 6773286490582299851
        self.vs[13]["mm__"] = """backward_link"""
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["GUID__"] = 305604528802121988
        self.vs[14]["associationType"] = """type"""
        self.vs[14]["mm__"] = """directLink_T"""
        self.vs[14]["GUID__"] = 2210064747841105927
        self.vs[15]["associationType"] = """baseType"""
        self.vs[15]["mm__"] = """directLink_T"""
        self.vs[15]["GUID__"] = 3957816232313400627
        self.vs[16]["associationType"] = """typeDef"""
        self.vs[16]["mm__"] = """directLink_T"""
        self.vs[16]["GUID__"] = 3066777865513538370
        self.vs[17]["mm__"] = """apply_contains"""
        self.vs[17]["GUID__"] = 6256009507961919864
        self.vs[18]["mm__"] = """apply_contains"""
        self.vs[18]["GUID__"] = 6965102191069548258
        self.vs[19]["mm__"] = """apply_contains"""
        self.vs[19]["GUID__"] = 4375460679360003428
        self.vs[20]["mm__"] = """apply_contains"""
        self.vs[20]["GUID__"] = 8367066554526963920

