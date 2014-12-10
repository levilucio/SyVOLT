'''
Created on 2013-01-22

@author: levi
'''

import unittest
import time

from path_condition_generator import PathConditionGenerator

from t_core.matcher import Matcher
from t_core.messages import Packet

# all runs are the same transformation, but with different metamodel elements
# the purpose is to do scalability testing with multiple configurations and multiple sets of rules

# run 1

from police_station_transformation.run1.transformation.HS2S_run1 import HS2S_run1
from police_station_transformation.run1.transformation.HM2M_run1 import HM2M_run1
from police_station_transformation.run1.transformation.HF2F_run1 import HF2F_run1
from police_station_transformation.run1.transformation.HSM2SM_run1 import HSM2SM_run1
from police_station_transformation.run1.transformation.HSF2SF_run1 import HSF2SF_run1
from police_station_transformation.run1.transformation.HMM2MM_run1 import HMM2MM_run1
from police_station_transformation.run1.transformation.HFF2FF_run1 import HFF2FF_run1

from police_station_transformation.run1.backward_matchers.HSM2SMBackS2S_run1LHS import HSM2SMBackS2S_run1LHS
from police_station_transformation.run1.backward_matchers.HSM2SMBackM2M_run1LHS import HSM2SMBackM2M_run1LHS
from police_station_transformation.run1.backward_matchers.HSF2SFBackS2S_run1LHS import HSF2SFBackS2S_run1LHS
from police_station_transformation.run1.backward_matchers.HSF2SFBackF2F_run1LHS import HSF2SFBackF2F_run1LHS
from police_station_transformation.run1.backward_matchers.HMM2MMBackM2M1_run1LHS import HMM2MMBackM2M1_run1LHS
from police_station_transformation.run1.backward_matchers.HMM2MMBackM2M2_run1LHS import HMM2MMBackM2M2_run1LHS
from police_station_transformation.run1.backward_matchers.HFF2FFBackF2F1_run1LHS import HFF2FFBackF2F1_run1LHS
from police_station_transformation.run1.backward_matchers.HFF2FFBackF2F2_run1LHS import HFF2FFBackF2F2_run1LHS

from police_station_transformation.run1.backward_matchers.HSM2SMBackComplete_run1LHS import HSM2SMBackComplete_run1LHS
from police_station_transformation.run1.backward_matchers.HSF2SFBackComplete_run1LHS import HSF2SFBackComplete_run1LHS
from police_station_transformation.run1.backward_matchers.HMM2MMBackComplete_run1LHS import HMM2MMBackComplete_run1LHS
from police_station_transformation.run1.backward_matchers.HFF2FFBackComplete_run1LHS import HFF2FFBackComplete_run1LHS

# run 1 properties

# from property.run1.positive.HFSMIsolated_run1LHS import HFSMIsolated_run1LHS
# from property.run1.positive.HFSMConnected_run1LHS import HFSMConnected_run1LHS
# from property.run1.positive.HFSMComplete_run1LHS import HFSMComplete_run1LHS
# 
# from property.run1.negative.HF2FFIsolated_run1LHS import HF2FFIsolated_run1LHS
# from property.run1.negative.HF2FFConnected_run1LHS import HF2FFConnected_run1LHS
# from property.run1.negative.HF2FFComplete_run1LHS import HF2FFComplete_run1LHS

# run 2

from police_station_transformation.run2.transformation.HS2S_run2 import HS2S_run2
from police_station_transformation.run2.transformation.HM2M_run2 import HM2M_run2
from police_station_transformation.run2.transformation.HF2F_run2 import HF2F_run2
from police_station_transformation.run2.transformation.HSM2SM_run2 import HSM2SM_run2
from police_station_transformation.run2.transformation.HSF2SF_run2 import HSF2SF_run2
from police_station_transformation.run2.transformation.HMM2MM_run2 import HMM2MM_run2
from police_station_transformation.run2.transformation.HFF2FF_run2 import HFF2FF_run2

