'''
Created on 2013-01-21

@author: levi
'''

'''
Useful Himesis-related operations

'''


try:
    import pydot
    has_pydot = True
except ImportError:
    has_pydot = False

import subprocess
import re
import sys
import os
from os import path

import uuid
from profiler import *

#cross-compatibility
try:
    import cPickle as pickle
except ImportError:
    import pickle as pickle

import igraph
import time

from copy import deepcopy

from util.newsizeof import total_size


#used to check if a constraint has been left as default
#note that all whitespace is removed to increase accuracy
default_constraint = re.sub(r'\s+', '', """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].                    
# If the constraint relies on attribute values from other nodes,                
# use the LHS/NAC constraint instead.                                           
# The given constraint must evaluate to a boolean expression.                   
#===============================================================================
                                                                                
return True                                                                     
""")

def get_attribute(s, attr):
    #remove whitespace to check against the default_constraint
    if re.sub(r'\s+', '', str(attr)) == default_constraint:
        return ""
    elif str(attr) == "return True":
        return ""
    else:
        attribute = str(attr).splitlines()
        for a in attribute:
            a = a.strip()
            if a.startswith("#"):
                continue
            s += a
        return s

def graph_to_dot(name, g, verbosity = 0):
    """
    build a dot file from a himesis graph
    verbosity = 0, represent directLink, indirectLink, backward, etc. edges as just edges in the dot graph
    verbosity = 1, represent these edges as their own node
    """

    if not has_pydot:
        return

    if g is None:
        print("graph_to_dot Error: Empty graph")
        return 
        
    vattr=''
    nodes = {}
    graph = pydot.Dot(name, graph_type='digraph')

    try:
        mms = g.vs["mm__"]
    except KeyError:
        mms = []

    skip_trace_links = False
    if mms.count("trace_link") > 20:
        skip_trace_links = True

    internal_links = {}

    i = 0
    for v in g.vs:
    
        node_type = str(v['mm__'])
        
        vattr = node_type + str(i)
        i += 1
        
        try:
            label = str(v["MT_label__"])
            vattr += "\\n Label " + label
        except Exception:
            pass
        
        if node_type in ['paired_with', 'MT_pre__paired_with', 'MT_post__paired_with']:
            # try:
            #     vattr += "\\n Rule = " + str(v['rulename'])
            # except KeyError:
            #     pass
            # fillcolor="lightgray"

            internal_links[int(v.index)] = {}
            continue

            
        elif node_type in ['MatchModel', 'MT_pre__MatchModel', 'MT_post__MatchModel']:
            fillcolor="#E15C34"
            
        elif node_type in ['match_contains', 'MT_pre__match_contains', 'MT_post__match_contains']:
            #fillcolor="#F798A1"
            internal_links[int(v.index)] = {}
            continue
            
        elif node_type in ['ApplyModel', 'MT_pre__ApplyModel', 'MT_post__ApplyModel']:
            fillcolor="#FED017"
            
        elif node_type in ['apply_contains', 'MT_pre__apply_contains', 'MT_post__apply_contains']:
            #fillcolor="#FCDB58"
            internal_links[int(v.index)] = {}
            continue

        elif node_type in ['Equation', 'MT_pre__Equation', 'MT_post__Equation']:
            fillcolor = "#66FF33"


        elif node_type in ['leftExpr', 'MT_pre__leftExpr', 'MT_post__leftExpr', "rightExpr", "MT_pre__rightExpr", 'MT_post__rightExpr']:
            fillcolor = "#22DDFF"

        elif node_type in ['hasAttr_S', 'MT_pre__hasAttr_S', 'MT_post__hasAttr_S', "hasAttribute_S"]:
            fillcolor = "#E34A0E"

        elif node_type in ['hasAttr_T', 'MT_pre__hasAttr_T', 'MT_post__hasAttr_T'] or "hasAttribute" in node_type:
            fillcolor = "#C75C0D"

        elif node_type in ['Attribute', 'MT_pre__Attribute', 'MT_post__Attribute']:
            try:
                vattr += "\\n Name = " + str(v['name'])
            except KeyError:
                pass

            fillcolor = "#FFCC00"

        elif "hasArgs" in node_type:
            fillcolor = "#FFFF99"

        elif "Concat" in node_type:
            fillcolor = "#9999FF"

        elif "Constant" in node_type:
            try:
                vattr += "\\n Name = " + str(v['name'])
            except KeyError:
                pass
            
            fillcolor = "#FF99FF"
            
        elif node_type in ['directLink_S', 'directLink_T', 'MT_pre__directLink_T', 'MT_pre__directLink_S', 'MT_post__directLink_T', 'MT_post__directLink_S']:

            #vattr += '\\n'
            if node_type in ['directLink_S', 'directLink_T']:
                try:
                    vattr += "\\naType = " + str(v['attr1'])
                except Exception:
                    pass

            elif node_type in ['MT_pre__directLink_T', 'MT_pre__directLink_S']:
                try:
                    code_str = re.sub('"', '', v['MT_pre__attr1'])
                    vattr += get_attribute("\\naType = ", code_str)
                except KeyError:
                    pass
                
            fillcolor="lightyellow"  
                       
        elif node_type in ['indirectLink_S', 'indirectLink_T', 'MT_pre__indirectLink_S', 'MT_pre__indirectLink_T', 'MT_post__indirectLink_S', 'MT_post__indirectLink_T']:
            fillcolor="lightgreen"
            try:
                vattr += "\\n Classtype = " + str(v['attr1'])
            except Exception:
                pass

                 
        elif node_type in ['backward_link', "MT_pre__backward_link", "MT_post__backward_link"]:
            fillcolor="coral"
            internal_links[int(v.index)] = {}
            continue
            
        elif node_type in ['trace_link', 'MT_pre__trace_link', 'MT_post__trace_link']:
            fillcolor="lightgoldenrod"
            internal_links[int(v.index)] = {}
            continue
              
        else:

            try:
              vattr += get_attribute("\\nPivotIn = ", v['MT_pivotIn__'])
            except Exception:
                pass

            try:
                vattr += get_attribute("\\nPivotOut = ", v['MT_pivotOut__'])
            except Exception:
                pass
                
            fillcolor="lightblue"

            #vattr += "\\n" + str(v['GUID__'])

        nodes[v.index] = pydot.Node(vattr, style="filled", fillcolor=fillcolor)
        graph.add_node(nodes[v.index])
        
    try:
        eqs = g["equations"]
        eq_str = g.name + "\\nEquations\\n"
        for eq in eqs:
            eq_str += str(eq) + "\\n"
        graph.add_node(pydot.Node(eq_str, style="filled", fillcolor='lightblue'))

    except KeyError:
        print("No equations on " + g.name)

    link_colours = {"paired_with": "#505050", "match_contains": "#6E2229", "apply_contains": "#938344",
                    "trace_link": "darkgoldenrod", "backward_link": "#B9512B"}

    for e in g.es:

        src = int(e.source)
        trgt = int(e.target)

        if src in internal_links.keys():
            internal_links[src]["target"] = trgt
            continue
        elif trgt in internal_links.keys():
            internal_links[trgt]["source"] = src
            continue

        else:

            color = "black"
            if "MatchModel" in mms[src]:
                color = link_colours["match_contains"]
            elif "ApplyModel" in mms[src]:
                color = link_colours["apply_contains"]
            graph.add_edge(pydot.Edge(nodes[src],nodes[trgt], color = color))

    for link in internal_links.keys():
        mm = mms[link].replace("MT_pre__", "").replace("MT_post__", "")
        src = internal_links[link]["source"]
        trgt = internal_links[link]["target"]

        #print("MM: " + str(mm) + " Source: " + str(src) + " Target: " + str(trgt))


        color = link_colours[mm]
        label = mm
        arrowhead = "vee"
        penwidth = 1

        if mm == "trace_link" and skip_trace_links:
            continue

        if mm == "trace_link" or mm == "backward_link":
            temp = src
            src = trgt
            trgt = temp

            arrowhead="none"
            penwidth = 2

        try:
            s = nodes[src]
        except KeyError:
            s = "NoSource"

        try:
            t = nodes[trgt]
        except KeyError:
            t = "NoTarget"

        graph.add_edge(pydot.Edge(s, t, color=color, label=label, arrowhead=arrowhead, penwidth = penwidth))

    if len(name) > 250:
        replace_tokens = [
                          ["_", ""],["a", ""],["e", ""],["i", ""],
                          ["o", ""],["u", ""],["y", ""],["-", ""],
                          ["0", ""], ["1", ""], ["2", ""]]

        for rt, rp in replace_tokens:
            #if len(name) < 240:
            #    break

            name = name.replace(rt, rp)

    name = name[:240]

    svg_filename = './dot/' + name + '.svg'


    try:
        graph.write_svg(svg_filename, prog = 'dot')

    except Exception as e:
        print("Error in graph_to_dot: " + str(e))
        #raise(e)

        dot_filename = svg_filename.replace(".svg", ".dot")
        graph.write(dot_filename, prog='dot')

        command = "dot -Tsvg " + dot_filename + " -o " + svg_filename
        subprocess.call(command, shell=True)

        command = "rm " + dot_filename
        subprocess.call(command, shell=True)


