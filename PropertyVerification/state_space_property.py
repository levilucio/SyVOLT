'''
Created on 2013-08-17

@author: gehan
'''
from abc import ABCMeta,abstractmethod
from property import Property

class StateSpaceProperty(Property):
    '''
    classdocs
    '''
    __metaclass__=ABCMeta
    
    @abstractmethod 
    def __init__(self,params):
        '''
        Constructor
        '''
        pass
    
    @abstractmethod 
    def verify (self, params):
        pass