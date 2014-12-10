from t_core.messages import Packet
from t_core.matcher import Matcher
from t_core.iterator import Iterator

from tc_python.srule import SRule
from tc_python.frule import FRule

from merge_inter_layer import MergeInterLayerFactory
from merge_preprocess import MergePreprocessFactory
from himesis_utils import graph_to_dot
from himesis_utils import disjoint_model_union
from tc_python.frule import FRule

from GM2AUTOSAR_MM.transformation.Himesis.HMapDistributable import HMapDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HMapECU2FiveElements import HMapECU2FiveElements
from GM2AUTOSAR_MM.transformation.Himesis.HMapVirtualDevice import HMapVirtualDevice

#layer 2
from GM2AUTOSAR_MM.transformation.Himesis.HConnVirtualDeviceToDistributable import HConnVirtualDeviceToDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HConnECU2VirtualDevice import HConnECU2VirtualDevice

#layer 3
from GM2AUTOSAR_MM.transformation.Himesis.HConnectPPortPrototype import HConnectPPortPrototype
from GM2AUTOSAR_MM.transformation.Himesis.HConnectRPortPrototype import HConnectRPortPrototype

from GM2AUTOSAR_MM.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from GM2AUTOSAR_MM.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS

# declare the necessary T-Core rules
#forward_cardinalities_to_apply = SRule(HForwardCardinalitiesToApplyModelLHS(), HForwardCardinalitiesToApplyModelRHS())
build_traceability_for_rule = FRule(HBuildTraceabilityForRuleLHS(), HBuildTraceabilityForRuleRHS())

if __name__ == '__main__':
    pass

merge_il = MergeInterLayerFactory(3)
merge_pp = MergePreprocessFactory(3)

r1_1 = HMapDistributable()
r1_2 = HMapECU2FiveElements()
r1_3 = HMapVirtualDevice()
r2 = HConnVirtualDeviceToDistributable()
r3 = HConnectPPortPrototype()

tmp = merge_pp.merge_two_rules_preprocess(r1_1,r1_2)
r1 = merge_pp.merge_two_rules_preprocess(tmp,r1_3)

p = Packet()
p.graph = r1_2
p = build_traceability_for_rule.packet_in(p)
r1 = p.graph

p = Packet()
p.graph = r2
p = build_traceability_for_rule.packet_in(p)
r2 = p.graph

p = Packet()
p.graph = r3
p = build_traceability_for_rule.packet_in(p)
r3 = p.graph

res1 = merge_il.merge_two_rules_inter_layer(r1_2,r2)
res2 = merge_il.merge_two_rules_inter_layer(res1,r3)

graph_to_dot('first', r1, 1)
graph_to_dot('second', r2, 1)
graph_to_dot('third', r3, 1)
graph_to_dot('merged1', res1)
graph_to_dot('merged2', res2)
