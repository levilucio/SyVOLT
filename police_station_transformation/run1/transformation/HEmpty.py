

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HEmpty(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HEmpty.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEmpty, self).__init__(name='HEmpty', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
.""")
        self["name"] = """empty"""
        self["GUID__"] = UUID('e4bbc6ca-64f7-4a89-b2f2-07856b586581')
        
        # Set the node attributes

