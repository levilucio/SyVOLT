
from enum import Enum
class MutationOperators(Enum):
    RENAME_CLASS = "RENAME"
    DELETE_CLASS = "DELETE"

    #CLASSES:
    #Replace class with another class
    #Add/remove classes
    #Change Any/Exists type of classes
    #Change positive/negative type of classes

    #ASSOCIATIONS:
    #Remove/add associations
    #Change class of associations
    #Change positive/negative associations
    #Change direct/indirect associations

    #BACKWARD LINKS
    #Add/remove backward links
    #Change negative/positive

    #ATTRIBUTES
    #Add/remove attributes
    #Change match attrib
    #Change Atom value (what values?)
    #Change apply attrib
    #Change target of attribRef
    #Concat, prefer one or the other side

class Mutator:



    def __init__(self):
        pass
