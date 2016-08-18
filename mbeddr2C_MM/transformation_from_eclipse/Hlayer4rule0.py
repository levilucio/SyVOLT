from core.himesis import Himesis
import uuid

class Hlayer4rule0(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer4rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer4rule0, self).__init__(name='Hlayer4rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer4rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer4rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
 
        
        # match class ImplementationModule(layer4rule0class0) node
        self.add_node()

        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match_contains node for class ImplementationModule(layer4rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        # match class InstanceConfiguration(layer4rule0class1) node
        self.add_node()

        self.vs[5]["mm__"] = """InstanceConfiguration""" 
        self.vs[5]["attr1"] = """+""" 
        # match_contains node for class InstanceConfiguration(layer4rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """match_contains"""
        # match class ComponentInstance(layer4rule0class2) node
        self.add_node()

        self.vs[7]["mm__"] = """ComponentInstance""" 
        self.vs[7]["attr1"] = """+""" 
        # match_contains node for class ComponentInstance(layer4rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """match_contains"""
        
        
        # apply class ImplementationModule(layer4rule0class3) node
        self.add_node()

        self.vs[9]["mm__"] = """ImplementationModule""" 
        self.vs[9]["attr1"] = """1"""
        # apply_contains node for class ImplementationModule(layer4rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class Function(layer4rule0class4) node
        self.add_node()

        self.vs[11]["mm__"] = """Function""" 
        self.vs[11]["attr1"] = """1"""
        # apply_contains node for class Function(layer4rule0class4)
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class VoidType(layer4rule0class5) node
        self.add_node()

        self.vs[13]["mm__"] = """VoidType""" 
        self.vs[13]["attr1"] = """1"""
        # apply_contains node for class VoidType(layer4rule0class5)
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class StatementList(layer4rule0class6) node
        self.add_node()

        self.vs[15]["mm__"] = """StatementList""" 
        self.vs[15]["attr1"] = """1"""
        # apply_contains node for class StatementList(layer4rule0class6)
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[17]["attr1"] = """contents"""
        self.vs[17]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[18]["attr1"] = """contents"""
        self.vs[18]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[19]["attr1"] = """contents"""
        self.vs[19]["mm__"] = """directLink_T"""
        # apply association Function--type-->VoidType node
        self.add_node()
        self.vs[20]["attr1"] = """type"""
        self.vs[20]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[21]["attr1"] = """body"""
        self.vs[21]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[22]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class ImplementationModule(layer4rule0class0)
                (0,6), # matchmodel -> match_contains
                (6,5), # match_contains -> match_class InstanceConfiguration(layer4rule0class1)
                (0,8), # matchmodel -> match_contains
                (8,7), # match_contains -> match_class ComponentInstance(layer4rule0class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class ImplementationModule(layer4rule0class3)
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class Function(layer4rule0class4)
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class VoidType(layer4rule0class5)
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class StatementList(layer4rule0class6)
                (3,17), # match_class ImplementationModule(layer4rule0class0) -> association contents
                (17,5), # association contents  -> match_class InstanceConfiguration(layer4rule0class1)
                (5,18), # match_class InstanceConfiguration(layer4rule0class1) -> association contents
                (18,7), # association contents  -> match_class ComponentInstance(layer4rule0class2)
                (9,19), # apply_class ImplementationModule(layer4rule0class3) -> association contents
                (19,11), # association contents  -> apply_class Function(layer4rule0class4)
                (11,20), # apply_class Function(layer4rule0class4) -> association type
                (20,13), # association type  -> apply_class VoidType(layer4rule0class5)
                (11,21), # apply_class Function(layer4rule0class4) -> association body
                (21,15), # association body  -> apply_class StatementList(layer4rule0class6)
                (9,22), # apply_class ImplementationModule(layer4rule0class3) -> backward_association
                (22,3), #  backward_association -> apply_class ImplementationModule(layer4rule0class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((9,'__ApplyAttribute'),('constant','ImplementationModule')), ((11,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((5,'name'),('concat',(('constant','_'),('concat',((7,'name'),('constant','__wire')))))))))))), ((15,'__ApplyAttribute'),('constant','WireFunctionStatements')), ]

        
