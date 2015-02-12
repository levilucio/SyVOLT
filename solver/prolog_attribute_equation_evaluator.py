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
    
    # to generate fresh var ID names    
    varID = 0
    
    # Keep the variable names in the prolog expression for all attributes of the same
    # name connected to the same object. This is necessary because an object may have connected
    # to it more than one attribute with the same name, which means the attribute has multiple
    # constraints for that object.
    
    varNameDatabase = {}
    
    def __init__(self, verbosity):
        self.verbosity = verbosity

    
    def newVarID(self):
        old_varID = self.varID
        self.varID += 1   
        return "V" + str(old_varID) 

    
#     def build_equation_expression(self, node, pathCondition, variablesInExpression, concatsInExpression):
#         """
#         helper for building the attribute equations by recursively going through the operations associated
#         to the left hand side and to the right hand side of an equation
#         """
#         
#         # in case it's an attribute, return the object's ID
#         if pathCondition.vs[node]['mm__'] == 'Attribute':
#             variablesInExpression.append("X" + str(node))
#             return "X" + str(node)
#         # in case it's a constant, return its value as a list
#         elif pathCondition.vs[node]['mm__'] == 'Constant':
#             constant = pathCondition.vs[node]['name']
#             print "------> " + constant
#             constAsList = "["
#             for c in range(0,len(constant)):
#                 constAsList += "'" + constant[c] + "'"
#                 if c < len(constant) - 1:
#                     constAsList += ","
#             constAsList += "]" 
#             return constAsList
#         # it's a concat operation
#         else:
#             # get the arguments of the concat operation
#             arg1Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'hasArgs'][0]    
#             arg2Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'hasArgs'][0]
#             arg1 = pathCondition.neighbors(arg1Edge,1)[0]
#             arg2 = pathCondition.neighbors(arg2Edge,1)[0]
#             newVar = self.newVarID()
#             
#             # add the concat operation to the set of append predicates in the body of the rule 
#             concatsInExpression.append("append(" + self.build_equation_expression(arg1, pathCondition, variablesInExpression, concatsInExpression) + "," + self.build_equation_expression(arg2, pathCondition, variablesInExpression, concatsInExpression) + "," + newVar + ")")
#             
#             # return the newly created variable
#             return newVar


