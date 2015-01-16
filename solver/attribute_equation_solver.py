'''
Created on 2015-01-16

@author: levi
'''

from abc import ABCMeta, abstractmethod

class AttributeEquationSolver():
    '''
    make sure the solver implements the __call__ method
    '''
    __metaclass__=ABCMeta

    @abstractmethod 
    def __call__(self, pathCondition):
        pass
        