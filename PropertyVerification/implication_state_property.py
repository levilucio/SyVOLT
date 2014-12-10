'''
Created on 2013-09-10

@author: gehan
'''
from state_property import StateProperty

class ImplicationStateProperty(StateProperty):
    '''
    classdocs
    '''
    propArg1=None
    propArg2=None

    def __init__(self, arg1, arg2):
        '''
        Constructor
        '''
        print ("Initializing an ImplicationStateProp Object")
        self.propArg1=arg1
        self.propArg2=arg2
        self.hasDefaultVerifResult=False
        self.verifResult=False
    
    def getAllOperands(self):
        return [self.propArg1, self.propArg2]
        
    def verify(self,state, StateSpace=None):
        print ("Started running function verify of Class ImplicationStateProp")
        #intermediateNot=NotProp(self.propArg1)
        result=(  not(self.propArg1.verify(state, StateSpace))  ) or (self.propArg2.verify(state,StateSpace))
        if (result):
            print ("ImplicationStateProp Holds !")
        else:
            print ("ImplicationStateProp Does Not Hold !")
        self.SETverifResult(result)
        return self.GETverifResult()