def draw_graphs(title, g_dir):
    for d in os.listdir(g_dir):
        if not os.path.isdir(g_dir + d):
            continue

        # ignore svn dirs
        if d.startswith('.'):
            continue

        graph_dir = g_dir + d + "/Himesis/"

        try:
            files = os.listdir(graph_dir)
        except OSError:
            print("Warning: " + graph_dir + " does not exist")
            files = []

        for f in files:
            if f == "__init__.py" or f.endswith(".pyc") or f.startswith("."):
                continue

            # print("Examining " + graph_dir + f)

            graph_file = graph_dir + f
            try:
                g = load_class(graph_file)
            except ImportError:
                print("ERROR " + graph_file)
                continue

            name = g.keys()[0]
            graph = g.values()[0]

            graph_to_dot(title +"_" + name, graph)


def get_preds_and_succs(graph):
    vcount = graph.vcount()
    preds = [[0, []] for i in range(vcount)]
    succs = [[0, []] for i in range(vcount)]

    for e in graph.es:
        source = e.source
        target = e.target
        preds[target][0] += 1
        preds[target][1].append(source)

        succs[source][0] += 1
        succs[source][1].append(target)

    return preds, succs


import gzip
import hashlib


def set_do_pickle(value):
    global do_pickle
    do_pickle = value

