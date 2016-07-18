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
        self.vs[2]["attr1"] = """layer6rule0"""
        
        # match class Function(layer6rule0class0) node
        self.add_node()
        
        self.vs[3]["mm__"] = """Function""" 
        self.vs[3]["attr1"] = """+""" 
        
        
        # apply class StatementList(layer6rule0class1) node
        self.add_node()

        self.vs[4]["mm__"] = """StatementList""" 
        self.vs[4]["attr1"] = """1"""
        # apply class ReturnStatement(layer6rule0class2) node
        self.add_node()

        self.vs[5]["mm__"] = """ReturnStatement""" 
        self.vs[5]["attr1"] = """1"""
        # apply class NumberLiteral(layer6rule0class3) node
        self.add_node()

        self.vs[6]["mm__"] = """NumberLiteral""" 
        self.vs[6]["attr1"] = """1"""
        
        
        
        # apply association StatementList--statements-->ReturnStatement node
        self.add_node()
        self.vs[7]["attr1"] = """statements"""
        self.vs[7]["mm__"] = """directLink_T"""
        # apply association ReturnStatement--expression-->NumberLiteral node
        self.add_node()
        self.vs[8]["attr1"] = """expression"""
        self.vs[8]["mm__"] = """directLink_T"""
        
        # backward association Function---->StatementList node
        self.add_node()

        self.vs[9]["mm__"] = """backward_link"""
        
        
        
        
        # Add the edges
        self.add_edges([
                (0,3), # matchmodel -> match_class Function(layer6rule0class0)
                (1,4), # applymodel -> -> apply_class StatementList(layer6rule0class1)
                (1,5), # applymodel -> -> apply_class ReturnStatement(layer6rule0class2)
                (1,6), # applymodel -> -> apply_class NumberLiteral(layer6rule0class3)
                (4,7), # apply_class StatementList(layer6rule0class1) -> association statements
                (7,5), # association statements  -> apply_class ReturnStatement(layer6rule0class2)
                (5,8), # apply_class ReturnStatement(layer6rule0class2) -> association expression
                (8,6), # association expression  -> apply_class NumberLiteral(layer6rule0class3)
                (4,9), # apply_class StatementList(layer6rule0class1) -> backward_association
                (9,3), #  backward_association -> apply_class Function(layer6rule0class0)
                (0,2), # matchmodel -> pairedwith
                (2,1) # pairedwith -> applyModel				
		])

        # Add the attribute equations
        self["equations"] = [((3,'name'),('constant','main')), ((4,'__ApplyAttribute'),('constant','MainBody')), ((6,'value'),('constant','0')), ]

        
