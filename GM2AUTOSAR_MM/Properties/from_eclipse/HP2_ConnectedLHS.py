from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HP2_ConnectedLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HP2_ConnectedLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True
        
                super(HP2_ConnectedLHS, self).__init__(name='HP2_ConnectedLHS', num_nodes=0, edges=[])
        
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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'P2')
        
                # Set the node attributes
        
                # match class PhysicalNode() node
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
                self.vs[0]["mm__"] = """MT_pre__PhysicalNode"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Partition() node
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
                self.vs[1]["mm__"] = """MT_pre__Partition"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Module() node
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
                self.vs[2]["mm__"] = """MT_pre__Module"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Scheduler() node
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
                self.vs[3]["mm__"] = """MT_pre__Scheduler"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
                # match class Service() node
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
                self.vs[4]["mm__"] = """MT_pre__Service"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
        
        # Nodes that represent the edges of the property.
        # match association PhysicalNode--partition-->Partition node
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

return attr_value == "partition"
"""

                self.vs[5]["MT_label__"] = """6"""
                self.vs[5]["MT_subtypes__"] = []
                self.vs[5]["MT_dirty__"] = False
                self.vs[5]["mm__"] = """MT_pre__directLink_S"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc5')
        # match association Partition--module-->Module node
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

return attr_value == "module"
"""

                self.vs[6]["MT_label__"] = """7"""
                self.vs[6]["MT_subtypes__"] = []
                self.vs[6]["MT_dirty__"] = False
                self.vs[6]["mm__"] = """MT_pre__directLink_S"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc6')
        # match association Module--scheduler-->Scheduler node
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

return attr_value == "scheduler"
"""

                self.vs[7]["MT_label__"] = """8"""
                self.vs[7]["MT_subtypes__"] = []
                self.vs[7]["MT_dirty__"] = False
                self.vs[7]["mm__"] = """MT_pre__directLink_S"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc7')
        # match association Scheduler--required-->Service node
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

return attr_value == "required"
"""

                self.vs[8]["MT_label__"] = """9"""
                self.vs[8]["MT_subtypes__"] = []
                self.vs[8]["MT_dirty__"] = False
                self.vs[8]["mm__"] = """MT_pre__directLink_S"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc8')
        
        # Add the edges
                self.add_edges([
                (0,5), # match_class PhysicalNode() -> association partition
                (5,1), # association partition  -> match_class Partition()
                (1,6), # match_class Partition() -> association module
                (6,2), # association module  -> match_class Module()
                (2,7), # match_class Module() -> association scheduler
                (7,3), # association scheduler  -> match_class Scheduler()
                (3,8), # match_class Scheduler() -> association required
                (8,4) # association required  -> match_class Service()
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

                return attr_value == "partition"


        def eval_attr17(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "module"


        def eval_attr18(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "scheduler"


        def eval_attr19(self, attr_value, this):
        
                #===============================================================================
                # This code is executed when evaluating if a node shall be matched by this rule.
                # You can access the value of the current node's attribute value by: attr_value.
                # You can access any attribute x of this node by: this['x'].
                # If the constraint relies on attribute values from other nodes,
                # use the LHS/NAC constraint instead.
                # The given constraint must evaluate to a boolean expression.
                #===============================================================================

                return attr_value == "required"


        
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
        
