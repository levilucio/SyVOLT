'''
Created on 2015-08-08

@author: levi
'''

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
from solver.prolog_attribute_equation_evaluator import PrologAttributeEquationEvaluator
# declare all the needed TCore rules

find_elements_collapse_match = Matcher(HFindTwoMatchElementsSameTypeDiffRulesLHS())       

# merge_cardinalities_matchmodel = ARule(HMergeCardinalitiesMatchDiffRulesLHS(), HMergeCardinalitiesMatchDiffRulesRHS())

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
        self.attributeEquationEvaluator = PrologAttributeEquationEvaluator(verbosity) 


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

        p = find_elements_collapse_match.packet_in(p)               
        if self.verbosity >= 2: print 'Found collapsable elements:' + str(find_elements_collapse_match.is_success)
        
        if find_elements_collapse_match.is_success:            
            
            p = i.packet_in(p)
            
            # continue while more pairs of elements can be collapsed
            while i.is_success:
                
                #                 p = merge_cardinalities_matchmodel.packet_in(p)
                #                 if self.verbosity >= 2: print 'merge_cardinalities_matchmodel:' + str( merge_cardinalities_matchmodel.is_success) 
                        
                p = move_input_repeated_direct.packet_in(p)
                if self.verbosity >= 2: print 'move_input_repeated_direct_matchmodel:' + str(move_input_repeated_direct.is_success)  
                if not move_input_repeated_direct.is_success:
                    p = move_input_direct.packet_in(p) 
                    if self.verbosity >= 2: print 'move_input_direct_matchmodel:' + str(move_input_direct.is_success) 
                      
                p = move_output_repeated_direct.packet_in(p)
                if self.verbosity >= 2: print 'move_output_repeated_direct_matchmodel:' + str(move_output_repeated_direct.is_success)
                if not move_output_repeated_direct.is_success:
                    p = move_output_direct.packet_in(p) 
                    if self.verbosity >= 2: print 'move_output_direct_matchmodel:' + str(move_output_direct.is_success)                
                
                p = move_input_repeated_indirect.packet_in(p) 
                if self.verbosity >= 2: print 'move_input_repeated_indirect_matchmodel:' + str(move_input_repeated_indirect.is_success)  
                if not move_input_repeated_indirect.is_success:
                    p = move_input_indirect.packet_in(p) 
                    if self.verbosity >= 2: print 'move_input_indirect_matchmodel:' + str(move_input_indirect.is_success)
                
                p = move_output_repeated_indirect.packet_in(p)
                if self.verbosity >= 2: print 'move_output_repeated_indirect_matchmodel:' + str(move_output_repeated_indirect.is_success)
                if not move_output_repeated_indirect.is_success:                       
                    p = move_output_indirect.packet_in(p)
                    if self.verbosity >= 2: print 'move_output_indirect_matchmodel:' + str(move_output_indirect.is_success)
                
                p = move_trace.packet_in(p)
                if self.verbosity >= 2: print 'move_backwardlink:' + str(move_trace.is_success)
                  
                p = delete_uncollapsed_element.packet_in(p)
                if self.verbosity >= 2: print 'delete_uncollapsed_element_match:' + str(delete_uncollapsed_element.is_success)
                
                # check if the equations on the attributes of the disambiguated solution can be satisfied
                if self.attributeEquationEvaluator(p.graph):
                    # store the current disambiguated solution            
                    disambiguated_solutions.append(p.graph)            
                
                # advance to the next pair of elements to be collapsed
                p = i.next_in(p)                
                              
        else:   
            return []
    

    
    def disambiguate(self, path_condition):
        """
        Build all the disambiguated path conditions for a generated path condition.
        This follows approximately the recursive algorithm explained in:
        http://msdl.cs.mcgill.ca/people/levi/30_publications/files/paper_models2010.pdf
        Note that duplicate path conditions resulting from the recursive combining algorithm might arise.
        Although these do not alter the result of the proof, they slow it down and a more optimized
        disambiguation algorithm should not produce them.
        """
        
        disambiguated_path_conditions = []
        
        collapse_step_result = self._collapse_step(path_condition)
        
        if collapse_step_result != []:
            disambiguated_path_conditions.extend(collapse_step_result)
            for disamb_path_cond in collapse_step_result:
                disambiguated_path_conditions.extend(self.disambiguate(disamb_path_cond))
                
        return disambiguated_path_conditions
        
                                              