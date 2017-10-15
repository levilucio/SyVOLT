'''
Created on 2017-02-10

@author: bentley
'''

from t_core.messages import Packet
from t_core.matcher import Matcher

from PropertyVerification.contract import Contract

from core.himesis_utils import graph_to_dot
from core.himesis_plus import look_for_attached

from core.match_algo import HimesisMatcher

from copy import deepcopy



class EmptyContract(Contract):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''

        super(EmptyContract, self).__init__()

        self.__name__ = "EmptyContract"

        self.isolated = None
        self.connected = None
        self.complete = None

        self.isolated_matcher = None
        self.connected_matcher = None
        self.complete_matcher = None

        self.name = "EmptyContract"

        self.last_packet = None

        self.verbosity = 0

        self.contract_mms = []


    def to_string(self):
        return self.name

    def get_graph(self):
        return [self.complete]

    def get_complete(self):
        return self.complete

    def draw(self):
        pass

    def has_pivots(self):
        return False

    def get_pivots(self):
        return {}

    def check_isolated(self, pc):
        return self.ISOLATED

    def check(self, pc, verbosity=0):
        return self.COMPLETE_FOUND
