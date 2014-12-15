"""
__PoliceStationMM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Dec 12 15:16:06 2014
_____________________________________________________________________________
"""
from ASG_PoliceStationMM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MetaModelElement_S       import *
from Station_S       import *
from Male_S       import *
from Female_S       import *
from MatchModel       import *
from ApplyModel       import *
from MetaModelElement_T       import *
from Station_T       import *
from Male_T       import *
from Female_T       import *
from Attribute       import *
from Equation       import *
from Expression       import *
from Constant       import *
from Concat       import *
from match_contains       import *
from apply_contains       import *
from backward_link       import *
from indirectLink_S       import *
from directLink_T       import *
from directLink_S       import *
from paired_with       import *
from trace_link       import *
from hasAttr_S       import *
from hasAttr_T       import *
from leftExpr       import *
from rightExpr       import *
from arg_1       import *
from arg_2       import *
def createNewASGroot(self):
   return ASG_PoliceStationMM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MetaModelElement_S", command=lambda x=self: x.createNewMetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New Station_S", command=lambda x=self: x.createNewStation_S(x, 100, 100) )
    modelMenu.add_command(label="New Male_S", command=lambda x=self: x.createNewMale_S(x, 100, 100) )
    modelMenu.add_command(label="New Female_S", command=lambda x=self: x.createNewFemale_S(x, 100, 100) )
    modelMenu.add_command(label="New MatchModel", command=lambda x=self: x.createNewMatchModel(x, 100, 100) )
    modelMenu.add_command(label="New ApplyModel", command=lambda x=self: x.createNewApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MetaModelElement_T", command=lambda x=self: x.createNewMetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New Station_T", command=lambda x=self: x.createNewStation_T(x, 100, 100) )
    modelMenu.add_command(label="New Male_T", command=lambda x=self: x.createNewMale_T(x, 100, 100) )
    modelMenu.add_command(label="New Female_T", command=lambda x=self: x.createNewFemale_T(x, 100, 100) )
    modelMenu.add_command(label="New Attribute", command=lambda x=self: x.createNewAttribute(x, 100, 100) )
    modelMenu.add_command(label="New Equation", command=lambda x=self: x.createNewEquation(x, 100, 100) )
    modelMenu.add_command(label="New Expression", command=lambda x=self: x.createNewExpression(x, 100, 100) )
    modelMenu.add_command(label="New Constant", command=lambda x=self: x.createNewConstant(x, 100, 100) )
    modelMenu.add_command(label="New Concat", command=lambda x=self: x.createNewConcat(x, 100, 100) )
    modelMenu.add_command(label="New match_contains", command=lambda x=self: x.createNewmatch_contains(x, 100, 100) )
    modelMenu.add_command(label="New apply_contains", command=lambda x=self: x.createNewapply_contains(x, 100, 100) )
    modelMenu.add_command(label="New backward_link", command=lambda x=self: x.createNewbackward_link(x, 100, 100) )
    modelMenu.add_command(label="New indirectLink_S", command=lambda x=self: x.createNewindirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New directLink_T", command=lambda x=self: x.createNewdirectLink_T(x, 100, 100) )
    modelMenu.add_command(label="New directLink_S", command=lambda x=self: x.createNewdirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New paired_with", command=lambda x=self: x.createNewpaired_with(x, 100, 100) )
    modelMenu.add_command(label="New trace_link", command=lambda x=self: x.createNewtrace_link(x, 100, 100) )
    modelMenu.add_command(label="New hasAttr_S", command=lambda x=self: x.createNewhasAttr_S(x, 100, 100) )
    modelMenu.add_command(label="New hasAttr_T", command=lambda x=self: x.createNewhasAttr_T(x, 100, 100) )
    modelMenu.add_command(label="New leftExpr", command=lambda x=self: x.createNewleftExpr(x, 100, 100) )
    modelMenu.add_command(label="New rightExpr", command=lambda x=self: x.createNewrightExpr(x, 100, 100) )
    modelMenu.add_command(label="New arg_1", command=lambda x=self: x.createNewarg_1(x, 100, 100) )
    modelMenu.add_command(label="New arg_2", command=lambda x=self: x.createNewarg_2(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['directLink_S']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'apply_contains': []
          ,'hasAttr_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'hasAttr_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['apply_contains']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'indirectLink_S': []
          ,'backward_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'directLink_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'paired_with': [] }
    self.ConnectivityMap['directLink_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'indirectLink_S': []
          ,'backward_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'directLink_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'Station_T', self.createNewStation_T), ( 'Male_T', self.createNewMale_T), ( 'Female_T', self.createNewFemale_T)]
          ,'paired_with': [] }
    self.ConnectivityMap['hasAttr_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['leftExpr']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['paired_with']={
           'directLink_S': []
          ,'apply_contains': [( 'ApplyModel', self.createNewApplyModel)]
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['backward_link']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'apply_contains': []
          ,'hasAttr_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'hasAttr_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['hasAttr_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Female_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'leftExpr': []
          ,'Female_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Station_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Station_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Concat': []
          ,'Female_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_T', self.createNewhasAttr_T)]
          ,'Male_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['indirectLink_S']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'apply_contains': []
          ,'hasAttr_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'hasAttr_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['MetaModelElement_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'leftExpr': []
          ,'Female_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Station_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Station_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Concat': []
          ,'Female_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_T', self.createNewhasAttr_T)]
          ,'Male_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Station_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Concat': []
          ,'Female_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_S', self.createNewhasAttr_S)]
          ,'Male_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Station_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'leftExpr': []
          ,'Female_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Station_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Station_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Concat': []
          ,'Female_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_T', self.createNewhasAttr_T)]
          ,'Male_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['ApplyModel']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': [( 'apply_contains', self.createNewapply_contains)]
          ,'leftExpr': []
          ,'Female_T': [( 'apply_contains', self.createNewapply_contains)]
          ,'Station_S': []
          ,'Station_T': [( 'apply_contains', self.createNewapply_contains)]
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': [( 'apply_contains', self.createNewapply_contains)]
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['MetaModelElement_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Concat': []
          ,'Female_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_S', self.createNewhasAttr_S)]
          ,'Male_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Concat']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': [( 'arg_1', self.createNewarg_1), ( 'arg_2', self.createNewarg_2)]
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': [( 'arg_1', self.createNewarg_1), ( 'arg_2', self.createNewarg_2)]
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'arg_1', self.createNewarg_1), ( 'arg_2', self.createNewarg_2)]
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Female_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Concat': []
          ,'Female_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_S', self.createNewhasAttr_S)]
          ,'Male_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Equation']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': [( 'leftExpr', self.createNewleftExpr), ( 'rightExpr', self.createNewrightExpr)]
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': [( 'leftExpr', self.createNewleftExpr), ( 'rightExpr', self.createNewrightExpr)]
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'leftExpr', self.createNewleftExpr), ( 'rightExpr', self.createNewrightExpr)]
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['match_contains']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'apply_contains': []
          ,'hasAttr_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'hasAttr_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Male_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'leftExpr': []
          ,'Female_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Station_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Station_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Concat': []
          ,'Female_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_T', self.createNewhasAttr_T)]
          ,'Male_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Expression']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['arg_1']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['arg_2']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Constant']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['rightExpr']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['MatchModel']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': [( 'match_contains', self.createNewmatch_contains)]
          ,'Station_T': []
          ,'ApplyModel': [( 'paired_with', self.createNewpaired_with)]
          ,'MetaModelElement_S': [( 'match_contains', self.createNewmatch_contains)]
          ,'Concat': []
          ,'Female_S': [( 'match_contains', self.createNewmatch_contains)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': [( 'match_contains', self.createNewmatch_contains)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Attribute']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['Male_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'indirectLink_S': []
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Concat': []
          ,'Female_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': [( 'hasAttr_S', self.createNewhasAttr_S)]
          ,'Male_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'trace_link': []
          ,'paired_with': [] }
    self.ConnectivityMap['trace_link']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'apply_contains': []
          ,'hasAttr_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'hasAttr_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'Station_S', self.createNewStation_S), ( 'Male_S', self.createNewMale_S), ( 'Female_S', self.createNewFemale_S)]
          ,'backward_link': []
          ,'directLink_T': []
          ,'MetaModelElement_T': []
          ,'leftExpr': []
          ,'Female_T': []
          ,'Station_S': []
          ,'Station_T': []
          ,'ApplyModel': []
          ,'MetaModelElement_S': []
          ,'Concat': []
          ,'Female_S': []
          ,'Equation': []
          ,'match_contains': []
          ,'Male_T': []
          ,'Expression': []
          ,'arg_1': []
          ,'arg_2': []
          ,'Constant': []
          ,'rightExpr': []
          ,'MatchModel': []
          ,'Attribute': []
          ,'Male_S': []
          ,'trace_link': []
          ,'paired_with': [] }
    
    self.CardinalityTable['MetaModelElement_S']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')]
          ,'hasAttr_S': [('0', 'N', 'Source')]
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Station_S']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')]
          ,'hasAttr_S': [('0', 'N', 'Source')]
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Male_S']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')]
          ,'hasAttr_S': [('0', 'N', 'Source')]
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Female_S']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')]
          ,'hasAttr_S': [('0', 'N', 'Source')]
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['MatchModel']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': [('0', 'N', 'Source')]
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': [('1', '1', 'Source')]
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['ApplyModel']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Source')]
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': [('1', '1', 'Destination')]
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['MetaModelElement_T']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')]
          ,'hasAttr_S': []
          ,'hasAttr_T': [('0', 'N', 'Source')]
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Station_T']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')]
          ,'hasAttr_S': []
          ,'hasAttr_T': [('0', 'N', 'Source')]
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Male_T']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')]
          ,'hasAttr_S': []
          ,'hasAttr_T': [('0', 'N', 'Source')]
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Female_T']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')]
          ,'hasAttr_S': []
          ,'hasAttr_T': [('0', 'N', 'Source')]
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Attribute']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': [('0', 'N', 'Destination')]
          ,'hasAttr_T': [('0', 'N', 'Destination')]
          ,'leftExpr': [('0', 'N', 'Destination')]
          ,'rightExpr': [('0', 'N', 'Destination')]
          ,'arg_1': [('0', 'N', 'Destination')]
          ,'arg_2': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Equation']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': [('0', 'N', 'Source')]
          ,'rightExpr': [('0', 'N', 'Source')]
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['Expression']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': [('0', 'N', 'Destination')]
          ,'rightExpr': [('0', 'N', 'Destination')]
          ,'arg_1': [('0', 'N', 'Destination')]
          ,'arg_2': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Constant']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': [('0', 'N', 'Destination')]
          ,'rightExpr': [('0', 'N', 'Destination')]
          ,'arg_1': [('0', 'N', 'Destination')]
          ,'arg_2': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Concat']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': [('0', 'N', 'Source')]
          ,'arg_2': [('0', 'N', 'Source')] }
    self.CardinalityTable['match_contains']={
          'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'Station_S': [('0', 'N', 'Source')]
          ,'Male_S': [('0', 'N', 'Source')]
          ,'Female_S': [('0', 'N', 'Source')]
          ,'MatchModel': [('0', 'N', 'Destination')]
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['apply_contains']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': [('0', 'N', 'Destination')]
          ,'MetaModelElement_T': [('0', 'N', 'Source')]
          ,'Station_T': [('0', 'N', 'Source')]
          ,'Male_T': [('0', 'N', 'Source')]
          ,'Female_T': [('0', 'N', 'Source')]
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['backward_link']={
          'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'Station_S': [('0', 'N', 'Source')]
          ,'Male_S': [('0', 'N', 'Source')]
          ,'Female_S': [('0', 'N', 'Source')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'Station_T': [('0', 'N', 'Destination')]
          ,'Male_T': [('0', 'N', 'Destination')]
          ,'Female_T': [('0', 'N', 'Destination')]
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['indirectLink_S']={
          'MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Station_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Male_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Female_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['directLink_T']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Station_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Male_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Female_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['directLink_S']={
          'MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Station_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Male_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Female_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['paired_with']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': [('1', '1', 'Destination')]
          ,'ApplyModel': [('1', '1', 'Source')]
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['trace_link']={
          'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'Station_S': [('0', 'N', 'Source')]
          ,'Male_S': [('0', 'N', 'Source')]
          ,'Female_S': [('0', 'N', 'Source')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'Station_T': [('0', 'N', 'Destination')]
          ,'Male_T': [('0', 'N', 'Destination')]
          ,'Female_T': [('0', 'N', 'Destination')]
          ,'Attribute': []
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['hasAttr_S']={
          'MetaModelElement_S': [('0', 'N', 'Destination')]
          ,'Station_S': [('0', 'N', 'Destination')]
          ,'Male_S': [('0', 'N', 'Destination')]
          ,'Female_S': [('0', 'N', 'Destination')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': [('0', 'N', 'Source')]
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['hasAttr_T']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'Station_T': [('0', 'N', 'Destination')]
          ,'Male_T': [('0', 'N', 'Destination')]
          ,'Female_T': [('0', 'N', 'Destination')]
          ,'Attribute': [('0', 'N', 'Source')]
          ,'Equation': []
          ,'Expression': []
          ,'Constant': []
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['leftExpr']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': [('0', 'N', 'Source')]
          ,'Equation': [('0', 'N', 'Destination')]
          ,'Expression': [('0', 'N', 'Source')]
          ,'Constant': [('0', 'N', 'Source')]
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['rightExpr']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': [('0', 'N', 'Source')]
          ,'Equation': [('0', 'N', 'Destination')]
          ,'Expression': [('0', 'N', 'Source')]
          ,'Constant': [('0', 'N', 'Source')]
          ,'Concat': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['arg_1']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': [('0', 'N', 'Source')]
          ,'Equation': []
          ,'Expression': [('0', 'N', 'Source')]
          ,'Constant': [('0', 'N', 'Source')]
          ,'Concat': [('0', 'N', 'Destination')]
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    self.CardinalityTable['arg_2']={
          'MetaModelElement_S': []
          ,'Station_S': []
          ,'Male_S': []
          ,'Female_S': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'Station_T': []
          ,'Male_T': []
          ,'Female_T': []
          ,'Attribute': [('0', 'N', 'Source')]
          ,'Equation': []
          ,'Expression': [('0', 'N', 'Source')]
          ,'Constant': [('0', 'N', 'Source')]
          ,'Concat': [('0', 'N', 'Destination')]
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': []
          ,'hasAttr_S': []
          ,'hasAttr_T': []
          ,'leftExpr': []
          ,'rightExpr': []
          ,'arg_1': []
          ,'arg_2': [] }
    
    self.entitiesInMetaModel['PoliceStationMM']=["MetaModelElement_S", "Station_S", "Male_S", "Female_S", "MatchModel", "ApplyModel", "MetaModelElement_T", "Station_T", "Male_T", "Female_T", "Attribute", "Equation", "Expression", "Constant", "Concat", "match_contains", "apply_contains", "backward_link", "indirectLink_S", "directLink_T", "directLink_S", "paired_with", "trace_link", "hasAttr_S", "hasAttr_T", "leftExpr", "rightExpr", "arg_1", "arg_2"]

    
def createNewMetaModelElement_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MetaModelElement_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MetaModelElement_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MetaModelElement_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MetaModelElement_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MetaModelElement_S", new_obj.tag)
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
def createNewStation_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Station_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Station_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Station_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Station_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Station_S", new_obj.tag)
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
def createNewMale_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Male_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Male_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Male_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Male_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Male_S", new_obj.tag)
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
def createNewFemale_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Female_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Female_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Female_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Female_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Female_S", new_obj.tag)
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
def createNewMatchModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MatchModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MatchModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MatchModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MatchModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MatchModel", new_obj.tag)
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
def createNewApplyModel(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = ApplyModel(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["ApplyModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ApplyModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ApplyModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ApplyModel", new_obj.tag)
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
def createNewMetaModelElement_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = MetaModelElement_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["MetaModelElement_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_MetaModelElement_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_MetaModelElement_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("MetaModelElement_T", new_obj.tag)
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
def createNewStation_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Station_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Station_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Station_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Station_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Station_T", new_obj.tag)
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
def createNewMale_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Male_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Male_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Male_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Male_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Male_T", new_obj.tag)
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
def createNewFemale_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Female_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Female_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Female_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Female_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Female_T", new_obj.tag)
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
def createNewAttribute(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Attribute(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Attribute"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Attribute(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Attribute(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Attribute", new_obj.tag)
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
def createNewEquation(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Equation(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Equation"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Equation(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Equation(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Equation", new_obj.tag)
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
def createNewExpression(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Expression(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Expression"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Expression(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Expression(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Expression", new_obj.tag)
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
def createNewConstant(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Constant(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Constant"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Constant(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Constant(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Constant", new_obj.tag)
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
def createNewConcat(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Concat(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Concat"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Concat(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Concat(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Concat", new_obj.tag)
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
def createNewmatch_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = match_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["match_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_match_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_match_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("match_contains", new_obj.tag)
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
def createNewapply_contains(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = apply_contains(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["apply_contains"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_apply_contains(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_apply_contains(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("apply_contains", new_obj.tag)
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
def createNewbackward_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = backward_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["backward_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_backward_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_backward_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("backward_link", new_obj.tag)
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
def createNewindirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = indirectLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["indirectLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_indirectLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_indirectLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("indirectLink_S", new_obj.tag)
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
def createNewdirectLink_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = directLink_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["directLink_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_directLink_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_directLink_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("directLink_T", new_obj.tag)
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
def createNewdirectLink_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = directLink_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["directLink_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_directLink_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_directLink_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("directLink_S", new_obj.tag)
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
def createNewpaired_with(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = paired_with(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["paired_with"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_paired_with(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_paired_with(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("paired_with", new_obj.tag)
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
def createNewtrace_link(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = trace_link(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["trace_link"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_trace_link(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_trace_link(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("trace_link", new_obj.tag)
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
def createNewhasAttr_S(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = hasAttr_S(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["hasAttr_S"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_hasAttr_S(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_hasAttr_S(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("hasAttr_S", new_obj.tag)
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
def createNewhasAttr_T(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = hasAttr_T(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["hasAttr_T"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_hasAttr_T(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_hasAttr_T(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("hasAttr_T", new_obj.tag)
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
def createNewleftExpr(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = leftExpr(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["leftExpr"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_leftExpr(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_leftExpr(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("leftExpr", new_obj.tag)
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
def createNewrightExpr(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = rightExpr(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["rightExpr"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_rightExpr(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_rightExpr(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("rightExpr", new_obj.tag)
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
def createNewarg_1(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = arg_1(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["arg_1"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_arg_1(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_arg_1(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("arg_1", new_obj.tag)
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
def createNewarg_2(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = arg_2(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["arg_2"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_arg_2(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_arg_2(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("arg_2", new_obj.tag)
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
   new_semantic_obj = ASG_PoliceStationMM(self)
   ne = len(self.ASGroot.listNodes["ASG_PoliceStationMM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_PoliceStationMM", new_obj.tag)
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

