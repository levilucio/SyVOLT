'''
Created on 2015-02-16

@author: levi
'''

from xml.dom import minidom
from copy import deepcopy
from core.himesis_utils import graph_to_dot
class EcoreUtils(object):
    '''
    a set of utils to deal with ecore files
    '''


    def __init__(self, xmlfileName):
        '''
        Constructor
        '''
        self.xmldoc = minidom.parse(xmlfileName)
        self.inheritanceRels = self.getSuperClassInheritanceRelationForClasses()
        
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')  
        self.mmClassContained = {}       
        self.containmentRels = []
        
        # first get a dictionary with all the metamodel classes that have containment relations towards them.
        # several containment relations can exist towards the same metamodel class. 
        # also keep a list of all containment relations in the metamodel.
        
        for mmClass in metamodelClasses:
            rels = mmClass.getElementsByTagName('eStructuralFeatures')
            for rel in rels:
                try:
                    if str(rel.attributes['containment'].value) == "true":
                        targetClassName = str(rel.attributes['eType'].value).split('#//', 1)[1]
                        relName = str(rel.attributes['name'].value)
                                                                 
                        if targetClassName not in self.mmClassContained.keys():
                            self.mmClassContained[targetClassName] = [relName]
                        else:
                            self.mmClassContained[targetClassName].append(relName)
                            
                        self.containmentRels.append(relName)
                                                
                except Exception:
                    pass
            
        # treat all the remaining classes that have no containment links to them but that
        # inherit from classes that do.
        
        mmClassNames = self.getMetamodelClassNames()
        remainingContClasses = set(mmClassNames) - set(self.mmClassContained.keys())
        
        for remContClass in remainingContClasses:
            parentClasses = self.inheritanceRels[remContClass]
            containedParentClasses = set(parentClasses).intersection(set(self.mmClassContained.keys()))
            for contParentClass in containedParentClasses:
                if remContClass not in self.mmClassContained.keys():
                    self.mmClassContained[remContClass] = deepcopy(self.mmClassContained[contParentClass])
                else:
                    self.mmClassContained[remContClass].extend(self.mmClassContained[contParentClass])

    
    
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
                
                # do not consider self loops in the containment classes, because they do not help with reaching the root
                # TODO: containment loops could involve more than one class (e.g. A contains B contains C contains A). This case is not yet treated.
                if trgtClassName == str(targetClass.attributes['name'].value) and not (trgtClassName == srcClassName):
                    
                    #return [str(cRel.attributes['name'].value)].extend(self.buildContaimentDependenciesForClass(sourceClass))
                    res.extend([(srcClassName, str(cRel.attributes['name'].value), trgtClassName)])
                    
                    res.extend(self.buildContaimentDependenciesForClass(sourceClass))
        
        return res
        


    def getContaimentLinksForClasses(self):
        '''
        get all containment relations for the classes in the metamodel
        '''    
        
        allContainmentRels = {}
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        
        for mmClass in metamodelClasses:
            allContainmentRels[str(mmClass.attributes['name'].value)] = self.buildContaimentDependenciesForClass(mmClass)

        # now add to the existing containment relations for a class the containment relations of its supertypes

        containmentRelsWithSuper = {}
        
        for mmClassName in allContainmentRels.keys():
            containmentRelsToAdd = []
            if mmClassName in self.inheritanceRels.keys():
                for superTypeName in self.inheritanceRels[mmClassName]:
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


     
    def getSuperClassInheritanceRelationForClasses(self):
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
            else:
                inheritanceRel[str(mmClass.attributes['name'].value)] = []
                        
        return inheritanceRel
    
    
    def getSubClassInheritanceRelationForClasses(self):
        '''
        build a dictionary where the key is the name of the metamodel class and the
        value is the list of children of that class
        '''
        subClasses = {}
        
        superClasses = self.getSuperClassInheritanceRelationForClasses()
        
        for childClassName in superClasses.keys():
            for parentClassName in superClasses[childClassName]:
                if parentClassName not in subClasses.keys():
                    subClasses[parentClassName] = [childClassName]
                else:
                    subClasses[parentClassName].append(childClassName)
                        
        return subClasses


    
    def inheritsFrom(self, subtype, supertype):
        '''
        quick and dirty method to check whether a class inherits from another
        '''
        if subtype == supertype: return True
        
        if subtype in self.inheritanceRels:
            if supertype in self.inheritanceRels[subtype]:
                return True
            
        return False

        
        
    def getBuiltClasses(self, pathCond):
        
        classesInOuputMM = self.getMetamodelClassNames()  
        classesBuiltByPC = []
        
        for node in range(len(pathCond.vs)):
            if pathCond.vs[node]["mm__"] in classesInOuputMM:
                instanceIsProduced = True
                inputClassNodes = pathCond.neighbors(pathCond.vs[node],1)
                for inputClassNode in inputClassNodes:
                    if pathCond.vs[inputClassNode]["mm__"] == "backward_link":
                        instanceIsProduced = False
                        break
                if instanceIsProduced:  
                    classesBuiltByPC.append(pathCond.vs[node]["mm__"])
                
        return classesBuiltByPC
        

                
    def getBuiltContainmentLinks(self, rule):
        '''
        return all the containment relations built by a rule, in the form of a
        dictionary having as key the name of the target classes and as elements a list
        with the containment relation(s).
        '''    
        
        containmentRelsInRule = {}
        
        # now check which relations in the rule are built by which containment relation
        
        for node in range(len(rule.vs)):
            
