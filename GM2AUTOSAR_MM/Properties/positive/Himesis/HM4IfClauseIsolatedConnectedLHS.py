

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HM4IfClauseIsolatedConnectedLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HM4IfClauseIsolatedConnectedLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HM4IfClauseIsolatedConnectedLHS, self).__init__(name='HM4IfClauseIsolatedConnectedLHS', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MoTifRule'
p2
a.""")
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
        self["name"] = """M4IfClauseIsolatedConnected"""
        self["GUID__"] = UUID('7db75145-2de3-4116-b0f1-ad6a7c873022')
        
        # Set the node attributes

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

