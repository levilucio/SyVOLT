import re

'''

1. Relaxation, which relaxes constraints on the language which are
no longer valid for the pattern language. For instance, it should
be possible to instantiate abstract classes in rule patterns.

2. Augmentation, which augments metamodel elements with at-
tributes used by the transformation engine.

3. Modification, which modifies the data type of attributes such
that they can express constraints on attribute values or actions
which compute the new value of the attribute.'''


#the default eval match code
def get_default_match_code():

    return """\"\"\"                                                                             
    #===============================================================================
    # This code is executed when evaluating if a node shall be matched by this rule.
    # You can access the value of the current node's attribute value by: attr_value.
    # You can access any attribute x of this node by: this['x'].                    
    # If the constraint relies on attribute values from other nodes,                
    # use the LHS/NAC constraint instead.                                           
    # The given constraint must evaluate to a boolean expression.                   
    #===============================================================================
                                                                                    
    return True                                                                     
    \"\"\"                                                                             \n"""

'''
 changeAttrType (M): Changes the type of attributes to 'string', which allows conditions and actions to be specified on attribute values in patterns.
 Also appends '__' to attributes starting with '__'. This is because the pLabel and pMatchSubtypes attributes (introduced in one of the next steps) need to be scoped appropriately for HOTs. 
 The first time a metamodel is ramified, each class will have a __pLabel and __pMatchSubtypes attribute.
 The next time, these attributes are renamed to ____pLabel and ____pMatchSubtypes, to allow a condition/action to be specified for the __pLabel and __pMatchSubtypes attributes which were introduced in the first RAMified metamodel.
'''
def changeAttrType(h):
    out_h = []	
    global g_attrs
    
    #make sure g_attrs is defined
    if not 'g_attrs' in globals():
        g_attrs = []
    
    for line in h:

        #grab all lines that aren't the GUID
        if "self.vs" in line and not "[\"GUID__\"]" in line:
            g_attrs.append(line.strip())


        #add 'MT_pre__' to all non-mm or GUID attributes
        if "self.vs" in line and not ( "[\"mm__\"]" in line or "[\"GUID__\"]" in line):

			#get the LHS
			first = line.split("=")[0]
			
			if "[\"__pre" in first:
				#double RAMify. Untested.
				first = re.sub(r'(")(\w+)(")', r'\1__\2\3', first)
			else:
				first = re.sub(r'(")(\w+)(")', r'\1MT_pre__\2\3', first)

            #make the RHS equal to the default match code
            #TODO: this should be consistent with the evals at the bottom of the himesis file
			second = line.split("=")[1]
			second = get_default_match_code()

			line = first + "= " + second
        out_h.append(line)
    return (out_h, False)

#returns the default constraint for the model transformation
def get_MT_constraint():
    return """
        self["MT_constraint__"] =  \"\"\"
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================

        return True
        \"\"\"
        \n"""


# renameClass, renameAssociation and renameSelfAssociation (M): 
#Appends '__p' to classes and associations, which is needed for the transformation engine.
def renameClass(h):


    out_h = []	
    for line in h:
        
        #add to import statement
        if "from core.himesis import Himesis" in line:
            line = line.strip() + ", HimesisPreConditionPatternLHS\n"
            
        #changes superclass of object
        if "class " in line and "(Himesis)" in line:
            line = line.replace("(Himesis)","(HimesisPreConditionPatternLHS)")
        
        #add in the MT_constraint
        if "self[\"name\"]" in line:
            out_h.append(get_MT_constraint())
    
        #add 'MT_pre__' before all mm__ attributes
        if "self.vs" in line and "[\"mm__\"]" in line:
            line = re.sub(r'(""")(\w+)(""")', r'\1MT_pre__\2\3', line)

        out_h.append(line)
    return (out_h, False)



#the default eval action
def addEval(attr_name, attr_number):
    return """    def eval_""" + attr_name + attr_number + """(self, attr_value, this):
            
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access any attribute x of this node by: this['x'].
        # If the constraint relies on attribute values from other nodes,
        # use the LHS/NAC constraint instead.
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True\n\n"""


