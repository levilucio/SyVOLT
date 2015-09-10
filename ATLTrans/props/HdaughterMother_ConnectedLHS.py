from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HdaughterMother_ConnectedLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HdaughterMother_ConnectedLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True
        
                super(HdaughterMother_ConnectedLHS, self).__init__(name='HdaughterMother_ConnectedLHS', num_nodes=0, edges=[])
        
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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMother')
        
                # Set the node attributes
        
                # match class Family() node
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
                self.vs[0]["mm__"] = """MT_pre__Family"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Member() node
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
                self.vs[1]["mm__"] = """MT_pre__Member"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Member() node
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
                self.vs[2]["mm__"] = """MT_pre__Member"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # Nodes that represent the edges of the property.
        # match association Family--mother-->Member node
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

return attr_value == "mother"
"""

                self.vs[3]["MT_label__"] = """4"""
                self.vs[3]["MT_subtypes__"] = []
                self.vs[3]["MT_dirty__"] = False
                self.vs[3]["mm__"] = """MT_pre__directLink_S"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc3')
        # match association Family--daughter-->Member node
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

return attr_value == "daughter"
"""

                self.vs[4]["MT_label__"] = """5"""
                self.vs[4]["MT_subtypes__"] = []
                self.vs[4]["MT_dirty__"] = False
                self.vs[4]["mm__"] = """MT_pre__directLink_S"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc4')
        
        # Add the edges
                self.add_edges([
                (0,3), # match_class Family() -> association mother
                (3,2), # association mother  -> match_class Member()
                (0,4), # match_class Family() -> association daughter
                (4,1) # association daughter  -> match_class Member()
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

                return attr_value == "mother"


        def eval_attr15(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "daughter"


        
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
        
        
