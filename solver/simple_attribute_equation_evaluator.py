'''
Created on 2015-02-13

@author: levi
'''

from .attribute_equation_solver import AttributeEquationSolver
from core.himesis_plus import find_nodes_with_mm

def is_consistent(graph, verbosity=0):


    eqs = graph["equations"]

    if not eqs:
        return True

    duplicates = []
    var_dict = {}

    if verbosity >= 2:
        print("\nis_consistent:")
        for eq in eqs:
            print(eq)

    i = -1
    for eq in eqs:
        node = eq[0][0]
        attr = eq[0][1]

        if attr == "pivot" or "ApplyAttribute" in attr:
            continue
            
        value = eq[1]

        i += 1

        if node not in var_dict:
            var_dict[node] = {attr : value}
            continue

        if attr not in var_dict[node]:
            var_dict[node][attr] = value
            continue

        #keep track of duplicates to remove
        duplicates.append(i)
        # print("Duplicate attr: " + attr + " " + str(value))

        if value != var_dict[node][attr]:
            if verbosity >= 2:
                print("Inconsistent values for " + str(eq[0]) + ": " + str(value) + " vs " + str(var_dict[node][attr]))
            return False



    #remove all duplicates
    new_eqs = [eqs[i] for i in range(len(eqs)) if i not in duplicates]
    if verbosity >= 2:
        print("New eqs: ")
        for eq in new_eqs:
            print(eq)
    graph["equations"] = new_eqs
    return True

class SimpleAttributeEquationEvaluator(AttributeEquationSolver):
    """
    Simple constraint solver based on python for string equations in path conditions.
    Checks for inconsistencies between values for the same attribute of an object in a path condition.
    Only looks at conditions for the match graph of a rule, i.e. elements from the match model or elements from the apply model connected to backward links.
    Does not take into consideration string concatenations during the evaluation. 
    """
        
    # We need to keep in a database a single variable names in for all attributes having the same
    # name and connected to the same object. This is necessary because an object may have connected
    # to it more than one attribute with the same name, which means the attribute has multiple
    # constraints for that object.
    
    varNameDatabase = {}

    # a couple of constants to make to code more readable    
    isVariable = True
    isConstant = False

    
    def __init__(self, verbosity):
        self.verbosity = verbosity

    
    def newVarID(self):
        old_varID = self.varID
        self.varID += 1   
        return "V" + str(old_varID) 


    def can_match(self, graph, condition):
        #see if the condition's equations match over this graph (and its equations)
        return True

    def combine_equations(self, graph, condition):

        #combine the equations from the graph with the equations
        #from the rewriter's LHS and RHS
        pass

    def is_consistent(self, graph):
        #see if the equations for this graph are internally consistent
        pass




    #@profile
    def build_equation_expression(self, node, pathCondition):
        """
        helper for building the attribute equations by recursively going through the operations associated
        to the left hand side and to the right hand side of an equation
        """

        graph_node = pathCondition.vs[node]

        # in case it's an attribute, return the object's ID
        if graph_node['mm__'] == 'Attribute':
            # get the parent object of the attribute


            attrEdgeMatch = [i for i in self.pred[node] if self.mms[i] == 'hasAttribute_S']
            attrEdgeApply = [i for i in self.pred[node] if self.mms[i] == 'hasAttribute_T']


            if attrEdgeMatch:
                parentObject = self.pred[attrEdgeMatch[0]][0]
            else:
                parentObject = self.pred[attrEdgeApply[0]][0]

            # check if a variable for an attribute having the same name and belonging to the same object has already been created  
            # and in case it has just return it, otherwise create a new variable
            
            attrName = graph_node['name']
            varDatabaseKey = str(parentObject) + "_" + attrName

            try:
                return (self.varNameDatabase[varDatabaseKey], self.isVariable)
            except KeyError:
                self.varNameDatabase[varDatabaseKey] = "X" + str(node)
                return ("X" + str(node), self.isVariable)
                

        # in case it's a constant, return its value
        elif graph_node['mm__'] == 'Constant':
            return (graph_node['name'], self.isConstant)

        # it's a concat operation
        else:
            # for the time being  we do not evaluate concat operations
            return None
