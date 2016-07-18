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
        self.vs[2]["attr1"] = """layer4rule0"""
        
        # match class ImplementationModule(layer4rule0class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """ImplementationModule""" 
        self.vs[3]["attr1"] = """+""" 
        # match class InstanceConfiguration(layer4rule0class1) node
        self.add_node()
        
        self.vs[4]["mm__"] = """InstanceConfiguration""" 
        self.vs[4]["attr1"] = """+""" 
        # match class ComponentInstance(layer4rule0class2) node
        self.add_node()
        
        self.vs[5]["mm__"] = """ComponentInstance""" 
        self.vs[5]["attr1"] = """+""" 
        
        
        # apply class ImplementationModule(layer4rule0class3) node
        self.add_node()

        self.vs[6]["mm__"] = """ImplementationModule""" 
        self.vs[6]["attr1"] = """1"""
        # apply class Function(layer4rule0class4) node
        self.add_node()

        self.vs[7]["mm__"] = """Function""" 
        self.vs[7]["attr1"] = """1"""
        # apply class VoidType(layer4rule0class5) node
        self.add_node()

        self.vs[8]["mm__"] = """VoidType""" 
        self.vs[8]["attr1"] = """1"""
        # apply class StatementList(layer4rule0class6) node
        self.add_node()

        self.vs[9]["mm__"] = """StatementList""" 
        self.vs[9]["attr1"] = """1"""
        
        
        # match association ImplementationModule--contents-->InstanceConfiguration node
        self.add_node()
        self.vs[10]["attr1"] = """contents"""
        self.vs[10]["mm__"] = """directLink_S"""
        # match association InstanceConfiguration--contents-->ComponentInstance node
        self.add_node()
        self.vs[11]["attr1"] = """contents"""
        self.vs[11]["mm__"] = """directLink_S"""
        
        # apply association ImplementationModule--contents-->Function node
        self.add_node()
        self.vs[12]["attr1"] = """contents"""
        self.vs[12]["mm__"] = """directLink_T"""
        # apply association Function--type-->VoidType node
        self.add_node()
        self.vs[13]["attr1"] = """type"""
        self.vs[13]["mm__"] = """directLink_T"""
        # apply association Function--body-->StatementList node
        self.add_node()
        self.vs[14]["attr1"] = """body"""
        self.vs[14]["mm__"] = """directLink_T"""
        
        # backward association ImplementationModule---->ImplementationModule node
        self.add_node()

        self.vs[15]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class ImplementationModule(layer4rule0class0)
                (0,4), # matchmodel -> match_class InstanceConfiguration(layer4rule0class1)
                (0,5), # matchmodel -> match_class ComponentInstance(layer4rule0class2)
                (1,6), # applymodel -> -> apply_class ImplementationModule(layer4rule0class3)
                (1,7), # applymodel -> -> apply_class Function(layer4rule0class4)
                (1,8), # applymodel -> -> apply_class VoidType(layer4rule0class5)
                (1,9), # applymodel -> -> apply_class StatementList(layer4rule0class6)
                (3,10), # match_class ImplementationModule(layer4rule0class0) -> association contents
                (10,4), # association contents  -> match_class InstanceConfiguration(layer4rule0class1)
                (4,11), # match_class InstanceConfiguration(layer4rule0class1) -> association contents
                (11,5), # association contents  -> match_class ComponentInstance(layer4rule0class2)
                (6,12), # apply_class ImplementationModule(layer4rule0class3) -> association contents
                (12,7), # association contents  -> apply_class Function(layer4rule0class4)
                (7,13), # apply_class Function(layer4rule0class4) -> association type
                (13,8), # association type  -> apply_class VoidType(layer4rule0class5)
                (7,14), # apply_class Function(layer4rule0class4) -> association body
                (14,9), # association body  -> apply_class StatementList(layer4rule0class6)
                (6,15), # apply_class ImplementationModule(layer4rule0class3) -> backward_association
                (15,3), #  backward_association -> apply_class ImplementationModule(layer4rule0class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((6,'__ApplyAttribute'),('constant','ImplementationModule')), ((7,'name'),('concat',((3,'name'),('concat',(('constant','_'),('concat',((4,'name'),('concat',(('constant','_'),('concat',((5,'name'),('constant','__wire')))))))))))), ((9,'__ApplyAttribute'),('constant','WireFunctionStatements')), ]

        
