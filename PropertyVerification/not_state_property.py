'''
Created on 2013-09-10

@author: gehan
'''

from state_property import StateProperty

class NotStateProperty(StateProperty):
    '''
    classdocs
    '''
    propArg1=None

    def __init__(self, arg1):
        '''
        Constructor
        '''

        StateProperty.__init__(self)

        #print ("Initializing a NotStateProp Object")
        self.propArg1=arg1
        self.hasDefaultVerifResult=False
        self.verifResult=False
        self.counterexamples = []
        
    def getAllOperands(self):
        return [self.propArg1]
        
    def verify(self,state, StateSpace=None):
        #print ("Started running function verify of Class NotStateProp")
        result=not(self.propArg1.verify(state, StateSpace))

        self.status = self.propArg1.status

        # if (result):
        #     print ("NotStateProp Holds !")
        # else:
        #     print ("NotStateProp Does Not Hold !")

        self.counterexamples = []#self.propArg1.counterexamples
        self.SETverifResult(result)
        return self.GETverifResult()

    def print_counterexamples(self):
        print("Not Property Counterexamples:")
        print("NOT IMPLEMENTED")