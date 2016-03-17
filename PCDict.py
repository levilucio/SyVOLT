
import collections


from core.himesis_utils import shrink_graph, expand_graph

class PCDict(object):


    def __init__(self, d, capacity=100):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.pcdict = d

    def __getitem__(self, key):

        return self.pcdict[key]
        # try:
        #     return self.cache[key]
        # except KeyError:
        #     value = expand_graph(self.pcdict[key])
        #
        #     self.__setitem__(key, value)
        #     return value

    def __setitem__(self, key, value):
        self.pcdict[key] = value
        # self.cache[key] = value
        #
        # if len(self.cache) > self.capacity:
        #
        #     (key, value) = self.cache.popitem(last=False)
        #
        #     small_value = shrink_graph(value)
        #     self.pcdict[key] = small_value