'''
Created on 2013-09-10

@author: gehan
'''

from state_property import StateProperty

class AndStateProperty(StateProperty):
    '''
    classdocs
    '''
    propArg1=None
    propArg2=None

    def __init__(self, arg1, arg2):
        '''
        Constructor
        '''
        #print ("Initializing an AndStateProp Object")
        self.propArg1=arg1
        self.propArg2=arg2
        self.hasDefaultVerifResult=False
        self.verifResult=False
     
    def getAllOperands(self):
        return [self.propArg1, self.propArg2]   
   
    def verify(self,state, StateSpace=None):

        #print ("Started running function verify of Class AndStateProp")
        result=(self.propArg1.verify(state,StateSpace)) and (self.propArg2.verify(state,StateSpace))
        # if (result):
        #     print ("AndStateProp Holds !")
        # else:
        #     print ("AndStateProp Does Not Hold !")
        self.counterexamples = [self.propArg1.counterexamples, self.propArg2.counterexamples]
        self.SETverifResult(result)
        return self.GETverifResult()

    def print_counterexamples(self):
        print("And Property Counterexamples:")
        print("First arg:")
        for c in self.counterexamples[0]:
            print(c.name)
        print("Second arg:")
        for c in self.counterexamples[1]:
            print(c.name)
