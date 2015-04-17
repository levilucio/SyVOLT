"""
__MT_pre__FamiliesToPersonsMM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Apr 17 14:23:22 2015
_________________________________________________________________________________________
"""
from ASG_MT_pre__FamiliesToPersonsMM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MT_pre__MetaModelElement_S       import *
from MT_pre__HouseholdRoot       import *
from MT_pre__Family       import *
from MT_pre__Member       import *
from MT_pre__MatchModel       import *
from MT_pre__ApplyModel       import *
from MT_pre__MetaModelElement_T       import *
from MT_pre__CommunityRoot       import *
from MT_pre__Person       import *
from MT_pre__Man       import *
from MT_pre__Attribute       import *
from MT_pre__Equation       import *
from MT_pre__Expression       import *
from MT_pre__Constant       import *
from MT_pre__Concat       import *
from MT_pre__Woman       import *
from MT_pre__GenericNode_FamiliesToPersonsMM       import *
from MT_pre__match_contains       import *
from MT_pre__apply_contains       import *
from MT_pre__backward_link       import *
from MT_pre__indirectLink_S       import *
from MT_pre__directLink_T       import *
from MT_pre__directLink_S       import *
from MT_pre__paired_with       import *
from MT_pre__trace_link       import *
from MT_pre__hasAttr_S       import *
from MT_pre__hasAttr_T       import *
from MT_pre__leftExpr       import *
from MT_pre__rightExpr       import *
from MT_pre__arg_1       import *
from MT_pre__arg_2       import *
from MT_pre__GenericEdge_FamiliesToPersonsMM       import *
def createNewASGroot(self):
   return ASG_MT_pre__FamiliesToPersonsMM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MT_pre__MetaModelElement_S", command=lambda x=self: x.createNewMT_pre__MetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__HouseholdRoot", command=lambda x=self: x.createNewMT_pre__HouseholdRoot(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Family", command=lambda x=self: x.createNewMT_pre__Family(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Member", command=lambda x=self: x.createNewMT_pre__Member(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__MatchModel", command=lambda x=self: x.createNewMT_pre__MatchModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__ApplyModel", command=lambda x=self: x.createNewMT_pre__ApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__MetaModelElement_T", command=lambda x=self: x.createNewMT_pre__MetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__CommunityRoot", command=lambda x=self: x.createNewMT_pre__CommunityRoot(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Person", command=lambda x=self: x.createNewMT_pre__Person(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Man", command=lambda x=self: x.createNewMT_pre__Man(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Attribute", command=lambda x=self: x.createNewMT_pre__Attribute(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Equation", command=lambda x=self: x.createNewMT_pre__Equation(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Expression", command=lambda x=self: x.createNewMT_pre__Expression(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Constant", command=lambda x=self: x.createNewMT_pre__Constant(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Concat", command=lambda x=self: x.createNewMT_pre__Concat(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__Woman", command=lambda x=self: x.createNewMT_pre__Woman(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__GenericNode_FamiliesToPersonsMM", command=lambda x=self: x.createNewMT_pre__GenericNode_FamiliesToPersonsMM(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__match_contains", command=lambda x=self: x.createNewMT_pre__match_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__apply_contains", command=lambda x=self: x.createNewMT_pre__apply_contains(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__backward_link", command=lambda x=self: x.createNewMT_pre__backward_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__indirectLink_S", command=lambda x=self: x.createNewMT_pre__indirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__directLink_T", command=lambda x=self: x.createNewMT_pre__directLink_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__directLink_S", command=lambda x=self: x.createNewMT_pre__directLink_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__paired_with", command=lambda x=self: x.createNewMT_pre__paired_with(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__trace_link", command=lambda x=self: x.createNewMT_pre__trace_link(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__hasAttr_S", command=lambda x=self: x.createNewMT_pre__hasAttr_S(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__hasAttr_T", command=lambda x=self: x.createNewMT_pre__hasAttr_T(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__leftExpr", command=lambda x=self: x.createNewMT_pre__leftExpr(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__rightExpr", command=lambda x=self: x.createNewMT_pre__rightExpr(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__arg_1", command=lambda x=self: x.createNewMT_pre__arg_1(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__arg_2", command=lambda x=self: x.createNewMT_pre__arg_2(x, 100, 100) )
    modelMenu.add_command(label="New MT_pre__GenericEdge_FamiliesToPersonsMM", command=lambda x=self: x.createNewMT_pre__GenericEdge_FamiliesToPersonsMM(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['MT_pre__arg_1']={
           'MT_pre__arg_1': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Man']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_T', self.createNewMT_pre__hasAttr_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__Person': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Woman': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__HouseholdRoot']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_S', self.createNewMT_pre__hasAttr_S)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)] }
    self.ConnectivityMap['MT_pre__apply_contains']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__backward_link']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__MatchModel']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': [( 'MT_pre__paired_with', self.createNewMT_pre__paired_with)]
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__match_contains', self.createNewMT_pre__match_contains)] }
    self.ConnectivityMap['MT_pre__match_contains']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Concat']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': [( 'MT_pre__arg_1', self.createNewMT_pre__arg_1), ( 'MT_pre__arg_2', self.createNewMT_pre__arg_2)]
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': [( 'MT_pre__arg_1', self.createNewMT_pre__arg_1), ( 'MT_pre__arg_2', self.createNewMT_pre__arg_2)]
          ,'MT_pre__Attribute': [( 'MT_pre__arg_1', self.createNewMT_pre__arg_1), ( 'MT_pre__arg_2', self.createNewMT_pre__arg_2)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': [( 'MT_pre__arg_1', self.createNewMT_pre__arg_1), ( 'MT_pre__arg_2', self.createNewMT_pre__arg_2)]
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__trace_link']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__ApplyModel']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__Woman': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__apply_contains', self.createNewMT_pre__apply_contains)]
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Constant']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Attribute']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__indirectLink_S']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__leftExpr']={
           'MT_pre__arg_1': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Expression']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__paired_with']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': [( 'MT_pre__ApplyModel', self.createNewMT_pre__ApplyModel)]
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__directLink_S']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__directLink_T']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__rightExpr']={
           'MT_pre__arg_1': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Member']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_S', self.createNewMT_pre__hasAttr_S)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)] }
    self.ConnectivityMap['MT_pre__MetaModelElement_T']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_T', self.createNewMT_pre__hasAttr_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__Person': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Woman': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__GenericEdge_FamiliesToPersonsMM']={
           'MT_pre__arg_1': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': [( 'MT_pre__ApplyModel', self.createNewMT_pre__ApplyModel)]
          ,'MT_pre__backward_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': [( 'MT_pre__MatchModel', self.createNewMT_pre__MatchModel)]
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': [( 'MT_pre__MatchModel', self.createNewMT_pre__MatchModel)]
          ,'MT_pre__directLink_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__directLink_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__hasAttr_S': [( 'MT_pre__MetaModelElement_S', self.createNewMT_pre__MetaModelElement_S), ( 'MT_pre__HouseholdRoot', self.createNewMT_pre__HouseholdRoot), ( 'MT_pre__Family', self.createNewMT_pre__Family), ( 'MT_pre__Member', self.createNewMT_pre__Member)]
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [( 'MT_pre__GenericNode_FamiliesToPersonsMM', self.createNewMT_pre__GenericNode_FamiliesToPersonsMM)]
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__hasAttr_T': [( 'MT_pre__MetaModelElement_T', self.createNewMT_pre__MetaModelElement_T), ( 'MT_pre__CommunityRoot', self.createNewMT_pre__CommunityRoot), ( 'MT_pre__Person', self.createNewMT_pre__Person), ( 'MT_pre__Man', self.createNewMT_pre__Man), ( 'MT_pre__Woman', self.createNewMT_pre__Woman)]
          ,'MT_pre__leftExpr': [( 'MT_pre__Equation', self.createNewMT_pre__Equation)]
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': [( 'MT_pre__Equation', self.createNewMT_pre__Equation)]
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__CommunityRoot']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_T', self.createNewMT_pre__hasAttr_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__Person': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Woman': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__Woman']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_T', self.createNewMT_pre__hasAttr_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__Person': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Woman': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__arg_2']={
           'MT_pre__arg_1': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': [( 'MT_pre__Concat', self.createNewMT_pre__Concat)]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__hasAttr_T']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__GenericNode_FamiliesToPersonsMM']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__Constant': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__Attribute': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__Expression': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__Person': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__Woman': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__GenericEdge_FamiliesToPersonsMM', self.createNewMT_pre__GenericEdge_FamiliesToPersonsMM)] }
    self.ConnectivityMap['MT_pre__Equation']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': [( 'MT_pre__leftExpr', self.createNewMT_pre__leftExpr), ( 'MT_pre__rightExpr', self.createNewMT_pre__rightExpr)]
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': [( 'MT_pre__leftExpr', self.createNewMT_pre__leftExpr), ( 'MT_pre__rightExpr', self.createNewMT_pre__rightExpr)]
          ,'MT_pre__Attribute': [( 'MT_pre__leftExpr', self.createNewMT_pre__leftExpr), ( 'MT_pre__rightExpr', self.createNewMT_pre__rightExpr)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': [( 'MT_pre__leftExpr', self.createNewMT_pre__leftExpr), ( 'MT_pre__rightExpr', self.createNewMT_pre__rightExpr)]
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__hasAttr_S']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': []
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [] }
    self.ConnectivityMap['MT_pre__Family']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_S', self.createNewMT_pre__hasAttr_S)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)] }
    self.ConnectivityMap['MT_pre__Person']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_T', self.createNewMT_pre__hasAttr_T)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__Person': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__Woman': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)]
          ,'MT_pre__MetaModelElement_T': [( 'MT_pre__directLink_T', self.createNewMT_pre__directLink_T)]
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__backward_link', self.createNewMT_pre__backward_link), ( 'MT_pre__trace_link', self.createNewMT_pre__trace_link)] }
    self.ConnectivityMap['MT_pre__MetaModelElement_S']={
           'MT_pre__arg_1': []
          ,'MT_pre__Man': []
          ,'MT_pre__HouseholdRoot': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__Concat': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Attribute': [( 'MT_pre__hasAttr_S', self.createNewMT_pre__hasAttr_S)]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__Expression': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__Member': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__Person': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Woman': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__Equation': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__Family': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__MetaModelElement_S': [( 'MT_pre__indirectLink_S', self.createNewMT_pre__indirectLink_S), ( 'MT_pre__directLink_S', self.createNewMT_pre__directLink_S)] }
    
    self.CardinalityTable['MT_pre__MetaModelElement_S']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__hasAttr_S': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__HouseholdRoot']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__hasAttr_S': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Family']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__hasAttr_S': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Member']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': [('0', 'N', 'Destination')]
          ,'MT_pre__indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Destination')]
          ,'MT_pre__hasAttr_S': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__MatchModel']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': [('0', 'N', 'Source')]
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': [('0', '1', 'Source')]
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__ApplyModel']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Source')]
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': [('0', '1', 'Destination')]
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__MetaModelElement_T']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': [('0', 'N', 'Source')]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__CommunityRoot']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': [('0', 'N', 'Source')]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Person']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': [('0', 'N', 'Source')]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Man']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': [('0', 'N', 'Source')]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Attribute']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': [('0', 'N', 'Destination')]
          ,'MT_pre__hasAttr_T': [('0', 'N', 'Destination')]
          ,'MT_pre__leftExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__rightExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_1': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_2': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Equation']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': [('0', 'N', 'Source')]
          ,'MT_pre__rightExpr': [('0', 'N', 'Source')]
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Expression']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__rightExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_1': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_2': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Constant']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__rightExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_1': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_2': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Concat']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__rightExpr': [('0', 'N', 'Destination')]
          ,'MT_pre__arg_1': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'MT_pre__arg_2': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__Woman']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': [('0', 'N', 'Destination')]
          ,'MT_pre__backward_link': [('0', 'N', 'Source')]
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': [('0', 'N', 'Source')]
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': [('0', 'N', 'Source')]
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__GenericNode_FamiliesToPersonsMM']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [('0', 'N', 'Source'), ('0', 'N', 'Destination')] }
    self.CardinalityTable['MT_pre__match_contains']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Source')]
          ,'MT_pre__Family': [('0', 'N', 'Source')]
          ,'MT_pre__Member': [('0', 'N', 'Source')]
          ,'MT_pre__MatchModel': [('0', 'N', 'Destination')]
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__apply_contains']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': [('0', 'N', 'Destination')]
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_pre__CommunityRoot': [('0', 'N', 'Source')]
          ,'MT_pre__Person': [('0', 'N', 'Source')]
          ,'MT_pre__Man': [('0', 'N', 'Source')]
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': [('0', 'N', 'Source')]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__backward_link']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Source')]
          ,'MT_pre__Family': [('0', 'N', 'Source')]
          ,'MT_pre__Member': [('0', 'N', 'Source')]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_pre__CommunityRoot': [('0', 'N', 'Destination')]
          ,'MT_pre__Person': [('0', 'N', 'Destination')]
          ,'MT_pre__Man': [('0', 'N', 'Destination')]
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__indirectLink_S']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Family': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Member': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__directLink_T']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__CommunityRoot': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Person': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Man': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__directLink_S']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Family': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Member': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__paired_with']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': [('0', '1', 'Destination')]
          ,'MT_pre__ApplyModel': [('0', '1', 'Source')]
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__trace_link']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Source')]
          ,'MT_pre__Family': [('0', 'N', 'Source')]
          ,'MT_pre__Member': [('0', 'N', 'Source')]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_pre__CommunityRoot': [('0', 'N', 'Destination')]
          ,'MT_pre__Person': [('0', 'N', 'Destination')]
          ,'MT_pre__Man': [('0', 'N', 'Destination')]
          ,'MT_pre__Attribute': []
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__hasAttr_S']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Destination')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Destination')]
          ,'MT_pre__Family': [('0', 'N', 'Destination')]
          ,'MT_pre__Member': [('0', 'N', 'Destination')]
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': [('0', 'N', 'Source')]
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__hasAttr_T']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'MT_pre__CommunityRoot': [('0', 'N', 'Destination')]
          ,'MT_pre__Person': [('0', 'N', 'Destination')]
          ,'MT_pre__Man': [('0', 'N', 'Destination')]
          ,'MT_pre__Attribute': [('0', 'N', 'Source')]
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': []
          ,'MT_pre__Constant': []
          ,'MT_pre__Concat': []
          ,'MT_pre__Woman': [('0', 'N', 'Destination')]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__leftExpr']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': [('0', 'N', 'Source')]
          ,'MT_pre__Equation': [('0', 'N', 'Destination')]
          ,'MT_pre__Expression': [('0', 'N', 'Source')]
          ,'MT_pre__Constant': [('0', 'N', 'Source')]
          ,'MT_pre__Concat': [('0', 'N', 'Source')]
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__rightExpr']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': [('0', 'N', 'Source')]
          ,'MT_pre__Equation': [('0', 'N', 'Destination')]
          ,'MT_pre__Expression': [('0', 'N', 'Source')]
          ,'MT_pre__Constant': [('0', 'N', 'Source')]
          ,'MT_pre__Concat': [('0', 'N', 'Source')]
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__arg_1']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': [('0', 'N', 'Source')]
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': [('0', 'N', 'Source')]
          ,'MT_pre__Constant': [('0', 'N', 'Source')]
          ,'MT_pre__Concat': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__arg_2']={
          'MT_pre__MetaModelElement_S': []
          ,'MT_pre__HouseholdRoot': []
          ,'MT_pre__Family': []
          ,'MT_pre__Member': []
          ,'MT_pre__MatchModel': []
          ,'MT_pre__ApplyModel': []
          ,'MT_pre__MetaModelElement_T': []
          ,'MT_pre__CommunityRoot': []
          ,'MT_pre__Person': []
          ,'MT_pre__Man': []
          ,'MT_pre__Attribute': [('0', 'N', 'Source')]
          ,'MT_pre__Equation': []
          ,'MT_pre__Expression': [('0', 'N', 'Source')]
          ,'MT_pre__Constant': [('0', 'N', 'Source')]
          ,'MT_pre__Concat': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MT_pre__Woman': []
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': []
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    self.CardinalityTable['MT_pre__GenericEdge_FamiliesToPersonsMM']={
          'MT_pre__MetaModelElement_S': [('0', 'N', 'Source')]
          ,'MT_pre__HouseholdRoot': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Family': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Member': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__MatchModel': [('0', 'N', 'Source')]
          ,'MT_pre__ApplyModel': [('0', 'N', 'Source')]
          ,'MT_pre__MetaModelElement_T': [('0', 'N', 'Source')]
          ,'MT_pre__CommunityRoot': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Person': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Man': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Attribute': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Equation': [('0', 'N', 'Source')]
          ,'MT_pre__Expression': [('0', 'N', 'Source')]
          ,'MT_pre__Constant': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Concat': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__Woman': [('0', 'N', 'Source'), ('0', 'N', 'Source')]
          ,'MT_pre__GenericNode_FamiliesToPersonsMM': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'MT_pre__match_contains': []
          ,'MT_pre__apply_contains': []
          ,'MT_pre__backward_link': []
          ,'MT_pre__indirectLink_S': []
          ,'MT_pre__directLink_T': []
          ,'MT_pre__directLink_S': []
          ,'MT_pre__paired_with': []
          ,'MT_pre__trace_link': []
          ,'MT_pre__hasAttr_S': []
          ,'MT_pre__hasAttr_T': []
          ,'MT_pre__leftExpr': []
          ,'MT_pre__rightExpr': []
          ,'MT_pre__arg_1': []
          ,'MT_pre__arg_2': []
          ,'MT_pre__GenericEdge_FamiliesToPersonsMM': [] }
    
    self.entitiesInMetaModel['MT_pre__FamiliesToPersonsMM']=["MT_pre__MetaModelElement_S", "MT_pre__HouseholdRoot", "MT_pre__Family", "MT_pre__Member", "MT_pre__MatchModel", "MT_pre__ApplyModel", "MT_pre__MetaModelElement_T", "MT_pre__CommunityRoot", "MT_pre__Person", "MT_pre__Man", "MT_pre__Attribute", "MT_pre__Equation", "MT_pre__Expression", "MT_pre__Constant", "MT_pre__Concat", "MT_pre__Woman", "MT_pre__GenericNode_FamiliesToPersonsMM", "MT_pre__match_contains", "MT_pre__apply_contains", "MT_pre__backward_link", "MT_pre__indirectLink_S", "MT_pre__directLink_T", "MT_pre__directLink_S", "MT_pre__paired_with", "MT_pre__trace_link", "MT_pre__hasAttr_S", "MT_pre__hasAttr_T", "MT_pre__leftExpr", "MT_pre__rightExpr", "MT_pre__arg_1", "MT_pre__arg_2", "MT_pre__GenericEdge_FamiliesToPersonsMM"]

    
