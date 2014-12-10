from collapse import CollapseFactory
from himesis_utils import graph_to_dot
from himesis_utils import disjoint_model_union

from t_core.messages import Packet
from tc_python.frule import FRule

#layer 1
from GM2AUTOSAR_MM.transformation.Himesis.HMapDistributable import HMapDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HMapECU2FiveElements import HMapECU2FiveElements
from GM2AUTOSAR_MM.transformation.Himesis.HMapVirtualDevice import HMapVirtualDevice

#layer 2
from GM2AUTOSAR_MM.transformation.Himesis.HConnVirtualDeviceToDistributable import HConnVirtualDeviceToDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HConnECU2VirtualDevice import HConnECU2VirtualDevice

#layer 3
from GM2AUTOSAR_MM.transformation.Himesis.HConnectPPortPrototype import HConnectPPortPrototype
from GM2AUTOSAR_MM.transformation.Himesis.HConnectRPortPrototype import HConnectRPortPrototype

from GM2AUTOSAR_MM.tests.Himesis.HRule1_1 import HRule1_1
from GM2AUTOSAR_MM.tests.Himesis.HRule1_2 import HRule1_2
from GM2AUTOSAR_MM.tests.Himesis.HRule1_1Exists import HRule1_1Exists
from GM2AUTOSAR_MM.tests.Himesis.HRule1_2Exists import HRule1_2Exists

# transformation to built traceability for rules
from GM2AUTOSAR_MM.traceability_construction.Himesis.HBuildTraceabilityForRuleLHS import HBuildTraceabilityForRuleLHS
from GM2AUTOSAR_MM.traceability_construction.Himesis.HBuildTraceabilityForRuleRHS import HBuildTraceabilityForRuleRHS

# declare the necessary T-Core rules
build_traceability_for_rule = FRule(HBuildTraceabilityForRuleLHS(), HBuildTraceabilityForRuleRHS())

if __name__ == '__main__':
    pass


collapseFactory = CollapseFactory(3)
#
#r1 = HConnectPPortPrototype()
#r2 = HConnectRPortPrototype()
#
#res = collapseFactory._collapse_two_rules(r1,r2)
#
#for i in range(0, len(res)):
#    graph_to_dot('collapsed.' + str(i), res[i])

r1 = HRule1_1()
r2 = HRule1_2()
r1e = HRule1_1Exists()
r2e = HRule1_1Exists()


graph_to_dot('rule1', r1e)
graph_to_dot('rule2', r2e)

rc = collapseFactory._collapse_two_rules(r1e, r2)

p = Packet()
p.graph = rc
p = build_traceability_for_rule.packet_in(p)
rc =  p.graph      

graph_to_dot('collapsed', rc)