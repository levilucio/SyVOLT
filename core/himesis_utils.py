'''
Created on 2013-01-21

@author: levi
'''

'''
Useful Himesis-related operations

'''


import pydot
import subprocess
import re
import sys
import os
import uuid
import cPickle as pickle
import igraph


from copy import deepcopy


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
        return s + str(attr)

def graph_to_dot(name, g, verbosity = 0):
    """
    build a dot file from a himesis graph
    verbosity = 0, represent directLink, indirectLink, backward, etc. edges as just edges in the dot graph
    verbosity = 1, represent these edges as their own node
    """
    
    if g == None:
        print("graph_to_dot Error: Empty graph")
        return 
        
    vattr=''
    nodes = {}
    graph = pydot.Dot(name, graph_type='digraph')

    i = 0
    for v in g.vs:
    
        node_type = str(v['mm__'])
        node_GUID = str(v['GUID__'])[-12:]
        
        vattr += node_type + str(i)
        i += 1
        
        try:
            label = str(v["MT_label__"])
            vattr += "\\n Label " + label
        except Exception:
            pass
                
        fillcolor = "lightblue"
        
        if node_type in ['paired_with', 'MT_pre__paired_with', 'MT_post__paired_with']:
            fillcolor="lightgray"
            
        elif node_type in ['MatchModel', 'MT_pre__MatchModel', 'MT_post__MatchModel']:
            fillcolor="#E15C34"
            
        elif node_type in ['match_contains', 'MT_pre__match_contains', 'MT_post__match_contains']:
            fillcolor="#F798A1" 
            
        elif node_type in ['ApplyModel', 'MT_pre__ApplyModel', 'MT_post__ApplyModel']:
            fillcolor="#FED017"  
            
        elif node_type in ['apply_contains', 'MT_pre__apply_contains', 'MT_post__apply_contains']:
            fillcolor="#FCDB58"

        elif node_type in ['Equation', 'MT_pre__Equation', 'MT_post__Equation']:
            fillcolor = "#66FF33"


        elif node_type in ['leftExpr', 'MT_pre__leftExpr', 'MT_post__leftExpr', "rightExpr", "MT_pre__rightExpr", 'MT_post__rightExpr']:
            fillcolor = "#22DDFF"

        elif node_type in ['hasAttr_S', 'MT_pre__hasAttr_S', 'MT_post__hasAttr_S']:
            fillcolor = "#FF8888"

        elif node_type in ['hasAttr_T', 'MT_pre__hasAttr_T', 'MT_post__hasAttr_T'] or "hasAttribute" in node_type:
            fillcolor = "#FF9999"

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

            vattr += '\\n'
            if node_type in ['directLink_S', 'directLink_T']:
                vattr += "A_Type = " + str(v['associationType'])

            elif node_type in ['MT_pre__directLink_T', 'MT_pre__directLink_S']:
                try:
                    vattr += get_attribute("\\nA_Type = ", v['MT_pre__associationType'])
                except KeyError:
                    pass
                
            fillcolor="lightyellow"  
                       
        elif node_type in ['indirectLink_S', 'indirectLink_T', 'MT_pre__indirectLink_S', 'MT_pre__indirectLink_T', 'MT_post__indirectLink_S', 'MT_post__indirectLink_T']:
            fillcolor="lightgreen"
            try:
                vattr += "\\n Classtype = " + str(v['associationType'])
            except Exception:
                pass

                 
        elif node_type in ['backward_link', "MT_pre__backward_link", "MT_post__backward_link"]:
            fillcolor="coral" 
            
        elif node_type in ['trace_link', 'MT_pre__trace_link', 'MT_post__trace_link']:
            fillcolor="lightgoldenrod"
            #if  verbosity == 1:
              #  nodes[v.index] = pydot.Node(vattr, style="filled", fillcolor="chocolate")
              
              
        else:
            # try:
            #     vattr += "\\n Classtype = " + str(v['classtype'])
            # except Exception:
            #     pass
                
            # try:
            #     vattr += "\\n Name = " + str(v['name'])
            # except Exception:
            #     pass
                
            # try:
            #     vattr += get_attribute("\\n Classtype = ", v['MT_pre__classtype'])
            # except Exception:
            #     pass
            #
            # try:
            #     vattr += get_attribute("\\n Name = ", v['MT_pre__name'])
            # except Exception:
            #     pass

            try:
              vattr += get_attribute("\\nPivotIn = ", v['MT_pivotIn__'])
            except Exception:
                pass

            try:
                vattr += get_attribute("\\nPivotOut = ", v['MT_pivotOut__'])
            except Exception:
                pass
                
            fillcolor="lightblue"
                
        nodes[v.index] = pydot.Node(vattr, style="filled", fillcolor=fillcolor)
        graph.add_node(nodes[v.index])  
        
        vattr = ''
        
        
        
        
    for e in g.es:
        graph.add_edge(pydot.Edge(nodes[e.source],nodes[e.target]))

    dot_filename = './dot/' + name + '.dot'

    graph.write(dot_filename)
    
    command = "dot -Tsvg " + dot_filename + " -o " + dot_filename.replace(".dot", ".svg")
    subprocess.call(command, shell=True)

    command = "rm " + dot_filename
    subprocess.call(command, shell=True)


