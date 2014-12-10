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
        print ("Initializing a NotStateProp Object")
        self.propArg1=arg1
        self.hasDefaultVerifResult=False
        self.verifResult=False
        
    def getAllOperands(self):
        return [self.propArg1]
        
    def verify(self,state, StateSpace=None):
        print ("Started running function verify of Class NotStateProp")
        result=not(self.propArg1.verify(state, StateSpace))
        if (result):
            print ("NotStateProp Holds !")
        else:
            print ("NotStateProp Does Not Hold !")
        self.SETverifResult(result)
        return self.GETverifResult()