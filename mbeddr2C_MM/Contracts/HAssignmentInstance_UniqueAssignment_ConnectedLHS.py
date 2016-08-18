from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HAssignmentInstance_UniqueAssignment_ConnectedLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HAssignmentInstance_UniqueAssignment_ConnectedLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True
        
                super(HAssignmentInstance_UniqueAssignment_ConnectedLHS, self).__init__(name='HAssignmentInstance_UniqueAssignment_ConnectedLHS', num_nodes=0, edges=[])
        
                # Set the graph attributes
                self["mm__"] = ['MT_pre__FamiliesToPersonsMM', 'MoTifRule']
                self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
                self["name"] = """"""
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'AssignmentInstance_UniqueAssignment')
        
                # Set the node attributes
        
                # match class AssemblyConnector() node
                self.add_node()
                self.vs[0]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[0]["MT_label__"] = """1"""
                self.vs[0]["MT_dirty__"] = False
                self.vs[0]["mm__"] = """MT_pre__AssemblyConnector"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class InstancePortRef() node
                self.add_node()
                self.vs[1]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[1]["MT_label__"] = """2"""
                self.vs[1]["MT_dirty__"] = False
                self.vs[1]["mm__"] = """MT_pre__InstancePortRef"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ComponentInstance() node
                self.add_node()
                self.vs[2]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[2]["MT_label__"] = """3"""
                self.vs[2]["MT_dirty__"] = False
                self.vs[2]["mm__"] = """MT_pre__ComponentInstance"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class RequiredPort() node
                self.add_node()
                self.vs[3]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[3]["MT_label__"] = """4"""
                self.vs[3]["MT_dirty__"] = False
                self.vs[3]["mm__"] = """MT_pre__RequiredPort"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class AtomicComponent() node
                self.add_node()
                self.vs[4]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[4]["MT_label__"] = """5"""
                self.vs[4]["MT_dirty__"] = False
                self.vs[4]["mm__"] = """MT_pre__AtomicComponent"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class InstancePortRef() node
                self.add_node()
                self.vs[5]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[5]["MT_label__"] = """6"""
                self.vs[5]["MT_dirty__"] = False
                self.vs[5]["mm__"] = """MT_pre__InstancePortRef"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ComponentInstance() node
                self.add_node()
                self.vs[6]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[6]["MT_label__"] = """7"""
                self.vs[6]["MT_dirty__"] = False
                self.vs[6]["mm__"] = """MT_pre__ComponentInstance"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class ProvidedPort() node
                self.add_node()
                self.vs[7]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[7]["MT_label__"] = """8"""
                self.vs[7]["MT_dirty__"] = False
                self.vs[7]["mm__"] = """MT_pre__ProvidedPort"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class AtomicComponent() node
                self.add_node()
                self.vs[8]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
                self.vs[8]["MT_label__"] = """9"""
                self.vs[8]["MT_dirty__"] = False
                self.vs[8]["mm__"] = """MT_pre__AtomicComponent"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # Nodes that represent the edges of the property.
        # match association AssemblyConnector--source-->InstancePortRef node
                self.add_node()
                self.vs[9]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "source"
"""

                self.vs[9]["MT_label__"] = """10"""
                self.vs[9]["MT_subtypes__"] = []
                self.vs[9]["MT_dirty__"] = False
                self.vs[9]["mm__"] = """MT_pre__directLink_S"""
                self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc9')
        # match association InstancePortRef--instance-->ComponentInstance node
                self.add_node()
                self.vs[10]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "instance"
"""

                self.vs[10]["MT_label__"] = """11"""
                self.vs[10]["MT_subtypes__"] = []
                self.vs[10]["MT_dirty__"] = False
                self.vs[10]["mm__"] = """MT_pre__directLink_S"""
                self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc10')
        # match association InstancePortRef--port-->RequiredPort node
                self.add_node()
                self.vs[11]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "port"
"""

                self.vs[11]["MT_label__"] = """12"""
                self.vs[11]["MT_subtypes__"] = []
                self.vs[11]["MT_dirty__"] = False
                self.vs[11]["mm__"] = """MT_pre__directLink_S"""
                self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
        # match association ComponentInstance--component-->AtomicComponent node
                self.add_node()
                self.vs[12]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "component"