#     def __call__(self, pathCondition):
#         """
#         Evaluates attribute equations by producing a Prolog predicate out of them and attempting to find a solution for that predicate.
#         The predicate has as arguments the attributes of the path condition for which a solution needs to exist such that the path condition is possible.
#         If a solution is found then the evaluator returns true, otherwise false.
#         """
# 
#         clauseBody = ""
#         variablesInExpression = []
#         concatsInExpression = []
#         
#         # grab all the equation nodes in the path condition
#         equationNodes = self._find_nodes_with_mm(pathCondition, "Equation")
#         # now build all the equations
#         if equationNodes != []:
#             for equationNode in range(0,len(equationNodes)):
#                 # get the left and the right expressions of the equation
#                 leftExprEdge = [i for i in pathCondition.neighbors(equationNodes[equationNode],1) if pathCondition.vs[i]['mm__'] == 'leftExpr'][0]    
#                 rightExprEdge = [i for i in pathCondition.neighbors(equationNodes[equationNode],1) if pathCondition.vs[i]['mm__'] == 'rightExpr'][0]
# 
#                 leftExprNode = pathCondition.neighbors(leftExprEdge,1)[0]
#                 rightExprNode = pathCondition.neighbors(rightExprEdge,1)[0] 
#                 
#                 leftExpr = self.build_equation_expression(leftExprNode, pathCondition, variablesInExpression, concatsInExpression)
#                 rightExpr = self.build_equation_expression(rightExprNode, pathCondition, variablesInExpression, concatsInExpression)  
# 
#                 if equationNode < len(equationNodes)-1:
#                     clauseBody += leftExpr + "=" +  rightExpr + ","
#                 else:
#                     clauseBody += leftExpr + "=" +  rightExpr
#             
#             if concatsInExpression != []:
#                 clauseBody += ","      
#             for concat in concatsInExpression:
#                 clauseBody += concat
# 
#         clauseHead = "solve("
# #        variablesInExpression = list(set(variablesInExpression))
#         for var in range(0,len(variablesInExpression)):
#             if var < len(variablesInExpression)-1:
#                 clauseHead += variablesInExpression[var] + ","
#             else:
#                 clauseHead += variablesInExpression[var]
#         clauseHead += ")"
#         
#         prologInput = clauseHead + ":-" + clauseBody
#         
#         if self.verbosity >= 2 :
#             print "\nChecking with Prolog:"
#             print "----------------"
#             print prologInput
#             print "\n"
# 
#         p = Prolog()
#         p.assertz(prologInput)           
# #        l = list(p.query(clauseHead))  
#       
#         print "Clause head: " + clauseHead
#         result = list(p.query(clauseHead))
#         print "Prolog result:"
#         print result
#         
#         if result == []:
#             if self.verbosity >= 2 : print "Prolog check failed!"
#             return False
#         else:
#             if self.verbosity >= 2 : print "Prolog check succeeded!"
#             return True


    def build_equation_expression(self, node, pathCondition, variablesInExpression, concatsInExpression, varParentObjects):
        """
        helper for building the attribute equations by recursively going through the operations associated
        to the left hand side and to the right hand side of an equation
        """
        
        # in case it's an attribute, return the object's ID
        if pathCondition.vs[node]['mm__'] == 'Attribute':
            variablesInExpression.append("X" + str(node))
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
            
            varDatabaseKey = str(parentObject) + attrName
            if not varDatabaseKey in set(self.varNameDatabase.keys()): 
                self.varNameDatabase[varDatabaseKey] = "X" + str(node)
                return "X" + str(node)
            else:
                return self.varNameDatabase[varDatabaseKey]
                

        # in case it's a constant, return its value as a list
        elif pathCondition.vs[node]['mm__'] == 'Constant':
            constant = pathCondition.vs[node]['name']
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
            arg1Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'hasArgs'][0]    
            arg2Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'hasArgs'][1]
            arg1 = pathCondition.neighbors(arg1Edge,1)[0]
            arg2 = pathCondition.neighbors(arg2Edge,1)[0]
            newVar = self.newVarID()
 
            # add the concat operation to the set of append predicates in the body of the rule 
            concatsInExpression.append("append(" + self.build_equation_expression(arg1, pathCondition, variablesInExpression, concatsInExpression, varParentObjects) + "," + self.build_equation_expression(arg2, pathCondition, variablesInExpression, concatsInExpression, varParentObjects) + "," + newVar + ")")
            
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
        varParentObjects = []
        
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

                leftExpr = self.build_equation_expression(leftExprNode, pathCondition, variablesInExpression, concatsInExpression, varParentObjects)
                rightExpr = self.build_equation_expression(rightExprNode, pathCondition, variablesInExpression, concatsInExpression, varParentObjects)  

                if equationNode < len(equationNodes)-1:
                    clauseBody += leftExpr + "=" +  rightExpr + ","
                else:
                    clauseBody += leftExpr + "=" +  rightExpr
              
            for concat in concatsInExpression:
                clauseBody += "," 
                clauseBody += concat

        clauseHead = "solve("
#        variablesInExpression = list(set(variablesInExpression))
        for var in range(0,len(variablesInExpression)):
            if var < len(variablesInExpression)-1:
                clauseHead += variablesInExpression[var] + ","
            else:
                clauseHead += variablesInExpression[var]
        clauseHead += ")"
        
        prologInput = clauseHead + ":-" + clauseBody
        
        if self.verbosity >= 2 :
            print "\nChecking with Prolog:"
            print "----------------"
            print prologInput
            print "\n"

        p = Prolog()
        p.assertz(prologInput)           
#        l = list(p.query(clauseHead))  

        if self.verbosity >= 2 :      
            print "Clause head: " + clauseHead
            result = list(p.query(clauseHead))
            print "Prolog result: " + str(result)
        
        if result == []:
            if self.verbosity >= 2 : print "Prolog check failed!"
            return False
        else:
            if self.verbosity >= 2 : print "Prolog check succeeded!"
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
        