'''
Created on 2015-01-16

@author: levi
'''

from pyswip import Prolog

from attribute_equation_solver import AttributeEquationSolver


class PrologAttributeEquationEvaluator(AttributeEquationSolver):
    """
    Simple constraint solver based on prolog for string equations in path conditions.
    Requires pyswip, a bridge between python and prolog to be installed.
    For information on how to install pyswip see: https://code.google.com/p/pyswip/
    """
    
    varID = 0
    
    def __init__(self, verbosity):
        self.verbosity = verbosity

    
    def newVarID(self):
        return "V" + str(self.varID)
        self.varID += 1    

    
    def build_equation_expression(self, node, pathCondition, variablesInExpression, concatsInExpression):
        """
        helper for building the attribute equations by recursively going through the operations associated
        to the left hand side and to the right hand side of an equation
        """
        
        # in case it's an attribute, return the object's ID
        if pathCondition.vs[node]['mm__'] == 'Attribute':
            variablesInExpression.append("X" + str(node))
            return "X" + str(node)
        # in case it's a constant, return it's value as a list
        elif pathCondition.vs[node]['mm__'] == 'Constant':
            constant = pathCondition.vs[node]['value']
            constAsList = "["
            for c in range(0,len(constant)):
                constAsList += "'" + constant[c] + "'"
                if c < len(constant) - 1:
                    constAsList += ","
            constAsList += "]" 
            return constAsList
        # it's a concat operation
        else:
            # get the arguments of the concat operation
            arg1Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'arg_1'][0]    
            arg2Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'arg_2'][0]
            arg1 = pathCondition.neighbors(arg1Edge,1)[0]
            arg2 = pathCondition.neighbors(arg2Edge,1)[0]
            newVar = self.newVarID()
            
            # add the concat operation to the set of append predicates in the body of the rule 
            concatsInExpression.append("append(" + self.build_equation_expression(arg1) + "," + self.build_equation_expression(arg2) + "," + newVar + ")")
            
            # return the newly created variable
            return newVar

    
    def __call__(self, pathCondition):
        """
        Evaluates attribute equations by producing a Prolog predicate out of them and attempting to find a solution for that predicate.
        The predicate has as arguments the attributes of the path condition for which a solution needs to exist such that the path condition is possible.
        If a solution is found then the evaluator returns true, otherwise false.
        """

        clauseBody = ""
        variablesInExpression = []
        concatsInExpression = []
        
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
                
                leftExpr = self.build_equation_expression(leftExprNode, pathCondition, variablesInExpression, concatsInExpression)
                rightExpr = self.build_equation_expression(rightExprNode, pathCondition, variablesInExpression, concatsInExpression)  

                if equationNode < len(equationNodes)-1:
                    clauseBody += leftExpr + "=" +  rightExpr + ","
                else:
                    clauseBody += leftExpr + "=" +  rightExpr       

        clauseHead = "solve("
        for var in range(0,len(variablesInExpression)):
            if var < len(variablesInExpression)-1:
                clauseHead += variablesInExpression[var] + ","
            else:
                clauseHead += variablesInExpression[var]
        clauseHead += ")"
        
        prologInput = clauseHead + ":-" + clauseBody

        p = Prolog()
        p.assertz(prologInput)           
#        l = list(p.query(clauseHead))   
        result = list(p.query(clauseHead))
        
        if result == []:
            return False
        else:
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
        