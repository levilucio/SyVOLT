from core.himesis import Himesis
import uuid

class HCompositeState2ProcDef(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule CompositeState2ProcDef.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCompositeState2ProcDef, self).__init__(name='HCompositeState2ProcDef', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """CompositeState2ProcDef"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'CompositeState2ProcDef')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """CompositeState2ProcDef"""
        
        # match class State() node
        self.add_node()
        self.vs[3]["name"] = """"""
        self.vs[3]["classtype"] = """State"""
        self.vs[3]["mm__"] = """State"""
        self.vs[3]["cardinality"] = """+"""
        # match_contains node for class State()
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class ProcDef() node
        self.add_node()
        self.vs[5]["name"] = """"""
        self.vs[5]["classtype"] = """ProcDef"""
        self.vs[5]["mm__"] = """ProcDef"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class ProcDef()
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class LocalDef() node
        self.add_node()
        self.vs[7]["name"] = """"""
        self.vs[7]["classtype"] = """LocalDef"""
        self.vs[7]["mm__"] = """LocalDef"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class LocalDef()
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[9]["name"] = """"""
        self.vs[9]["classtype"] = """Name"""
        self.vs[9]["mm__"] = """Name"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        # apply class New() node
        self.add_node()
        self.vs[11]["name"] = """"""
        self.vs[11]["classtype"] = """New"""
        self.vs[11]["mm__"] = """New"""
        self.vs[11]["cardinality"] = """1"""
        # apply_contains node for class New()
        self.add_node()
        self.vs[12]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[13]["name"] = """"""
        self.vs[13]["classtype"] = """Name"""
        self.vs[13]["mm__"] = """Name"""
        self.vs[13]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[14]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[15]["name"] = """"""
        self.vs[15]["classtype"] = """Name"""
        self.vs[15]["mm__"] = """Name"""
        self.vs[15]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[16]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[17]["name"] = """"""
        self.vs[17]["classtype"] = """Name"""
        self.vs[17]["mm__"] = """Name"""
        self.vs[17]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[18]["mm__"] = """apply_contains"""
        # apply class Par() node
        self.add_node()
        self.vs[19]["name"] = """"""
        self.vs[19]["classtype"] = """Par"""
        self.vs[19]["mm__"] = """Par"""
        self.vs[19]["cardinality"] = """1"""
        # apply_contains node for class Par()
        self.add_node()
        self.vs[20]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()
        self.vs[21]["name"] = """"""
        self.vs[21]["classtype"] = """Inst"""
        self.vs[21]["mm__"] = """Inst"""
        self.vs[21]["cardinality"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[22]["mm__"] = """apply_contains"""
        # apply class Inst() node
        self.add_node()
        self.vs[23]["name"] = """"""
        self.vs[23]["classtype"] = """Inst"""
        self.vs[23]["mm__"] = """Inst"""
        self.vs[23]["cardinality"] = """1"""
        # apply_contains node for class Inst()
        self.add_node()
        self.vs[24]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[25]["name"] = """"""
        self.vs[25]["classtype"] = """Name"""
        self.vs[25]["mm__"] = """Name"""
        self.vs[25]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[26]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[27]["name"] = """"""
        self.vs[27]["classtype"] = """Name"""
        self.vs[27]["mm__"] = """Name"""
        self.vs[27]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[28]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[29]["name"] = """"""
        self.vs[29]["classtype"] = """Name"""
        self.vs[29]["mm__"] = """Name"""
        self.vs[29]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[30]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[31]["name"] = """"""
        self.vs[31]["classtype"] = """Name"""
        self.vs[31]["mm__"] = """Name"""
        self.vs[31]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[32]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[33]["name"] = """"""
        self.vs[33]["classtype"] = """Name"""
        self.vs[33]["mm__"] = """Name"""
        self.vs[33]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[34]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[35]["name"] = """"""
        self.vs[35]["classtype"] = """Name"""
        self.vs[35]["mm__"] = """Name"""
        self.vs[35]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[36]["mm__"] = """apply_contains"""
        # apply class Name() node
        self.add_node()
        self.vs[37]["name"] = """"""
        self.vs[37]["classtype"] = """Name"""
        self.vs[37]["mm__"] = """Name"""
        self.vs[37]["cardinality"] = """1"""
        # apply_contains node for class Name()
        self.add_node()
        self.vs[38]["mm__"] = """apply_contains"""
        
        
        
        # apply association ProcDef--p-->LocalDef node
        self.add_node()
        self.vs[39]["associationType"] = """p"""
        self.vs[39]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[40]["associationType"] = """channelNames"""
        self.vs[40]["mm__"] = """directLink_T"""
        # apply association LocalDef--p-->New node
        self.add_node()
        self.vs[41]["associationType"] = """p"""
        self.vs[41]["mm__"] = """directLink_T"""
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[42]["associationType"] = """channelNames"""
        self.vs[42]["mm__"] = """directLink_T"""
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[43]["associationType"] = """channelNames"""
        self.vs[43]["mm__"] = """directLink_T"""
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[44]["associationType"] = """channelNames"""
        self.vs[44]["mm__"] = """directLink_T"""
        # apply association New--p-->Par node
        self.add_node()
        self.vs[45]["associationType"] = """p"""
        self.vs[45]["mm__"] = """directLink_T"""
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[46]["associationType"] = """p"""
        self.vs[46]["mm__"] = """directLink_T"""
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[47]["associationType"] = """p"""
        self.vs[47]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[48]["associationType"] = """channelNames"""
        self.vs[48]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[49]["associationType"] = """channelNames"""
        self.vs[49]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[50]["associationType"] = """channelNames"""
        self.vs[50]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[51]["associationType"] = """channelNames"""
        self.vs[51]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[52]["associationType"] = """channelNames"""
        self.vs[52]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[53]["associationType"] = """channelNames"""
        self.vs[53]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[54]["associationType"] = """channelNames"""
        self.vs[54]["mm__"] = """directLink_T"""
        
        # backward association State---->ProcDef node
        self.add_node()
        self.vs[55]["type"] = """ruleDef"""
        self.vs[55]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class State()
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class ProcDef()
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class LocalDef()
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class Name()
                (1,12), # applymodel -> apply_contains
                (12,11), # apply_contains -> apply_class New()
                (1,14), # applymodel -> apply_contains
                (14,13), # apply_contains -> apply_class Name()
                (1,16), # applymodel -> apply_contains
                (16,15), # apply_contains -> apply_class Name()
                (1,18), # applymodel -> apply_contains
                (18,17), # apply_contains -> apply_class Name()
                (1,20), # applymodel -> apply_contains
                (20,19), # apply_contains -> apply_class Par()
                (1,22), # applymodel -> apply_contains
                (22,21), # apply_contains -> apply_class Inst()
                (1,24), # applymodel -> apply_contains
                (24,23), # apply_contains -> apply_class Inst()
                (1,26), # applymodel -> apply_contains
                (26,25), # apply_contains -> apply_class Name()
                (1,28), # applymodel -> apply_contains
                (28,27), # apply_contains -> apply_class Name()
                (1,30), # applymodel -> apply_contains
                (30,29), # apply_contains -> apply_class Name()
                (1,32), # applymodel -> apply_contains
                (32,31), # apply_contains -> apply_class Name()
                (1,34), # applymodel -> apply_contains
                (34,33), # apply_contains -> apply_class Name()
                (1,36), # applymodel -> apply_contains
                (36,35), # apply_contains -> apply_class Name()
                (1,38), # applymodel -> apply_contains
                (38,37), # apply_contains -> apply_class Name()
                (5,39), # apply_class ProcDef() -> association p
                (39,7), # association p  -> apply_class LocalDef()
                (5,40), # apply_class ProcDef() -> association channelNames
                (40,9), # association channelNames  -> apply_class Name()
                (7,41), # apply_class LocalDef() -> association p
                (41,11), # association p  -> apply_class New()
                (11,42), # apply_class New() -> association channelNames
                (42,13), # association channelNames  -> apply_class Name()
                (11,43), # apply_class New() -> association channelNames
                (43,15), # association channelNames  -> apply_class Name()
                (11,44), # apply_class New() -> association channelNames
                (44,17), # association channelNames  -> apply_class Name()
                (11,45), # apply_class New() -> association p
                (45,19), # association p  -> apply_class Par()
                (19,46), # apply_class Par() -> association p
                (46,23), # association p  -> apply_class Inst()
                (19,47), # apply_class Par() -> association p
                (47,21), # association p  -> apply_class Inst()
                (21,48), # apply_class Inst() -> association channelNames
                (48,25), # association channelNames  -> apply_class Name()
                (21,49), # apply_class Inst() -> association channelNames
                (49,27), # association channelNames  -> apply_class Name()
                (21,50), # apply_class Inst() -> association channelNames
                (50,29), # association channelNames  -> apply_class Name()
                (21,51), # apply_class Inst() -> association channelNames
                (51,31), # association channelNames  -> apply_class Name()
                (23,52), # apply_class Inst() -> association channelNames
                (52,33), # association channelNames  -> apply_class Name()
                (23,53), # apply_class Inst() -> association channelNames
                (53,35), # association channelNames  -> apply_class Name()
                (23,54), # apply_class Inst() -> association channelNames
                (54,37), # association channelNames  -> apply_class Name()
                (5,55), # apply_class ProcDef() -> backward_association
                (55,3), #  backward_association -> apply_class State()
		])
		
        # Add the equations
        self.equations = [((3,'isComposite'),('constant','true')), ((5,'__ApplyAttribute'),('constant','procdef')), ((7,'__ApplyAttribute'),('constant','localdefcompstate')), ((9,'literal'),('constant','sh')), ((13,'literal'),('constant','exit_in')), ((15,'literal'),('constant','exack_in')), ((17,'literal'),('constant','sh_in')), ((21,'name'),('constant','C')), ((23,'name'),('constant','H')), ((25,'literal'),('constant','enp')), ((27,'literal'),('constant','exit_in')), ((29,'literal'),('constant','exack_in')), ((31,'literal'),('constant','sh_in')), ((33,'literal'),('constant','exit_in')), ((35,'literal'),('constant','exack_in')), ((37,'literal'),('constant','sh_in')), ]
        
