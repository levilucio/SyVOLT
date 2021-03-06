'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time
import sys

from path_condition_generator import PathConditionGenerator

from t_core.matcher import Matcher
from t_core.messages import Packet

from PyRamify import PyRamify

from core.himesis_utils import graph_to_dot


from util.ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules


from PropertyVerification.state_property import StateProperty
from PropertyVerification.atomic_state_property import AtomicStateProperty
from PropertyVerification.and_state_property import AndStateProperty
from PropertyVerification.or_state_property import OrStateProperty
from PropertyVerification.not_state_property import NotStateProperty
from PropertyVerification.implication_state_property import ImplicationStateProperty
from PropertyVerification.Not import Not #StateSpace Prop
from PropertyVerification.Implication import Implication #StateSpace Prop
from PropertyVerification.And import And #StateSpace Prop
from PropertyVerification.Or import Or #StateSpace Prop
from PropertyVerification.BACKUP_atomic_state_property import BKUPAtomicStateProperty
#from lib2to3.fixer_util import p1

from PropertyVerification.PropertyVerifier import PropertyVerifier


#positive

from FamiliesToPersons_MM.Properties.Positive.Himesis.HEmpty_IsolatedConnectedLHS import HEmpty_IsolatedConnectedLHS

from ECore_Copier_MM.properties.positive.himesis.HProperty1_isolatedLHS import HProperty1_isolatedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty1_connectedLHS import HProperty1_connectedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty1_completeLHS import HProperty1_completeLHS

#negative
from ECore_Copier_MM.properties.positive.himesis.HProperty2_isolatedLHS import HProperty2_isolatedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty2_connectedLHS import HProperty2_connectedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty2_completeLHS import HProperty2_completeLHS





from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):
        pyramify = PyRamify(verbosity=args.verbosity, draw_svg=args.draw_svg)
        self.rules = pyramify.get_rules("ECore_Copier_Large_MM/transformation/")



        #print("Rules: " + str(self.rules.keys()))


    def select_rules(self, full_transformation, num_rules):
        selected_transformation = []

        print("Selecting " + str(num_rules) + " rules")

        i = 1
        for layer in range(len(full_transformation)):
            selected_transformation.append([])
            for rule in full_transformation[layer]:
                selected_transformation[layer].append(rule)
                i += 1
                if i > num_rules:
                    print("Returning: " + str(selected_transformation))
                    return selected_transformation

    def test_correct_ecore_copier(self,args):
        
        self.slice_for_prop1 = False

        pyramify = PyRamify(verbosity = args.verbosity, draw_svg=args.draw_svg)

        a1 = self.rules['HEClass']
        a1_2 = self.rules['HEClass_Copy']
        
        b1 = self.rules['HEReference']
        b1_2 = self.rules['HEReference_Copy']

        c1 = self.rules['HeclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation']
        d1 = self.rules['HeclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter']

        e1 = self.rules['HeclassOUTeSuperTypesSolveRefEClassEClassEClassEClass']
        f1 = self.rules['HeclassOUTeOperationsSolveRefEClassEOperationEClassEOperation']

        g1 = self.rules['HeclassOUTeStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature']
        h1 = self.rules['HeclassOUTeGenericSuperTypesSolveRefEClassEGenericTypeEClassEGenericType']

        i1 = self.rules['HereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation']
        j1 = self.rules['HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier']

        k1 = self.rules['HereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType']
        l1 = self.rules['HereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference']

        m1 = self.rules['HereferenceOUTeKeysSolveRefEReferenceEAttributeEReferenceEAttribute']

        n1 = self.rules['HeattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation']
        o1 = self.rules['HeattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier']

        p1 = self.rules['HeattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType']

        q1 = self.rules['HEAttribute']




        #get the expected num from the args
        #expected_num_pcs = args.num_pcs
        expected_num_pcs = 330
                
        #TODO: Change this number if you are modifying the transformation at all
        #if args.num_rules == -1:
        
        if self.slice_for_prop1:
            transformation = [[a1], [a1_2], [b1], [b1_2], [c1], [d1], [e1], [f1], [g1], [h1], [i1], [j1], [k1], [l1], [m1]]
            #transformation = [[a1], [a1_2], [b1],  [g1]]
        else:
            transformation = [[a1], [b1], [q1], [c1], [d1], [e1], [f1], [g1], [h1], [i1], [j1], [k1], [l1], [m1], [n1], [o1], [p1]]            

        #else:
        #    transformation = self.select_rules([[a1,a2], [b1,b2,b3], [c1,c2,c3], [d1,d2,d3], [e1,e2,e3,e4], [f1]], args.num_rules)

        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        subclasses_dict = {}
        eu1 = EcoreUtils("ECore_Copier_Large_MM/Ecore.ecore")
        subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(eu1.getMetamodelClassNames())
        

        
        subclasses_dict["MT_pre__EStructuralFeature"] = ["MT_pre__EAttribute", "MT_pre__EReference"]
        subclasses_dict["MT_pre__ModelElement"] = ["MT_pre__EAnnotation", "MT_pre__EFactory", "MT_pre__ENamedElement"]
        subclasses_dict["MT_pre__EClassifier"] = ["MT_pre__EClass", "MT_pre__EDataType"]
        subclasses_dict["MT_pre__EDataType"] = ["MT_pre__EEnum"]
        subclasses_dict["MT_pre__ENamedElement"] = ["MT_pre__EEnumLiteral", "MT_pre__ENamedElement", "MT_pre__EPackage", "MT_pre__ETypedElement"]        
        subclasses_dict["MT_pre__EObject"] = ["MT_pre__EModelElement"]    
        subclasses_dict["MT_pre__ETypedElement"] = ["MT_pre__EOperation", "MT_pre__EParameter", "MT_pre__EStructuralFeature"]  
        subclasses_dict["MT_pre__EStructuralFeature"] = ["MT_pre__EReference"]
             
         
        eu2 = EcoreUtils("ECore_Copier_Large_MM/Ecore.ecore")
        subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(eu2.getMetamodelClassNames())

        #print subclasses_dict

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators] = \
            pyramify.ramify_directory("ECore_Copier_Large_MM/transformation/", transformation)

        def change_subtype_matching(match_rule, subclass_info, verbosity = 0):
            for v in match_rule.condition.vs():
                if v["mm__"] in set(subclass_info.keys()):
                    v["MT_subtypes__"] = subclass_info[v["mm__"]]
                    v["MT_subtypeMatching__"] = True

                    if verbosity > 0:
                        print("Changing subtypes for " + v["mm__"] + " to " + str(v["MT_subtypes__"]))
                    #print "Changed one: " + v["mm__"]
                                                                   
         
        # add polymorphism for the matchers
        for matcher_key in self.matchRulePatterns.keys():
            change_subtype_matching(self.matchRulePatterns[matcher_key][0],subclasses_dict)
             
        # add polymorphism for the combinators
        for combs_key in self.ruleCombinators.keys():
            if self.ruleCombinators[combs_key] != None:
                for combinator in self.ruleCombinators[combs_key]:
                    change_subtype_matching(combinator[0],subclasses_dict)
 
        # add polymorphism for the tracers
        for tracer_key in self.ruleTraceCheckers.keys():
            if self.ruleTraceCheckers[tracer_key] != None:
                change_subtype_matching(self.ruleTraceCheckers[tracer_key],subclasses_dict)    
 
        s = PathConditionGenerator(transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, args)#
    
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
 
        print(s.num_path_conditions)
             
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))
 
