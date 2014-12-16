'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time

from path_condition_generator import *

from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator
from t_core.messages import Packet

from t_core.tc_python.frule import FRule
from t_core.tc_python.arule import ARule

from himesis_utils import graph_to_dot, disjoint_model_union

from PoliceStationMM.transformation_1.Himesis.HS2S import HS2S
from PoliceStationMM.transformation_1.Himesis.HM2M import HM2M
from PoliceStationMM.transformation_1.Himesis.HF2F import HF2F
from PoliceStationMM.transformation_2.Himesis.HSM2SM import HSM2SM
from PoliceStationMM.transformation_1.Himesis.HSF2SF import HSF2SF
from PoliceStationMM.transformation_1.Himesis.HMM2MM import HMM2MM
from PoliceStationMM.transformation_1.Himesis.HFF2FF import HFF2FF


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def test_equations(self):

        pathCondition = HSM2SM()       
        pathCondition1 = HS2S()
        
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
                
                leftExpr = self.build_equation_expression(leftExprNode, pathCondition, variablesInExpression)
                rightExpr = self.build_equation_expression(rightExprNode, pathCondition, variablesInExpression)  

                Z3Input += "(assert (= " + leftExpr + " " +  rightExpr + ") )\n"
        
        Z3Input = "\n" + Z3Input
        for var in variablesInExpression:
            Z3Input = "(declare-variable " + var + " String)\n" + Z3Input
        Z3Input += "\n(check-sat)"   
           
        print Z3Input
        
        with open("./tmp/Output.txt", "w") as text_file:
            text_file.write(Z3Input)


    def build_equation_expression(self, node, pathCondition, variablesInExpression):

        # in case it's an attribute, return the object's ID
        if pathCondition.vs[node]['mm__'] == 'Attribute':
            variablesInExpression.append("a" + str(node))
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

                
    def _find_nodes_with_mm(self, graph, mm_names):
        nodes = []
        for node in graph.vs:
            if node["mm__"] in mm_names:
                nodes.append(node)
        return nodes      