#add evals for each attribute
def addEvals(h):
    output = []
    element_desc = []
    
    for attr in g_attrs:
        print("Attr: " + attr)
        
    #for each of the attributes found for the nodes
    for attr in g_attrs:
        attr_split = attr.split("=")
       
        #get the node number for this attribute
        attr_number = re.search(r'(\[)(\d+)(\])', attr).group(2)
        index = int(attr_number)
        
        #add a new eval section if this node is new
        if len(output) <= index:
            output.append("")
            element_desc.append("")
        
        #get the name and value for this attribute
        attr_name = re.search(r'(\[")(\w+)("\])',attr_split[0]).group(2)
        attr_value = re.search(r'(""")(.+)(""")',attr_split[1].strip()).group(2)

        #if not the mm, add the eval function, and add to the header
        if not attr_name == "mm__":
            output[index] = output[index] + addEval(attr_name, attr_number)
            element_desc[index] = element_desc[index] + "(" + attr_name + ", " + attr_value + ") "
        
        #when the mm is seen
        else:
            #if something has been added, add the header to the output line
            if output[index] != "":
                output[index] = "    #" + attr_name + ": " + attr_value + " = " + element_desc[index] + "\n" + output[index]
    

    #add each output line to the file
    for i in range(len(output)):
        h.append(output[i])
        
    return (h, False)



#add the constraint at the bottom of the himesis file
def addConstraint(h):

    constraint_line = """
    def constraint(self, PreNode, graph):
        \"\"\"
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                        and returns the node corresponding to that label.
        \"\"\"
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================

        return True\n"""

    h.append(constraint_line)
   
    return (h, False)


#(R) Disables global actions and constraints defined on the metamodel.
def disableAction(h):
	return (h, False)

def disableConstraint(h):
	return (h, False)

# removeLowerBound (R): Sets the lower bound of multiplicites to 0.
def removeLowerBound(h):
	return (h, False)
	
	
#covered by renameClass?
def renameAssociation(h):
	return (h, False)

def renameSelfAssociation(h):
	return (h, False)



# makeConcrete (R): Makes abstract classes concrete.
def makeConcrete(h):
	return (h, False)


# disableClassActionsConstraints (R): Disables actions and constraints defined on the classes of the metamodel.
def disableClassActionsConstraints(h):
	return (h, False)


# renameCardinalities (M): Modifies the cardinalities such that they reflect the change in name of the association.
def renameCardinalities(h):
	return (h, False)
	

# addPLabel (A): Adds the pLabel attribute to classes, which is used to identify elements across patterns of a rule.
def addPLabel(h):
    
	return (h, False)


# addPLabelAction (A): Adds the action which automatically assigns the pLabel attribute when a class is instantiated.
def addPLabelAction(h):
	return (h, False)


# addMatchSubtypes (A): Adds the pMatchSubtypes attribute, which signifies whether instances of the subclasses of an element of a pattern should also be matched.
def addMatchSubtypes(h):
	return (h, False)


# addSelfAssociationAttributes and addAssociationAttributes (A): Adds the pMatchSubtypes and pLabel attributes to associations.
def addSelfAssociationAttributes(h):
	return (h, False)

def addAssociationAttributes(h):
	return (h, False)


# renameCS (M): Renames the concrete syntax icon of a class to match its new name.
def renameCS(h):
	return (h, False)


# renameCSConnector (M): Renames the concrete syntax connector of an association to match its new name.
def renameCSConnector(h):
	return (h, False)


# clearParserMappers and clearIconParserMappers (M): Disables parsers and mappers of classes and icons.
def clearParserMappers(h):
	return (h, False)

def clearIconParserMappers(h):
	return (h, False)

# addCS (A): Adds a concrete syntax icon for (former) abstract classes.
def addCS(h):
	return (h, False)


# addCSPLabel and addCSConnectorPLabel (A): Adds a concrete syntax representation for the pLabel attribute.
def addCSPLabel(h):
	return (h, False)

def addCSConnectorPLabel(h):
	return (h, False)


# addCSContents (A): Adds a concrete syntax representation to the icon introduced for (former) abstract classes.
def addCSContents(h):
	return (h, False)


# remove*Link*: Removes GenericLinks introduced during the transformation.
def removeLink(h):
	return (h, False)
	