def set_compression(value):
    global compression
    compression = value

pickle_dir = "pickle/"

def delete_graph(graph_name):
    file_name = hashlib.md5(graph_name.encode("UTF-8")).hexdigest()
    file_name_as_int = str(int(file_name, 16))

    try:
        os.remove(pickle_dir + "/" + file_name_as_int)
    except FileNotFoundError:
        pass
        #print("Graph: " + graph_name + " did not exist")

# shrink a graph into an array
def shrink_graph(graph):
    value = graph.__reduce__()

    if do_pickle:
        file_name = hashlib.md5(graph.name.encode("UTF-8")).hexdigest()
        file_name_as_int = int(file_name, 16)

        #print("Saved " + graph.name + " as " + file_name_as_int)

        if compression == 0:
            f = open(pickle_dir + str(file_name_as_int), "wb")
        else:
            f = gzip.open(pickle_dir + str(file_name_as_int), "wb", compresslevel=compression)
        pickle.dump(value, f)
        f.close()
        return file_name_as_int
    else:
        return value


#expand the graph from an array
#@do_cprofile
def expand_graph(small_value):

    if do_pickle:
        if compression == 0:
            f = open(pickle_dir + str(small_value), "rb")
        else:
            f = gzip.open(pickle_dir + str(small_value), "rb")
        small_value = pickle.load(f)
        f.close()

    #igraph_dict = small_value

    #constructor = igraph_dict[0]
    #print(small_value)
    vcount, edgelist, is_directed, gattrs, vattrs, eattrs = small_value[1]


    do_old_expand = False
    if do_old_expand:



        graph = igraph.Graph(n=vcount, edges=edgelist, directed=is_directed, graph_attrs=gattrs, vertex_attrs=vattrs, edge_attrs=eattrs)
        graph.name = small_value[0]

        from .himesis import Himesis
        graph.__class__ = Himesis

    else:

        from .himesis import Himesis
        graph = Himesis.__new__(Himesis)
        graph.__class__ = Himesis

        igraph.GraphBase.__init__(graph, vcount, edgelist, is_directed)
        # Set the graph attributes
        for key, value in gattrs.items():
            graph[key] = value


        # Set the vertex attributes
        vs = graph.vs
        for key, value in vattrs.items():
            vs[key] = value

        graph.name = small_value[0]

        #assume no edge attributes


    #graph.name = name
    #print(graph.name)
    #graph.is_compiled = is_compiled


    return graph

