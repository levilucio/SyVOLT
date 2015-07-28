from core.himesis import Himesis
import uuid

class HConnectPPortPrototype(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule ConnectPPortPrototype.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConnectPPortPrototype, self).__init__(name='HConnectPPortPrototype', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """ConnectPPortPrototype"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConnectPPortPrototype')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """ConnectPPortPrototype"""
        
        # match class PhysicalNode() node
        self.add_node()
        self.vs[3]["name"] = """""" 
        self.vs[3]["classtype"] = """PhysicalNode"""
        self.vs[3]["mm__"] = """PhysicalNode"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class PhysicalNode()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class Partition() node
        self.add_node()
        self.vs[5]["name"] = """""" 
        self.vs[5]["classtype"] = """Partition"""
        self.vs[5]["mm__"] = """Partition"""
        self.vs[5]["cardinality"] = """+""" 
        # match_contains node for class Partition()
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class Module() node
        self.add_node()
        self.vs[7]["name"] = """""" 
        self.vs[7]["classtype"] = """Module"""
        self.vs[7]["mm__"] = """Module"""
        self.vs[7]["cardinality"] = """+""" 
        # match_contains node for class Module()
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        # match class Scheduler() node
        self.add_node()
        self.vs[9]["name"] = """""" 
        self.vs[9]["classtype"] = """Scheduler"""
        self.vs[9]["mm__"] = """Scheduler"""
        self.vs[9]["cardinality"] = """+""" 
        # match_contains node for class Scheduler()
        self.add_node()
        self.vs[10]["mm__"] = """match_contains"""
        # match class Service() node
        self.add_node()
        self.vs[11]["name"] = """""" 
        self.vs[11]["classtype"] = """Service"""
        self.vs[11]["mm__"] = """Service"""
        self.vs[11]["cardinality"] = """1""" 
        # match_contains node for class Service()
        self.add_node()
        self.vs[12]["mm__"] = """match_contains"""
        
        
        # apply class CompositionType() node
        self.add_node()
        self.vs[13]["name"] = """""" 
        self.vs[13]["classtype"] = """CompositionType"""
        self.vs[13]["mm__"] = """CompositionType"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class CompositionType()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class PPortPrototype() node
        self.add_node()
        self.vs[15]["name"] = """""" 
        self.vs[15]["classtype"] = """PPortPrototype"""
        self.vs[15]["mm__"] = """PPortPrototype"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class PPortPrototype()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        
        
        # match association PhysicalNode--partition-->Partition node
        self.add_node()
        self.vs[17]["associationType"] = """partition"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association Partition--module-->Module node
        self.add_node()
        self.vs[18]["associationType"] = """module"""
        self.vs[18]["mm__"] = """directLink_S"""
        # match association Module--scheduler-->Scheduler node
        self.add_node()
        self.vs[19]["associationType"] = """scheduler"""
        self.vs[19]["mm__"] = """directLink_S"""
        # match association Scheduler--provided-->Service node
        self.add_node()
        self.vs[20]["associationType"] = """provided"""
        self.vs[20]["mm__"] = """directLink_S"""
        
        # apply association CompositionType--port-->PPortPrototype node
        self.add_node()
        self.vs[21]["associationType"] = """port"""
        self.vs[21]["mm__"] = """directLink_T"""
        
        # backward association PhysicalNode---->CompositionType node
        self.add_node()
        self.vs[22]["type"] = """ruleDef"""
        self.vs[22]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class PhysicalNode()
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class Partition()
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class Module()
                (0,10), # matchmodel -> match_contains
                (10,9), # match_contains -> match_class Scheduler()
                (0,12), # matchmodel -> match_contains
                (12,11), # match_contains -> match_class Service()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class CompositionType()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class PPortPrototype()
                (3,17), # match_class PhysicalNode() -> association partition
                (17,5), # association partition  -> match_class Partition()
                (5,18), # match_class Partition() -> association module
                (18,7), # association module  -> match_class Module()
                (7,19), # match_class Module() -> association scheduler
                (19,9), # association scheduler  -> match_class Scheduler()
                (9,20), # match_class Scheduler() -> association provided
                (20,11), # association provided  -> match_class Service()
                (13,21), # apply_class CompositionType() -> association port
                (21,15), # association port  -> apply_class PPortPrototype()
                (13,22), # apply_class CompositionType() -> backward_association
                (22,3), #  backward_association -> apply_class PhysicalNode()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((13,'ApplyAttribute'),('constant','solveRef')), ((15,'shortName'),('concat',((9,'name'),('constant','PROV')))), ]

        
