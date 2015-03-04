import cPickle as pickle
import gzip
import os
import sys
import collections


from himesis_utils import shrink_graph, expand_graph

class PCDict(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.dict = {}

    def __getitem__(self, key):
        try:
            return self.cache[key]
        except KeyError:
            value = expand_graph(self.dict[key])

            self.__setitem__(key, value)
            return value

    def __setitem__(self, key, value):
        self.cache[key] = value

        if len(self.cache) > self.capacity:

            (key, value) = self.cache.popitem(last=False)

            small_value = shrink_graph(value)
            self.dict[key] = small_value