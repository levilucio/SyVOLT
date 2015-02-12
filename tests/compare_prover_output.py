'''
Created on 2015-02-12

@author: levi
'''
import unittest


class Test(unittest.TestCase):


    def findPathCondition(self,pc,listpc):
        foundit = False
        for pc2 in listpc:
            diffRule = [rule for rule in pc if rule not in pc2]
            if diffRule == [] and len(pc) == len(pc2):
                foundit = True
                break 
        return foundit          
        

    def testCompare(self):
        
        with open("tmp/run_bentley_up_to_e1.txt") as f:
            bentley_content = f.readlines()
            
        toRemove = []
        
        for line in bentley_content:
            if line[0] == "-":
                toRemove.append(line)
                
        bentley_content = [line for line in bentley_content if line not in toRemove]
        
        print "Bentley: " + str(len(bentley_content))
        
        with open("tmp/run_levi_up_to_e1.txt") as f:
            levi_content = f.readlines()
            
        toRemove = []
        
        for line in levi_content:
            if line[0] == "-":
                toRemove.append(line)
                
        levi_content = [line for line in levi_content if line not in toRemove]
        
        print "Levi: " + str(len(levi_content))
        
#         difference = [line for line in bentley_content if line not in levi_content]
# 
#         print "Difference: " + str(len(difference))

        difference_bentley_levi = []

        split_bentley_content = []
        for line in bentley_content:
            line = line[:-1]
            split_bentley_content.append(line.split("_"))
            
        split_levi_content = []
        for line in levi_content:
            line = line[:-1]
            split_levi_content.append(line.split("_"))
        
        for l1 in split_bentley_content:
            if not self.findPathCondition(l1,split_levi_content): difference_bentley_levi.append(l1)          

        difference_levi_bentley = []
        
        for l1 in split_levi_content:
            if not self.findPathCondition(l1,split_bentley_content): difference_levi_bentley.append(l1)  
        
        print "\n"
        print "Difference size bentley levi: " + str(len(difference_bentley_levi))
        print difference_bentley_levi
        print "\n"
        print "Difference size levi bentley: " + str(len(difference_levi_bentley))
        print difference_levi_bentley
        
        pcdiff = difference_bentley_levi[0][:-1]
        
        print pcdiff
        
        if self.findPathCondition(pcdiff, split_levi_content):
            print "Found smaller..."
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()