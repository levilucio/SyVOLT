'''
Created on 2013-09-24

@author: gehan
'''
from state_space_property import StateSpaceProperty
class And(StateSpaceProperty):
    '''
    classdocs
    '''
    propArg1=None
    propArg2=None

    def __init__(self, arg1, arg2):
        '''
        Constructor
        '''
        print ("Initializing an And Property Object")
        self.propArg1=arg1
        self.propArg2=arg2

    def verify(self):
        print ("Started running function verify of Class And")
        result=(self.propArg1) and (self.propArg2)
        if (result):
            print ("And Property Holds !")
        else:
            print ("And Property Does Not Hold !")
        return result