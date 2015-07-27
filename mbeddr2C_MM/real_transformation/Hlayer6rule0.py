from core.himesis import Himesis
import uuid

class Hlayer6rule0(Himesis):
    def __init__(self):

    
    
        """
        Creates the himesis graph representing the DSLTrans rule layer6rule0.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(Hlayer6rule0, self).__init__(name='Hlayer6rule0', num_nodes=0, edges=[])
        
        
        # Set the graph attributes
        self["mm__"] = ['HimesisMM']
        
        self["name"] = """layer6rule0"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'layer6rule0')
        
        # match model. We only support one match model
        self.add_node()
        self.vs[0]["mm__"] = """MatchModel"""
        
        # apply model node
        self.add_node()
        self.vs[1]["mm__"] = """ApplyModel"""
        
        # paired with relation between match and apply models
        self.add_node()
        self.vs[2]["mm__"] = """paired_with"""
        self.vs[2]["rulename"] = """layer6rule0"""
        
        # match class Function(layer6rule0class0) node
        self.add_node()
        self.vs[3]["name"] = """layer6rule0class0""" 
        self.vs[3]["classtype"] = """Function"""
        self.vs[3]["mm__"] = """Function"""
        self.vs[3]["cardinality"] = """+""" 
        # match_contains node for class Function(layer6rule0class0)
        self.add_node()
        self.vs[4]["mm__"] = """match_contains"""
        
        
        # apply class StatementList(layer6rule0class1) node
        self.add_node()
        self.vs[5]["name"] = """layer6rule0class1""" 
        self.vs[5]["classtype"] = """StatementList"""
        self.vs[5]["mm__"] = """StatementList"""
        self.vs[5]["cardinality"] = """1"""
        # apply_contains node for class StatementList(layer6rule0class1)
        self.add_node()
        self.vs[6]["mm__"] = """apply_contains"""
        # apply class ReturnStatement(layer6rule0class2) node
        self.add_node()
        self.vs[7]["name"] = """layer6rule0class2""" 
        self.vs[7]["classtype"] = """ReturnStatement"""
        self.vs[7]["mm__"] = """ReturnStatement"""
        self.vs[7]["cardinality"] = """1"""
        # apply_contains node for class ReturnStatement(layer6rule0class2)
        self.add_node()
        self.vs[8]["mm__"] = """apply_contains"""
        # apply class NumberLiteral(layer6rule0class3) node
        self.add_node()
        self.vs[9]["name"] = """layer6rule0class3""" 
        self.vs[9]["classtype"] = """NumberLiteral"""
        self.vs[9]["mm__"] = """NumberLiteral"""
        self.vs[9]["cardinality"] = """1"""
        # apply_contains node for class NumberLiteral(layer6rule0class3)
        self.add_node()
        self.vs[10]["mm__"] = """apply_contains"""
        
        
        
        # apply association StatementList--statements-->ReturnStatement node
        self.add_node()
        self.vs[11]["associationType"] = """statements"""
        self.vs[11]["mm__"] = """directLink_T"""
        # apply association ReturnStatement--expression-->NumberLiteral node
        self.add_node()
        self.vs[12]["associationType"] = """expression"""
        self.vs[12]["mm__"] = """directLink_T"""
        
        # backward association Function---->StatementList node
        self.add_node()
        self.vs[13]["type"] = """ruleDef"""
        self.vs[13]["mm__"] = """backward_link"""
        
        
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,4), # matchmodel -> match_contains
                (4,3), # match_contains -> match_class Function(layer6rule0class0)
                (1,6), # applymodel -> apply_contains
                (6,5), # apply_contains -> apply_class StatementList(layer6rule0class1)
                (1,8), # applymodel -> apply_contains
                (8,7), # apply_contains -> apply_class ReturnStatement(layer6rule0class2)
                (1,10), # applymodel -> apply_contains
                (10,9), # apply_contains -> apply_class NumberLiteral(layer6rule0class3)
                (5,11), # apply_class StatementList(layer6rule0class1) -> association statements
                (11,7), # association statements  -> apply_class ReturnStatement(layer6rule0class2)
                (7,12), # apply_class ReturnStatement(layer6rule0class2) -> association expression
                (12,9), # association expression  -> apply_class NumberLiteral(layer6rule0class3)
                (5,13), # apply_class StatementList(layer6rule0class1) -> backward_association
                (13,3), #  backward_association -> apply_class Function(layer6rule0class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])
		
        # Add the attribute equations
        self["equations"] = [((3,'name'),('constant','main')), ((5,'__ApplyAttribute'),('constant','MainBody')), ((9,'value'),('constant','0')), ]

        
