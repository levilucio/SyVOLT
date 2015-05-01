'''
Created on 2013-09-24

@author: gehan
'''
from abc import ABCMeta,abstractmethod
class Property(object):
    '''
    classdocs
    '''
    __metaclass__=ABCMeta
    
    @abstractmethod 
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @abstractmethod 
    def verify (self,params):
        pass