import os
import sys
import time

class PySolver:

    def __init__(self):

        #mapping from graphs to their equations
        #fills up as graphs are seen
        self.graph_eq_map = {}


    # function to dynamically load a new class
    import importlib

    def load_class(self, full_class_string):
        directory, module_name = os.path.split(full_class_string)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, directory)

        try:
            module = __import__(module_name)
            loaded_module = {module_name: getattr(module, module_name)()}
        finally:
            sys.path[:] = path  # restore
        return loaded_module


    #find the node numbers for the children of this node
    #TODO: Make faster
    # Use caching or find children for multiple nodes at once
    def find_children(self, node_num, graph):
        children = []
        for e in graph.es:
            if str(node_num) == str(e.source):
                children.append(e.target)
        return children

    #find the node numbers of the parents of this node
    #TODO: Use a dictionary to make faster
    def find_parents(self, node_num, graph):
        parents = []
        for e in graph.es:
            if str(node_num) == str(e.target):
                parents.append(e.source)
        return parents


    #get the node that is connected to this attribute node
    #for example, a node of type Name that is used in an equation
    #structure is: Node -> hasAttribute[_S|_T] -> Attribute
    #very annoying and slow to find
    def get_attrib(self, attribute_node, graph):
        parents = self.find_parents(attribute_node, graph)
        assert len(parents) == 2, "Wrong number of parents"

        #find the hasAttribute node by the metamodel
        hasAttribute_node = None
        for p in parents:
            if graph.vs[p]["mm__"].startswith("hasAttribute"):
                hasAttribute_node = p
                break

        assert hasAttribute_node is not None, "Could not find hasAttribute node"

        has_attrib_parents = self.find_parents(hasAttribute_node, graph)
        assert len(has_attrib_parents) == 1, "Wrong number of parents"
        return has_attrib_parents[0]


    #return a structure that represents the equations in this graph
    def find_equations(self, graph):

        #store for each node in the graph the associated equations
        self.graph_eq_map[graph] = {}

        #find equation nodes
        for i in range(len(graph.vs)):
            node = graph.vs[i]

            #only find the equations in the graph
            if node["mm__"] == "Equation":

                #get the children of the equations
                children = self.find_children(i, graph)

                #get the left and right expressions of the equation
                left_expr = None
                right_expr = None
                for c in children:
                    if graph.vs[c]["mm__"] == "leftExpr":
                        left_expr = c
                    elif graph.vs[c]["mm__"] == "rightExpr":
                        right_expr = c

                #find the children nodes
                left_children = self.find_children(left_expr, graph)
                right_children = self.find_children(right_expr, graph)

                #there should only be one child for these nodes
                if len(left_children) != 1 or len(right_children) != 1 :
                    raise Exception("Error: 0 or more than 1 children for left and right expression")

                #get the actual child
                left_child = left_children[0]
                right_child = right_children[0]

                #if the children are attributes, find the attached node
                left_attrib = None
                right_attrib = None
                if graph.vs[left_child]["mm__"] == "Attribute":
                    left_attrib = self.get_attrib(left_child, graph)

                if graph.vs[right_child]["mm__"] == "Attribute":
                    right_attrib = self.get_attrib(right_child, graph)

                #create the equation object
                eq = [left_child, left_attrib, right_child, right_attrib, graph]

                try:
                    self.graph_eq_map[graph][left_attrib].append(eq)
                except KeyError:
                    self.graph_eq_map[graph][left_attrib] = [eq]

    #get eqs for each attribute
    def get_attrib_map(self, eqs):
        attrib_map = {}
        for eq in eqs:

            #break apart the equation
            left_expr, left_attrib, right_expr, right_attrib, graph = eq
            assert graph.vs[left_expr]["mm__"] == "Attribute", "Left expr is not an Attribute"

            #add to map using the attribute name
            attrib_name = graph.vs[left_expr]["name"]

            try:
                attrib_map[attrib_name].append([right_expr, graph])
            except KeyError:
                attrib_map[attrib_name] = [[right_expr, graph]]
        return attrib_map


    #try to resolve two graphs
    #can also specify two nodes
    def attempt_resolve(self, a_graph, b_graph, a_node = None, b_node = None):
        resolve_type = "graphs"

        if a_node is not None and b_node is not None:
            resolve_type = "nodes"

        print("\nAttempting to resolve two " + resolve_type)

        start_time = time.clock()

        # check to see if the graphs have already been processed
        if a_graph not in self.graph_eq_map.keys():
            self.find_equations(a_graph)

        #get the equations from the map
        a_eqs = self.graph_eq_map[a_graph]

        if b_graph not in self.graph_eq_map.keys():
            self.find_equations(b_graph)

        b_eqs = self.graph_eq_map[b_graph]

        #get the node num of the node
        a_node_num = None
        b_node_num = None
        if a_node is not None:
            a_node_num = self.find_num_of_node(a_node, a_graph)
        if b_node is not None:
            b_node_num = self.find_num_of_node(b_node, b_graph)


        #put all the equations into one array
        #narrow the equations down to specific nodes if desired

        all_eqs = []
        for node_num in a_eqs.keys():
            if a_node_num is not None and node_num != a_node_num:
                continue
            eq = a_eqs[node_num]
            all_eqs = all_eqs + eq

        for node_num in b_eqs.keys():
            if b_node_num is not None and node_num != b_node_num:
                continue
            eq = b_eqs[node_num]
            all_eqs = all_eqs + eq

        #go through the eqs, and pull out the ones that belong to each attrib
        attrib_map = self.get_attrib_map(all_eqs)


        can_resolve = True

        #for each attrib, see if it can be resolved
        for attrib in attrib_map.keys():
            eqs = attrib_map[attrib]

            if len(eqs) == 1:
                #print("No conflict on node: " + str(attrib))
                continue

            #do the resolve check
            can_resolve = self.can_resolve_attrib(attrib, eqs)

            if not can_resolve:
                break

        end_time = time.clock()

        print("Resolving two " + resolve_type + " took " + str((end_time - start_time) * 1000) + " ms.")

        assert can_resolve, "Can't resolve these equations"

    #find out what number the node has in the himesis graph
    def find_num_of_node(self, node, graph):
        num = -1
        for i in range(len(graph.vs)):
            #TODO: Find best way of matching node
            if node == graph.vs[i]:
                num = i
                break

        assert num != -1, "Could not find node in graph"
        return num

    #see if this attrib name can be resolved using these RHS values
    def can_resolve_attrib(self, attrib, values):

        #store the values from each RHS in this array
        stored_values = []

        #the value_node is the num of the RHS node in the eq, in this graph
        for value_node, graph in values:

            #get the actual node
            node = graph.vs[value_node]

            #store the constant value as a strign
            if node["mm__"] == "Constant":
                value = node["name"]
                stored_values.append(value)

            #store the result of the concat operation
            elif node["mm__"] == "Concat":
                concat_children = self.find_children(value_node, graph)

                concat_left = self.find_children(concat_children[0], graph)[0]
                concat_right = self.find_children(concat_children[1], graph)[0]

                left_value = graph.vs[concat_left]["name"]
                right_value = graph.vs[concat_right]["name"]

                stored_values.append(left_value + right_value)

            #look up the attached node
            #and store which attrib is asked for
            elif node["mm__"] == "Attribute":
                attrib_name = node["name"]

                attrib_node = self.get_attrib(value_node, graph)

                stored_values.append(attrib_name + "@" + graph.vs[attrib_node]["name"])

            #else, something needs to be added
            else:
                print("Error on attrib: " + str(attrib))
                print("Error on values: " + str(values))
                raise Exception("Cannot get value from node class: " + node["mm__"])

        #print out the values from the RHS
        print("RHS values: " + str(stored_values))

        #Uses set to see if there is a common value
        if len(set(stored_values)) > 1:
            print("Error: Different values")
            print("Attrib: " + attrib)
            print("Stored values: " + str(stored_values))

            #TODO: Uncomment to make this code work
            #return False

        return True


#do a brute-force test of the methods
if __name__ == "__main__":

    directory = "UMLRT2Kiltera_MM/transformation/Himesis/"

    graphs = []

    pysolver = PySolver()

    for f in os.listdir(directory):
        if f.startswith("__") or f.endswith(".pyc") or f.startswith("."):
            continue
        rule = pysolver.load_class(directory + "/" + f)

        rule_name = rule.keys()[0]
        rule_graph = rule[rule.keys()[0]]

        graphs.append(rule_graph)


    #print("Length: " + str(len(graphs)))

    for i in range(len(graphs)):
        a_graph = graphs[i]
        for j in range(i+1, len(graphs)):
            b_graph = graphs[j]
            #print("A Name:" + str(a_graph["name"]))
            #print("B Name:" + str(b_graph["name"]))
            pysolver.attempt_resolve(a_graph, b_graph)

            for a_node in a_graph.vs:
                for b_node in b_graph.vs:
                    pysolver.attempt_resolve(a_graph, b_graph, a_node, b_node)

