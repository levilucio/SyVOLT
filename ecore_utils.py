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


    def getMetamodelContainmentLinks(self):
        '''
        Get all the containment links in a metamodel.
        '''
        containmentLinkList = self.xmldoc.getElementsByTagName('eStructuralFeatures')
        containmentReferences = []
        for element in containmentLinkList:
            try:
                if element.attributes.item(4).value == "true":
                    containmentReferences.append(str(element.attributes['name'].value))
            except Exception:
                pass 
        return containmentReferences
    
    
    def buildContaimentDependenciesForClass(self, targetClass, depth):
        '''
        auxiliary, build all containment relations for a class, recursively
        '''        
        
        print("------------------> Depth: " + str(depth))
        depth = depth + 1
        
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')  
        
        for sourceClass in metamodelClasses:
            print("   Class: " + str(sourceClass.attributes['name'].value))
            rels = sourceClass.getElementsByTagName('eStructuralFeatures')
            containmentRels = []
            for rel in rels:
                try:
                    if rel.attributes.item(4).value == "true":
                        containmentRels.append(rel)
                except Exception:
                    pass 
            for cRel in containmentRels:
                trgtClassName = str(cRel.attributes['eType'].value).split('#//', 1)[1]
                print("   -------------------")
                print("   Rel target: " + trgtClassName)
                print("   Class target: " + str(targetClass.attributes['name'].value))
                print("   -------------------")
                if trgtClassName == str(targetClass.attributes['name'].value):
                    #return [str(cRel.attributes['name'].value)].extend(self.buildContaimentDependenciesForClass(sourceClass))
                    containerClasses = self.buildContaimentDependenciesForClass(sourceClass, depth)
                    res = [str(cRel.attributes['name'].value)]
                    res.extend(containerClasses)
                    return res
        
        return []


    def getContaimentDependenciesForClass(self):
        '''
        get all containment relations for a class
        '''    
        
        allContainmentRels = []
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        
        for mmClass in metamodelClasses:
            print("Going to treat: " + str(mmClass.attributes['name'].value))
            allContainmentRels.append((str(mmClass.attributes['name'].value), self.buildContaimentDependenciesForClass(mmClass,0)))
            
        return allContainmentRels
                

if __name__ == '__main__':
    t1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#    t2 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#    r1 = t1.getMetamodelContainmentLinks()
#    r2 = t2.getMetamodelContainmentLinks()
#    print(r1)
#    print(r2)    
    print(str(t1.getContaimentDependenciesForClass()))
