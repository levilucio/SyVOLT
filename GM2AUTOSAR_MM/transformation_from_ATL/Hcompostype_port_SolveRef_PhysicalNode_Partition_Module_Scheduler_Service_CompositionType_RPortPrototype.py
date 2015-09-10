

from core.himesis import Himesis

class Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_RPortPrototype(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_RPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_RPortPrototype, self).__init__(name='Hcompostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_RPortPrototype', num_nodes=40, edges=[])
        
        # Add the edges
        self.add_edges([[0, 35], [35, 3], [0, 36], [36, 4], [0, 37], [37, 5], [0, 38], [38, 6], [0, 39], [39, 7], [1, 14], [14, 8], [1, 15], [15, 9], [3, 31], [31, 4], [4, 32], [32, 5], [5, 33], [33, 6], [6, 34], [34, 7], [8, 10], [10, 9], [8, 11], [11, 3], [6, 12], [12, 28], [8, 16], [16, 29], [17, 18], [18, 29], [17, 19], [19, 20], [9, 21], [21, 30], [22, 23], [23, 30], [22, 24], [13, 25], [25, 28], [13, 26], [26, 27], [24, 13], [0, 2], [2, 1]])
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        self["name"] = """compostype_port_SolveRef_PhysicalNode_Partition_Module_Scheduler_Service_CompositionType_RPortPrototype"""
        self["GUID__"] = 5811576133363509735
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MatchModel"""
        self.vs[0]["GUID__"] = 5034515599242533837
        self.vs[1]["mm__"] = """ApplyModel"""
        self.vs[1]["GUID__"] = 2547939610998836644
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["GUID__"] = 2781549158868115425
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+"""
        self.vs[3]["GUID__"] = 4102412556719755944
        self.vs[4]["name"] = """"""
        self.vs[4]["classtype"] = """Partition"""
        self.vs[4]["mm__"] = """Partition"""
        self.vs[4]["cardinality"] = """+"""
        self.vs[4]["GUID__"] = 4385933893497684840
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """Module"""
        self.vs[5]["mm__"] = """Module"""
        self.vs[5]["cardinality"] = """+"""
        self.vs[5]["GUID__"] = 3592887460656493278
        self.vs[6]["name"] = """"""
        self.vs[6]["classtype"] = """Scheduler"""
        self.vs[6]["mm__"] = """Scheduler"""
        self.vs[6]["cardinality"] = """+"""
        self.vs[6]["GUID__"] = 375372794992940814
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """Service"""
        self.vs[7]["mm__"] = """Service"""
        self.vs[7]["cardinality"] = """1"""
        self.vs[7]["GUID__"] = 2718174488376801044
        self.vs[8]["name"] = """"""
        self.vs[8]["classtype"] = """CompositionType"""
        self.vs[8]["mm__"] = """CompositionType"""
        self.vs[8]["cardinality"] = """1"""
        self.vs[8]["GUID__"] = 3507052233244577473
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """RPortPrototype"""
        self.vs[9]["mm__"] = """RPortPrototype"""
        self.vs[9]["cardinality"] = """1"""
        self.vs[9]["GUID__"] = 2163204670517425810
        self.vs[10]["associationType"] = """port"""
        self.vs[10]["mm__"] = """directLink_T"""
        self.vs[10]["GUID__"] = 4207626294899012781
        self.vs[11]["mm__"] = """backward_link"""
        self.vs[11]["type"] = """ruleDef"""
        self.vs[11]["GUID__"] = 3820704333244997721
        self.vs[12]["mm__"] = """hasAttribute_S"""
        self.vs[12]["GUID__"] = 7544332680484584476
        self.vs[13]["name"] = """Concat36"""
        self.vs[13]["Type"] = """'String'"""
        self.vs[13]["mm__"] = """Concat"""
        self.vs[13]["GUID__"] = 6133452662261811716
        self.vs[14]["mm__"] = """apply_contains"""
        self.vs[14]["GUID__"] = 7166276267258392352
        self.vs[15]["mm__"] = """apply_contains"""
        self.vs[15]["GUID__"] = 791686793296522816
        self.vs[16]["mm__"] = """hasAttribute_T"""
        self.vs[16]["GUID__"] = 3838309199242472111
        self.vs[17]["name"] = """eq_"""
        self.vs[17]["mm__"] = """Equation"""
        self.vs[17]["GUID__"] = 3040232616928965086
        self.vs[18]["mm__"] = """leftExpr"""
        self.vs[18]["GUID__"] = 8395162386016366905
        self.vs[19]["mm__"] = """rightExpr"""
        self.vs[19]["GUID__"] = 6446996503552889516
        self.vs[20]["name"] = """solveRef"""
        self.vs[20]["Type"] = """'String'"""
        self.vs[20]["mm__"] = """Constant"""
        self.vs[20]["GUID__"] = 4380193899985297801
        self.vs[21]["mm__"] = """hasAttribute_T"""
        self.vs[21]["GUID__"] = 3090711843124307493
        self.vs[22]["name"] = """eq_"""
        self.vs[22]["mm__"] = """Equation"""
        self.vs[22]["GUID__"] = 6563791109000567492
        self.vs[23]["mm__"] = """leftExpr"""
        self.vs[23]["GUID__"] = 7312783210468111068
        self.vs[24]["mm__"] = """rightExpr"""
        self.vs[24]["GUID__"] = 9220638157370647100
        self.vs[25]["mm__"] = """hasArgs"""
        self.vs[25]["GUID__"] = 1725431290885655654
        self.vs[26]["mm__"] = """hasArgs"""
        self.vs[26]["GUID__"] = 1587322777181840741
        self.vs[27]["name"] = """REQ"""
        self.vs[27]["Type"] = """'String'"""
        self.vs[27]["mm__"] = """Constant"""
        self.vs[27]["GUID__"] = 1584553080451353584
        self.vs[28]["name"] = """name"""
        self.vs[28]["Type"] = """'String'"""
        self.vs[28]["mm__"] = """Attribute"""
        self.vs[28]["GUID__"] = 4312548592263787405
        self.vs[29]["name"] = """ApplyAttribute"""
        self.vs[29]["Type"] = """'String'"""
        self.vs[29]["mm__"] = """Attribute"""
        self.vs[29]["GUID__"] = 8249766013631463790
        self.vs[30]["name"] = """shortName"""
        self.vs[30]["Type"] = """'String'"""
        self.vs[30]["mm__"] = """Attribute"""
        self.vs[30]["GUID__"] = 6911836760928741979
        self.vs[31]["associationType"] = """partition"""
        self.vs[31]["mm__"] = """directLink_S"""
        self.vs[31]["GUID__"] = 4635227676451909746
        self.vs[32]["associationType"] = """module"""
        self.vs[32]["mm__"] = """directLink_S"""
        self.vs[32]["GUID__"] = 7984029781673856728
        self.vs[33]["associationType"] = """scheduler"""
        self.vs[33]["mm__"] = """directLink_S"""
        self.vs[33]["GUID__"] = 5996033610815853781
        self.vs[34]["associationType"] = """provided"""
        self.vs[34]["mm__"] = """directLink_S"""
        self.vs[34]["GUID__"] = 7544144827221240716
        self.vs[35]["mm__"] = """match_contains"""
        self.vs[35]["GUID__"] = 1438168992576212574
        self.vs[36]["mm__"] = """match_contains"""
        self.vs[36]["GUID__"] = 5263446536098024421
        self.vs[37]["mm__"] = """match_contains"""
        self.vs[37]["GUID__"] = 22527004003284979
        self.vs[38]["mm__"] = """match_contains"""
        self.vs[38]["GUID__"] = 1376851004555263142
        self.vs[39]["mm__"] = """match_contains"""
        self.vs[39]["GUID__"] = 1917432809308706135

