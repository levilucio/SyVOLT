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


from ecore_utils import EcoreUtils
from core.himesis_plus import buildPreListFromClassNames

from util.test_script_utils import select_rules, slice_transformation

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

from PropertyVerification.PropertyVerifier import PropertyVerifier


#positive


from ECore_Copier_MM.properties.positive.himesis.HProperty1_isolatedLHS import HProperty1_isolatedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty1_connectedLHS import HProperty1_connectedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty1_completeLHS import HProperty1_completeLHS

from ECore_Copier_MM.properties.positive.himesis.HProperty2_isolatedLHS import HProperty2_isolatedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty2_connectedLHS import HProperty2_connectedLHS
from ECore_Copier_MM.properties.positive.himesis.HProperty2_completeLHS import HProperty2_completeLHS




from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):
        pyramify = PyRamify(verbosity = args.verbosity, draw_svg=args.draw_svg)

        # full_transformation = [
        #     ['HEAttribute'],
        #
        #     ['HEClass',
        #     'HEDataType'],
        #
        #     ['HEEnum',
        #     'HEEnumLiteral'],
        #
        #     ['HEFactory',
        #     'HEOperation',
        #      'HEAnnotation'],
        #
        #     ['HEPackage',
        #     'HEParameter'],
        #
        #     ['HEReference',
        #     'HEStringToStringMapEntry'],
        #
        #     ['HeattributelefteTypeSolveRefEAttributeEClassifierEAttributeEClassifier'],
        #
        #     ['HeclasslefteOperationsSolveRefEClassEOperationEClassEOperation'],
        #     #        'HeclasslefteSuperTypesSolveRefEClassEClassEClassEClass']
        #
        #     ['HeenumlefteLiteralsSolveRefEEnumEEnumLiteralEEnumEEnumLiteral',
        #     'HefactoryleftePackageSolveRefEFactoryEPackageEFactoryEPackage'],
        #
        #     ['HeoperationlefteParametersSolveRefEOperationEParameterEOperationEParameter',
        #     'HeoperationlefteTypeSolveRefEOperationEClassifierEOperationEClassifier'],
        #
        #     ['HepackagelefteFactoryInstanceSolveRefEPackageEFactoryEPackageEFactory'],
        #     #'HepackagelefteSubpackagesSolveRefEPackageEPackageEPackageEPackage']
        #
        #     ['HeparameterlefteTypeSolveRefEParameterEClassifierEParameterEClassifier'],
        #     #'HereferencelefteOppositeSolveRefEReferenceEReferenceEReferenceEReference']
        #
        #     ['HereferencelefteTypeSolveRefEReferenceEClassifierEReferenceEClassifier',
        #     'HeclasslefteStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature'],
        #
        #     ['HeattributelefteAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation'
        #     'HedatatypelefteAnnotationsSolveRefEDataTypeEAnnotationEDataTypeEAnnotation'],
        #
        #     ['HeenumlefteAnnotationsSolveRefEEnumEAnnotationEEnumEAnnotation'],
        #
        #
        #     ['HeoperationlefteExceptionsSolveRefEOperationEClassifierEOperationEClassifier'],
        #
        #     ['HepackagelefteAnnotationsSolveRefEPackageEAnnotationEPackageEAnnotation'],
        #     ['HepackagelefteClassifiersSolveRefEPackageEClassifierEPackageEClassifier'],
        #
        #     ['HereferencelefteAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation'],
        #
        #     ['HereferencelefteKeysSolveRefEReferenceEAttributeEReferenceEAttribute']
        # ]

        full_transformation = [
            ['HEClass'], #a1
            ['HEClass_Copy'], #a1_2

            ['HEReference'], #b1
            ['HEReference_Copy'], #b1_2

            ['HeclassOUTeAnnotationsSolveRefEClassEAnnotationEClassEAnnotation'], #c1
            ['HeclassOUTeTypeParametersSolveRefEClassETypeParameterEClassETypeParameter'], #d1

            ['HeclassOUTeSuperTypesSolveRefEClassEClassEClassEClass'], #e1
            ['HeclassOUTeOperationsSolveRefEClassEOperationEClassEOperation'], #f1

            ['HeclassOUTeStructuralFeaturesSolveRefEClassEStructuralFeatureEClassEStructuralFeature'], #g1
            ['HeclassOUTeGenericSuperTypesSolveRefEClassEGenericTypeEClassEGenericType'], #h1

            ['HereferenceOUTeAnnotationsSolveRefEReferenceEAnnotationEReferenceEAnnotation'], #i1
            ['HereferenceOUTeTypeSolveRefEReferenceEClassifierEReferenceEClassifier'], #j1

            ['HereferenceOUTeGenericTypeSolveRefEReferenceEGenericTypeEReferenceEGenericType'], #k1
            ['HereferenceOUTeOppositeSolveRefEReferenceEReferenceEReferenceEReference'], #l1

            ['HereferenceOUTeKeysSolveRefEReferenceEAttributeEReferenceEAttribute'], #m1

            ['HeattributeOUTeAnnotationsSolveRefEAttributeEAnnotationEAttributeEAnnotation'], #n1
            ['HeattributeOUTeTypeSolveRefEAttributeEClassifierEAttributeEClassifier'], #o1

            ['HeattributeOUTeGenericTypeSolveRefEAttributeEGenericTypeEAttributeEGenericType'], #p1

            ['HEAttribute'] #q1
        ]



        # if self.slice_for_prop1:
        #  #15 rules
        #     transformation = [[a1], [a1_2], [b1], [b1_2], [c1], [d1], [e1], [f1], [g1], [h1], [i1], [j1], [k1], [l1], [m1]]
        # else:
        #  #17 rules
        #     transformation = [[a1], [b1], [q1], [c1], [d1], [e1], [f1], [g1], [h1], [i1], [j1], [k1], [l1], [m1], [n1], [o1],
        #                       [p1]]



        self.rules, self.transformation = pyramify.get_rules("ECore_Copier_Large_MM/transformation/", full_transformation)

        #print("Rules: " + str(self.rules.keys()))

        #make sure the superclasses are there
        subclasses_dict, superclasses_dict = self.get_sub_and_super_classes()

        for rule in self.rules.values():
            rule["superclasses_dict"] = superclasses_dict

        for layer in self.transformation:
            for rule in layer:
                rule["superclasses_dict"] = superclasses_dict


        prop1_atomic = AtomicStateProperty(HProperty1_isolatedLHS(), HProperty1_connectedLHS(), HProperty1_completeLHS())
        prop2_atomic = AtomicStateProperty(HProperty2_isolatedLHS(), HProperty2_connectedLHS(), HProperty2_completeLHS())

        # graph_to_dot("prop2_iso", HProperty2_isolatedLHS())
        # graph_to_dot("prop2_con", HProperty2_connectedLHS())
        # graph_to_dot("prop2_comp", HProperty2_completeLHS())

        #
        # #atomic_properties = [["HDaughterMother_atomic", HDaughterMother_atomic]]
        self.atomic_properties = [["prop1", prop1_atomic], ["prop2", prop2_atomic]]

        self.if_then_properties = []
        #
        # if_then_properties = [["HCommunityPerson", HCommunityPersonIfClause, HCommunityPersonThenClause]]
        #

        #print("Trans length before: " + str(len(self.transformation)))
        if args.slice > 0:
            contract = self.atomic_properties[args.slice - 1]
            contract[1].CompleteQuantified["superclasses_dict"] = superclasses_dict
            self.rules, self.transformation = slice_transformation(self.rules, self.transformation, contract, args)

        #print("Transformation:")
        #print("Trans length after: " + str(len(self.transformation)))
        # for layer in self.transformation:
        #     for rule in layer:
        #         print(rule.name)

        raise Exception()


    def test_correct_ecore_copier(self,args):

        pyramify = PyRamify(verbosity = args.verbosity, draw_svg=args.draw_svg)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns,
         self.ruleCombinators, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption] = \
            pyramify.ramify_directory("ECore_Copier_Large_MM/transformation/", self.transformation)

        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]

        subclasses_dict, superclasses_dict = self.get_sub_and_super_classes()

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)




        # def change_subtype_matching(match_rule, subclass_info):
        #     for v in match_rule.condition.vs():
        #         if v["mm__"] in set(subclass_info.keys()):
        #             v["MT_subtypes__"] = subclass_info[v["mm__"]]
        #             v["MT_subtypeMatching__"] = True
        #             print("Changed one: " + v["mm__"])
                                                                  
        
        # add polymorphism for the matchers
        for matcher_key in self.matchRulePatterns.keys():
            self.matchRulePatterns[matcher_key][0].condition["superclasses_dict"] = supertypes
            #change_subtype_matching(self.matchRulePatterns[matcher_key][0],subclasses_dict)
            
        # add polymorphism for the combinators
        for combs_key in self.ruleCombinators.keys():
            if self.ruleCombinators[combs_key] != None:
                for combinator in self.ruleCombinators[combs_key]:
                    combinator[0].condition["superclasses_dict"] = supertypes
                    #change_subtype_matching(combinator[0],subclasses_dict)

        # add polymorphism for the tracers
        for tracer_key in self.ruleTraceCheckers.keys():
            if self.ruleTraceCheckers[tracer_key] != None:
                self.ruleTraceCheckers[tracer_key].condition["superclasses_dict"] = supertypes
                #change_subtype_matching(self.ruleTraceCheckers[tracer_key],subclasses_dict)


        s = PathConditionGenerator(self.transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, self.overlapping_rules, self.subsumption, self.loopingRuleSubsumption, args)#
   
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()

        print(s.num_path_conditions)
            
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))