#             # get the arguments of the concat operation
#             arg1Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'hasArgs'][0]    
#             arg2Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'hasArgs'][1]
#             arg1 = pathCondition.neighbors(arg1Edge,1)[0]
#             arg2 = pathCondition.neighbors(arg2Edge,1)[0]
#             newVar = self.newVarID()
#  
#             # add the concat operation to the set of append predicates in the body of the rule 
#             concatsInExpression.append("append(" + self.build_equation_expression(arg1, pathCondition, variablesInExpression, concatsInExpression, varParentObjects) + "," + self.build_equation_expression(arg2, pathCondition, variablesInExpression, concatsInExpression, varParentObjects) + "," + newVar + ")")
#             
#             # return the newly created variable
#             return newVar


    def __call__(self, pathCondition):
        """
        Evaluates attribute equations by producing a Prolog predicate out of them and attempting to find a solution for that predicate.
        The predicate has as arguments the attributes of the path condition for which a solution needs to exist such that the path condition is possible.
        If a solution is found then the evaluator returns true, otherwise false.
        """

        variableValues = {}

        #get all mms for the path condition at once
        self.mms = pathCondition.vs["mm__"]







        # grab all the equation node numbers in the path condition
        equationNodes = []
        i = 0
        for mm in self.mms:
            if mm == "Equation":
                equationNodes.append(i)
            i += 1

        # now build all the equations
        if not equationNodes:
            return True


        #store the first successor for Equation, leftExpr, and rightExpr
        #store the first predecessor for Attributes and hasAttribute_[S,T]
        #igraph.IN = 2, igraph.OUT = 1
        self.succ = {}
        self.pred = {}

        for edge in pathCondition.get_edgelist():
            if self.mms[edge[0]] in ["Equation", "leftExpr", "rightExpr"]:
                try:
                    self.succ[edge[0]].append(edge[1])
                except KeyError:
                    self.succ[edge[0]] = [edge[1]]

            if self.mms[edge[1]] in ["Attribute", "hasAttribute_S", "hasAttribute_T"]:
                try:
                    self.pred[edge[1]].append(edge[0])
                except KeyError:
                    self.pred[edge[1]] = [edge[0]]



        for equationNode in equationNodes:
            # get the left and the right expressions of the equation
            #[i for i in pathCondition.neighbors(equationNode,1) if self.mms[i] == 'leftExpr'][0]

            mm = self.mms[self.succ[equationNode][0]]
            if mm == 'leftExpr':
                leftExprEdge = self.succ[equationNode][0]
                rightExprEdge = self.succ[equationNode][1]
            else:
                leftExprEdge = self.succ[equationNode][1]
                rightExprEdge = self.succ[equationNode][0]


            #rightExprEdge = [i for i in pathCondition.neighbors(equationNode,1) if self.mms[i] == 'rightExpr'][0]

            leftExprNode = self.succ[leftExprEdge][0] #pathCondition.neighbors(leftExprEdge,1)[0]
            rightExprNode = self.succ[rightExprEdge][0] #pathCondition.neighbors(rightExprEdge,1)[0]

            leftExpr = self.build_equation_expression(leftExprNode, pathCondition)
            rightExpr = self.build_equation_expression(rightExprNode, pathCondition)

            if leftExpr == None or rightExpr == None or (leftExpr[1] == self.isVariable and rightExpr[1] == self.isVariable):
                # got a concat operation, or both are variables, skipping the evaluation here
                continue

            # otherwise we evaluate
            # look for the variable
            if leftExpr[1] == self.isVariable:
                varInEquation = leftExpr[0]
                valueInEquation = rightExpr[0]
            else:
                varInEquation = rightExpr[0]
                valueInEquation = leftExpr[0]

            if varInEquation in variableValues:
                if variableValues[varInEquation] != valueInEquation:
                    # evaluation has failed, two different values were found for the same attribute
                    if self.verbosity >= 2:
                        objectAttrName = [item[0] for item in self.varNameDatabase.items() if item[1] == varInEquation][0]
                        splitObjectAttrName = objectAttrName.split('_')
                        print("Python solver check failed! Object " + splitObjectAttrName[0] + " has values " + "'" + \
                        variableValues[varInEquation] + "'" + " and " + "'" + valueInEquation + "'")

                    return False
            else:
                # otherwise add the value to variableValues dictionary for future comparisons
                variableValues[varInEquation] = valueInEquation


        # no contradictions were found, check succeeded  
        if self.verbosity >= 2 : print("Python check succeeded!")
        return True
