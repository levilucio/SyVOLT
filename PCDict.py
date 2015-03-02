import random
import cPickle as pickle
import gzip
import os
import sys

from himesis_utils import load_class

class PCDict(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dict = {}

    def __getitem__(self, key):
        try:
            return self.cache[key]
        except KeyError:
            fname = self.dict[key]
            #print("Was pickled " + fname)

            value = load_class(fname)
            value = value.values()[0]
            # f = gzip.open(fname, 'rb')
            # value = pickle.load(f)
            # f.close()
            return value

    def __setitem__(self, key, value):
        self.cache[key] = value
        fname = "pickle/" + key
        self.dict[key] = fname

        if len(self.cache) > self.capacity:
            #print("Pop something out")
            random_key = random.choice(self.cache.keys())
            #random_key = self.cache.keys()[1]

            value = self.cache.pop(random_key)
            fdir = "pickle/"

            try:
                value.compile(fdir)
            except IOError:
                self.cache[key] = value
            # f = gzip.open(fname, 'wb')
            # pickle.dump(value, f)
            # f.close()

    # function to dynamically load a new class
    import importlib

    def load_class(self, full_class_string, args = None):
        directory, module_name = os.path.split(full_class_string)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, directory)

        try:
            module = __import__(module_name)
            if args is None:
                loaded_class = getattr(module, module_name)()
            else:
                loaded_class = getattr(module, module_name)(args[0])

            loaded_module = {module_name: loaded_class}

        finally:
            sys.path[:] = path  # restore
        return loaded_module