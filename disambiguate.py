'''
Created on 2015-08-08

@author: levi
'''

from copy import deepcopy


from core.himesis_utils import graph_to_dot
from t_core.tc_python.arule import ARule
from t_core.tc_python.frule import FRule

from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter
from t_core.iterator import Iterator

from property_prover_rules.disambiguation_rules.Himesis.HFindTwoMatchElementsSameTypeDiffRulesLHS import HFindTwoMatchElementsSameTypeDiffRulesLHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputDirectLHS import HMoveOneInputDirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputDirectRHS import HMoveOneInputDirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputRepeatedDirectLHS import HMoveOneInputRepeatedDirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputRepeatedDirectRHS import HMoveOneInputRepeatedDirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputDirectLHS import HMoveOneOutputDirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputDirectRHS import HMoveOneOutputDirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputRepeatedDirectLHS import HMoveOneOutputRepeatedDirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputRepeatedDirectRHS import HMoveOneOutputRepeatedDirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputIndirectLHS import HMoveOneInputIndirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputIndirectRHS import HMoveOneInputIndirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputRepeatedIndirectLHS import HMoveOneInputRepeatedIndirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneInputRepeatedIndirectRHS import HMoveOneInputRepeatedIndirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputIndirectLHS import HMoveOneOutputIndirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputIndirectRHS import HMoveOneOutputIndirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputRepeatedIndirectLHS import HMoveOneOutputRepeatedIndirectLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneOutputRepeatedIndirectRHS import HMoveOneOutputRepeatedIndirectRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneTraceLHS import HMoveOneTraceLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneTraceRHS import HMoveOneTraceRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneEquationsRightExpressionLHS import HMoveOneEquationsRightExpressionLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneEquationsRightExpressionRHS import HMoveOneEquationsRightExpressionRHS

from property_prover_rules.disambiguation_rules.Himesis.HMoveOneEquationsLeftExpressionLHS import HMoveOneEquationsLeftExpressionLHS
from property_prover_rules.disambiguation_rules.Himesis.HMoveOneEquationsLeftExpressionRHS import HMoveOneEquationsLeftExpressionRHS

from property_prover_rules.disambiguation_rules.Himesis.HDelOneAttributeFromUncollapsedElemLHS import HDelOneAttributeFromUncollapsedElemLHS
from property_prover_rules.disambiguation_rules.Himesis.HDelOneAttributeFromUncollapsedElemRHS import HDelOneAttributeFromUncollapsedElemRHS

from property_prover_rules.disambiguation_rules.Himesis.HDeleteUncollapsedElementLHS import HDeleteUncollapsedElementLHS
from property_prover_rules.disambiguation_rules.Himesis.HDeleteUncollapsedElementRHS import HDeleteUncollapsedElementRHS

#from solver.z3_attribute_equation_evaluator import AttributeEquationEvaluator
from solver.simple_attribute_equation_evaluator import SimpleAttributeEquationEvaluator
# declare all the needed TCore rules

find_elements_collapse_match = Matcher(HFindTwoMatchElementsSameTypeDiffRulesLHS())

# merge_cardinalities_matchmodel = ARule(HMergeCardinalitiesMatchDiffRulesLHS(), HMergeCardi1nalitiesMatchDiffRulesRHS())

move_input_direct = FRule(HMoveOneInputDirectLHS(), HMoveOneInputDirectRHS())
move_input_repeated_direct = FRule(HMoveOneInputRepeatedDirectLHS(), HMoveOneInputRepeatedDirectRHS())
move_output_direct = FRule(HMoveOneOutputDirectLHS(), HMoveOneOutputDirectRHS())
move_output_repeated_direct = FRule(HMoveOneOutputRepeatedDirectLHS(), HMoveOneOutputRepeatedDirectRHS())

move_input_indirect = FRule(HMoveOneInputIndirectLHS(), HMoveOneInputIndirectRHS())
move_input_repeated_indirect = FRule(HMoveOneInputRepeatedIndirectLHS(), HMoveOneInputRepeatedIndirectRHS())
move_output_indirect = FRule(HMoveOneOutputIndirectLHS(), HMoveOneOutputIndirectRHS())
move_output_repeated_indirect = FRule(HMoveOneOutputRepeatedIndirectLHS(), HMoveOneOutputRepeatedIndirectRHS())

move_trace = FRule(HMoveOneTraceLHS(), HMoveOneTraceRHS())