from police_station_transformation.run2.backward_matchers.HSM2SMBackS2S_run2LHS import HSM2SMBackS2S_run2LHS
from police_station_transformation.run2.backward_matchers.HSM2SMBackM2M_run2LHS import HSM2SMBackM2M_run2LHS
from police_station_transformation.run2.backward_matchers.HSF2SFBackS2S_run2LHS import HSF2SFBackS2S_run2LHS
from police_station_transformation.run2.backward_matchers.HSF2SFBackF2F_run2LHS import HSF2SFBackF2F_run2LHS
from police_station_transformation.run2.backward_matchers.HMM2MMBackM2M1_run2LHS import HMM2MMBackM2M1_run2LHS
from police_station_transformation.run2.backward_matchers.HMM2MMBackM2M2_run2LHS import HMM2MMBackM2M2_run2LHS
from police_station_transformation.run2.backward_matchers.HFF2FFBackF2F1_run2LHS import HFF2FFBackF2F1_run2LHS
from police_station_transformation.run2.backward_matchers.HFF2FFBackF2F2_run2LHS import HFF2FFBackF2F2_run2LHS

from police_station_transformation.run2.backward_matchers.HSM2SMBackComplete_run2LHS import HSM2SMBackComplete_run2LHS
from police_station_transformation.run2.backward_matchers.HSF2SFBackComplete_run2LHS import HSF2SFBackComplete_run2LHS
from police_station_transformation.run2.backward_matchers.HMM2MMBackComplete_run2LHS import HMM2MMBackComplete_run2LHS
from police_station_transformation.run2.backward_matchers.HFF2FFBackComplete_run2LHS import HFF2FFBackComplete_run2LHS

# run 2 properties

# from property.run2.positive.HFSMIsolated_run2LHS import HFSMIsolated_run2LHS
# from property.run2.positive.HFSMConnected_run2LHS import HFSMConnected_run2LHS
# from property.run2.positive.HFSMComplete_run2LHS import HFSMComplete_run2LHS
# 
# from property.run2.negative.HF2FFIsolated_run2LHS import HF2FFIsolated_run2LHS
# from property.run2.negative.HF2FFConnected_run2LHS import HF2FFConnected_run2LHS
# from property.run2.negative.HF2FFComplete_run2LHS import HF2FFComplete_run2LHS

# run 3

from police_station_transformation.run3.transformation.HS2S_run3 import HS2S_run3
from police_station_transformation.run3.transformation.HM2M_run3 import HM2M_run3
from police_station_transformation.run3.transformation.HF2F_run3 import HF2F_run3
from police_station_transformation.run3.transformation.HSM2SM_run3 import HSM2SM_run3
from police_station_transformation.run3.transformation.HSF2SF_run3 import HSF2SF_run3
from police_station_transformation.run3.transformation.HMM2MM_run3 import HMM2MM_run3
from police_station_transformation.run3.transformation.HFF2FF_run3 import HFF2FF_run3

from police_station_transformation.run3.backward_matchers.HSM2SMBackS2S_run3LHS import HSM2SMBackS2S_run3LHS
from police_station_transformation.run3.backward_matchers.HSM2SMBackM2M_run3LHS import HSM2SMBackM2M_run3LHS
from police_station_transformation.run3.backward_matchers.HSF2SFBackS2S_run3LHS import HSF2SFBackS2S_run3LHS
from police_station_transformation.run3.backward_matchers.HSF2SFBackF2F_run3LHS import HSF2SFBackF2F_run3LHS
from police_station_transformation.run3.backward_matchers.HMM2MMBackM2M1_run3LHS import HMM2MMBackM2M1_run3LHS
from police_station_transformation.run3.backward_matchers.HMM2MMBackM2M2_run3LHS import HMM2MMBackM2M2_run3LHS
from police_station_transformation.run3.backward_matchers.HFF2FFBackF2F1_run3LHS import HFF2FFBackF2F1_run3LHS
from police_station_transformation.run3.backward_matchers.HFF2FFBackF2F2_run3LHS import HFF2FFBackF2F2_run3LHS

