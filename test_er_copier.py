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

from ER_Copier_MM.properties.positive.Himesis.HProperty1_isolatedLHS import HProperty1_isolatedLHS
from ER_Copier_MM.properties.positive.Himesis.HProperty1_connectedLHS import HProperty1_connectedLHS
from ER_Copier_MM.properties.positive.Himesis.HProperty1_completeLHS import HProperty1_completeLHS

from property_prover_rules.HEmptyPathCondition import HEmptyPathCondition
##Pattern COntract - END
class Test():

    def setUp(self, args):
        pyramify = PyRamify(draw_svg=args.draw_svg)

        [self.rules, self.ruleTraceCheckers, backwardPatterns2Rules, backwardPatternsComplete, self.matchRulePatterns, self.ruleCombinators] = \
            pyramify.ramify_directory("ER_Copier_MM/transformation/")

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

        pyramify = PyRamify(verbosity = 2)



        a1 = self.rules['HAttribute']

        b1 = self.rules['HEntityType']
        c1 = self.rules['HERModel']

        d1 = self.rules['HStrongReference']
        e1 = self.rules['HWeakReference']


        f1 = self.rules['HentitytypeOUTfeaturesSolveRefEntityTypeFeatureEntityTypeFeature']
        g1 = self.rules['HermodelOUTentitiesSolveRefERModelEntityTypeERModelEntityType']

        h1 = self.rules['HstrongreferenceOUTtypeSolveRefStrongReferenceEntityTypeStrongReferenceEntityType']
        i1 = self.rules['HweakreferenceOUTtypeSolveRefWeakReferenceEntityTypeWeakReferenceEntityType']




        #get the expected num from the args
        #expected_num_pcs = args.num_pcs
        expected_num_pcs = 330
                
        #TODO: Change this number if you are modifying the transformation at all
        #if args.num_rules == -1:
        transformation = [[a1], [b1], [c1], [d1], [e1], [f1], [g1], [h1], [i1]]
        
        #else:
        #    transformation = self.select_rules([[a1,a2], [b1,b2,b3], [c1,c2,c3], [d1,d2,d3], [e1,e2,e3,e4], [f1]], args.num_rules)


        #transformation =[[a1], [ b3]]
        #transformation =[[a1], [b1,b2,b3], [c1,c2,c3], [d1,d2,d3], [e1,e2,e3,e4], [f1]]
        pre_metamodel = ["MT_pre__S_MM", "MoTifRule"]
        post_metamodel = ["MT_post__T_MM", "MoTifRule"]
        

        subclasses_dict = {}

        eu1 = EcoreUtils("ER_Copier_MM/ER_MM.ecore")
        subclasses_dict["MT_pre__MetaModelElement_S"] = buildPreListFromClassNames(eu1.getMetamodelClassNames())
        subclasses_dict["MT_pre__Reference"] = ["MT_pre__WeakReference", "MT_pre__StrongReference"]
        subclasses_dict["MT_pre__Feature"] = ["MT_pre__Reference", "MT_pre__ERAttribute"]

        eu2 = EcoreUtils("ER_Copier_MM/ER_MM.ecore")
        subclasses_dict["MT_pre__MetaModelElement_T"] = buildPreListFromClassNames(eu2.getMetamodelClassNames())

        pyramify.changePropertyProverMetamodel(pre_metamodel, post_metamodel, subclasses_dict)
        
        # now go through all the matchers, combinators and tracers to add polymorphism on all classes in an
        # inheritance hierarchy
        
        def change_subtype_matching(match_rule, subclass_info):
            for v in match_rule.condition.vs():
                if v["mm__"] in set(subclass_info.keys()):
                    v["MT_subtypes__"] = subclass_info[v["mm__"]]
                    v["MT_subtypeMatching__"] = True
                    print "Changed one: " + v["mm__"]
                                                                  
        
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
            

        s = PathConditionGenerator(transformation, self.ruleCombinators, self.ruleTraceCheckers, self.matchRulePatterns, 1, draw_svg=args.draw_svg, run_tests=args.run_tests)#
    
        ts0 = time.time()
        s.build_path_conditions()
        ts1 = time.time()
 
        print(s.num_path_conditions)
             
        print("\n\nTime to build the set of path conditions: " + str(ts1 - ts0))
#        print("Size of the set of path conditions: " + str(float(sys.getsizeof(s.pathConditionSet) / 1024)))
        print("Number of path conditions: " + str(s.num_path_conditions))
 
        #check if the correct number of path conditions were produced
        if not int(expected_num_pcs) == -1 and not int(expected_num_pcs) == s.num_path_conditions:
 
            #TODO: Make this an exception
            num_pcs_s = "The number of produced path conditions is incorrect.\n" + str(expected_num_pcs) + " were expected, but " + str(s.num_path_conditions) + " were produced."
            print(num_pcs_s)
            #raise Exception(num_pcs_s)
  
        # print("printing path conditions")
        # #s.print_path_conditions_screen()
        #
        # # check for reachability of rules
        #
        # for layer in s.transformation:
        #     for rule in layer:
        #         StateProperty.checkRuleReachability(s.rule_names[rule.name], s)
        #
        #
        # #s.print_path_conditions_file()
        #
        # prop1_atomic = AtomicStateProperty(HProperty1_isolatedLHS(), HProperty1_connectedLHS(),
        #     HProperty1_completeLHS())
        #
        # graph_to_dot("prop1_iso", HProperty1_isolatedLHS())
        # graph_to_dot("prop1_con", HProperty1_connectedLHS())
        # graph_to_dot("prop1_comp", HProperty1_completeLHS())
        #
        # #
        # # #atomic_properties = [["HDaughterMother_atomic", HDaughterMother_atomic]]
        # atomic_properties = [["prop1", prop1_atomic]]
        #
        # for name, atomic_prop in atomic_properties:
        #     ts0 = time.time()
        #     finalresult = StateProperty.verifyCompositeStateProperty(s, atomic_prop)
        #     ts1 = time.time()
        #     if len(finalresult) == 0:
        #         print("Atomic property: " + name + " holds\n")
        #     else:
        #         print("Atomic property: " + name + " does not hold\n")
        #     print("Took " + str(ts1 - ts0) + " time to verify ")



def _print_states(self,s):
        for state in s.symbStateSpace:
            print "----------"
            if state == ():
                print 'Empty'
            else:
                for s in state:
                    print s.name


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Run the ecore_copier test.')
    parser.add_argument('--skip_tests', dest = 'run_tests', action = 'store_false',
                        help = 'Option to skip the running of matching tests')
    parser.set_defaults(run_tests = True)

    parser.add_argument('--no_svg', dest = 'draw_svg', action = 'store_false',
                        help = 'Flag to force svg files to not be drawn')
    parser.set_defaults(draw_svg = True)

    parser.add_argument('--num_pcs', type = int, default = -1,
                        help = 'Number of path conditions which should be produced by this test (default: -1)')

    parser.add_argument('--num_rules', type = int, default = -1,
                        help = 'Number of rules in the transformation (default: -1)')
    args = parser.parse_args()


    ecore_copier = Test()
    ecore_copier.setUp(args)
    ecore_copier.test_correct_ecore_copier(args)

    