#         #check if the correct number of path conditions were produced
#         if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:
#  
#             #TODO: Make this an exception
#             num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
#             print(num_pcs_s)
#            raise Exception(num_pcs_s)
 
        print("printing path conditions")
        #s.print_path_conditions_screen()
        
        
        # check for reachability of rules
        
#         for layer in s.transformation:
#             for rule in layer:
#                 StateProperty.checkRuleReachability(s.rule_names[rule.name], s)

        #s.print_path_conditions_file()

        print("\nProperty proving:")

        s.verbosity = 0


        # HFourMembers_atomic = AtomicStateProperty(HFourMembers_IsolatedLHS(), HFourMembers_ConnectedLHS(), HFourMembers_CompleteLHS())
        #
        #
        # HMotherFather_atomic = AtomicStateProperty(HMotherFather_IsolatedLHS(), HMotherFather_ConnectedLHS(), HMotherFather_CompleteLHS())
        #
        #
        # HDaughterMother_atomic = AtomicStateProperty(HDaughterMother_IsolatedLHS(), HDaughterMother_ConnectedLHS(), HDaughterMother_CompleteLHS())
        #
        #
        #
        # # HCommunityPersonIfClause = AtomicStateProperty(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(), HCommunityPerson1_CompleteLHS())
        # #
        # #
        # # HCommunityPersonThenClause = AndStateProperty(
        # #     AtomicStateProperty(HCommunityPerson1_IsolatedLHS(), HCommunityPerson1_ConnectedLHS(),
        # #         HCommunityPerson1_CompleteLHS()),
        # #     NotStateProperty(
        # #         AtomicStateProperty(HCommunityPerson2_IsolatedLHS(), HCommunityPerson2_ConnectedLHS(),
        # #             HCommunityPerson2_CompleteLHS())))
        #
        #
        # HCommunityPersonIfClause = AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(),
        #     HCommunityPerson1_CompleteLHS())
        #
        # HCommunityPersonThenClause = NotStateProperty(
        #         AtomicStateProperty(HEmpty_IsolatedConnectedLHS(), HEmpty_IsolatedConnectedLHS(),
        #             HCommunityPerson2_CompleteLHS()))
        #
        #
        #
        Atomic1 = AtomicStateProperty(HProperty1_isolatedLHS(), HProperty1_connectedLHS(), HProperty1_completeLHS())
        Atomic2 = AtomicStateProperty(HProperty2_isolatedLHS(), HProperty2_connectedLHS(), HProperty2_completeLHS())
        #
        # #graph_to_dot("HCommunityPerson1_IsolatedLHS", HCommunityPerson1_IsolatedLHS())
        #
        #
        # #graph_to_dot("HCommunityPerson1_ConnectedLHS", HCommunityPerson1_ConnectedLHS())
        #
        # #graph_to_dot("HCommunityPerson1_CompleteLHS", HCommunityPerson1_CompleteLHS())
        #
        #
        # #graph_to_dot("HCommunityPerson1_CompleteLHS", HCommunityPerson1_CompleteLHS())
        # #graph_to_dot("HCommunityPerson2_CompleteLHS", HCommunityPerson2_CompleteLHS())
        #
        # if args.draw_svg:
        #     graph_to_dot("HDaughterMother_ConnectedLHS", HDaughterMother_ConnectedLHS())
        #     graph_to_dot("HDaughterMother_CompleteLHS", HDaughterMother_CompleteLHS())
        #
        #     graph_to_dot("HMotherFather_IsolatedLHS", HMotherFather_IsolatedLHS())
        #     graph_to_dot("HMotherFather_ConnectedLHS", HMotherFather_ConnectedLHS())
        #     graph_to_dot("HMotherFather_CompleteLHS", HMotherFather_CompleteLHS())
        #
        #     #graph_to_dot("HMotherFather_CompleteLHS", HMotherFather_CompleteLHS())
        #     #graph_to_dot("HDaughterMother_CompleteLHS", HDaughterMother_CompleteLHS())
        #
        #     #
        #
        #     #
        #     # for state in s.get_path_conditions():
        #     #     graph_to_dot(state.name, state)
        #
        # #atomic_properties = [["HDaughterMother_atomic", HDaughterMother_atomic]]
        atomic_properties = []
        if self.slice_for_prop1:
            atomic_properties.append(["Property1", Atomic1])

        else:
            atomic_properties.append(["Property2", Atomic2])
        #
        if_then_properties = []#["HCommunityPerson", HCommunityPersonIfClause, HCommunityPersonThenClause]]
        #
        #
        # #s.verbosity = 2


        # finalresult = StateProperty.verifyCompositeStateProperty(s, HCommunityPerson1)
        # if finalresult:
        #     print("Atomic property: " +"HCommunityPerson1" + " holds")
        # else:
        #     print("Atomic property: " + "HCommunityPerson1" + " does not hold")


        for name, atomic_prop in atomic_properties:
            finalresult = StateProperty.verifyCompositeStateProperty(s, atomic_prop)
            if len(finalresult) == 0:
                print("Atomic property: " + name + " holds\n")
            else:
                print("Atomic property: " + name + " does not hold\n")

        for name, i, t in if_then_properties:
            finalresult = StateProperty.verifyCompositeStateProperty(s, ImplicationStateProperty(i, t))
            if len(finalresult) == 0:
                print("If-then property: " + name + " holds\n")
            else:
                print("If-then property: " + name + " does not hold\n")

        ts1 = time.time()

        prop_length = len(atomic_properties) + len(if_then_properties)
        print("\n\nTime to verify " + str(prop_length) + " properties: " + str(ts1 - ts0))


