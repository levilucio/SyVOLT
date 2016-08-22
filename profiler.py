#profile memory
global global_profile_memory
global global_memory_tracker

global_profile_memory = False

#create the tracker object
global_memory_tracker = None

try:
    from pympler import tracker, asizeof
except ImportError:
    global_profile_memory = False

# try:
#     from memory_profiler import profile
# except ImportError:
#     pass

if global_profile_memory:
    pass
    # try:
    #     from guppy import hpy
    #     global_hp = hpy()
    # except ImportError:
    #     global_profile_memory = False

#
    #import pympler

#
    # try:
    #     from memory_profiler import profile
    # except ImportError:
    #     global_profile_memory = False


#set up cProfile
#and the do_cprofile wrapper
try:
    import cProfile as pp
except (ImportError, AttributeError):
    import profile as pp



try:

    from StringIO import StringIO
except ImportError:
    from io import StringIO

from random import randint

import pstats
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = pp.Profile()
        try:
            # if global_profile_memory:
            # #     global_hp.setref()
            #     global_memory_tracker = tracker.SummaryTracker()
            profile.enable()

            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:


            print("\nFunction: " + str(func.__name__))

            if global_profile_memory and global_memory_tracker:
                global_memory_tracker.print_diff()

            # if global_profile_memory:
            #     h = global_hp.heap()
            #     print("\nMemory usage:")
            #     print(h)
            #
            #     print("\nBy id:")
            #     print(h.byid)
            #     print(h.byvia)
            #     print(h.byrcs)
            #     print(h.referents)
            #
            #     print("\nreferents[0]:")
            #     print(h.referents[0].byid)
            #     print(h.referents[0].byvia)
            #     print(h.referents[0].byrcs)
            #     print(h.referents[0].referents)

            s = StringIO()
            sortby = 'time'
            ps = pstats.Stats(profile, stream = s).sort_stats(sortby)
            ps.print_stats()

            print("Time usage:")
            time_table = str(s.getvalue()).split("\n")
            for i in range(25):
                if i >= len(time_table):
                    break

                if time_table[i].strip() == "":
                    continue

                print(time_table[i])




            print("")
    return profiled_func

class Profiler(object):

    profiler = None
    function_name = ""
    f = None

    @classmethod
    def get_profiler(cls):
        return Profiler.profiler

    def __init__(self, f):
        Profiler.profiler = pp.Profile()
        Profiler.f = f

    def func(self, *args, **kwargs):

        Profiler.profiler.enable()
        if global_profile_memory:
            global_hp.setref()

        result = Profiler.f(*args, **kwargs)
        Profiler.function_name = str(Profiler.f.__name__)
        Profiler.profiler.disable()

        # if randint(0, self.freq) == 0:
        #     self.print_profiler(function_name)
        return result


    @classmethod
    def print_profiler(self):

        if Profiler.function_name == "":
            return
        
        print("\nFunction: " + Profiler.function_name)

        if global_profile_memory:
            h = global_hp.heap()
            print("\nMemory usage:")
            print(h)

            print("\nBy id:")
            print(h.byid)
            print(h.byvia)
            print(h.byrcs)
            print(h.referents)

            print("\nreferents[0]:")
            print(h.referents[0].byid)
            print(h.referents[0].byvia)
            print(h.referents[0].byrcs)
            print(h.referents[0].referents)

        s = StringIO()
        sortby = 'time'
        ps = pstats.Stats(Profiler.profiler, stream = s).sort_stats(sortby)
        ps.print_stats()

        print("Time usage:")
        time_table = str(s.getvalue()).split("\n")
        for i in range(25):
            if i >= len(time_table):
                break

            if time_table[i].strip() == "":
                continue

            print(time_table[i])

        print("")


class Profiler1(Profiler):

    def __call__(self, *args, **kwargs):
        result = super(Profiler1, self).func(*args, **kwargs)
        return result

class Profiler2(Profiler):

    def __call__(self, *args, **kwargs):
        return super(Profiler2, self).func
