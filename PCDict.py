import random
import cPickle as pickle
import gzip
import os
import sys

from himesis_utils import shrink_graph, expand_graph

class PCDict(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dict = {}

    def __getitem__(self, key):
        try:
            return self.cache[key]
        except KeyError:
            small_value = self.dict[key]
            value = expand_graph(small_value)
            return value

    def __setitem__(self, key, value):
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            random_key = random.choice(self.cache.keys())

            value = self.cache.pop(random_key)

            small_value = shrink_graph(value)
            self.dict[random_key] = small_value