from police_station_transformation.run3.backward_matchers.HSM2SMBackComplete_run3LHS import HSM2SMBackComplete_run3LHS
from police_station_transformation.run3.backward_matchers.HSF2SFBackComplete_run3LHS import HSF2SFBackComplete_run3LHS
from police_station_transformation.run3.backward_matchers.HMM2MMBackComplete_run3LHS import HMM2MMBackComplete_run3LHS
from police_station_transformation.run3.backward_matchers.HFF2FFBackComplete_run3LHS import HFF2FFBackComplete_run3LHS

# run 3 properties

# from property.run3.positive.HFSMIsolated_run3LHS import HFSMIsolated_run3LHS
# from property.run3.positive.HFSMConnected_run3LHS import HFSMConnected_run3LHS
# from property.run3.positive.HFSMComplete_run3LHS import HFSMComplete_run3LHS
# 
# from property.run3.negative.HF2FFIsolated_run3LHS import HF2FFIsolated_run3LHS
# from property.run3.negative.HF2FFConnected_run3LHS import HF2FFConnected_run3LHS
# from property.run3.negative.HF2FFComplete_run3LHS import HF2FFComplete_run3LHS

# run 4

from police_station_transformation.run4.transformation.HS2S_run4 import HS2S_run4
from police_station_transformation.run4.transformation.HM2M_run4 import HM2M_run4
from police_station_transformation.run4.transformation.HF2F_run4 import HF2F_run4
from police_station_transformation.run4.transformation.HSM2SM_run4 import HSM2SM_run4
from police_station_transformation.run4.transformation.HSF2SF_run4 import HSF2SF_run4
from police_station_transformation.run4.transformation.HMM2MM_run4 import HMM2MM_run4
from police_station_transformation.run4.transformation.HFF2FF_run4 import HFF2FF_run4

from police_station_transformation.run4.backward_matchers.HSM2SMBackS2S_run4LHS import HSM2SMBackS2S_run4LHS
from police_station_transformation.run4.backward_matchers.HSM2SMBackM2M_run4LHS import HSM2SMBackM2M_run4LHS
from police_station_transformation.run4.backward_matchers.HSF2SFBackS2S_run4LHS import HSF2SFBackS2S_run4LHS
from police_station_transformation.run4.backward_matchers.HSF2SFBackF2F_run4LHS import HSF2SFBackF2F_run4LHS
from police_station_transformation.run4.backward_matchers.HMM2MMBackM2M1_run4LHS import HMM2MMBackM2M1_run4LHS
from police_station_transformation.run4.backward_matchers.HMM2MMBackM2M2_run4LHS import HMM2MMBackM2M2_run4LHS
from police_station_transformation.run4.backward_matchers.HFF2FFBackF2F1_run4LHS import HFF2FFBackF2F1_run4LHS
from police_station_transformation.run4.backward_matchers.HFF2FFBackF2F2_run4LHS import HFF2FFBackF2F2_run4LHS

from police_station_transformation.run4.backward_matchers.HSM2SMBackComplete_run4LHS import HSM2SMBackComplete_run4LHS
from police_station_transformation.run4.backward_matchers.HSF2SFBackComplete_run4LHS import HSF2SFBackComplete_run4LHS
from police_station_transformation.run4.backward_matchers.HMM2MMBackComplete_run4LHS import HMM2MMBackComplete_run4LHS
from police_station_transformation.run4.backward_matchers.HFF2FFBackComplete_run4LHS import HFF2FFBackComplete_run4LHS

# run 4 properties

# from property.run4.positive.HFSMIsolated_run4LHS import HFSMIsolated_run4LHS
# from property.run4.positive.HFSMConnected_run4LHS import HFSMConnected_run4LHS
# from property.run4.positive.HFSMComplete_run4LHS import HFSMComplete_run4LHS
# 
# from property.run4.negative.HF2FFIsolated_run4LHS import HF2FFIsolated_run4LHS
# from property.run4.negative.HF2FFConnected_run4LHS import HF2FFConnected_run4LHS
# from property.run4.negative.HF2FFComplete_run4LHS import HF2FFComplete_run4LHS