def update_equation(part, node_mapping):
    if part[0] == 'constant':
        return deepcopy(part)
    elif part[0] == 'concat':

        left = update_equation(part[1][0], node_mapping)
        right = update_equation(part[1][1], node_mapping)
        return ('concat', (left, right))
    else:
        try:
            return node_mapping[part[0]], part[1]
        except KeyError:
            print("Could not update equation")
            print(part)
            print(node_mapping)

def update_equations(equations, node_mapping):
    new_eqs = []
    #print("Initial equations: " + str(equations))
    for eq in equations:
        LHS = update_equation(eq[0], node_mapping)
        RHS = update_equation(eq[1], node_mapping)
        new_eqs.append((LHS, RHS))

    #print("After equations: " + str(new_eqs))
    return new_eqs

#@do_cprofile
def disjoint_model_union(first, second):
    """
    merge two himesis graphs
    """

    nb_nodes_first = first.vcount()
    nb_nodes_second = second.vcount()

    if nb_nodes_first == 0:
        return second.copy()
    
    if nb_nodes_second == 0:
        return first.copy()

    node_num_mapping = {}

    first.add_vertices(nb_nodes_second)

    # first copy the nodes
    attrib_names = second.vs[0].attribute_names()
    for index_v in range(nb_nodes_second):

        new_node_index = index_v + nb_nodes_first

        new_node = first.vs[new_node_index]

        node_num_mapping[index_v] = new_node_index

        for attrib in attrib_names:

            #skip None attribs
            if second.vs[index_v][attrib] is not None:
                #copy the other attribs
                new_node[attrib] = second.vs[index_v][attrib]
 
    # then copy the edges
    # for index_e in second.edge_iter():
    #    first.add_edges([(nb_nodes_first + second.es[index_e].tuple[0],nb_nodes_first + second.es[index_e].tuple[1])])


    edges = [(nb_nodes_first + e.source, nb_nodes_first + e.target) for e in second.es]
    first.add_edges(edges)

    first["equations"] += update_equations(second["equations"], node_num_mapping)


    return first

def standardize_name(name):
    """
        Converts the given name into a standard Himesis name.
        @param name: The name of the Himesis graph
    """
    if name.startswith('H'):
        return name
    return 'H%s%s' % (name[0].capitalize(), name[1:])

def is_RAM_attribute(attr_name):
    return (attr_name.startswith('MT_pre__')
            or attr_name.startswith('MT_post__'))

def to_non_RAM_attribute(attr_name):
    if attr_name.startswith('MT_pre__'):
        return attr_name[8:]
    elif attr_name.startswith('MT_post__'):
        return attr_name[9:]
    else:
        return attr_name

def clean_graph(graph):
    #shrink the size of the uuids into ints
    if isinstance(graph["GUID__"], uuid.UUID):
        # get the uuid as an int
        #and fit it in 24 bytes
        uuid_int = graph["GUID__"].int
        uuid_int %= 9223372036854775806

        #have to do this to get in into 24 bytes
        graph["GUID__"] = int(str(uuid_int))

    for i in range(graph.vcount()):
        node = graph.vs[i]
        if isinstance(node["GUID__"], uuid.UUID):
            uuid_int = node["GUID__"].int
            uuid_int %= 9223372036854775806
            node["GUID__"] = int(str(uuid_int))

    return graph


