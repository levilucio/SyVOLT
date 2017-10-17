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

        self.debug = False

        if self.debug:
            print("Parsing: " + xmlfileName)

        self.xmldoc = None

        try:
            self.xmldoc = minidom.parse(xmlfileName)
        except FileNotFoundError:
            raise FileNotFoundError("Metamodel file not found: " + xmlfileName + "\nWas the metamodel placed in the 'SyVOLT/eclipse_integration/metamodels/' folder?")

        self.inheritanceRels = self.getSuperClassInheritanceRelationForClasses()

        self.containmentRels = []


        self.mmClassParents = self.getSuperClassInheritanceRelationForClasses()
        self.mmClassChildren = self.getSubClassInheritanceRelationForClasses()

        self.containmentLinks = {}
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')

        # first get a dictionary with all the metamodel classes that have containment relations towards them.
        # several containment relations can exist towards the same metamodel class.
        # also keep a list of all containment relations in the metamodel.


        debug_contain_links = False

        for mmClass in metamodelClasses:
            mmClassName = mmClass.attributes['name'].value
            rels = mmClass.getElementsByTagName('eStructuralFeatures')

            for rel in rels:

                try:
                    if str(rel.attributes['containment'].value) == "true":
                        targetClassName = str(rel.attributes['eType'].value).split('#//', 1)[1]
                        relName = str(rel.attributes['name'].value)

                        containment_link = (mmClassName, relName)

                        if targetClassName not in self.containmentLinks.keys():
                            self.containmentLinks[targetClassName] = [containment_link]
                        else:
                            if containment_link not in self.containmentLinks[targetClassName]:
                                self.containmentLinks[targetClassName].append(containment_link)
                        self.containmentRels.append(relName)
                except KeyError:
                    pass


        if debug_contain_links:
            print("Contain links:")
            for k, v in sorted(self.containmentLinks.items()):
                print(str(k) + ":" + str(v))

        #raise Exception()

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

    
    
    def buildContainmentDependenciesForClass(self, targetClass):
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
                    
                    #return [str(cRel.attributes['name'].value)].extend(self.buildContainmentDependenciesForClass(sourceClass))
                    res.extend([(srcClassName, str(cRel.attributes['name'].value), trgtClassName)])
                    
                    res.extend(self.buildContainmentDependenciesForClass(sourceClass))
        
        return res
        


    def getContainmentLinksForClasses(self):
        '''
        get all containment relations for the classes in the metamodel
        '''    
        
        allContainmentRels = {}
        metamodelClasses = self.xmldoc.getElementsByTagName('eClassifiers')
        
        for mmClass in metamodelClasses:
            allContainmentRels[str(mmClass.attributes['name'].value)] = self.buildContainmentDependenciesForClass(mmClass)

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
            
            if parentNames:
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

        mms = rule.vs["mm__"]
        attr1s = rule.vs["attr1"]

        for node in range(rule.vcount()):
            
#             if rule.vs[node]["mm__"] == "directLink_T":
#                 print("................ Containment link: " + rule.vs[node]["attr1"])
#                 print("................ self.containmentRels: " + str(self.containmentRels))
                
            if mms[node] == "directLink_T" and attr1s[node] in self.containmentRels:
                
                # find the types of the source and the target elements of the containment in the rule
                neighbours_out = rule.neighbors(node, 1)
                neighbours_in = rule.neighbors(node, 2)

                targetClassName = mms[neighbours_out[0]]
                sourceClassName = mms[neighbours_in[0]]

                link = (sourceClassName, attr1s[node])


                try:
                    if link not in containmentRelsInRule[targetClassName]:
                        containmentRelsInRule[targetClassName].append(link)
                except KeyError:
                    containmentRelsInRule[targetClassName] = [link]

        return containmentRelsInRule



    def getMissingContainmentLinks(self, rule):
        '''
        return all missing containment relations in a rule, in the form of a
        dictionary having as key the targetClass and as data the containmentLinks that 
        can be used to build the missing containment link.
        '''

        debug = False

        # if "HExitPoint2BProcDefWhetherOrNotExitPtHasOutgoingTrans" in rule.name or "3R0" in rule.name:
        #     debug = True
        #     print("\nExamining: " + rule.name)

        if debug:
            print("===========================")
            print("Examining: " + rule.name)

        missingContainmentLinks = {}

        try:
            mms = rule.vs["mm__"]
        except KeyError:
            return {}

        #print("Rule Name: " + pathCond.name)
        for node in range(len(mms)):
            targetClassName = mms[node]

            if targetClassName in ["trace_link", "MatchModel", "ApplyModel", "paired_with", "directLink_S", "directlink_T"]:
                continue

            class_inheri = [targetClassName]
            try:
                class_inheri += self.mmClassParents[targetClassName]
            except KeyError:
                pass

            has_links = False
            for cl in class_inheri:
                if cl in self.containmentLinks.keys():
                    has_links = True
            if not has_links:
                continue

            if debug:
                print("\nTarget Class: " + targetClassName)

            skip_match_nodes = False
            neighbours_in = rule.neighbors(node, 2)
            for n in neighbours_in:
                if mms[n] in ["MatchModel", "match_contains"]:
                    skip_match_nodes = True
                    break
            if skip_match_nodes:
                continue

            for cl in class_inheri:

                if cl in self.containmentLinks:

                    if debug:
                        print("\tClassname: " + str(cl) + ":")

                    for containLink in self.containmentLinks[cl]:
                        if debug:
                            print("\t\t" + str(containLink))
                        try:
                            if containLink not in missingContainmentLinks[targetClassName]:
                                missingContainmentLinks[targetClassName].append(containLink)
                        except KeyError:
                            missingContainmentLinks[targetClassName] = [containLink]

        if debug:
            if len(missingContainmentLinks) > 0:
                print("Missing containment links:")
                for link in missingContainmentLinks:
                    print(link + " : " + str(missingContainmentLinks[link]))
                #raise Exception()

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
