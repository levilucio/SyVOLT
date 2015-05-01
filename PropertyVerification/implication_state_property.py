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
        StateProperty.__init__(self)
        #print ("Initializing an ImplicationStateProp Object")
        self.propArg1=arg1
        self.propArg2=arg2
        self.hasDefaultVerifResult=False
        self.verifResult=False

        self.counterexamples = []

        self.debug = False
    
    def getAllOperands(self):
        return [self.propArg1, self.propArg2]
        
    def verify(self,state, StateSpace=None):
        #print ("Started running function verify of Class ImplicationStateProp")
        #intermediateNot=NotProp(self.propArg1)

        propArg1b = self.propArg1.verify(state, StateSpace)

        if self.debug:
            print("\nPropArg1 Holds: " + str(propArg1b))

        propArg2b = self.propArg2.verify(state, StateSpace)

        if self.debug:
            print("PropArg2 Holds: " + str(propArg2b))

        result=(  not propArg1b  ) or propArg2b

        if self.debug and not result:
            print("Implication does not hold")
            #self.propArg2.print_counterexamples()
            # for c in self.propArg2.counterexamples:
            #     print(c.name)

        self.status = "Prop1: " + self.propArg1.status + " Prop2: " + self.propArg2.status
        # if (result):
        #     print ("ImplicationStateProp Holds !")
        # else:
        #     print ("ImplicationStateProp Does Not Hold !")
        self.SETverifResult(result)
        return self.GETverifResult()