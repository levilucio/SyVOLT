
import collections


from core.himesis_utils import shrink_graph, expand_graph

class PCDict(object):


    def __init__(self, d, capacity=100):
        self.capacity = capacity
        self.get_cache = collections.OrderedDict()
        self.set_cache = collections.OrderedDict()
        self.pcdict = d

    def __getitem__(self, key):

        try:
            return self.get_cache[key]
        except KeyError:
            pass
        value = self.pcdict[key]

        if len(self.get_cache) > self.capacity:
            self.get_cache.popitem(last = False)

        self.get_cache[key] = value
        return value


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