'''
Created on 2013-09-24

@author: gehan
'''

from state_space_property import StateSpaceProperty
class Or(StateSpaceProperty):
    '''
    classdocs
    '''
    propArg1=None
    propArg2=None

    def __init__(self, arg1, arg2):
        '''
        Constructor
        '''
        print ("Initializing an Or Property Object")
        self.propArg1=arg1
        self.propArg2=arg2

    def verify(self):
        print ("Started running function verify of Class Or")
        result=(self.propArg1) or (self.propArg2)
        if (result):
            print ("Or Property Holds !")
        else:
            print ("Or Property Does Not Hold !")
        return result