class Test(unittest.TestCase):

    def setUp(self):
        
        self.rules = {                'HS2S_run1': HS2S_run1(),
                                      'HM2M_run1': HM2M_run1(),
                                      'HF2F_run1': HF2F_run1(),
                                      'HSM2SM_run1': HSM2SM_run1(),
                                      'HSF2SF_run1': HSF2SF_run1(),
                                      'HMM2MM_run1': HMM2MM_run1(),
                                      'HFF2FF_run1': HFF2FF_run1(),
                                      'HS2S_run2': HS2S_run2(),
                                      'HM2M_run2': HM2M_run2(),
                                      'HF2F_run2': HF2F_run2(),
                                      'HSM2SM_run2': HSM2SM_run2(),
                                      'HSF2SF_run2': HSF2SF_run2(),
                                      'HMM2MM_run2': HMM2MM_run2(),
                                      'HFF2FF_run2': HFF2FF_run2(),
                                      'HS2S_run3': HS2S_run3(),
                                      'HM2M_run3': HM2M_run3(),
                                      'HF2F_run3': HF2F_run3(),
                                      'HSM2SM_run3': HSM2SM_run3(),
                                      'HSF2SF_run3': HSF2SF_run3(),
                                      'HMM2MM_run3': HMM2MM_run3(),
                                      'HFF2FF_run3': HFF2FF_run3(),
                                      'HS2S_run4': HS2S_run4(),
                                      'HM2M_run4': HM2M_run4(),
                                      'HF2F_run4': HF2F_run4(),
                                      'HSM2SM_run4': HSM2SM_run4(),
                                      'HSF2SF_run4': HSF2SF_run4(),
                                      'HMM2MM_run4': HMM2MM_run4(),
                                      'HFF2FF_run4': HFF2FF_run4()}

        self.backwardPatterns = {     'HS2S_run1': None,
                                      'HM2M_run1': None,  
                                      'HF2F_run1': None,                 
                                      'HSM2SM_run1': [Matcher(HSM2SMBackS2S_run1LHS()),Matcher(HSM2SMBackM2M_run1LHS())],
                                      'HSF2SF_run1': [Matcher(HSF2SFBackS2S_run1LHS()),Matcher(HSF2SFBackF2F_run1LHS())],
                                      'HMM2MM_run1': [Matcher(HMM2MMBackM2M1_run1LHS()),Matcher(HMM2MMBackM2M2_run1LHS())],
                                      'HFF2FF_run1': [Matcher(HFF2FFBackF2F1_run1LHS()),Matcher(HFF2FFBackF2F2_run1LHS())],
                                      'HS2S_run2': None,
                                      'HM2M_run2': None,  
                                      'HF2F_run2': None,                 
                                      'HSM2SM_run2': [Matcher(HSM2SMBackS2S_run2LHS()),Matcher(HSM2SMBackM2M_run2LHS())],
                                      'HSF2SF_run2': [Matcher(HSF2SFBackS2S_run2LHS()),Matcher(HSF2SFBackF2F_run2LHS())],
                                      'HMM2MM_run2': [Matcher(HMM2MMBackM2M1_run2LHS()),Matcher(HMM2MMBackM2M2_run2LHS())],
                                      'HFF2FF_run2': [Matcher(HFF2FFBackF2F1_run2LHS()),Matcher(HFF2FFBackF2F2_run2LHS())],
                                      'HS2S_run3': None,
                                      'HM2M_run3': None,  
                                      'HF2F_run3': None,                 
                                      'HSM2SM_run3': [Matcher(HSM2SMBackS2S_run3LHS()),Matcher(HSM2SMBackM2M_run3LHS())],
                                      'HSF2SF_run3': [Matcher(HSF2SFBackS2S_run3LHS()),Matcher(HSF2SFBackF2F_run3LHS())],
                                      'HMM2MM_run3': [Matcher(HMM2MMBackM2M1_run3LHS()),Matcher(HMM2MMBackM2M2_run3LHS())],
                                      'HFF2FF_run3': [Matcher(HFF2FFBackF2F1_run3LHS()),Matcher(HFF2FFBackF2F2_run3LHS())],
                                      'HS2S_run4': None,
                                      'HM2M_run4': None,  
                                      'HF2F_run4': None,                 
                                      'HSM2SM_run4': [Matcher(HSM2SMBackS2S_run4LHS()),Matcher(HSM2SMBackM2M_run4LHS())],
                                      'HSF2SF_run4': [Matcher(HSF2SFBackS2S_run4LHS()),Matcher(HSF2SFBackF2F_run4LHS())],
                                      'HMM2MM_run4': [Matcher(HMM2MMBackM2M1_run4LHS()),Matcher(HMM2MMBackM2M2_run4LHS())],
                                      'HFF2FF_run4': [Matcher(HFF2FFBackF2F1_run4LHS()),Matcher(HFF2FFBackF2F2_run4LHS())]}
         
        self.backwardPatterns2Rules = {     'HSM2SMBackS2S_run1LHS': 'HSM2SM_run1',
                                            'HSM2SMBackM2M_run1LHS': 'HSM2SM_run1',
                                            'HSF2SFBackS2S_run1LHS': 'HSF2SF_run1',
                                            'HSF2SFBackF2F_run1LHS': 'HSF2SF_run1',                                        
                                            'HMM2MMBackM2M1_run1LHS': 'HMM2MM_run1',
                                            'HMM2MMBackM2M2_run1LHS': 'HMM2MM_run1',                                      
                                            'HFF2FFBackF2F1_run1LHS': 'HFF2FF_run1',
                                            'HFF2FFBackF2F2_run1LHS': 'HFF2FF_run1',
                                            'HSM2SMBackS2S_run2LHS': 'HSM2SM_run2',
                                            'HSM2SMBackM2M_run2LHS': 'HSM2SM_run2',
                                            'HSF2SFBackS2S_run2LHS': 'HSF2SF_run2',
                                            'HSF2SFBackF2F_run2LHS': 'HSF2SF_run2',                                        
                                            'HMM2MMBackM2M1_run2LHS': 'HMM2MM_run2',
                                            'HMM2MMBackM2M2_run2LHS': 'HMM2MM_run2',                                      
                                            'HFF2FFBackF2F1_run2LHS': 'HFF2FF_run2',
                                            'HFF2FFBackF2F2_run2LHS': 'HFF2FF_run2',
                                            'HSM2SMBackS2S_run3LHS': 'HSM2SM_run3',
                                            'HSM2SMBackM2M_run3LHS': 'HSM2SM_run3',
                                            'HSF2SFBackS2S_run3LHS': 'HSF2SF_run3',
                                            'HSF2SFBackF2F_run3LHS': 'HSF2SF_run3',                                        
                                            'HMM2MMBackM2M1_run3LHS': 'HMM2MM_run3',
                                            'HMM2MMBackM2M2_run3LHS': 'HMM2MM_run3',                                      
                                            'HFF2FFBackF2F1_run3LHS': 'HFF2FF_run3',
                                            'HFF2FFBackF2F2_run3LHS': 'HFF2FF_run3',
                                            'HSM2SMBackS2S_run4LHS': 'HSM2SM_run4',
                                            'HSM2SMBackM2M_run4LHS': 'HSM2SM_run4',
                                            'HSF2SFBackS2S_run4LHS': 'HSF2SF_run4',
                                            'HSF2SFBackF2F_run4LHS': 'HSF2SF_run4',                                        
                                            'HMM2MMBackM2M1_run4LHS': 'HMM2MM_run4',
                                            'HMM2MMBackM2M2_run4LHS': 'HMM2MM_run4',                                      
                                            'HFF2FFBackF2F1_run4LHS': 'HFF2FF_run4',
                                            'HFF2FFBackF2F2_run4LHS': 'HFF2FF_run4'}
        
        self.backwardPatternsComplete = {
                                      'HS2S_run1': None,
                                      'HM2M_run1': None,
                                      'HF2F_run1': None,
                                      'HSM2SM_run1': [Matcher(HSM2SMBackComplete_run1LHS())],
                                      'HSF2SF_run1': [Matcher(HSF2SFBackComplete_run1LHS())],
                                      'HMM2MM_run1': [Matcher(HMM2MMBackComplete_run1LHS())],
                                      'HFF2FF_run1': [Matcher(HFF2FFBackComplete_run1LHS())],
                                      'HS2S_run2': None,
                                      'HM2M_run2': None,
                                      'HF2F_run2': None,
                                      'HSM2SM_run2': [Matcher(HSM2SMBackComplete_run2LHS())],
                                      'HSF2SF_run2': [Matcher(HSF2SFBackComplete_run2LHS())],
                                      'HMM2MM_run2': [Matcher(HMM2MMBackComplete_run2LHS())],
                                      'HFF2FF_run2': [Matcher(HFF2FFBackComplete_run2LHS())],
                                      'HS2S_run3': None,
                                      'HM2M_run3': None,
                                      'HF2F_run3': None,
                                      'HSM2SM_run3': [Matcher(HSM2SMBackComplete_run3LHS())],
                                      'HSF2SF_run3': [Matcher(HSF2SFBackComplete_run3LHS())],
                                      'HMM2MM_run3': [Matcher(HMM2MMBackComplete_run3LHS())],
                                      'HFF2FF_run3': [Matcher(HFF2FFBackComplete_run3LHS())],
                                      'HS2S_run4': None,
                                      'HM2M_run4': None,
                                      'HF2F_run4': None,
                                      'HSM2SM_run4': [Matcher(HSM2SMBackComplete_run4LHS())],
                                      'HSF2SF_run4': [Matcher(HSF2SFBackComplete_run4LHS())],
                                      'HMM2MM_run4': [Matcher(HMM2MMBackComplete_run4LHS())],
                                      'HFF2FF_run4': [Matcher(HFF2FFBackComplete_run4LHS())]}


        
    def test_verify_run1(self):
        
        transformation = [[HS2S_run1(), HM2M_run1(), HF2F_run1()], [HSM2SM_run1(), HMM2MM_run1(), HSF2SF_run1(), HFF2FF_run1()]]
        rulesIncludingBackLinks = [[], [transformation[1][0], transformation[1][1], transformation[1][2], transformation[1][3]]]
        ts0 = time.time()
        s = PathConditionGenerator(self.rules, transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
                                   self.backwardPatternsComplete, self.backwardPatternsComplete, 0, False)
        s.build_symbolic_state_space()
        ts1 = time.time()
        
