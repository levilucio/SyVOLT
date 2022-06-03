from core.himesis import Himesis, HimesisPreConditionPatternLHS
import uuid

class HM1_if_IsolatedLHS(HimesisPreConditionPatternLHS):
        def __init__(self, *args, **kwargs):
                """
        Creates the himesis graph representing the AToM3 model HM1_if_IsolatedLHS.
                """
        # Flag this instance as compiled now
                self.is_compiled = True
        
                super(HM1_if_IsolatedLHS, self).__init__(name='HM1_if_IsolatedLHS', num_nodes=0, edges=[])
        
        # Add the edges
                self.add_edges([])
        
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
                self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'M1_if')
        
        # Set the node attributes
        
        
                # Add the attribute equations
                self["equations"] = []    
        
        
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
        
        
