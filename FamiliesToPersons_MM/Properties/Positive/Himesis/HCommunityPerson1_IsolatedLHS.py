

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HCommunityPerson1_IsolatedLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HCommunityPerson1_IsolatedLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCommunityPerson1_IsolatedLHS, self).__init__(name='HCommunityPerson1_IsolatedLHS', num_nodes=0, edges=[])
        
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
        self["name"] = """"""
        self["GUID__"] = UUID('bbb0ae2f-e5c2-4776-9bf1-965069e77dbc')
        
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

