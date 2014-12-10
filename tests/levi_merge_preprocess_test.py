from merge_preprocess import MergePreprocessFactory
from himesis_utils import graph_to_dot
from himesis_utils import disjoint_model_union
from tc_python.frule import FRule

from GM2AUTOSAR_MM.transformation.Himesis.HMapDistributable import HMapDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HMapECU2FiveElementsFAULTY import HMapECU2FiveElementsFAULTY
from GM2AUTOSAR_MM.transformation.Himesis.HMapVirtualDeviceFAULTY import HMapVirtualDeviceFAULTY

#layer 2
from GM2AUTOSAR_MM.transformation.Himesis.HConnVirtualDeviceToDistributable import HConnVirtualDeviceToDistributable
from GM2AUTOSAR_MM.transformation.Himesis.HConnECU2VirtualDevice import HConnECU2VirtualDevice

#layer 3
from GM2AUTOSAR_MM.transformation.Himesis.HConnectPPortPrototype import HConnectPPortPrototype
from GM2AUTOSAR_MM.transformation.Himesis.HConnectRPortPrototype import HConnectRPortPrototype

if __name__ == '__main__':
    pass

mergeFactory = MergePreprocessFactory(3)

r1 = HMapDistributable()
r2 = HMapVirtualDeviceFAULTY()
r3 = HMapECU2FiveElementsFAULTY()

print r1.name

restmp = mergeFactory.merge_two_rules_preprocess(r1,r2)
res = mergeFactory.merge_two_rules_preprocess(restmp,r3)

graph_to_dot('first', r1, 1)
graph_to_dot('second', r2, 1)
graph_to_dot('third', r3, 1)
graph_to_dot('merged', res, 1)

