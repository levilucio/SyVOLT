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
        self.vs[2]["attr1"] = """CompositeState2ProcDef"""
        
        # match class State() node
        self.add_node()
        
        self.vs[3]["mm__"] = """State""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class ProcDef() node
        self.add_node()

        self.vs[4]["mm__"] = """ProcDef""" 
        self.vs[4]["attr1"] = """1"""
        # apply class LocalDef() node
        self.add_node()

        self.vs[5]["mm__"] = """LocalDef""" 
        self.vs[5]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[6]["mm__"] = """Name""" 
        self.vs[6]["attr1"] = """1"""
        # apply class New() node
        self.add_node()

        self.vs[7]["mm__"] = """New""" 
        self.vs[7]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[8]["mm__"] = """Name""" 
        self.vs[8]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[9]["mm__"] = """Name""" 
        self.vs[9]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[10]["mm__"] = """Name""" 
        self.vs[10]["attr1"] = """1"""
        # apply class Par() node
        self.add_node()

        self.vs[11]["mm__"] = """Par""" 
        self.vs[11]["attr1"] = """1"""
        # apply class Inst() node
        self.add_node()

        self.vs[12]["mm__"] = """Inst""" 
        self.vs[12]["attr1"] = """1"""
        # apply class Inst() node
        self.add_node()

        self.vs[13]["mm__"] = """Inst""" 
        self.vs[13]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[14]["mm__"] = """Name""" 
        self.vs[14]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[15]["mm__"] = """Name""" 
        self.vs[15]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[16]["mm__"] = """Name""" 
        self.vs[16]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[17]["mm__"] = """Name""" 
        self.vs[17]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[18]["mm__"] = """Name""" 
        self.vs[18]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[19]["mm__"] = """Name""" 
        self.vs[19]["attr1"] = """1"""
        # apply class Name() node
        self.add_node()

        self.vs[20]["mm__"] = """Name""" 
        self.vs[20]["attr1"] = """1"""
        
        
        
        # apply association ProcDef--p-->LocalDef node
        self.add_node()
        self.vs[21]["attr1"] = """p"""
        self.vs[21]["mm__"] = """directLink_T"""
        # apply association ProcDef--channelNames-->Name node
        self.add_node()
        self.vs[22]["attr1"] = """channelNames"""
        self.vs[22]["mm__"] = """directLink_T"""
        # apply association LocalDef--p-->New node
        self.add_node()
        self.vs[23]["attr1"] = """p"""
        self.vs[23]["mm__"] = """directLink_T"""
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[24]["attr1"] = """channelNames"""
        self.vs[24]["mm__"] = """directLink_T"""
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[25]["attr1"] = """channelNames"""
        self.vs[25]["mm__"] = """directLink_T"""
        # apply association New--channelNames-->Name node
        self.add_node()
        self.vs[26]["attr1"] = """channelNames"""
        self.vs[26]["mm__"] = """directLink_T"""
        # apply association New--p-->Par node
        self.add_node()
        self.vs[27]["attr1"] = """p"""
        self.vs[27]["mm__"] = """directLink_T"""
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[28]["attr1"] = """p"""
        self.vs[28]["mm__"] = """directLink_T"""
        # apply association Par--p-->Inst node
        self.add_node()
        self.vs[29]["attr1"] = """p"""
        self.vs[29]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[30]["attr1"] = """channelNames"""
        self.vs[30]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[31]["attr1"] = """channelNames"""
        self.vs[31]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[32]["attr1"] = """channelNames"""
        self.vs[32]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[33]["attr1"] = """channelNames"""
        self.vs[33]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[34]["attr1"] = """channelNames"""
        self.vs[34]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[35]["attr1"] = """channelNames"""
        self.vs[35]["mm__"] = """directLink_T"""
        # apply association Inst--channelNames-->Name node
        self.add_node()
        self.vs[36]["attr1"] = """channelNames"""
        self.vs[36]["mm__"] = """directLink_T"""
        
        # backward association State---->ProcDef node
        self.add_node()

        self.vs[37]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class State()
                (1,4), # applymodel -> -> apply_class ProcDef()
                (1,5), # applymodel -> -> apply_class LocalDef()
                (1,6), # applymodel -> -> apply_class Name()
                (1,7), # applymodel -> -> apply_class New()
                (1,8), # applymodel -> -> apply_class Name()
                (1,9), # applymodel -> -> apply_class Name()
                (1,10), # applymodel -> -> apply_class Name()
                (1,11), # applymodel -> -> apply_class Par()
                (1,12), # applymodel -> -> apply_class Inst()
                (1,13), # applymodel -> -> apply_class Inst()
                (1,14), # applymodel -> -> apply_class Name()
                (1,15), # applymodel -> -> apply_class Name()
                (1,16), # applymodel -> -> apply_class Name()
                (1,17), # applymodel -> -> apply_class Name()
                (1,18), # applymodel -> -> apply_class Name()
                (1,19), # applymodel -> -> apply_class Name()
                (1,20), # applymodel -> -> apply_class Name()
                (4,21), # apply_class ProcDef() -> association p
                (21,5), # association p  -> apply_class LocalDef()
                (4,22), # apply_class ProcDef() -> association channelNames
                (22,6), # association channelNames  -> apply_class Name()
                (5,23), # apply_class LocalDef() -> association p
                (23,7), # association p  -> apply_class New()
                (7,24), # apply_class New() -> association channelNames
                (24,8), # association channelNames  -> apply_class Name()
                (7,25), # apply_class New() -> association channelNames
                (25,9), # association channelNames  -> apply_class Name()
                (7,26), # apply_class New() -> association channelNames
                (26,10), # association channelNames  -> apply_class Name()
                (7,27), # apply_class New() -> association p
                (27,11), # association p  -> apply_class Par()
                (11,28), # apply_class Par() -> association p
                (28,13), # association p  -> apply_class Inst()
                (11,29), # apply_class Par() -> association p
                (29,12), # association p  -> apply_class Inst()
                (12,30), # apply_class Inst() -> association channelNames
                (30,14), # association channelNames  -> apply_class Name()
                (12,31), # apply_class Inst() -> association channelNames
                (31,15), # association channelNames  -> apply_class Name()
                (12,32), # apply_class Inst() -> association channelNames
                (32,16), # association channelNames  -> apply_class Name()
                (12,33), # apply_class Inst() -> association channelNames
                (33,17), # association channelNames  -> apply_class Name()
                (13,34), # apply_class Inst() -> association channelNames
                (34,18), # association channelNames  -> apply_class Name()
                (13,35), # apply_class Inst() -> association channelNames
                (35,19), # association channelNames  -> apply_class Name()
                (13,36), # apply_class Inst() -> association channelNames
                (36,20), # association channelNames  -> apply_class Name()
                (4,37), # apply_class ProcDef() -> backward_association
                (37,3), #  backward_association -> apply_class State()
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'isComposite'),('constant','true')), ((6,'literal'),('constant','sh')), ((8,'literal'),('constant','exit_in')), ((9,'literal'),('constant','exack_in')), ((10,'literal'),('constant','sh_in')), ((12,'name'),('constant','C')), ((13,'name'),('constant','H')), ((14,'literal'),('constant','enp')), ((15,'literal'),('constant','exit_in')), ((16,'literal'),('constant','exack_in')), ((17,'literal'),('constant','sh_in')), ((18,'literal'),('constant','exit_in')), ((19,'literal'),('constant','exack_in')), ((20,'literal'),('constant','sh_in')), ]

        
