from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP2_ConnectedLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HPP2_ConnectedLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True
        
                super(HPP2_ConnectedLHS, self).__init__(name='HPP2_ConnectedLHS', num_nodes=0, edges=[])
        
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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'PP2')
        
                # Set the node attributes
        
                # match class OUT2() node
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
                self.vs[0]["mm__"] = """MT_pre__OUT2"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Transition() node
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
                self.vs[1]["mm__"] = """MT_pre__Transition"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Trigger() node
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
                self.vs[2]["mm__"] = """MT_pre__Trigger"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Signal() node
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
                self.vs[3]["mm__"] = """MT_pre__Signal"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # Nodes that represent the edges of the property.
        # match association Transition--type-->OUT2 node
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

return attr_value == "type"
"""

                self.vs[4]["MT_label__"] = """5"""
                self.vs[4]["MT_subtypes__"] = []
                self.vs[4]["MT_dirty__"] = False
                self.vs[4]["mm__"] = """MT_pre__directLink_S"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc4')
        # match association Transition--triggers-->Trigger node
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

return attr_value == "triggers"
"""

                self.vs[5]["MT_label__"] = """6"""
                self.vs[5]["MT_subtypes__"] = []
                self.vs[5]["MT_dirty__"] = False
                self.vs[5]["mm__"] = """MT_pre__directLink_S"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc5')
        # match association Trigger--signal-->Signal node
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

return attr_value == "signal"
"""

                self.vs[6]["MT_label__"] = """7"""
                self.vs[6]["MT_subtypes__"] = []
                self.vs[6]["MT_dirty__"] = False
                self.vs[6]["mm__"] = """MT_pre__directLink_S"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc6')
        
        # Add the edges
                self.add_edges([
                (1,4), # match_class Transition() -> association type
                (4,0), # association type  -> match_class OUT2()
                (1,5), # match_class Transition() -> association triggers
                (5,2), # association triggers  -> match_class Trigger()
                (2,6), # match_class Trigger() -> association signal
                (6,3) # association signal  -> match_class Signal()
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

                return attr_value == "type"


        def eval_attr16(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "triggers"


        def eval_attr17(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "signal"


        
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
        
