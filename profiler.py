#profile memory
global global_profile_memory
global global_hp

global_profile_memory= False

if global_profile_memory:

    #import heapy
    from guppy import hpy

    #create the heapy object
    global_hp = hpy()


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

import pstats
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = pp.Profile()
        try:
            profile.enable()
            if global_profile_memory:
                global_hp.setref()

            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:


            print("\nFunction: " + str(func.__name__))

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