move_right_expression_of_equation = FRule(HMoveOneEquationsRightExpressionLHS(), HMoveOneEquationsRightExpressionRHS())
move_left_expression_of_equation = FRule(HMoveOneEquationsLeftExpressionLHS(), HMoveOneEquationsLeftExpressionRHS())

delete_uncollapsed_element = FRule(HDeleteUncollapsedElementLHS(), HDeleteUncollapsedElementRHS())
delete_attributes_from_uncollapsed_element = FRule(HDelOneAttributeFromUncollapsedElemLHS(), HDelOneAttributeFromUncollapsedElemRHS())


class Disambiguator():
    """
    The disambiguator allows building all possibilities of transformation executions where injective matches exist between those
    transformation executions and the match part of each rule in the path condition. Note that in general we assume each rule in
    the path condition executes only once during the transformation execution.
    More details can be found in:
    http://msdl.cs.mcgill.ca/people/levi/30_publications/files/A_Technique_for_Symbolically_Verifying_Properties_of_Model_Transf.pdf (section 5)
    """
    
    def __init__(self, verbosity):
        self.verbosity = verbosity
        self.attributeEquationEvaluator = SimpleAttributeEquationEvaluator(verbosity)

        if True:
            graph_to_dot("HFindTwoMatchElementsSameTypeDiffRulesLHS", HFindTwoMatchElementsSameTypeDiffRulesLHS())

            graph_to_dot("HMoveOneInputDirectLHS", HMoveOneInputDirectLHS())
            graph_to_dot("HMoveOneInputRepeatedDirectLHS", HMoveOneInputRepeatedDirectLHS())
            graph_to_dot("HMoveOneOutputDirectLHS", HMoveOneOutputDirectLHS())
            graph_to_dot("HMoveOneOutputRepeatedDirectLHS", HMoveOneOutputRepeatedDirectLHS())

            graph_to_dot("HMoveOneInputDirectRHS", HMoveOneInputDirectRHS())
            graph_to_dot("HMoveOneInputRepeatedDirectRHS", HMoveOneInputRepeatedDirectRHS())
            graph_to_dot("HMoveOneOutputDirectRHS", HMoveOneOutputDirectRHS())
            graph_to_dot("HMoveOneOutputRepeatedDirectRHS", HMoveOneOutputRepeatedDirectRHS())

            graph_to_dot("HMoveOneTraceLHS", HMoveOneTraceLHS())
            graph_to_dot("HMoveOneTraceRHS", HMoveOneTraceRHS())

            graph_to_dot("HDeleteUncollapsedElementLHS", HDeleteUncollapsedElementLHS())
            graph_to_dot("HDeleteUncollapsedElementRHS", HDeleteUncollapsedElementRHS())

    def _collapse_step(self, path_condition):
        """
        Perform a step of merging two objects the same type, but belonging to different rules, in the match part of the path condition.
        The merge step make all objects originally pointing to the second object point to the first object.
        Additionally, all equations pointing to attributes of the second object will point to the first object.
        The first object will be part of its original rule and also of the rule of the second object.    
        """
        
        disambiguated_solutions = []

        p = Packet()        
        i = Iterator()
        
        p.graph = path_condition

        #graph_to_dot("packet", p.graph)

        p = find_elements_collapse_match.packet_in(p)

        if self.verbosity >= 2: print 'Found collapsable elements:' + str(find_elements_collapse_match.is_success)

        #print("Size of match sets: " + str(p.match_sets))

        
        if not find_elements_collapse_match.is_success:   #identifies 2 things in different rules
            print("Could not find two elements to collapse")
            return []


        for k in p.match_sets.keys():
            match_set = p.match_sets[k]
            match_set.print_matches(path_condition)


        p = i.packet_in(p) #iterates on all matches

        j=0

        # continue while more pairs of elements can be collapsed
        while i.is_success: #operation of iterator worked

            p2 = deepcopy(p)
            p2.graph = deepcopy(p.graph)

            #print("I is success")

            #                 p = merge_cardinalities_matchmodel.packet_in(p)
            #                 if self.verbosity >= 2: print 'merge_cardinalities_matchmodel:' + str( merge_cardinalities_matchmodel.is_success)

            p2 = move_input_repeated_direct.packet_in(p2)
            if self.verbosity >= 2: print 'move_input_repeated_direct_matchmodel: ' + str(move_input_repeated_direct.is_success)

            if not move_input_repeated_direct.is_success: #repeated already have a link of the same type
                # not repeated - dont have it there so u copy on top
                # direct/indirect and whether theyr going in/out of second element


                #graph_to_dot("move_input_direct_LHS", HMoveOneInputDirectLHS())
                #graph_to_dot("move_input_direct_RHS", HMoveOneInputDirectRHS())
                #graph_to_dot("move_input_repeated_direct_LHS", HMoveOneInputRepeatedDirectLHS())
                #graph_to_dot("move_input_repeated_direct_RHS", HMoveOneInputRepeatedDirectRHS())


                #i2 = Iterator()
                #p3 = i2.packet_in(p2)
                #print("Checking move_input_direct_matchmodel: " + str(j))
                j +=1
                #print("Global pivots: " + str(p2.global_pivots))
                p2 = move_input_direct.packet_in(p2) #direct link going in
                if self.verbosity >= 2: print 'move_input_direct_matchmodel: ' + str(move_input_direct.is_success)

                #print("Checking move_output_repeated_direct_matchmodel")
                p2 = move_output_repeated_direct.packet_in(p2) #direct link going out
                if self.verbosity >= 2: print 'move_output_repeated_direct_matchmodel: ' + str(move_output_repeated_direct.is_success)
                if not move_output_repeated_direct.is_success:
                    p2 = move_output_direct.packet_in(p2)
                    if self.verbosity >= 2: print 'move_output_direct_matchmodel: ' + str(move_output_direct.is_success)

                p2 = move_input_repeated_indirect.packet_in(p2)
                if self.verbosity >= 2: print 'move_input_repeated_indirect_matchmodel: ' + str(move_input_repeated_indirect.is_success)
                if not move_input_repeated_indirect.is_success:
                    p2 = move_input_indirect.packet_in(p2)
                    if self.verbosity >= 2: print 'move_input_indirect_matchmodel: ' + str(move_input_indirect.is_success)

                p2 = move_output_repeated_indirect.packet_in(p2)
                if self.verbosity >= 2: print 'move_output_repeated_indirect_matchmodel:' + str(move_output_repeated_indirect.is_success)
                if not move_output_repeated_indirect.is_success:
                    p2 = move_output_indirect.packet_in(p2)
                    if self.verbosity >= 2: print 'move_output_indirect_matchmodel:' + str(move_output_indirect.is_success)

                graph_to_dot("before_move_trace", p2.graph)

                p2 = move_trace.packet_in(p2)
                if self.verbosity >= 2: print 'move_backwardlink:' + str(move_trace.is_success)

                graph_to_dot("before_delete_uncollapsed", p2.graph)
                p2 = delete_uncollapsed_element.packet_in(p2)
                if not delete_uncollapsed_element.is_success:
                    raise Exception("Uncollapsed element was not deleted")

                if self.verbosity >= 2: print 'delete_uncollapsed_element_match:' + str(delete_uncollapsed_element.is_success)

                # check if the equations on the attributes of the disambiguated solution can be satisfied

                attribute = self.attributeEquationEvaluator(p.graph)
                print("Attribute Evaluator: " + str(attribute))
                if attribute:
                    #print("Adding")
                    # store the current disambiguated solution
                    disambiguated_solutions.append(p2.graph)
                    #print("Disambig: " + str(disambiguated_solutions))

                # advance to the next pair of elements to be collapsed
            p = i.next_in(p)

        return disambiguated_solutions
    

    
    def disambiguate(self, path_condition, level = 0):
        """
        Build all the disambiguated path conditions for a generated path condition.
        This follows approximately the recursive algorithm explained in:
        http://msdl.cs.mcgill.ca/people/levi/30_publications/files/paper_models2010.pdf
        Note that duplicate path conditions resulting from the recursive combining algorithm might arise.
        Although these do not alter the result of the proof, they slow it down and a more optimized
        disambiguation algorithm should not produce them.
        """

        level += 1

        #if level == 3:
        #    return []

        disambiguated_path_conditions = []

        graph_to_dot("path_condition", path_condition)

        collapse_step_result = self._collapse_step(path_condition)

        print("Collapse Result: " + str(collapse_step_result))

        for i in range(len(collapse_step_result)):
            graph_to_dot(path_condition.name + "_collapsed" + str(i), collapse_step_result[i])
            collapse_step_result[i].name += str(i)

        if collapse_step_result != []:
            disambiguated_path_conditions.extend(collapse_step_result)
        #    print("Collapse Length: " + str(len(collapse_step_result)))

            for disamb_path_cond in collapse_step_result:
                disamb_path_cond = deepcopy(disamb_path_cond)

                disambiguated_path_conditions.extend(self.disambiguate(disamb_path_cond, level))
                
        return disambiguated_path_conditions            