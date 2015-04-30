from abc import ABCMeta, abstractmethod
from property import Property
# from atomic_state_property import AtomicStateProperty

from disambiguate import Disambiguator
from core.himesis_utils import disjoint_model_union
from copy import deepcopy
from core.himesis_utils import graph_to_dot
from t_core.messages import Packet
from t_core.matcher import Matcher

import time
import PropertyVerification


class PropertyVerifier(object):

    @staticmethod
    def verifyCompositeStateProperty(StateSpace, stateprop):

        for pc in StateSpace.get_path_conditions():

            print("PathCondition: " + pc.name)

            disamb = Disambiguator(0)  # (StateSpace.verbosity)
            disambiguated_states = disamb.disambiguate(pc)
            print("Disambiguated size: " + str(len(disambiguated_states)))


        return True