'''
Created on 2015-02-16

@author: levi
'''

from xml.dom import minidom

class EcoreUtils(object):
    '''
    a set of utils to deal with ecore files
    '''

    def __init__(self, xmlfileName):
        '''
        Constructor
        '''
        self.xmldoc = minidom.parse(xmlfileName)
    
    
    def getMetamodelClassNames(self):
        '''
        Get a list with all the names of the classes in the ecore metamodel file.
        Discard duplicates.
        TODO: For the time being does not care about inheritance relations.
        '''
        classNameList = self.xmldoc.getElementsByTagName('eClassifiers')
        return [str(item.attributes['name'].value) for item in classNameList]


# if __name__ == '__main__':
#     t1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/C.ecore")
#     t2 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#     t1.getMetamodelClassNames()
#     t2.getMetamodelClassNames()
