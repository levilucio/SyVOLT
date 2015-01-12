'''
Created on 2015-08-09

@author: levi
'''

import subprocess

class AttributeEquationEvaluator():
    
    Z3Location = "/home/levi/z3-str/Z3-str.py"
    Z3InputFile = "./tmp/Z3EquationFile"
    
    
    def __init__(self, verbosity):
        self.verbosity = verbosity

    
    def _build_equation_expression(self, node, pathCondition, variablesInExpression):
        """
        helper for building the attribute equations by recursively going through the operations associated
        to the left hand side and to the right hand side of an equation
        """

        # in case it's an attribute, return the object's ID
        if pathCondition.vs[node]['mm__'] == 'Attribute':
            newVar = "a" + str(node)
            if newVar not in set(variablesInExpression):
                variablesInExpression.append(newVar)
            return "a" + str(node)
        # in case it's a constant, return it's value
        elif pathCondition.vs[node]['mm__'] == 'Constant':
            return "\"" + pathCondition.vs[node]['value'] + "\""
        # it's a concat operation
        else:
            # get the arguments of the concat operation
            arg1Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'arg_1'][0]    
            arg2Edge = [i for i in pathCondition.neighbors(node,1) if pathCondition.vs[i]['mm__'] == 'arg_2'][0]
            arg1 = pathCondition.neighbors(arg1Edge,1)[0]
            arg2 = pathCondition.neighbors(arg2Edge,1)[0]

            return "( Concat " + self.build_equation_expression(arg1) + " " + self.build_equation_expression(arg2) + ")"       

    
    def __call__(self, pathCondition):
        """
        Build the necessary set of equations to be passed onto Z3 for evaluation (SAT/UNSAT) given a path condition.
        Equations have an abstract syntax tree structure inside the path condition that needs to be parsed.
        Note that some equations share the same variables, and as such those variables have to be given the same identifiers throughout the Z3 expression.
        Evaluate the set of equations using Z3 and return True if there is a solution for them, false otherwise
        """

        Z3Input = ""
        variablesInExpression = []
        
        # grab all the equation nodes in the path condition
        equationNodes = self._find_nodes_with_mm(pathCondition, "Equation")
        # now build all the equations
        if equationNodes != []:
            for equationNode in equationNodes:
                # get the left and the right expressions of the equation
                leftExprEdge = [i for i in pathCondition.neighbors(equationNode,1) if pathCondition.vs[i]['mm__'] == 'leftExpr'][0]    
                rightExprEdge = [i for i in pathCondition.neighbors(equationNode,1) if pathCondition.vs[i]['mm__'] == 'rightExpr'][0]

                leftExprNode = pathCondition.neighbors(leftExprEdge,1)[0]
                rightExprNode = pathCondition.neighbors(rightExprEdge,1)[0] 
                
                leftExpr = self._build_equation_expression(leftExprNode, pathCondition, variablesInExpression)
                rightExpr = self._build_equation_expression(rightExprNode, pathCondition, variablesInExpression)  

                Z3Input += "(assert (= " + leftExpr + " " +  rightExpr + ") )\n"
        
            Z3Input = "\n" + Z3Input
            for var in variablesInExpression:
                Z3Input = "(declare-variable " + var + " String)\n" + Z3Input
            Z3Input += "\n(check-sat)"
            
            if self.verbosity >= 2 :
                print "\nChecking with Z3:"
                print "----------------"
                print Z3Input
                print "\n"
             
            # for now write the file with the equation formulas to be caught by the binary
            # TODO: this is WAY TOO SLOW and needs to be done via an API or something faster    
            with open(self.Z3InputFile, "w") as text_file:
                text_file.write(Z3Input)
                 
            # now call the z3-str binary to get the result of checking the formula
            command = "python " + self.Z3Location + " -f " + self.Z3InputFile
            z3_output = subprocess.check_output(command, shell=True)   
             
            if self.verbosity >= 2 :
                print z3_output                                                                                      
            
            if "UNSAT" not in z3_output:   
                return True
            else:
                return False
            
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