def build_traceability(graph, add_label = False):
    #print("Building traceability for: " + graph.name)
    #graph_to_dot("building_trace_" + graph.name, graph)

    vs = graph.vs
    mms = vs["mm__"]

    match_nodes = []
    apply_nodes = []

    match_in_linked = []
    apply_in_linked = []

    has_contains = "match_contains" in mms

    for e in graph.es:
        source = e.source
        target = e.target

        if has_contains:
            if mms[source] == "match_contains":
                match_nodes.append(target)
            elif mms[source] == "apply_contains":
                apply_nodes.append(target)
        else:
            if mms[source] == "MatchModel" and mms[target] != "paired_with":
                match_nodes.append(target)
            elif mms[source] == "ApplyModel" and mms[target] != "paired_with":
                apply_nodes.append(target)

        if mms[source] in ["backward_link", "trace_link"]:
            match_in_linked.append([source, target])
        elif mms[target] in ["backward_link", "trace_link"]:
            apply_in_linked.append([target, source])

    for match in match_nodes:
        for apply in apply_nodes:

            has_link = False
            for apply_back_link, apply_element in apply_in_linked:

                if has_link:
                    break

                #if this apply node has a backward link
                if apply == apply_element:

                    for match_back_link, match_element in match_in_linked:

                        #if this match node has a backward link
                        #and its the same backward link
                        if match == match_element and match_back_link == apply_back_link:
                            has_link = True
                            break

            #there's a backward or trace link, so ignore this match/apply element pair
            if has_link:
                continue

            #print("Building link: " + str(match) + " to " + str(apply))
            node_count = len(vs)
            graph.add_node()

            graph.vs[node_count]["mm__"] = """trace_link"""

            if add_label:
                graph.vs[node_count]["MT_label__"] = str(node_count)

            # Add the edges
            graph.add_edges([
                (apply, node_count),  # apply_element -> trace_link
                (node_count, match), ]) # trace_link -> match_element

    #graph_to_dot("built_trace_" + graph.name, graph)
    return graph


#function to dynamically load a new class

try:
    import importlib
except ImportError:
    pass

from time import sleep
def load_class(full_class_string, args = None):

    directory, module_name = os.path.split(full_class_string)
    module_name = os.path.splitext(module_name)[0]

    old_path = list(sys.path)
    sys.path.insert(0, directory)

    # sometimes the file is still being written,
    # so wait for a bit
    if not path.isfile(full_class_string):
        sleep(0.001)

    succeed = True
    try:
        module = __import__(module_name)
        if args is None:
            loaded_class = getattr(module, module_name)()
        else:
            loaded_class = getattr(module, module_name)(args[0])

        clean_graph(loaded_class)

        loaded_module = {module_name : loaded_class}

    except Exception as e:
        print("Error: " + str(e))
        succeed = False
        loaded_module = None
    finally:
        sys.path[:] = old_path # restore

    if not succeed:

        print("File: " + full_class_string)
        print("Exists: " + str(path.isfile(full_class_string)))
        raise Exception("Could not load module: " + module_name)

    return loaded_module

def load_directory(directory):
    class_dict = {}

    try:
        files = os.listdir(directory)
    except OSError:
        print("Warning: " + directory + " does not exist")
        files = []

    for f in sorted(files):

        if not f.endswith(".py") or f.startswith("__"):
            continue

        file_name = directory + "/" + f

        c = load_class(file_name)

        class_dict.update(c)

    return class_dict


def print_file(file_name):
    graph = load_class(file_name)
    print_graph(graph.values()[0])

def print_GUIDs(graph):
    print("GUIDs of graph nodes:")
    for n in range(len(graph.vs)):
        node = graph.vs[n]
        print(str(n) + " : " + node["mm__"] + " : " + str(node["GUID__"]) )


def print_graph(graph):
    """
    pretty print a Himesis graph
    """
    # first print the nodes
    print('Name: ' + graph.name)
    #print("MM: " + str(graph["mm__"]))

    #try:
    #    print("MT_constraint__" + str(graph["MT_constraint__"]))
    #except Exception:
    #    pass

    print('Nodes: ')
    nodes = {}
    node_num_mapping = {}

    i = 0
    for v in graph.vs:
        nodes[v["mm__"]] = v
        #print(v["mm__"])
        node_num_mapping[i] = v["mm__"]
        i += 1

    print("Num of nodes: " + str(len(nodes.keys())))
    for v in sorted(nodes.keys()):
        print(v)

    # then print the edges
    print('\nEdges: ')
    print("Num of edges: " + str(len(graph.get_edgelist())))
    #for e in graph.get_edgelist():
    #    print("Edge: " + str(e))
    edges = []
    for e in graph.get_edgelist():
        n1 = node_num_mapping[e[0]]
        n2 = node_num_mapping[e[1]]
        edges.append(n1 + " -> " + n2)

    for e in edges:
        print(e)

    print_all = False
    if print_all == True:
        print("\nNode details:")
        for v in sorted(nodes.keys()):
            n = nodes[v]
            print(n["mm__"])

            for a in sorted(n.attributes()):
                if a == "GUID__":
                    continue
                print("\t" + a + ": " + str(n[a]))

def main(argv = None):
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print("Need arguments of one Himesis file")
        return

    print_file(argv[1])

if __name__ == "__main__":
    main()
