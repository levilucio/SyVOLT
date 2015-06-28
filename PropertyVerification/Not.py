'''
Created on 2013-09-24

@author: gehan
'''

from .state_space_property import StateSpaceProperty
class Not(StateSpaceProperty):
    '''
    classdocs
    '''
    propArg1=None

    def __init__(self, arg1):
        '''
        Constructor
        '''
        print ("Initializing a Not Property Object")
        self.propArg1=arg1

    def verify(self):
        print ("Started running function verify of Class Not")
        result=not (self.propArg1)
        if (result):
            print ("Not Property Holds !")
        else:
            print ("Not Property Does Not Hold !")
        return result