

from core.himesis import Himesis, HimesisPreConditionPatternLHS

class HFindTwoMatchElementsSameTypeDiffRulesLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HFindTwoMatchElementsSameTypeDiffRulesLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFindTwoMatchElementsSameTypeDiffRulesLHS, self).__init__(name='HFindTwoMatchElementsSameTypeDiffRulesLHS', num_nodes=6, edges=[])
        
        # Add the edges
        self.add_edges([[4, 0], [0, 2], [5, 1], [1, 3]])
        # Set the graph attributes
        self["name"] = """"""
        self["mm__"] = ['MT_pre__FamiliesToPersons_MM', 'MoTifRule']
        self["MT_constraint__"] = """
guid1 = PreNode('1').index
guid2 = PreNode('2').index

matchModel1ID = PreNode('3').index
matchModel2ID = PreNode('4').index

if PreNode('1')['mm__'] == PreNode('2')['mm__'] and int(guid1) < int(guid2) and int(matchModel1ID) < int(matchModel2ID):
    return True
return False
"""
        self["superclasses_dict"] = {'Woman': ['MetaModelElement_T'], 'HouseholdRoot': ['MetaModelElement_S'], 'Family': ['MetaModelElement_S'], 'Member': ['MetaModelElement_S'], 'Person': ['MetaModelElement_T'], 'CommunityRoot': ['MetaModelElement_T'], 'Man': ['MetaModelElement_T']}
        self["equations"] = []
        self["GUID__"] = 4448450274503426919
        
        # Set the node attributes
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["mm__"] = """MT_pre__match_contains"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = 7181928297639646230
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["mm__"] = """MT_pre__match_contains"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = 7943422122721247554
        self.vs[2]["MT_pivotOut__"] = """element1"""
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__attr1"] = """

return True
"""
        self.vs[2]["GUID__"] = 2210858195324649237
        self.vs[3]["MT_pivotOut__"] = """element2"""
        self.vs[3]["MT_label__"] = """2"""
        self.vs[3]["mm__"] = """MT_pre__MetaModelElement_S"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__attr1"] = """

return True
"""
        self.vs[3]["GUID__"] = 2056133774871146816
        self.vs[4]["MT_label__"] = """3"""
        self.vs[4]["mm__"] = """MT_pre__MatchModel"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = 4699185555220633200
        self.vs[5]["MT_label__"] = """4"""
        self.vs[5]["mm__"] = """MT_pre__MatchModel"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = 1687034107671583005

    def eval_attr11(self, attr_value, this):
        
        
        return True


    def eval_attr12(self, attr_value, this):
        
        
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        
        guid1 = PreNode('1').index
        guid2 = PreNode('2').index
        
        matchModel1ID = PreNode('3').index
        matchModel2ID = PreNode('4').index
        
        if PreNode('1')['mm__'] == PreNode('2')['mm__'] and int(guid1) < int(guid2) and int(matchModel1ID) < int(matchModel2ID):
            return True
        return False

