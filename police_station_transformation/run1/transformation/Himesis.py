

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class Himesis(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model Himesis.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Himesis, self).__init__(name='Himesis', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
.""")
        self["name"] = """"""
        self["GUID__"] = UUID('c4186d01-2fbe-4b9b-a597-faa7d8469cc9')
        
        # Set the node attributes