import gzip
use_pickle = False

# shrink a graph into an array
def shrink_graph(graph):
    value = graph.__reduce__()

    if use_pickle:
        fname = "pickle/" + graph.name
        f = gzip.open(fname, "wb")
        pickle.dump(value, f)
        f.close()
        return fname
    else:
        return value


#expand the graph from an array
def expand_graph(small_value):
    from himesis import Himesis

    if use_pickle:
        f = gzip.open(small_value, "rb")
        arr = pickle.load(f)
        f.close()
    else:
        arr = small_value

    igraph_dict, name, is_compiled = arr

    #constructor = igraph_dict[0]
    vcount, edgelist, is_directed, gattrs, vattrs, eattrs = igraph_dict[1]
    dict = igraph_dict[2]

    graph = igraph.Graph(n=vcount, edges=edgelist, directed=is_directed, graph_attrs=gattrs, vertex_attrs=vattrs, edge_attrs=eattrs)
    graph.__dict__ = dict


    graph.name = name
    graph.is_compiled = is_compiled

    graph.__class__ = Himesis

    return graph





def disjoint_model_union(first, second):
    """
    merge two himesis graphs
    """
    
    if first.vcount() == 0:
        return deepcopy(second)
    
    if second.vcount() == 0:
        return deepcopy(first)

    nb_nodes_first = first.vcount()
     
    # first copy the nodes
    for index_v in second.node_iter():
        new_node_index = first.add_node()
        new_node = first.vs[new_node_index]

        for attrib in second.vs[index_v].attribute_names():

            #skip copying the GUID
            if attrib == "GUID__":
                continue

            #skip None attribs
            if second.vs[index_v][attrib] is not None:
                #copy the other attribs
                new_node[attrib] = second.vs[index_v][attrib]

 
    # then copy the edges
    for index_e in second.edge_iter():
        first.add_edges([(nb_nodes_first + second.es[index_e].tuple[0],nb_nodes_first + second.es[index_e].tuple[1])])
  
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


#function to dynamically load a new class
import importlib
def load_class(full_class_string, args = None):
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

        clean_graph(loaded_class)

        loaded_module = {module_name : loaded_class}

    finally:
        sys.path[:] = path # restore
    return loaded_module


def print_file(file_name):
    graph = load_class(file_name)
    print_graph(graph.values()[0])

def print_graph(graph):
    """
    pretty print a Himesis graph
    """
    # first print the nodes
    print 'Name: ' + graph.name
    #print "MM: " + str(graph["mm__"])

    #try:
    #    print "MT_constraint__" + str(graph["MT_constraint__"])
    #except Exception:
    #    pass

    print 'Nodes: '
    nodes = {}
    node_num_mapping = {}

    i = 0
    for v in graph.vs:
        nodes[v["mm__"]] = v
        print(v["mm__"])
        node_num_mapping[i] = v["mm__"]
        i += 1

    print("Num of nodes: " + str(len(nodes.keys())))
    for v in sorted(nodes.keys()):
        print v

    # then print the edges
    print '\nEdges: '
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
