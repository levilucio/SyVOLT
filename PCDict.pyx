import cPickle as pickle
import gzip
import os
import sys
import collections


from core.himesis_utils import shrink_graph, expand_graph

cdef class PCDict(object):

    cdef public int capacity
    cdef public dict cache
    cdef public dict pcdict

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.pcdict = {}

    def __getitem__(self, char *key):
        try:
            return self.cache[key]
        except KeyError:
            value = expand_graph(self.pcdict[key])

            self.__setitem__(key, value)
            return value

    def __setitem__(self, char * key, object value):
        self.cache[key] = value

        if len(self.cache) > self.capacity:

            (key, value) = self.cache.popitem(last=False)

            small_value = shrink_graph(value)
            self.pcdict[key] = small_value