from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HSimpleAssignmentInstance_UniqueAssignment_CompleteLHS(HimesisPreConditionPatternLHS):
        def __init__(self):
                """
                Creates the himesis graph representing the AToM3 model HSimpleAssignmentInstance_UniqueAssignment_CompleteLHS.
                """
                # Flag this instance as compiled now
                self.is_compiled = True

                super(HSimpleAssignmentInstance_UniqueAssignment_CompleteLHS, self).__init__(name='HSimpleAssignmentInstance_UniqueAssignment_CompleteLHS', num_nodes=0, edges=[])

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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'SimpleAssignmentInstance_UniqueAssignment')
        
                # Nodes that represent match classes
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
        
        
        #Nodes that represent apply classes
        # match class GenericDotExpression() node
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
                self.vs[2]["mm__"] = """MT_pre__GenericDotExpression"""
                self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GlobalVariableDeclaration() node
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
                self.vs[3]["mm__"] = """MT_pre__GlobalVariableDeclaration"""
                self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GenericMemberRef() node
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
                self.vs[4]["mm__"] = """MT_pre__GenericMemberRef"""
                self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class GlobalVarRef() node
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
                self.vs[5]["mm__"] = """MT_pre__GlobalVarRef"""
                self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class AssignmentExpr() node
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
                self.vs[6]["mm__"] = """MT_pre__AssignmentExpr"""
                self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StructDeclaration() node
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
                self.vs[7]["mm__"] = """MT_pre__StructDeclaration"""
                self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class Member() node
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
                self.vs[8]["mm__"] = """MT_pre__Member"""
                self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class TypeDefType() node
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
                self.vs[9]["mm__"] = """MT_pre__TypeDefType"""
                self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class TypeDef() node
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

return True
"""
                self.vs[10]["MT_label__"] = """11"""
                self.vs[10]["MT_subtypes__"] = []
                self.vs[10]["MT_dirty__"] = False
                self.vs[10]["mm__"] = """MT_pre__TypeDef"""
                self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        # match class StructType() node
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

return True
"""
                self.vs[11]["MT_label__"] = """12"""
                self.vs[11]["MT_subtypes__"] = []
                self.vs[11]["MT_dirty__"] = False
                self.vs[11]["mm__"] = """MT_pre__StructType"""
                self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'')
        
                
        # Nodes that represent the match associations of the property.
        # match association AssemblyConnector--source-->InstancePortRef node
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

return attr_value == "source"
"""
                self.vs[12]["MT_label__"] = """13"""
                self.vs[12]["MT_subtypes__"] = []
                self.vs[12]["MT_dirty__"] = False
                self.vs[12]["mm__"] = """MT_pre__directLink_S"""
                self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc12')
        
        
        # Nodes that represent the apply associations of the property.
        # apply association AssignmentExpr--left-->GenericDotExpression node
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

return attr_value == "left"
"""
                self.vs[13]["MT_label__"] = """14"""
                self.vs[13]["MT_subtypes__"] = []
                self.vs[13]["MT_dirty__"] = False
                self.vs[13]["mm__"] = """MT_pre__directLink_T"""
                self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc13')
        # apply association GenericDotExpression--expression-->GlobalVarRef node
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

return attr_value == "expression"
"""
                self.vs[14]["MT_label__"] = """15"""
                self.vs[14]["MT_subtypes__"] = []
                self.vs[14]["MT_dirty__"] = False
                self.vs[14]["mm__"] = """MT_pre__directLink_T"""
                self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc14')
        # apply association GenericDotExpression--target-->GenericMemberRef node
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

return attr_value == "target"
"""
                self.vs[15]["MT_label__"] = """16"""
                self.vs[15]["MT_subtypes__"] = []
                self.vs[15]["MT_dirty__"] = False
                self.vs[15]["mm__"] = """MT_pre__directLink_T"""
                self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc15')
        # apply association GlobalVarRef--var-->GlobalVariableDeclaration node
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

return attr_value == "var"
"""
                self.vs[16]["MT_label__"] = """17"""
                self.vs[16]["MT_subtypes__"] = []
                self.vs[16]["MT_dirty__"] = False
                self.vs[16]["mm__"] = """MT_pre__directLink_T"""
                self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc16')
        # apply association GenericMemberRef--member-->Member node
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

return attr_value == "member"
"""
                self.vs[17]["MT_label__"] = """18"""
                self.vs[17]["MT_subtypes__"] = []
                self.vs[17]["MT_dirty__"] = False
                self.vs[17]["mm__"] = """MT_pre__directLink_T"""
                self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc17')
        # apply association StructDeclaration--members-->Member node
                self.add_node()
                self.vs[18]["MT_subtypeMatching__"] = False
                self.vs[18]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "members"
