

from core.himesis import Himesis

class HMapHeirarchyOfStates2HeirarchyOfProcs(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMapHeirarchyOfStates2HeirarchyOfProcs.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HMapHeirarchyOfStates2HeirarchyOfProcs, self).__init__(name='HMapHeirarchyOfStates2HeirarchyOfProcs', num_nodes=33, edges=[])
        
        # Add the edges
        self.add_edges([[12, 0], [0, 13], [3, 1], [1, 7], [21, 18], [18, 30], [22, 19], [19, 31], [23, 20], [20, 32], [3, 8], [8, 25], [7, 9], [9, 26], [5, 2], [2, 14], [2, 15], [14, 3], [3, 16], [6, 10], [10, 12], [6, 11], [11, 13], [12, 4], [4, 24], [16, 12], [17, 13], [6, 5], [21, 27], [22, 28], [23, 29], [15, 7], [7, 17], [27, 24], [28, 25], [29, 26]])
        # Set the graph attributes
        self["mm__"] = ['UMLRT2Kiltera_MM']
        self["name"] = """MapHeirarchyOfStates2HeirarchyOfProcs"""
        self["GUID__"] = 5416545687951613537
        
        # Set the node attributes
        self.vs[0]["associationType"] = """states"""
        self.vs[0]["mm__"] = """directLink_S"""
        self.vs[0]["GUID__"] = 5483566163924865856
        self.vs[1]["associationType"] = """def"""
        self.vs[1]["mm__"] = """directLink_T"""
        self.vs[1]["GUID__"] = 8545717591904813909
        self.vs[2]["mm__"] = """ApplyModel"""
        self.vs[2]["GUID__"] = 529914756162826721
        self.vs[3]["name"] = """localDef1"""
        self.vs[3]["classtype"] = """LocalDef"""
        self.vs[3]["mm__"] = """LocalDef"""
        self.vs[3]["cardinality"] = """1"""
        self.vs[3]["GUID__"] = 3557002846557320221
        self.vs[4]["mm__"] = """hasAttribute_S"""
        self.vs[4]["GUID__"] = 9185749292460276803
        self.vs[5]["mm__"] = """paired_with"""
        self.vs[5]["GUID__"] = 4771099051806587059
        self.vs[6]["mm__"] = """MatchModel"""
        self.vs[6]["GUID__"] = 2506288651542669277
        self.vs[7]["name"] = """procDef1"""
        self.vs[7]["classtype"] = """ProcDef"""
        self.vs[7]["mm__"] = """ProcDef"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1893214579207665547
        self.vs[8]["mm__"] = """hasAttribute_T"""
        self.vs[8]["GUID__"] = 170417659263179755
        self.vs[9]["mm__"] = """hasAttribute_T"""
        self.vs[9]["GUID__"] = 453484419190516263
        self.vs[10]["mm__"] = """match_contains"""
        self.vs[10]["GUID__"] = 5984069521712190661
        self.vs[11]["mm__"] = """match_contains"""
        self.vs[11]["GUID__"] = 5176132816562651016
        self.vs[12]["name"] = """state1"""
        self.vs[12]["classtype"] = """State"""
        self.vs[12]["mm__"] = """State"""
        self.vs[12]["cardinality"] = """+"""
        self.vs[12]["GUID__"] = 4479815499956768999
        self.vs[13]["name"] = """state2"""
        self.vs[13]["classtype"] = """State"""
        self.vs[13]["mm__"] = """State"""
        self.vs[13]["cardinality"] = """+"""
        self.vs[13]["GUID__"] = 269376023764123904
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 2577250574431284978
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 9152885534165922710
        self.vs[16]["mm__"] = """backward_link"""
        self.vs[16]["type"] = """ruleDef"""
        self.vs[16]["GUID__"] = 3484097463472971311
        self.vs[17]["mm__"] = """backward_link"""
        self.vs[17]["type"] = """ruleDef"""
        self.vs[17]["GUID__"] = 4916019268555635280
        self.vs[18]["mm__"] = """rightExpr"""
        self.vs[18]["GUID__"] = 8693618482046457550
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 1242299020525932118
        self.vs[20]["mm__"] = """rightExpr"""
        self.vs[20]["GUID__"] = 2550244229116469818
        self.vs[21]["name"] = """eq1"""
        self.vs[21]["mm__"] = """Equation"""
        self.vs[21]["GUID__"] = 4192198646386358172
        self.vs[22]["name"] = """eq2"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 2794230553850329955
        self.vs[23]["name"] = """eq3"""
        self.vs[23]["mm__"] = """Equation"""
        self.vs[23]["GUID__"] = 4803160228692826892
        self.vs[24]["name"] = """isComposite"""
        self.vs[24]["Type"] = """'Bool'"""
        self.vs[24]["mm__"] = """Attribute"""
        self.vs[24]["GUID__"] = 1395576476172480674
        self.vs[25]["name"] = """pivot"""
        self.vs[25]["Type"] = """'String'"""
        self.vs[25]["mm__"] = """Attribute"""
        self.vs[25]["GUID__"] = 1408162411022791864
        self.vs[26]["name"] = """pivot"""
        self.vs[26]["Type"] = """'String'"""
        self.vs[26]["mm__"] = """Attribute"""
        self.vs[26]["GUID__"] = 2541952595983329473
        self.vs[27]["mm__"] = """leftExpr"""
        self.vs[27]["GUID__"] = 2138326963493789917
        self.vs[28]["mm__"] = """leftExpr"""
        self.vs[28]["GUID__"] = 8757412254348853079
        self.vs[29]["mm__"] = """leftExpr"""
        self.vs[29]["GUID__"] = 2826502017608889656
        self.vs[30]["name"] = """true"""
        self.vs[30]["Type"] = """'Bool'"""
        self.vs[30]["mm__"] = """Constant"""
        self.vs[30]["GUID__"] = 470173319355056899
        self.vs[31]["name"] = """localdefcompstate"""
        self.vs[31]["Type"] = """'String'"""
        self.vs[31]["mm__"] = """Constant"""
        self.vs[31]["GUID__"] = 2304997843816112847
        self.vs[32]["name"] = """procdef"""
        self.vs[32]["Type"] = """'String'"""
        self.vs[32]["mm__"] = """Constant"""
        self.vs[32]["GUID__"] = 5687618000152590131

