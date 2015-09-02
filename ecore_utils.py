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
    
    
    def buildContaimentDependenciesForClass(self, targetClass):
        '''
        auxiliary, build all containment relations for a class, recursively
        '''        
        
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
                    res = [str(cRel.attributes['name'].value)]
                    res.extend(self.buildContaimentDependenciesForClass(sourceClass))
                    return res
        
        return []
        

    def getContaimentDependenciesForClasses(self):
        '''
        get all containment relations for the classes in the metamodel
        '''    
        
        allContainmentRels = []
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        
        for mmClass in metamodelClasses:
            print("Going to treat: " + str(mmClass.attributes['name'].value))
            allContainmentRels.append((str(mmClass.attributes['name'].value), self.buildContaimentDependenciesForClass(mmClass,0)))
            
        return allContainmentRels


    def buildInheritanceDependenciesForClass(self, mmClassNames):
        '''
        build a list of all parents of the given class
        '''
        inheritanceRel = {}
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        
        mmClassesToTreat = []
        
        for mmClass in metamodelClasses:
            for mmClassName in mmClassNames:
                if mmClassName == str(mmClass.attributes['name'].value):
                    mmClassesToTreat.append(mmClass)
                    break
        
        parentNames = []
        
        for mmClass in mmClassesToTreat:
            superTypeNames = []
            try:
                superTypeNames = str(mmClass.attributes['eSuperTypes'].value)
                superTypeNames = superTypeNames.replace(" ", "")
                superTypeNames = superTypeNames[3:]
                superTypeNames = superTypeNames.split('#//')
            except Exception:
                pass           
            
#             parentClass = None
#             for mmClass2 in metamodelClasses:
#                 if str(mmClass.attributes['name'].value) == superTypeName:
#                     parentClass = mmClass2
                    
            parentNames.extend(superTypeNames)
            
            if parentNames != None:
                parentNames.extend(self.buildInheritanceDependenciesForClass(parentNames))
            
        return list(set(parentNames))

     
    def getInheritanceRelationForClasses(self):
        '''
        build a dictionary where the key is the name of the metamodel class and the
        value is the list of parents of that class
        '''
        inheritanceRel = {}
        
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        for mmClass in metamodelClasses:
            superTypeNames = []
            try:
                superTypeNames = str(mmClass.attributes['eSuperTypes'].value)
                superTypeNames = superTypeNames.replace(" ", "")
                superTypeNames = superTypeNames[3:]
                superTypeNames = superTypeNames.split('#//')
            except Exception:
                pass    
            if superTypeNames != []: 
                superTypeNames.extend(self.buildInheritanceDependenciesForClass(superTypeNames))
                inheritanceRel[str(mmClass.attributes['name'].value)] = superTypeNames
                    
        
        return inheritanceRel
                

if __name__ == '__main__':
    t1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#    t2 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#    r1 = t1.getMetamodelContainmentLinks()
#    r2 = t2.getMetamodelContainmentLinks()
#    print(r1)
#    print(r2)    
    print(str(t1.getInheritanceRelationForClasses()))