"""
                self.vs[18]["MT_label__"] = """19"""
                self.vs[18]["MT_subtypes__"] = []
                self.vs[18]["MT_dirty__"] = False
                self.vs[18]["mm__"] = """MT_pre__directLink_T"""
                self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc18')
        # apply association GlobalVariableDeclaration--type-->TypeDefType node
                self.add_node()
                self.vs[19]["MT_subtypeMatching__"] = False
                self.vs[19]["MT_pre__attr1"] = """
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
                self.vs[19]["MT_label__"] = """20"""
                self.vs[19]["MT_subtypes__"] = []
                self.vs[19]["MT_dirty__"] = False
                self.vs[19]["mm__"] = """MT_pre__directLink_T"""
                self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc19')
        # apply association TypeDefType--typeDef-->TypeDef node
                self.add_node()
                self.vs[20]["MT_subtypeMatching__"] = False
                self.vs[20]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "typeDef"
"""
                self.vs[20]["MT_label__"] = """21"""
                self.vs[20]["MT_subtypes__"] = []
                self.vs[20]["MT_dirty__"] = False
                self.vs[20]["mm__"] = """MT_pre__directLink_T"""
                self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc20')
        # apply association TypeDef--original-->StructType node
                self.add_node()
                self.vs[21]["MT_subtypeMatching__"] = False
                self.vs[21]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "original"
"""
                self.vs[21]["MT_label__"] = """22"""
                self.vs[21]["MT_subtypes__"] = []
                self.vs[21]["MT_dirty__"] = False
                self.vs[21]["mm__"] = """MT_pre__directLink_T"""
                self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc21')
        # apply association StructType--struct-->StructDeclaration node
                self.add_node()
                self.vs[22]["MT_subtypeMatching__"] = False
                self.vs[22]["MT_pre__attr1"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "struct"
"""
                self.vs[22]["MT_label__"] = """23"""
                self.vs[22]["MT_subtypes__"] = []
                self.vs[22]["MT_dirty__"] = False
                self.vs[22]["mm__"] = """MT_pre__directLink_T"""
                self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'assoc22')
        
                # Nodes that represent trace relations


        
        
        
        
        
                # Add the edges
                self.add_edges([
                (6,13), # apply_class AssignmentExpr() -> association left
                (13,2), # association left  -> apply_class GenericDotExpression()
                (2,14), # apply_class GenericDotExpression() -> association expression
                (14,5), # association expression  -> apply_class GlobalVarRef()
                (2,15), # apply_class GenericDotExpression() -> association target
                (15,4), # association target  -> apply_class GenericMemberRef()
                (5,16), # apply_class GlobalVarRef() -> association var
                (16,3), # association var  -> apply_class GlobalVariableDeclaration()
                (4,17), # apply_class GenericMemberRef() -> association member
                (17,8), # association member  -> apply_class Member()
                (7,18), # apply_class StructDeclaration() -> association members
                (18,8), # association members  -> apply_class Member()
                (3,19), # apply_class GlobalVariableDeclaration() -> association type
                (19,9), # association type  -> apply_class TypeDefType()
                (9,20), # apply_class TypeDefType() -> association typeDef
                (20,10), # association typeDef  -> apply_class TypeDef()
                (10,21), # apply_class TypeDef() -> association original
                (21,11), # association original  -> apply_class StructType()
                (11,22), # apply_class StructType() -> association struct
                (22,7), # association struct  -> apply_class StructDeclaration()
                (0,12), # match_class AssemblyConnector() -> association source
                (12,1) # association source  -> match_class InstancePortRef()
                ])
        
                # Add the attribute equations
                self["equations"] = [((3,'name'),('concat',(('wildcard'),('constant','__instance')))), ((7,'name'),('concat',(('wildcard'),('constant','__cdata')))), ((8,'name'),('concat',(('wildcard'),('constant','__ops')))), ]
        
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
        
        
        def eval_attr113(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "source"


        
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

                return True
        
        def eval_attr112(self, attr_value, this):

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

                return attr_value == "left"


        def eval_attr115(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "expression"


        def eval_attr116(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "target"


        def eval_attr117(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "var"


        def eval_attr118(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "member"


        def eval_attr119(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "members"


        def eval_attr120(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "type"


        def eval_attr121(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "typeDef"


        def eval_attr122(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "original"


        def eval_attr123(self, attr_value, this):

                        #===============================================================================
                        # This code is executed when evaluating if a node shall be matched by this rule.
                        # You can access the value of the current node's attribute value by: attr_value.
                        # You can access any attribute x of this node by: this['x'].
                        # If the constraint relies on attribute values from other nodes,
                        # use the LHS/NAC constraint instead.
                        # The given constraint must evaluate to a boolean expression.
                        #===============================================================================

                return attr_value == "struct"


        
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

