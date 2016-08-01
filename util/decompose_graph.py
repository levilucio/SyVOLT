
from core.himesis_plus import look_for_attached, get_all_attached
from core.himesis_utils import graph_to_dot
from copy import deepcopy
from profiler import *

try:
    from functools import lru_cache
except ImportError:
    print("Warning: Could not import lru_cache")
    def lru_cache(maxsize=32):
        def true_decorator(f):
            return f
        return true_decorator

#@do_cprofile
#@Profiler
@lru_cache(maxsize=1024)
#@profile
def decompose_graph(graph, verbosity = 0, ignore_apply_dls = False, isolated_if_attached_backward = False):
    #decompose graph into directLinks, backwardLinks, and isolated elements

    debug = False

    #debug = "Hlayer1rule10" in graph.name

    if debug:
        print("\nDecomposing graph: " + graph.name)
        #graph_to_dot(graph.name, graph)

    match_elements = []
    #isolated_match_elements = []
    apply_elements = []


    try:
        mms = graph.vs["mm__"]
        if mms[0].startswith("MT_pre__"):
            mms = [mm[8:] for mm in mms]
    except KeyError:
        mms = []
        
    vcount = len(mms)

    # only get the match direct links
    if ignore_apply_dls:
        dls = [i for i in range(vcount) if mms[i] == "directLink_S"]
    else:
        dls = [i for i in range(vcount) if mms[i] in ["directLink_S", "directLink_T"]]

    bls = [i for i in range(vcount) if mms[i] in ["trace_link", "backward_link"]]

    direct_links_dict = {n: [None, None] for n in dls}
    backward_links_dict = {n: [None, None] for n in bls}

    # direct_links_dict = {}
    # for n in dls:
    #     direct_links_dict[n] = [None, None]
    #
    # backward_links_dict = {}
    # for n in bls:
    #     backward_links_dict[n] = [None, None]

    has_contains = "match_contains" in mms

    for e in graph.es:
        source = e.source
        target = e.target

        if source in bls:
            backward_links_dict[source][1] = target
            continue
        elif target in bls:
            backward_links_dict[target][0] = source
            continue

        if source in dls:
            direct_links_dict[source][1] = target
            continue
        elif target in dls:
            direct_links_dict[target][0] = source
            continue


        source_mm = mms[source]
        target_mm = mms[target]

        if not has_contains:
            if source_mm == "MatchModel" and target_mm != "paired_with":
                match_elements.append(target)
            elif source_mm == "ApplyModel" and target_mm != "paired_with":
                apply_elements.append(target)
        else:
            if source_mm == "match_contains":
                match_elements.append(target)
            elif source_mm == "apply_contains":
                apply_elements.append(target)



    direct_links = [[val[0], val[1], dl] for dl, val in direct_links_dict.items()]

    if debug:
        print("Direct links: ")
        for n0, n1, nlink in direct_links:
            print_link(graph, n0, n1, nlink)

    backward_links = [[val[0], val[1], bl] for bl, val in backward_links_dict.items()]

    if debug:
        print("Backward links: ")
        for n0, n1, nlink in backward_links:
            print_link(graph, n0, n1, nlink)



    # for matchers, there might not be a match model
    if "MatchModel" not in mms:
        link_mms = ["directLink_S", "directLink_T", "backward_link", "trace_link"]
        match_elements = [i for i in range(len(mms)) if mms[i] not in link_mms]

    # find the non-isolated elements
    isolated_match_elements = []
    links = list.copy(direct_links)

    if not isolated_if_attached_backward:
        links += backward_links
    for me in match_elements:
        isolated = True
        for dl in links:
            if me == dl[0] or me == dl[1]:
                isolated = False
                break
        if isolated:
            isolated_match_elements.append(me)

    if debug:
        print("\nRule name: " + graph.name)
        print("Match contains: " + str(match_elements))
        print("Isolated match elements: " + str(isolated_match_elements))
        print("Apply contains: " + str(apply_elements))

        graph_to_dot(graph.name, graph)
        #raise Exception()

    data = {"direct_links" : direct_links, "backward_links" : backward_links, "match_elements" : match_elements, "isolated_match_elements" : isolated_match_elements, "apply_elements" : apply_elements}
    return data


