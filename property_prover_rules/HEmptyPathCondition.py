

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HEmptyPathCondition(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEmptyPathCondition.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEmptyPathCondition, self).__init__(name='HEmptyPathCondition', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
.""")
        self["name"] = """EmptyPathCondition"""
        self["GUID__"] = UUID('680ca2cf-04c0-48ec-904a-be75541a077f')
        
        # Set the node attributes