#        self._print_states(s)
        
#         tv00 = time.time()
#         s.verify_property(HFSMIsolated_run1LHS(), HFSMConnected_run1LHS(), HFSMComplete_run1LHS())
#         tv01 = time.time()
# 
#         tv10 = time.time()        
#         s.verify_property(HF2FFIsolated_run1LHS(), HF2FFConnected_run1LHS(), HF2FFComplete_run1LHS())
#         tv11 = time.time()

        print '\n'        
        print 'Number of produced states: ' + str(len(s.symbStateSpace))    
        print 'Time to build the state space: ' + str(ts1-ts0)
#         print 'Time to verify the first property: ' + str(tv01-tv00)       
#         print 'Time to verify the second property: ' + str(tv11-tv10)    


#     def test_verify_run2(self):
#         
#         transformation = [[HS2S_run2(), HM2M_run2(), HF2F_run2()], [HSM2SM_run2(), HMM2MM_run2(), HSF2SF_run2(), HFF2FF_run2()]]
#         rulesIncludingBackLinks = [[], [transformation[1][0], transformation[1][1], transformation[1][2], transformation[1][3]]]
#         ts0 = time.time()
#         s = SymbolicStateSpace(self.rules, transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
#                                    self.backwardPatternsComplete, 0, False)
#         s.build_symbolic_state_space()
#         ts1 = time.time()   
#         
# #        self._print_states(s)
#         
#         tv00 = time.time()
#         s.verify_property(HFSMIsolated_run2LHS(), HFSMConnected_run2LHS(), HFSMComplete_run2LHS())
#         tv01 = time.time()
# 
#         tv10 = time.time()   
#         s.verify_property(HF2FFIsolated_run2LHS(), HF2FFConnected_run2LHS(), HF2FFComplete_run2LHS())
#         tv11 = time.time()
# 
#         print '\n'        
#         print 'Number of produced states: ' + str(len(s.symbStateSpace))    
#         print 'Time to build the state space: ' + str(ts1-ts0)
#         print 'Time to verify the first property: ' + str(tv01-tv00)       
#         print 'Time to verify the second property: ' + str(tv11-tv10)
#         
# 
#     def test_verify_run3(self):
#         
#         transformation = [[HS2S_run3(), HM2M_run3(), HF2F_run3()], [HSM2SM_run3(), HMM2MM_run3(), HSF2SF_run3(), HFF2FF_run3()]]
#         rulesIncludingBackLinks = [[], [transformation[1][0], transformation[1][1], transformation[1][2], transformation[1][3]]]
#         ts0 = time.time()
#         s = SymbolicStateSpace(self.rules, transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
#                                    self.backwardPatternsComplete, 0, False)
#         s.build_symbolic_state_space()
#         ts1 = time.time()
#         
#         tv00 = time.time()
#         s.verify_property(HFSMIsolated_run3LHS(), HFSMConnected_run3LHS(), HFSMComplete_run3LHS())
#         tv01 = time.time()
# 
#         tv10 = time.time()        
#         s.verify_property(HF2FFIsolated_run3LHS(), HF2FFConnected_run3LHS(), HF2FFComplete_run3LHS())
#         tv11 = time.time()
#         
#         print '\n'
#         print 'Number of produced states: ' + str(len(s.symbStateSpace))    
#         print 'Time to build the state space: ' + str(ts1-ts0)
#         print 'Time to verify the first property: ' + str(tv01-tv00)       
#         print 'Time to verify the second property: ' + str(tv11-tv10) 
# 
# 
#     def test_verify_run4(self):
#         
#         transformation = [[HS2S_run4(), HM2M_run4(), HF2F_run4()], [HSM2SM_run4(), HMM2MM_run4(), HSF2SF_run4(), HFF2FF_run4()]]
#         rulesIncludingBackLinks = [[], [transformation[1][0], transformation[1][1], transformation[1][2], transformation[1][3]]]
#         ts0 = time.time()
#         s = SymbolicStateSpace(self.rules, transformation, rulesIncludingBackLinks, self.backwardPatterns, self.backwardPatterns2Rules,\
#                                    self.backwardPatternsComplete, 0, False)
#         s.build_symbolic_state_space()
#         ts1 = time.time()
#         
#         tv00 = time.time()
#         s.verify_property(HFSMIsolated_run4LHS(), HFSMConnected_run4LHS(), HFSMComplete_run4LHS())
#         tv01 = time.time()
# 
#         tv10 = time.time()        
#         s.verify_property(HF2FFIsolated_run4LHS(), HF2FFConnected_run4LHS(), HF2FFComplete_run4LHS())
#         tv11 = time.time()
#         
#         print '\n'
#         print 'Number of produced states: ' + str(len(s.symbStateSpace))    
#         print 'Time to build the state space: ' + str(ts1-ts0)
#         print 'Time to verify the first property: ' + str(tv01-tv00)       
#         print 'Time to verify the second property: ' + str(tv11-tv10) 
#       
# 
#     def _print_states(self,s):
#         for state in s.symbStateSpace:
#             print "----------"
#             if state == ():
#                 print 'Empty'
#             else:
#                 for s in state:
#                     print s
# 
# 
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.test']
#     unittest.main()
    