def _print_states(self, s):
    for state in s.symbStateSpace:
        print("----------")
        if state == ():
            print('Empty')
        else:
            for s in state:
                print(s.name)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run the ecore_copier test.')
    parser.add_argument('--skip_tests', dest = 'run_tests', action = 'store_false',
                        help = 'Option to skip the running of matching tests')
    parser.set_defaults(run_tests = True)

    parser.add_argument('--skip_parallel', dest = 'do_parallel', action = 'store_false',
                        help = 'Option to force computation to run single-thread')
    parser.set_defaults(do_parallel = True)

    parser.add_argument('--skip_pickle', dest = 'do_pickle', action = 'store_false',
                        help = 'Option to skip the use of pickling')
    parser.set_defaults(do_pickle = True)

    parser.add_argument('--no_svg', dest = 'draw_svg', action = 'store_false',
                        help = 'Flag to force svg files to not be drawn')
    parser.set_defaults(draw_svg = True)

    parser.add_argument('--num_pcs', type = int, default = -1,
                        help = 'Number of path conditions which should be produced by this test (default: -1)')

    parser.add_argument('--num_rules', type = int, default = -1,
                        help = 'Number of rules in the transformation (default: -1)')

    parser.add_argument('--verbosity', type = int, default = 0,
                        help = 'Verbosity level (default: 0 - minimum output)')


    args = parser.parse_args()


    ecore_copier = Test()
    ecore_copier.setUp(args)
    ecore_copier.test_correct_ecore_copier(args)

    
