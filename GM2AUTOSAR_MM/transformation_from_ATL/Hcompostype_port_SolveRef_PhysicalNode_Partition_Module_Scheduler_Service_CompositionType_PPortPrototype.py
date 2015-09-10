

from core.himesis import Himesis

class Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype, self).__init__(name='Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype', num_nodes=40, edges=[])
        
        # Add the edges
        self.add_edges([[0, 35], [35, 3], [0, 36], [36, 4], [0, 37], [37, 5], [0, 38], [38, 6], [0, 39], [39, 7], [1, 14], [14, 8], [1, 15], [15, 9], [3, 31], [31, 4], [4, 32], [32, 5], [5, 33], [33, 6], [6, 34], [34, 7], [8, 10], [10, 9], [8, 11], [11, 3], [6, 12], [12, 28], [8, 16], [16, 29], [17, 18], [18, 29], [17, 19], [19, 20], [9, 21], [21, 30], [22, 23], [23, 30], [22, 24], [13, 25], [25, 28], [13, 26], [26, 27], [24, 13], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_PPortPrototype"""
        self["GUID__"] = 8493701695731458962
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5009786563446005454
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2518674482087352307
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 7098411700267954992
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 693847336776460024
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 982652165032256159
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Module"""
        self.vs[5]["mm__"] = """Module"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 7143989269016792613
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """Scheduler"""
        self.vs[6]["mm__"] = """Scheduler"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 5389932794564821905
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Service"""
        self.vs[7]["mm__"] = """Service"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 1978897333579052228
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """CompositionType"""
        self.vs[8]["mm__"] = """CompositionType"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 3181940558231624232
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """PPortPrototype"""
        self.vs[9]["mm__"] = """PPortPrototype"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 9159030790329523439
        self.vs[10]["associationType"] = """port"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 3184385748932349750
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 6074350542361725753
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 7993527965323902336
        self.vs[13]["name"] = """Concat36"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["mm__"] = """Concat"""
        self.vs[13]["GUID__"] = 4117622620453396577
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 2212694533574936279
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 8171250160474766455
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 3461706554544706977
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 97895700566679173
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 2528501530017514722
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6134632606734548937
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 904859969266671479
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 7374848081738079381
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 7850682278350301139
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 8343437249472975260
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 2302435956545572683
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = 330826146261537480
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = 5314822509520020617
        self.vs[27]["name"] = """PROV"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 4222995900048882412
        self.vs[28]["name"] = """name"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["GUID__"] = 3996850121403357841
        self.vs[29]["name"] = """ApplyAttribute"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["GUID__"] = 5101881015540320036
        self.vs[30]["name"] = """shortName"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["GUID__"] = 2282686787098277654
        self.vs[31]["associationType"] = """partition"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = 936604644932167283
        self.vs[32]["associationType"] = """module"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = 8553192678221154460
        self.vs[33]["associationType"] = """scheduler"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = 4516014226369612936
        self.vs[34]["associationType"] = """required"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = 2366860206345644862
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = 5068531495684029364
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = 14191530394951649
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = 2507430236518571156
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = 2221931532292385328
        self.vs[39]["mm__"] = """match_contains"""
        self.vs[39]["GUID__"] = 5582610693857001273

