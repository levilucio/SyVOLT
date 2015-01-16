'''
Created on 2015-01-13

@author: levi
'''
import unittest
from pyswip import Prolog, Query

# pyswip is a bridge with Prolog
# download it here: https://code.google.com/p/pyswip/downloads/list
# installation instructions are in the package

from PoliceStationMM.transformation_1.Himesis.HS2S import HS2S
from PoliceStationMM.transformation_2.Himesis.HSM2SM import HSM2SM
from PoliceStationMM.transformation_1.Himesis.HSF2SF import HSF2SF
from PoliceStationMM.transformation_1.Himesis.HMM2MM import HMM2MM
from PoliceStationMM.transformation_1.Himesis.HFF2FF import HFF2FF


class Test(unittest.TestCase):

    varID = 0
    
    def newVarID(self):
        return "V" + str(self.varID)
        self.varID += 1

    def test_equations(self):

        pathCondition = HSM2SM()       
        pathCondition1 = HS2S()
        
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
        p.query(clauseHead)   
        
           
#        print l
        
#         with open("./tmp/Output.txt", "w") as text_file:
#             text_file.write(prologInput)


    def build_equation_expression(self, node, pathCondition, variablesInExpression, concatsInExpression):

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

                
    def _find_nodes_with_mm(self, graph, mm_names):
        nodes = []
        for node in graph.vs:
            if node["mm__"] in mm_names:
                nodes.append(node)
        return nodes      

#     def test_solve(self):
#         p = Prolog()
#         p.assertz("father(michael,john)")
#         p.assertz("father(michael,levi)")
# #        p.assertz("get(Name1,Name2,Name3):- Name1 = [m,a,i,n], Name1 = [b,l,a], Name2 = L1, Name3 = L2, append(L2,[c,o,n,s,t],L1)")
# #         for result in p.query("father(michael,X)"):
# #             print result              
#         l = list(p.query("father(michael,X)"))
#         print l                                                                                                                                                                                                                                                  
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()