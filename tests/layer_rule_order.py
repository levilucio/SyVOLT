'''
Created on 2014-12-23

@author: levi
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        
        self.orderedNodes = []
#         self.partialOrder = {'R1' : ['R2'],
#                              'R3' : ['R4'],
#                              'R4' : ['R5'],
#                              'R5' : ['R6'],
#                              'R6' : ['R7','R8']}

        self.partialOrder = {'R1' : ['R2'],
                             'R2' : ['R3'],
                             'R4' : ['R5'],
                             'R6' : ['R7','R8'],
                             'R8' : ['R9','R10']}
        
        self.build_depth()
        
        req = self.calc_required(['R2'], self.partialOrder)
        
        print req
        
    
    def build_depth(self):
        
        # first find all the top nodes
        topNodes = []
        for node in self.partialOrder.keys():
            topnode = True
            for nodepass in self.partialOrder.keys():
                if node in set(self.partialOrder[nodepass]):
                    topnode = False
            if topnode: topNodes.append(node)
        
        self.orderedNodes.extend(topNodes)
        
        # continue adding nodes as we go down the tree
        self.build_ordered_nodes(topNodes)
        
        print list(reversed(self.orderedNodes))
        
        
    def build_ordered_nodes(self,topNodes):
        newTopNodes = []
        for node in topNodes:
            if node in set(self.partialOrder.keys()):
                newTopNodes.extend(self.partialOrder[node])
                self.orderedNodes.extend(self.partialOrder[node])
        
        if newTopNodes != [] : self.build_ordered_nodes(newTopNodes)
        

    def calc_required(self, rules, ruleContainment):
        requiredRules = []
        for rule in rules:
            if rule in set(ruleContainment.keys()):
                requiredRules = ruleContainment[rule]
                requiredRules.extend(self.calc_required(ruleContainment[rule], ruleContainment))
        return requiredRules
                
        
            
        
            
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()