def createNewMT_pre__MetaModelElement_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__MetaModelElement_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__MetaModelElement_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__MetaModelElement_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__MetaModelElement_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_S", new_obj.tag)
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
def createNewMT_pre__HouseholdRoot(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__HouseholdRoot(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__HouseholdRoot"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__HouseholdRoot(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__HouseholdRoot(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__HouseholdRoot", new_obj.tag)
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
def createNewMT_pre__Family(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Family(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Family"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Family(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Family(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Family", new_obj.tag)
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
def createNewMT_pre__Member(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Member(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Member"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Member(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Member(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Member", new_obj.tag)
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
def createNewMT_pre__MatchModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__MatchModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__MatchModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__MatchModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__MatchModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__MatchModel", new_obj.tag)
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
def createNewMT_pre__ApplyModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__ApplyModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__ApplyModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__ApplyModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__ApplyModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__ApplyModel", new_obj.tag)
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
def createNewMT_pre__MetaModelElement_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__MetaModelElement_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__MetaModelElement_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__MetaModelElement_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__MetaModelElement_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__MetaModelElement_T", new_obj.tag)
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
def createNewMT_pre__CommunityRoot(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__CommunityRoot(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__CommunityRoot"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__CommunityRoot(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__CommunityRoot(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__CommunityRoot", new_obj.tag)
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
def createNewMT_pre__Person(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Person(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Person"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Person(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Person(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Person", new_obj.tag)
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
def createNewMT_pre__Man(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Man(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Man"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Man(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Man(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Man", new_obj.tag)
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
def createNewMT_pre__Attribute(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Attribute(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Attribute"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Attribute(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Attribute(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Attribute", new_obj.tag)
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
def createNewMT_pre__Equation(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Equation(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Equation"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Equation(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Equation(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Equation", new_obj.tag)
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
def createNewMT_pre__Expression(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Expression(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Expression"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Expression(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Expression(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Expression", new_obj.tag)
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
def createNewMT_pre__Constant(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Constant(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Constant"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Constant(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Constant(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Constant", new_obj.tag)
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
def createNewMT_pre__Concat(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Concat(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Concat"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Concat(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Concat(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Concat", new_obj.tag)
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
def createNewMT_pre__Woman(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__Woman(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__Woman"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__Woman(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__Woman(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__Woman", new_obj.tag)
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
def createNewMT_pre__GenericNode_FamiliesToPersonsMM(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__GenericNode_FamiliesToPersonsMM(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__GenericNode_FamiliesToPersonsMM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__GenericNode_FamiliesToPersonsMM(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__GenericNode_FamiliesToPersonsMM(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__GenericNode_FamiliesToPersonsMM", new_obj.tag)
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
def createNewMT_pre__match_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__match_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__match_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__match_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__match_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__match_contains", new_obj.tag)
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
def createNewMT_pre__apply_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__apply_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__apply_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__apply_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__apply_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__apply_contains", new_obj.tag)
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
def createNewMT_pre__backward_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__backward_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__backward_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__backward_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__backward_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__backward_link", new_obj.tag)
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
def createNewMT_pre__indirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__indirectLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__indirectLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__indirectLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__indirectLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__indirectLink_S", new_obj.tag)
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
def createNewMT_pre__directLink_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__directLink_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__directLink_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__directLink_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__directLink_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__directLink_T", new_obj.tag)
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
def createNewMT_pre__directLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__directLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__directLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__directLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__directLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__directLink_S", new_obj.tag)
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
def createNewMT_pre__paired_with(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__paired_with(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__paired_with"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__paired_with(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__paired_with(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__paired_with", new_obj.tag)
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
def createNewMT_pre__trace_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__trace_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__trace_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__trace_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__trace_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__trace_link", new_obj.tag)
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
def createNewMT_pre__hasAttr_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__hasAttr_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__hasAttr_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__hasAttr_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__hasAttr_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__hasAttr_S", new_obj.tag)
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
def createNewMT_pre__hasAttr_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__hasAttr_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__hasAttr_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__hasAttr_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__hasAttr_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__hasAttr_T", new_obj.tag)
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
def createNewMT_pre__leftExpr(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__leftExpr(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__leftExpr"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__leftExpr(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__leftExpr(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__leftExpr", new_obj.tag)
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
def createNewMT_pre__rightExpr(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__rightExpr(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__rightExpr"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__rightExpr(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__rightExpr(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__rightExpr", new_obj.tag)
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
def createNewMT_pre__arg_1(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__arg_1(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__arg_1"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__arg_1(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__arg_1(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__arg_1", new_obj.tag)
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
def createNewMT_pre__arg_2(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__arg_2(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__arg_2"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__arg_2(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__arg_2(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__arg_2", new_obj.tag)
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
def createNewMT_pre__GenericEdge_FamiliesToPersonsMM(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MT_pre__GenericEdge_FamiliesToPersonsMM(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MT_pre__GenericEdge_FamiliesToPersonsMM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MT_pre__GenericEdge_FamiliesToPersonsMM(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MT_pre__GenericEdge_FamiliesToPersonsMM(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MT_pre__GenericEdge_FamiliesToPersonsMM", new_obj.tag)
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
   new_semantic_obj = ASG_MT_pre__FamiliesToPersonsMM(self)
   ne = len(self.ASGroot.listNodes["ASG_MT_pre__FamiliesToPersonsMM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_MT_pre__FamiliesToPersonsMM", new_obj.tag)
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

