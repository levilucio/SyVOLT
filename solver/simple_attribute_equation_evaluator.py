'''
Created on 2015-02-13

@author: levi
'''

from .attribute_equation_solver import AttributeEquationSolver


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


    def build_equation_expression(self, node, pathCondition):
        """
        helper for building the attribute equations by recursively going through the operations associated
        to the left hand side and to the right hand side of an equation
        """       
        # in case it's an attribute, return the object's ID
        if pathCondition.vs[node]['mm__'] == 'Attribute':
            # get the parent object of the attribute
            
            attrEdgeMatch = [i for i in pathCondition.neighbors(node,2) if pathCondition.vs[i]['mm__'] == 'hasAttribute_S']
            attrEdgeApply = [i for i in pathCondition.neighbors(node,2) if pathCondition.vs[i]['mm__'] == 'hasAttribute_T'] 
            if attrEdgeMatch != []:
                parentObject = pathCondition.neighbors(attrEdgeMatch[0],2)[0]
            else:
                parentObject = pathCondition.neighbors(attrEdgeApply[0],2)[0]

            # check if a variable for an attribute having the same name and belonging to the same object has already been created  
            # and in case it has just return it, otherwise create a new variable
            
            attrName = pathCondition.vs[node]['name']         
            varDatabaseKey = str(parentObject) + "_" + attrName
            if not varDatabaseKey in set(self.varNameDatabase.keys()): 
                self.varNameDatabase[varDatabaseKey] = "X" + str(node)
                return (self.varNameDatabase[varDatabaseKey], self.isVariable)
            else:
                return (self.varNameDatabase[varDatabaseKey], self.isVariable)
                

        # in case it's a constant, return its value
        elif pathCondition.vs[node]['mm__'] == 'Constant':
            return (pathCondition.vs[node]['name'], self.isConstant)

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
        
        # grab all the equation nodes in the path condition
        equationNodes = self._find_nodes_with_mm(pathCondition, "Equation")
        # now build all the equations
        if equationNodes != []:
            for equationNode in range(0,len(equationNodes)):
                # get the left and the right expressions of the equation
                leftExprEdge = [i for i in pathCondition.neighbors(equationNodes[equationNode],1) if pathCondition.vs[i]['mm__'] == 'leftExpr'][0]    
                rightExprEdge = [i for i in pathCondition.neighbors(equationNodes[equationNode],1) if pathCondition.vs[i]['mm__'] == 'rightExpr'][0]

                leftExprNode = pathCondition.neighbors(leftExprEdge,1)[0]
                rightExprNode = pathCondition.neighbors(rightExprEdge,1)[0]              

                leftExpr = self.build_equation_expression(leftExprNode, pathCondition)
                rightExpr = self.build_equation_expression(rightExprNode, pathCondition)

                if leftExpr == None or rightExpr == None or (leftExpr[1] == self.isVariable and rightExpr[1] == self.isVariable):
                    # got a concat operation, or both are variables, skipping the evaluation here
                    continue
                
                # otherwise we evaluate
                # look for the variable
                varInEquation = None
                valueInEquation = None
                if leftExpr[1] == self.isVariable:
                    varInEquation = leftExpr[0]
                    valueInEquation = rightExpr[0]
                else:
                    varInEquation = rightExpr[0]
                    valueInEquation = leftExpr[0]
                    
                if varInEquation in variableValues.keys():
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



        
    def _find_nodes_with_mm(self, graph, mm_names):
        """
        Find all objects of a given type in a rules having theur type name in the mm_names set.
        TODO: move this method to the himesis_utils file, together with the one from PyRamify 
        """
        nodes = []
        for node in graph.vs:
            if node["mm__"] in mm_names:
                nodes.append(node)
        return nodes
             