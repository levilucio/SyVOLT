

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HCommunityPerson2_IsolatedLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HCommunityPerson2_IsolatedLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCommunityPerson2_IsolatedLHS, self).__init__(name='HCommunityPerson2_IsolatedLHS', num_nodes=0, edges=[])
        
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
        self["name"] = """communityPerson2_Isolated"""
        self["GUID__"] = UUID('dd48df30-c83f-401b-a1f9-437ffa6fdcb5')
        
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