#         print("printing path conditions")
#         s.print_path_conditions_screen()
        
        
        # check for reachability of rules
        #
        # for layer in s.transformation:
        #     for rule in layer:
        #         StateProperty.checkRuleReachability(s.rule_names[rule.name], s)


        #s.print_path_conditions_file()


         #
        # #s.verbosity = 2
        #
        #
        # # finalresult = StateProperty.verifyCompositeStateProperty(s, HCommunityPerson1)
        # # if finalresult:
        # #     print("Atomic property: " +"HCommunityPerson1" + " holds")
        # # else:
        # #     print("Atomic property: " + "HCommunityPerson1" + " does not hold")
        #
        #

        verifier = StateProperty()
        for name, atomic_prop in self.atomic_properties:
            ts0 = time.time()
            finalresult = verifier.verifyCompositeStateProperty(s, atomic_prop)
            ts1 = time.time()
            if len(finalresult) == 0:
                print("Atomic property: " + name + " holds\n")
            else:
                print("Atomic property: " + name + " does not hold\n")
            print("Took " + str(ts1 - ts0) + " time to verify ")
        #
        # for name, i, t in self.if_then_properties:
        #     finalresult = verifier.verifyCompositeStateProperty(s, ImplicationStateProperty(i, t))
        #     if len(finalresult) == 0:
        #         print("If-then property: " + name + " holds\n")
        #     else:
        #         print("If-then property: " + name + " does not hold\n")
        #
        # ts1 = time.time()
        #
        # prop_length = len(self.atomic_properties) + len(self.if_then_properties)
        # print("\n\nTime to verify " + str(prop_length) + " properties: " + str(ts1 - ts0))


    def get_sub_and_super_classes(self):


        subclasses_dict = {}
        eu1 = EcoreUtils("ECore_Copier_MM/Ecore.ecore")
        subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(eu1.getMetamodelClassNames())
        subclasses_dict["MT_pre__EStructuralFeature"] = ["MT_pre__EAttribute", "MT_pre__EReference"]
        subclasses_dict["MT_pre__ModelElement"] = ["MT_pre__EAnnotation", "MT_pre__EFactory", "MT_pre__ENamedElement"]
        subclasses_dict["MT_pre__EClassifier"] = ["MT_pre__EClass", "MT_pre__EDataType"]
        subclasses_dict["MT_pre__EDataType"] = ["MT_pre__EEnum"]
        subclasses_dict["MT_pre__ENamedElement"] = ["MT_pre__EEnumLiteral", "MT_pre__ENamedElement", "MT_pre__EPackage",
                                                    "MT_pre__ETypedElement"]
        subclasses_dict["MT_pre__EObject"] = ["MT_pre__EModelElement"]
        subclasses_dict["MT_pre__ETypedElement"] = ["MT_pre__EOperation", "MT_pre__EParameter",
                                                    "MT_pre__EStructuralFeature"]

        #TODO: Is this an error?
        #subclasses_dict["MT_pre__EStructuralFeature"] = ["MT_pre__EReference"]

        eu2 = EcoreUtils("ECore_Copier_Large_MM/Ecore.ecore")
        subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(eu2.getMetamodelClassNames())

        # keep a dictionary from each child to its parent
        supertypes = {}

        for supertype in subclasses_dict:
            for subtype in subclasses_dict[supertype]:
                subtype = subtype[8:]
                try:
                    supertypes[subtype].append(supertype[8:])
                except KeyError:
                    supertypes[subtype] = [supertype[8:]]

        return subclasses_dict, supertypes


def _print_states(self,s):
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

    parser.add_argument('--compression', type = int, default = 6,
                        help = 'Level of compression to use with pickling. Range: 0 (no compression) to 9 (high compression) (default: 6)')
    parser.set_defaults(compression = 6)

    parser.add_argument('--slice', type = int, default = 0,
                        help = 'Index of contract to slice for. Range: 0 (no slicing) to #CONTRACTS (default: 0)')
    parser.set_defaults(slice = 0)

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

    