#             if rule.vs[node]["mm__"] == "directLink_T":
#                 print("................ Containment link: " + rule.vs[node]["attr1"])
#                 print("................ self.containmentRels: " + str(self.containmentRels))
                
            if rule.vs[node]["mm__"] == "directLink_T" and rule.vs[node]["attr1"] in self.containmentRels:
                
                # find the types of the source and the target elements of the containment in the rule
                targetClassNode = rule.neighbors(rule.vs[node],1)                
                targetClassName = rule.vs[targetClassNode]["mm__"][0]                

                if targetClassName not in containmentRelsInRule.keys():
                    containmentRelsInRule[targetClassName] = rule.vs[node]["attr1"]                       
                 
        return containmentRelsInRule



    def getMissingContainmentLinks(self, pathCond):
        '''
        return all missing containment relations in a path condition, in the form of a
        dictionary having as key the targetClass and as data the containmentLinks that 
        can be used to build the missing containment link.
        '''  
        
        missingContainmentLinks = {}

        for node in range(len(pathCond.vs)):
            targetClassName = pathCond.vs[node]["mm__"]

            if targetClassName in self.mmClassContained.keys() and targetClassName not in missingContainmentLinks.keys():
                # get all the containment relations into produced call instances, if an apply class
                # of this type without containment links has not been found yet. Only one apply class
                # of a given type without containment links is kept. 
                inputRelNodes = pathCond.neighbors(pathCond.vs[node],2)
                
                inputRelNames = []
                
                for inputRelNode in inputRelNodes:
                    if pathCond.vs[inputRelNode]["mm__"] == "directLink_T":
                        inputRelNames.append(pathCond.vs[inputRelNode]["attr1"])

                # check if any containment relation into the class already exists
                if set(inputRelNames).intersection(set(self.containmentRels)) == set():

                    # get the containment links already built in this pathcond
                    builtContainmentLinks = self.getBuiltContainmentLinks(pathCond)

                    for attr1 in self.mmClassContained[targetClassName]:

                        #if this link is built already in this pathCond, do nothing
                        if targetClassName in builtContainmentLinks and attr1 in builtContainmentLinks[targetClassName]:
                            pass
                        else:
                            #mark this as a missing containment link
                            try:
                                missingContainmentLinks[targetClassName].append(attr1)
                            except KeyError:
                                missingContainmentLinks[targetClassName] = [attr1]

        return missingContainmentLinks
            
    
        


if __name__ == '__main__':
    from ATLTrans.HUnionMotherRule import HUnionMotherRule
    pathCond = HUnionMotherRule()
    t1 = EcoreUtils("../UMLRT2Kiltera_MM/metamodels/rt_new.ecore")
#    t1 = EcoreUtils("../eclipse_integration/examples/families_to_persons/metamodels/Community.ecore")
#    t1 = EcoreUtils("./mbeddr2C_MM/ecore_metamodels/Module.ecore")
#    r1 = t1.getMetamodelContainmentLinks()
#    r2 = t2.getMetamodelContainmentLinks()
#    print(r1)
#    print(r2)    
#    print(str(t1.buildInheritanceDependenciesForClass(["IN1"])))
#    print (str(t1.mmClassContained))
