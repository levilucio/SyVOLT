from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HS1_if_CompleteLHS(HimesisPreConditionPatternLHS):
        def __init__(self, *args, **kwargs):
                """
                Creates the himesis graph representing the AToM3 model HS1_if_CompleteLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True

                super(HS1_if_CompleteLHS, self).__init__(name='HS1_if_CompleteLHS', num_nodes=0, edges=[])

                # Set the graph attributes
                self["mm__"] = []

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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'S1_if')
        
                # Nodes that represent match classes
        
        
        #Nodes that represent apply classes
        # match class System() node
                self.add_node()
                self.vs[0]["MT_subtypeMatching__"] = False
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
                self.vs[0]["MT_subtypes__"] = []
                self.vs[0]["MT_dirty__"] = False
                self.vs[0]["mm__"] = """MT_pre__System"""
                self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class SystemMapping() node
                self.add_node()
                self.vs[1]["MT_subtypeMatching__"] = False
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
                self.vs[1]["MT_subtypes__"] = []
                self.vs[1]["MT_dirty__"] = False
                self.vs[1]["mm__"] = """MT_pre__SystemMapping"""
                self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class SwcToEcuMapping() node
                self.add_node()
                self.vs[2]["MT_subtypeMatching__"] = False
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
                self.vs[2]["MT_subtypes__"] = []
                self.vs[2]["MT_dirty__"] = False
                self.vs[2]["mm__"] = """MT_pre__SwcToEcuMapping"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class ComponentPrototype() node
                self.add_node()
                self.vs[3]["MT_subtypeMatching__"] = False
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
                self.vs[3]["MT_subtypes__"] = []
                self.vs[3]["MT_dirty__"] = False
                self.vs[3]["mm__"] = """MT_pre__ComponentPrototype"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class SwCompToEcuMapping_component() node
                self.add_node()
                self.vs[4]["MT_subtypeMatching__"] = False
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
                self.vs[4]["MT_subtypes__"] = []
                self.vs[4]["MT_dirty__"] = False
                self.vs[4]["mm__"] = """MT_pre__SwCompToEcuMapping_component"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
                
        # Nodes that represent the match associations of the property.
        
        
        # Nodes that represent the apply associations of the property.
        # apply association System--mapping-->SystemMapping node
                self.add_node()
                self.vs[5]["MT_subtypeMatching__"] = False
                self.vs[5]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "mapping"
"""
                self.vs[5]["MT_label__"] = """6"""
                self.vs[5]["MT_subtypes__"] = []
                self.vs[5]["MT_dirty__"] = False
                self.vs[5]["mm__"] = """MT_pre__directLink_T"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc5')
        # apply association SystemMapping--swMapping-->SwcToEcuMapping node
                self.add_node()
                self.vs[6]["MT_subtypeMatching__"] = False
                self.vs[6]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "swMapping"
"""
                self.vs[6]["MT_label__"] = """7"""
                self.vs[6]["MT_subtypes__"] = []
                self.vs[6]["MT_dirty__"] = False
                self.vs[6]["mm__"] = """MT_pre__directLink_T"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc6')
        # apply association SwcToEcuMapping--component-->SwCompToEcuMapping_component node
                self.add_node()
                self.vs[7]["MT_subtypeMatching__"] = False
                self.vs[7]["MT_pre__attr1"] = """
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
                self.vs[7]["MT_label__"] = """8"""
                self.vs[7]["MT_subtypes__"] = []
                self.vs[7]["MT_dirty__"] = False
                self.vs[7]["mm__"] = """MT_pre__directLink_T"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc7')
        # apply association SwCompToEcuMapping_component--componentPrototype-->ComponentPrototype node
                self.add_node()
                self.vs[8]["MT_subtypeMatching__"] = False
                self.vs[8]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "componentPrototype"
"""
                self.vs[8]["MT_label__"] = """9"""
                self.vs[8]["MT_subtypes__"] = []
                self.vs[8]["MT_dirty__"] = False
                self.vs[8]["mm__"] = """MT_pre__directLink_T"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc8')
        
                # Nodes that represent trace relations


        
        
        
        
        
                # Add the edges
                self.add_edges([
                (0,5), # apply_class System() -> association mapping
                (5,1), # association mapping  -> apply_class SystemMapping()
                (1,6), # apply_class SystemMapping() -> association swMapping
                (6,2), # association swMapping  -> apply_class SwcToEcuMapping()
                (2,7), # apply_class SwcToEcuMapping() -> association component
                (7,4), # association component  -> apply_class SwCompToEcuMapping_component()
                (4,8), # apply_class SwCompToEcuMapping_component() -> association componentPrototype
                (8,3), # association componentPrototype  -> apply_class ComponentPrototype()
                ])
        
                # Add the attribute equations
                self["equations"] = [((0,'pivot'),('constant','SYSTEM')), ((3,'pivot'),('constant','COMPONENTPROTOTYPE')), ]
        
        
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

                return attr_value == "mapping"


        def eval_attr17(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "swMapping"


        def eval_attr18(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "component"


        def eval_attr19(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "componentPrototype"


        
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

