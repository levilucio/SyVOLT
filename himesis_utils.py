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
    verbosity = 0, no traceability in the dot graph
    verbosity = 1, traceability in the dot graph
    """
    
    if g == None:
        print("graph_to_dot Error: Empty graph")
        return 
        
    vattr=''
    nodes = {}
    graph = pydot.Dot(name, graph_type='digraph')
    #print("graph_to_dot: " + str(g))
    
    #print("===================================================\n")
    i = 0
    for v in g.vs:
        #print(v)
        #print("============\n")
    
        node_type = str(v['mm__'])
        node_GUID = str(v['GUID__'])[-12:]
        
        vattr += node_type + str(i)
        i += 1
        #vattr += node_GUID
        
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

        elif node_type in ['hasAttr_T', 'MT_pre__hasAttr_T', 'MT_post__hasAttr_T']:
            fillcolor = "#FF6666"

        elif node_type in ['Attribute', 'MT_pre__Attribute', 'MT_post__Attribute']:
            fillcolor = "#FFCC00"
            
        elif node_type in ['directLink_S', 'directLink_T', 'MT_pre__directLink_T', 'MT_pre__directLink_S', 'MT_post__directLink_T', 'MT_post__directLink_S']:
            
            vattr += '\\n'     
            if node_type in ['directLink_S', 'directLink_T']:
                #vattr += "Association Type = " + str(v['associationType'])
                pass
            elif node_type in ['MT_pre__directLink_T', 'MT_pre__directLink_S']:
                try:
                    vattr += get_attribute("\\n Association Type = ", v['MT_pre__associationType'])
                except KeyError:
                    pass
                
            fillcolor="lightyellow"  
                       
        elif node_type in ['indirectLink_S', 'indirectLink_T', 'MT_pre__indirectLink_S', 'MT_pre__indirectLink_T', 'MT_post__indirectLink_S', 'MT_post__indirectLink_T']:
            fillcolor="lightgreen"          
                 
        elif node_type in ['backward_link', "MT_pre__backward_link", "MT_post__backward_link"]:
            fillcolor="coral" 
            
        elif node_type in ['trace_link', 'MT_pre__trace_link', 'MT_post__trace_link']:
            fillcolor="lightgoldenrod"
            #if  verbosity == 1:
              #  nodes[v.index] = pydot.Node(vattr, style="filled", fillcolor="chocolate")
              
              
        else:
            try:
                vattr += "\\n Classtype = " + str(v['classtype'])
            except Exception:
                pass
                
            try:
                vattr += "\\n Name = " + str(v['name'])
            except Exception:
                pass
                
            try:
                vattr += get_attribute("\\n Classtype = ", v['MT_pre__classtype'])
            except Exception:
                pass
                
            try:
                vattr += get_attribute("\\n Name = ", v['MT_pre__name'])
            except Exception:
                pass
                
            fillcolor="lightblue"
                
        nodes[v.index] = pydot.Node(vattr, style="filled", fillcolor=fillcolor)
        graph.add_node(nodes[v.index])  
        
        vattr = ''
        
        
        
        
    for e in g.es:
        # if verbosity == 0:
        #     if g.vs[e.source]['mm__'] != 'trace_link' and g.vs[e.target]['mm__'] != 'trace_link':
        #         graph.add_edge(pydot.Edge(nodes[e.source],nodes[e.target]))
        # else:
        graph.add_edge(pydot.Edge(nodes[e.source],nodes[e.target]))

    dot_filename = './dot/' + name + '.dot'
    #print("Wrote to file: " + dot_filename)
    graph.write(dot_filename)
    
    command = "dot -Tsvg " + dot_filename + " -o " + dot_filename.replace(".dot", ".svg")
    #print(command)
    subprocess.call(command, shell=True)
#    graph.write('/home/gehan/OutputDotFiles/%s.dot'%name)    

    
def disjoint_model_union(first, second):
    """
    merge two himesis graphs
    IMPORTANT: only makes sense if the graphs are instances of the same metamodel
    """
    
    if first.vcount() == 0:
        return deepcopy(second)
    
    if second.vcount() == 0:
        return deepcopy(first)
 
    nr_attr_first = len(first.vs[0].attribute_names())
    nr_attr_second = len(second.vs[0].attribute_names())
     
    # graphs need to be swapped in case the nodes in the second graph have more attributes than the ones in the first
    # this is so because each node in a model has the maximum amount of attributes used in the model
     
    if nr_attr_second > nr_attr_first:
        swapbuffer = deepcopy(second)
        second = deepcopy(first)
        first = swapbuffer
 
    # get the list of attributes to copy from the second graph but don't copy the GUIDs because they are newly created        
    attribute_names = [attr for attr in second.vs[0].attribute_names() if attr != 'GUID__']
    nb_nodes_first = len(first.vs)
     
    # first copy the nodes
    for index_v in range(len(second.vs)):
        first.add_node()
        for attr_name in attribute_names:
            first.vs[nb_nodes_first + index_v][attr_name] = second.vs[index_v][attr_name]
 
    # then copy the edges
    for index_e in range(len(second.es)):
        first.add_edges([(nb_nodes_first + second.es[index_e].tuple[0],nb_nodes_first + second.es[index_e].tuple[1])])
  
    return first


#function to dynamically load a new class
import importlib
def load_class(full_class_string):
    directory, module_name = os.path.split(full_class_string)
    module_name = os.path.splitext(module_name)[0]

    path = list(sys.path)
    sys.path.insert(0, directory)

    try:
        module = __import__(module_name)
    finally:
        sys.path[:] = path # restore
    return {module_name : getattr(module, module_name)()}


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