"""

                self.vs[12]["MT_label__"] = """13"""
                self.vs[12]["MT_subtypes__"] = []
                self.vs[12]["MT_dirty__"] = False
                self.vs[12]["mm__"] = """MT_pre__directLink_S"""
                self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        # match association AtomicComponent--contents-->RequiredPort node
                self.add_node()
                self.vs[13]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "contents"
"""

                self.vs[13]["MT_label__"] = """14"""
                self.vs[13]["MT_subtypes__"] = []
                self.vs[13]["MT_dirty__"] = False
                self.vs[13]["mm__"] = """MT_pre__directLink_S"""
                self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc13')
        # match association AssemblyConnector--target-->InstancePortRef node
                self.add_node()
                self.vs[14]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "target"
"""

                self.vs[14]["MT_label__"] = """15"""
                self.vs[14]["MT_subtypes__"] = []
                self.vs[14]["MT_dirty__"] = False
                self.vs[14]["mm__"] = """MT_pre__directLink_S"""
                self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc14')
        # match association InstancePortRef--instance-->ComponentInstance node
                self.add_node()
                self.vs[15]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "instance"
"""

                self.vs[15]["MT_label__"] = """16"""
                self.vs[15]["MT_subtypes__"] = []
                self.vs[15]["MT_dirty__"] = False
                self.vs[15]["mm__"] = """MT_pre__directLink_S"""
                self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        # match association InstancePortRef--port-->ProvidedPort node
                self.add_node()
                self.vs[16]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "port"
"""

                self.vs[16]["MT_label__"] = """17"""
                self.vs[16]["MT_subtypes__"] = []
                self.vs[16]["MT_dirty__"] = False
                self.vs[16]["mm__"] = """MT_pre__directLink_S"""
                self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc16')
        # match association ComponentInstance--component-->AtomicComponent node
                self.add_node()
                self.vs[17]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "component"
"""

                self.vs[17]["MT_label__"] = """18"""
                self.vs[17]["MT_subtypes__"] = []
                self.vs[17]["MT_dirty__"] = False
                self.vs[17]["mm__"] = """MT_pre__directLink_S"""
                self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
        # match association AtomicComponent--contents-->ProvidedPort node
                self.add_node()
                self.vs[18]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "contents"
"""

                self.vs[18]["MT_label__"] = """19"""
                self.vs[18]["MT_subtypes__"] = []
                self.vs[18]["MT_dirty__"] = False
                self.vs[18]["mm__"] = """MT_pre__directLink_S"""
                self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc18')
        
        # Add the edges
                self.add_edges([
                (0,9), # match_class AssemblyConnector() -> association source
                (9,1), # association source  -> match_class InstancePortRef()
                (1,10), # match_class InstancePortRef() -> association instance
                (10,2), # association instance  -> match_class ComponentInstance()
                (1,11), # match_class InstancePortRef() -> association port
                (11,3), # association port  -> match_class RequiredPort()
                (2,12), # match_class ComponentInstance() -> association component
                (12,4), # association component  -> match_class AtomicComponent()
                (4,13), # match_class AtomicComponent() -> association contents
                (13,3), # association contents  -> match_class RequiredPort()
                (0,14), # match_class AssemblyConnector() -> association target
                (14,5), # association target  -> match_class InstancePortRef()
                (5,15), # match_class InstancePortRef() -> association instance
                (15,6), # association instance  -> match_class ComponentInstance()
                (5,16), # match_class InstancePortRef() -> association port
                (16,7), # association port  -> match_class ProvidedPort()
                (6,17), # match_class ComponentInstance() -> association component
                (17,8), # association component  -> match_class AtomicComponent()
                (8,18), # match_class AtomicComponent() -> association contents
                (18,7) # association contents  -> match_class ProvidedPort()
        ])
        
                # Add the attribute equations
                self["equations"] = []
        
        def eval_attr11(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr12(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr13(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr14(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr15(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr16(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr17(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr18(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        
        def eval_attr19(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return True        
        

        def eval_attr110(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "source"


        def eval_attr111(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "instance"


        def eval_attr112(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "port"


        def eval_attr113(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "component"


        def eval_attr114(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "contents"


        def eval_attr115(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "target"


        def eval_attr116(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "instance"


        def eval_attr117(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "port"


        def eval_attr118(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "component"


        def eval_attr119(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "contents"


        
        def constraint(self, PreNode, graph):
                """
                Executable constraint code.
                @param PreNode: Function taking an integer as parameter
                                and returns the node corresponding to that label.
                """
                #===============================================================================
                # This code is executed after the nodes in the LHS have been matched.
                # You can access a matched node labelled n by: PreNode('n').
                # To access attribute x of node n, use: PreNode('n')['x'].
                # The given constraint must evaluate to a boolean expression:
                #    returning True enables the rule to be applied,
                #    returning False forbids the rule from being applied.
                #===============================================================================

                return True
        
