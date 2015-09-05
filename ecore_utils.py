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
    
    
#     def addSuperTypeContainmentRels(self,containmentRels):
#         '''
#         add to the existing containment relations for a class the containment relations of it's supertypes
#         '''
#         inheritanceRels = self.getInheritanceRelationForClasses()
#         containmentRelsWithSuper = {}
#         
#         for mmClassName in inheritanceRels.keys():
#             contaimentRelsToAdd = []
#             for superType in inheritanceRels[mmClassName]:
#                 contaimentRelsToAdd.append(containmentRels[superType])
#             containmentRelsWithSuper[mmClassName] = containmentRels[mmClassName].extend(contaimentRelsToAdd)
#         
#         return containmentRelsWithSuper
             
        
    
    def buildContaimentDependenciesForClass(self, targetClass):
        '''
        auxiliary, build all containment relations for a class, recursively
        '''        
        
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')  
        
        res = []
        
        for sourceClass in metamodelClasses:
            rels = sourceClass.getElementsByTagName('eStructuralFeatures')
            containmentRels = []
            for rel in rels:
                try:
                    if str(rel.attributes['containment'].value) == "true":
                        containmentRels.append(rel)
                except Exception:
                    pass 
                
            for cRel in containmentRels:
                trgtClassName = str(cRel.attributes['eType'].value).split('#//', 1)[1]
                
                srcClassName = str(sourceClass.attributes['name'].value)
                if trgtClassName == str(targetClass.attributes['name'].value):
                    
                    #return [str(cRel.attributes['name'].value)].extend(self.buildContaimentDependenciesForClass(sourceClass))
                    res.extend([(srcClassName, str(cRel.attributes['name'].value), trgtClassName)])
                    res.extend(self.buildContaimentDependenciesForClass(sourceClass))
        
        return res
        

    def getContaimentDependenciesForClasses(self):
        '''
        get all containment relations for the classes in the metamodel
        '''    
        
        allContainmentRels = {}
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        
        for mmClass in metamodelClasses:
            allContainmentRels[str(mmClass.attributes['name'].value)] = self.buildContaimentDependenciesForClass(mmClass)

        # now add to the existing containment relations for a class the containment relations of it's supertypes
        
        #return allContainmentRels

        inheritanceRels = self.getInheritanceRelationForClasses()
        containmentRelsWithSuper = {}
        
        for mmClassName in allContainmentRels.keys():
            containmentRelsToAdd = []
            if mmClassName in inheritanceRels.keys():
                for superTypeName in inheritanceRels[mmClassName]:
                    if superTypeName in allContainmentRels.keys():
                        for containmentLink in allContainmentRels[superTypeName]:
                            containmentRelsToAdd.append((containmentLink[0], containmentLink[1], mmClassName))
            
            res = allContainmentRels[mmClassName]
            res.extend(containmentRelsToAdd)         
            containmentRelsWithSuper[mmClassName] = list(set(res))
        
        return containmentRelsWithSuper



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
#    t1 = EcoreUtils("./UMLRT2Kiltera_MM/metamodels/klt_new.ecore")
    t1 = EcoreUtils("./eclipse_integration/examples/families_to_persons/metamodels/Community.ecore")
#    t1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#    r1 = t1.getMetamodelContainmentLinks()
#    r2 = t2.getMetamodelContainmentLinks()
#    print(r1)
#    print(r2)    
    print(str(t1.getContaimentDependenciesForClasses()))
