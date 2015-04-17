"""
__MT_post___MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Jan 25 15:25:49 2013
_______________________________________________________________________
"""
from ASG_MT_post__ import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MT_post__MetaModelElement_S       import *
from MT_post__Station_S       import *
from MT_post__Male_S       import *
from MT_post__Female_S       import *
from MT_post__MatchModel       import *
from MT_post__ApplyModel       import *
from MT_post__MetaModelElement_T       import *
from MT_post__Station_T       import *
from MT_post__Male_T       import *
from MT_post__Female_T       import *
from MT_post__GenericNode_       import *
from MT_post__match_contains       import *
from MT_post__apply_contains       import *
from MT_post__backward_link       import *
from MT_post__indirectLink_S       import *
from MT_post__directLink_T       import *
from MT_post__directLink_S       import *
from MT_post__GenericEdge_       import *
def createNewASGroot(self):
   return ASG_MT_post__(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MT_post__MetaModelElement_S", command=lambda x=self: x.createNewMT_post__MetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Station_S", command=lambda x=self: x.createNewMT_post__Station_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Male_S", command=lambda x=self: x.createNewMT_post__Male_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Female_S", command=lambda x=self: x.createNewMT_post__Female_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__MatchModel", command=lambda x=self: x.createNewMT_post__MatchModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__ApplyModel", command=lambda x=self: x.createNewMT_post__ApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__MetaModelElement_T", command=lambda x=self: x.createNewMT_post__MetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Station_T", command=lambda x=self: x.createNewMT_post__Station_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Male_T", command=lambda x=self: x.createNewMT_post__Male_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__Female_T", command=lambda x=self: x.createNewMT_post__Female_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__GenericNode_", command=lambda x=self: x.createNewMT_post__GenericNode_(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__match_contains", command=lambda x=self: x.createNewMT_post__match_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__apply_contains", command=lambda x=self: x.createNewMT_post__apply_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__backward_link", command=lambda x=self: x.createNewMT_post__backward_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__indirectLink_S", command=lambda x=self: x.createNewMT_post__indirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__directLink_T", command=lambda x=self: x.createNewMT_post__directLink_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__directLink_S", command=lambda x=self: x.createNewMT_post__directLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_post__GenericEdge_", command=lambda x=self: x.createNewMT_post__GenericEdge_(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['MT_post__match_contains']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__MetaModelElement_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__GenericEdge_']={
           'MT_post__match_contains': [( 'MT_post__MatchModel', self.createNewMT_post__MatchModel)]
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': [( 'MT_post__GenericNode_', self.createNewMT_post__GenericNode_)]
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__Station_T', self.createNewMT_post__Station_T), ( 'MT_post__Male_T', self.createNewMT_post__Male_T), ( 'MT_post__Female_T', self.createNewMT_post__Female_T)]
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__Station_T', self.createNewMT_post__Station_T), ( 'MT_post__Male_T', self.createNewMT_post__Male_T), ( 'MT_post__Female_T', self.createNewMT_post__Female_T)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [( 'MT_post__ApplyModel', self.createNewMT_post__ApplyModel)] }
    self.ConnectivityMap['MT_post__directLink_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__MetaModelElement_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Station_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__Male_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Male_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__directLink_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__Station_T', self.createNewMT_post__Station_T), ( 'MT_post__Male_T', self.createNewMT_post__Male_T), ( 'MT_post__Female_T', self.createNewMT_post__Female_T)]
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__Station_T', self.createNewMT_post__Station_T), ( 'MT_post__Male_T', self.createNewMT_post__Male_T), ( 'MT_post__Female_T', self.createNewMT_post__Female_T)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__Female_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__MatchModel']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': [( 'MT_post__match_contains', self.createNewMT_post__match_contains)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__indirectLink_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__Female_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Station_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__Male_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Male_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__apply_contains']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__Station_T', self.createNewMT_post__Station_T), ( 'MT_post__Male_T', self.createNewMT_post__Male_T), ( 'MT_post__Female_T', self.createNewMT_post__Female_T)]
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': [( 'MT_post__MetaModelElement_T', self.createNewMT_post__MetaModelElement_T), ( 'MT_post__Station_T', self.createNewMT_post__Station_T), ( 'MT_post__Male_T', self.createNewMT_post__Male_T), ( 'MT_post__Female_T', self.createNewMT_post__Female_T)]
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__backward_link']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': [( 'MT_post__MetaModelElement_S', self.createNewMT_post__MetaModelElement_S), ( 'MT_post__Station_S', self.createNewMT_post__Station_S), ( 'MT_post__Male_S', self.createNewMT_post__Male_S), ( 'MT_post__Female_S', self.createNewMT_post__Female_S)]
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__ApplyModel']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': []
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__Station_T': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_T': [( 'MT_post__apply_contains', self.createNewMT_post__apply_contains)]
          ,'MT_post__Male_S': []
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__GenericNode_']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__MatchModel': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__Station_T': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__GenericNode_': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__Station_S': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__Male_T': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__Male_S': [( 'MT_post__GenericEdge_', self.createNewMT_post__GenericEdge_)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__Station_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__Male_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Station_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__Male_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Male_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__Male_S']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__Male_T': []
          ,'MT_post__Male_S': [( 'MT_post__indirectLink_S', self.createNewMT_post__indirectLink_S), ( 'MT_post__directLink_S', self.createNewMT_post__directLink_S)]
          ,'MT_post__apply_contains': [] }
    self.ConnectivityMap['MT_post__Station_T']={
           'MT_post__match_contains': []
          ,'MT_post__MetaModelElement_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__GenericEdge_': []
          ,'MT_post__directLink_S': []
          ,'MT_post__MetaModelElement_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__directLink_T': []
          ,'MT_post__Female_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__MatchModel': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__Female_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Station_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__backward_link': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__Station_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__Male_T': [( 'MT_post__directLink_T', self.createNewMT_post__directLink_T)]
          ,'MT_post__Male_S': [( 'MT_post__backward_link', self.createNewMT_post__backward_link)]
          ,'MT_post__apply_contains': [] }
    
    self.CardinalityTable['MT_post__MetaModelElement_S']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Station_S']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Male_S']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Female_S']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': [('0', 'N', 'Destination')]
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': [('0', 'N', 'Destination')]
          ,'MT_post__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__MatchModel']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': [('0', 'N', 'Source')]
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__ApplyModel']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': [('0', 'N', 'Source')]
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__MetaModelElement_T']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Station_T']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Male_T']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__Female_T']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_post__backward_link': [('0', 'N', 'Source')]
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__GenericNode_']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [('0', 'N', 'Source'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_post__match_contains']={
          'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__Station_S': [('0', 'N', 'Source')]
          ,'MT_post__Male_S': [('0', 'N', 'Source')]
          ,'MT_post__Female_S': [('0', 'N', 'Source')]
          ,'MT_post__MatchModel': [('0', 'N', 'Destination')]
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    self.CardinalityTable['MT_post__apply_contains']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': [('0', 'N', 'Destination')]
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_post__Station_T': [('0', 'N', 'Source')]
          ,'MT_post__Male_T': [('0', 'N', 'Source')]
          ,'MT_post__Female_T': [('0', 'N', 'Source')]
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    self.CardinalityTable['MT_post__backward_link']={
          'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__Station_S': [('0', 'N', 'Source')]
          ,'MT_post__Male_S': [('0', 'N', 'Source')]
          ,'MT_post__Female_S': [('0', 'N', 'Source')]
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_post__Station_T': [('0', 'N', 'Destination')]
          ,'MT_post__Male_T': [('0', 'N', 'Destination')]
          ,'MT_post__Female_T': [('0', 'N', 'Destination')]
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    self.CardinalityTable['MT_post__indirectLink_S']={
          'MT_post__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Station_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Male_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Female_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    self.CardinalityTable['MT_post__directLink_T']={
          'MT_post__MetaModelElement_S': []
          ,'MT_post__Station_S': []
          ,'MT_post__Male_S': []
          ,'MT_post__Female_S': []
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Station_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Male_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Female_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    self.CardinalityTable['MT_post__directLink_S']={
          'MT_post__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Station_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Male_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__Female_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_post__MatchModel': []
          ,'MT_post__ApplyModel': []
          ,'MT_post__MetaModelElement_T': []
          ,'MT_post__Station_T': []
          ,'MT_post__Male_T': []
          ,'MT_post__Female_T': []
          ,'MT_post__GenericNode_': []
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    self.CardinalityTable['MT_post__GenericEdge_']={
          'MT_post__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_post__Station_S': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__Male_S': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__Female_S': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__MatchModel': [('0', 'N', 'Source')]
          ,'MT_post__ApplyModel': [('0', 'N', 'Source')]
          ,'MT_post__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_post__Station_T': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__Male_T': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__Female_T': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_post__GenericNode_': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'MT_post__match_contains': []
          ,'MT_post__apply_contains': []
          ,'MT_post__backward_link': []
          ,'MT_post__indirectLink_S': []
          ,'MT_post__directLink_T': []
          ,'MT_post__directLink_S': []
          ,'MT_post__GenericEdge_': [] }
    
    self.entitiesInMetaModel['MT_post__']=["MT_post__MetaModelElement_S", "MT_post__Station_S", "MT_post__Male_S", "MT_post__Female_S", "MT_post__MatchModel", "MT_post__ApplyModel", "MT_post__MetaModelElement_T", "MT_post__Station_T", "MT_post__Male_T", "MT_post__Female_T", "MT_post__GenericNode_", "MT_post__match_contains", "MT_post__apply_contains", "MT_post__backward_link", "MT_post__indirectLink_S", "MT_post__directLink_T", "MT_post__directLink_S", "MT_post__GenericEdge_"]

    
def createNewMT_post__MetaModelElement_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__MetaModelElement_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__MetaModelElement_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__MetaModelElement_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__MetaModelElement_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__Station_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Station_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Station_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Station_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Station_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Station_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__Male_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Male_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Male_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Male_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Male_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Male_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__Female_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Female_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Female_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Female_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Female_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Female_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__MatchModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__MatchModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__MatchModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__MatchModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__MatchModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__MatchModel", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__ApplyModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__ApplyModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__ApplyModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__ApplyModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__ApplyModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__ApplyModel", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__MetaModelElement_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__MetaModelElement_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__MetaModelElement_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__MetaModelElement_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__MetaModelElement_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__MetaModelElement_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__Station_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Station_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Station_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Station_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Station_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Station_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__Male_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Male_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Male_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Male_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Male_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Male_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__Female_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__Female_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__Female_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__Female_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__Female_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__Female_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__GenericNode_(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__GenericNode_(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__GenericNode_"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__GenericNode_(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__GenericNode_(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__GenericNode_", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__match_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__match_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__match_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__match_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__match_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__match_contains", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__apply_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__apply_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__apply_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__apply_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__apply_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__apply_contains", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__backward_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__backward_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__backward_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__backward_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__backward_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__backward_link", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__indirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__indirectLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__indirectLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__indirectLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__indirectLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__indirectLink_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__directLink_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__directLink_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__directLink_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__directLink_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__directLink_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__directLink_T", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__directLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__directLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__directLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__directLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__directLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__directLink_S", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewMT_post__GenericEdge_(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_post__GenericEdge_(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_post__GenericEdge_"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_post__GenericEdge_(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_post__GenericEdge_(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_post__GenericEdge_", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_MT_post__(self)
   ne = len(self.ASGroot.listNodes["ASG_MT_post__"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_MT_post__", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("String", "ATOM3String", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Boolean", "ATOM3Boolean", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Float", "ATOM3Float", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Action", "ATOM3Action", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Link", "ATOM3Link", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Port", "ATOM3Port", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Connection", "ATOM3Connection", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("MSEnum", "ATOM3MSEnum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Text", "ATOM3Text", params, (None, 0) ))
    objs.append(obj)
    self.typeList.setValue(objs)

