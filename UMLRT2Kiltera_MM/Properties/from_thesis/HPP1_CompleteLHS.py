from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HPP1_CompleteLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HPP1_CompleteLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True

                super(HPP1_CompleteLHS, self).__init__(name='HPP1_CompleteLHS', num_nodes=0, edges=[])

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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'PP1')
        
                # Nodes that represent match classes
                # match class SIBLING0() node
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
                self.vs[0]["mm__"] = """MT_pre__SIBLING0"""
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
        
        
        #Nodes that represent apply classes
        # match class ListenBranch() node
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
                self.vs[4]["mm__"] = """MT_pre__ListenBranch"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Inst() node
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

return True
"""
                self.vs[5]["MT_label__"] = """6"""
                self.vs[5]["MT_subtypes__"] = []
                self.vs[5]["MT_dirty__"] = False
                self.vs[5]["mm__"] = """MT_pre__Inst"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Name() node
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

return True
"""
                self.vs[6]["MT_label__"] = """7"""
                self.vs[6]["MT_subtypes__"] = []
                self.vs[6]["MT_dirty__"] = False
                self.vs[6]["mm__"] = """MT_pre__Name"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Name() node
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

return True
"""
                self.vs[7]["MT_label__"] = """8"""
                self.vs[7]["MT_subtypes__"] = []
                self.vs[7]["MT_dirty__"] = False
                self.vs[7]["mm__"] = """MT_pre__Name"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Name() node
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

return True
"""
                self.vs[8]["MT_label__"] = """9"""
                self.vs[8]["MT_subtypes__"] = []
                self.vs[8]["MT_dirty__"] = False
                self.vs[8]["mm__"] = """MT_pre__Name"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Name() node
                self.add_node()
                self.vs[9]["MT_subtypeMatching__"] = False
                self.vs[9]["MT_pre__attr1"] = """
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
                self.vs[9]["MT_label__"] = """10"""
                self.vs[9]["MT_subtypes__"] = []
                self.vs[9]["MT_dirty__"] = False
                self.vs[9]["mm__"] = """MT_pre__Name"""
                self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
                
        # Nodes that represent the match associations of the property.
        # match association Transition--type-->SIBLING0 node
                self.add_node()
                self.vs[10]["MT_subtypeMatching__"] = False
                self.vs[10]["MT_pre__attr1"] = """
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
                self.vs[10]["MT_label__"] = """11"""
                self.vs[10]["MT_subtypes__"] = []
                self.vs[10]["MT_dirty__"] = False
                self.vs[10]["mm__"] = """MT_pre__directLink_S"""
                self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc10')
        # match association Transition--triggers-->Trigger node
                self.add_node()
                self.vs[11]["MT_subtypeMatching__"] = False
                self.vs[11]["MT_pre__attr1"] = """
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
                self.vs[11]["MT_label__"] = """12"""
                self.vs[11]["MT_subtypes__"] = []
                self.vs[11]["MT_dirty__"] = False
                self.vs[11]["mm__"] = """MT_pre__directLink_S"""
                self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc11')
        # match association Trigger--signal-->Signal node
                self.add_node()
                self.vs[12]["MT_subtypeMatching__"] = False
                self.vs[12]["MT_pre__attr1"] = """
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
                self.vs[12]["MT_label__"] = """13"""
                self.vs[12]["MT_subtypes__"] = []
                self.vs[12]["MT_dirty__"] = False
                self.vs[12]["mm__"] = """MT_pre__directLink_S"""
                self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
        
        # Nodes that represent the apply associations of the property.
        # apply association ListenBranch--p-->Inst node
                self.add_node()
                self.vs[13]["MT_subtypeMatching__"] = False
                self.vs[13]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "p"
"""
                self.vs[13]["MT_label__"] = """14"""
                self.vs[13]["MT_subtypes__"] = []
                self.vs[13]["MT_dirty__"] = False
                self.vs[13]["mm__"] = """MT_pre__directLink_T"""
                self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc13')
        # apply association Inst--channelNames-->Name node
                self.add_node()
                self.vs[14]["MT_subtypeMatching__"] = False
                self.vs[14]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "channelNames"
"""
                self.vs[14]["MT_label__"] = """15"""
                self.vs[14]["MT_subtypes__"] = []
                self.vs[14]["MT_dirty__"] = False
                self.vs[14]["mm__"] = """MT_pre__directLink_T"""
                self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc14')
        # apply association Inst--channelNames-->Name node
                self.add_node()
                self.vs[15]["MT_subtypeMatching__"] = False
                self.vs[15]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "channelNames"
"""
                self.vs[15]["MT_label__"] = """16"""
                self.vs[15]["MT_subtypes__"] = []
                self.vs[15]["MT_dirty__"] = False
                self.vs[15]["mm__"] = """MT_pre__directLink_T"""
                self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        # apply association Inst--channelNames-->Name node
                self.add_node()
                self.vs[16]["MT_subtypeMatching__"] = False
                self.vs[16]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "channelNames"
"""
                self.vs[16]["MT_label__"] = """17"""
                self.vs[16]["MT_subtypes__"] = []
                self.vs[16]["MT_dirty__"] = False
                self.vs[16]["mm__"] = """MT_pre__directLink_T"""
                self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc16')
        # apply association Inst--channelNames-->Name node
                self.add_node()
                self.vs[17]["MT_subtypeMatching__"] = False
                self.vs[17]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "channelNames"
"""
                self.vs[17]["MT_label__"] = """18"""
                self.vs[17]["MT_subtypes__"] = []
                self.vs[17]["MT_dirty__"] = False
                self.vs[17]["mm__"] = """MT_pre__directLink_T"""
                self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
        
                # Nodes that represent trace relations
                # backward association Transition---->Inst node
                self.add_node()
                self.vs[18]["MT_subtypeMatching__"] = False
                self.vs[18]["MT_label__"] = """19"""
                self.vs[18]["MT_subtypes__"] = []
                self.vs[18]["MT_dirty__"] = False
                self.vs[18]["mm__"] = """MT_pre__trace_link"""
                self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'blink18')


        
        
        
        
        
                # Add the edges
                self.add_edges([
                (5,18), # apply_class Inst() -> backward_association
                (18,1), #  backward_association -> apply_class Transition()
                (4,13), # apply_class ListenBranch() -> association p
                (13,5), # association p  -> apply_class Inst()
                (5,14), # apply_class Inst() -> association channelNames
                (14,6), # association channelNames  -> apply_class Name()
                (5,15), # apply_class Inst() -> association channelNames
                (15,7), # association channelNames  -> apply_class Name()
                (5,16), # apply_class Inst() -> association channelNames
                (16,9), # association channelNames  -> apply_class Name()
                (5,17), # apply_class Inst() -> association channelNames
                (17,8), # association channelNames  -> apply_class Name()
                (1,10), # match_class Transition() -> association type
                (10,0), # association type  -> match_class SIBLING0()
                (1,11), # match_class Transition() -> association triggers
                (11,2), # association triggers  -> match_class Trigger()
                (2,12), # match_class Trigger() -> association signal
                (12,3) # association signal  -> match_class Signal()
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
        
        
        def eval_attr111(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "type"


        def eval_attr112(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "triggers"


        def eval_attr113(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "signal"


        
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

                return True
        
        def eval_attr114(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "p"


        def eval_attr115(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "channelNames"


        def eval_attr116(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "channelNames"


        def eval_attr117(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "channelNames"


        def eval_attr118(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "channelNames"


        
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

