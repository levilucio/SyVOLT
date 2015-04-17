"""
__FamiliesToPersonsMM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: levi
Modified: Fri Apr 17 11:06:50 2015
_________________________________________________________________________________
"""
from ASG_FamiliesToPersonsMM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from MetaModelElement_S       import *
from HouseholdRoot       import *
from Family       import *
from Member       import *
from MatchModel       import *
from ApplyModel       import *
from MetaModelElement_T       import *
from CommunityRoot       import *
from Person       import *
from Man       import *
from Woman       import *
from match_contains       import *
from apply_contains       import *
from backward_link       import *
from indirectLink_S       import *
from directLink_T       import *
from directLink_S       import *
from paired_with       import *
from trace_link       import *
def createNewASGroot(self):
   return ASG_FamiliesToPersonsMM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New MetaModelElement_S", command=lambda x=self: x.createNewMetaModelElement_S(x, 100, 100) )
    modelMenu.add_command(label="New HouseholdRoot", command=lambda x=self: x.createNewHouseholdRoot(x, 100, 100) )
    modelMenu.add_command(label="New Family", command=lambda x=self: x.createNewFamily(x, 100, 100) )
    modelMenu.add_command(label="New Member", command=lambda x=self: x.createNewMember(x, 100, 100) )
    modelMenu.add_command(label="New MatchModel", command=lambda x=self: x.createNewMatchModel(x, 100, 100) )
    modelMenu.add_command(label="New ApplyModel", command=lambda x=self: x.createNewApplyModel(x, 100, 100) )
    modelMenu.add_command(label="New MetaModelElement_T", command=lambda x=self: x.createNewMetaModelElement_T(x, 100, 100) )
    modelMenu.add_command(label="New CommunityRoot", command=lambda x=self: x.createNewCommunityRoot(x, 100, 100) )
    modelMenu.add_command(label="New Person", command=lambda x=self: x.createNewPerson(x, 100, 100) )
    modelMenu.add_command(label="New Man", command=lambda x=self: x.createNewMan(x, 100, 100) )
    modelMenu.add_command(label="New Woman", command=lambda x=self: x.createNewWoman(x, 100, 100) )
    modelMenu.add_command(label="New match_contains", command=lambda x=self: x.createNewmatch_contains(x, 100, 100) )
    modelMenu.add_command(label="New apply_contains", command=lambda x=self: x.createNewapply_contains(x, 100, 100) )
    modelMenu.add_command(label="New backward_link", command=lambda x=self: x.createNewbackward_link(x, 100, 100) )
    modelMenu.add_command(label="New indirectLink_S", command=lambda x=self: x.createNewindirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New directLink_T", command=lambda x=self: x.createNewdirectLink_T(x, 100, 100) )
    modelMenu.add_command(label="New directLink_S", command=lambda x=self: x.createNewdirectLink_S(x, 100, 100) )
    modelMenu.add_command(label="New paired_with", command=lambda x=self: x.createNewpaired_with(x, 100, 100) )
    modelMenu.add_command(label="New trace_link", command=lambda x=self: x.createNewtrace_link(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['directLink_S']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['apply_contains']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'CommunityRoot', self.createNewCommunityRoot), ( 'Person', self.createNewPerson), ( 'Man', self.createNewMan), ( 'Woman', self.createNewWoman)]
          ,'indirectLink_S': []
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'CommunityRoot', self.createNewCommunityRoot), ( 'Person', self.createNewPerson), ( 'Man', self.createNewMan), ( 'Woman', self.createNewWoman)]
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'CommunityRoot', self.createNewCommunityRoot), ( 'Person', self.createNewPerson), ( 'Man', self.createNewMan), ( 'Woman', self.createNewWoman)]
          ,'Man': [] }
    self.ConnectivityMap['Woman']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'HouseholdRoot': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Family': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Person': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ApplyModel': []
          ,'CommunityRoot': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'Man': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['paired_with']={
           'directLink_S': []
          ,'apply_contains': [( 'ApplyModel', self.createNewApplyModel)]
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['HouseholdRoot']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Family': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['Family']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Family': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['MetaModelElement_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'HouseholdRoot': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Family': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Person': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ApplyModel': []
          ,'CommunityRoot': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'Man': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['MatchModel']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': [( 'match_contains', self.createNewmatch_contains)]
          ,'Family': [( 'match_contains', self.createNewmatch_contains)]
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'match_contains', self.createNewmatch_contains)]
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'match_contains', self.createNewmatch_contains)]
          ,'ApplyModel': [( 'paired_with', self.createNewpaired_with)]
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['directLink_T']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'CommunityRoot', self.createNewCommunityRoot), ( 'Person', self.createNewPerson), ( 'Man', self.createNewMan), ( 'Woman', self.createNewWoman)]
          ,'indirectLink_S': []
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'CommunityRoot', self.createNewCommunityRoot), ( 'Person', self.createNewPerson), ( 'Man', self.createNewMan), ( 'Woman', self.createNewWoman)]
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': [( 'MetaModelElement_T', self.createNewMetaModelElement_T), ( 'CommunityRoot', self.createNewCommunityRoot), ( 'Person', self.createNewPerson), ( 'Man', self.createNewMan), ( 'Woman', self.createNewWoman)]
          ,'Man': [] }
    self.ConnectivityMap['Person']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'HouseholdRoot': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Family': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Person': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ApplyModel': []
          ,'CommunityRoot': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'Man': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['Member']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Family': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['ApplyModel']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': [( 'apply_contains', self.createNewapply_contains)]
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': [( 'apply_contains', self.createNewapply_contains)]
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': []
          ,'MetaModelElement_T': [( 'apply_contains', self.createNewapply_contains)]
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': [( 'apply_contains', self.createNewapply_contains)]
          ,'backward_link': []
          ,'Man': [( 'apply_contains', self.createNewapply_contains)] }
    self.ConnectivityMap['match_contains']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['trace_link']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['indirectLink_S']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['MetaModelElement_S']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Family': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'indirectLink_S', self.createNewindirectLink_S), ( 'directLink_S', self.createNewdirectLink_S)]
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['CommunityRoot']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'HouseholdRoot': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Family': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Person': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ApplyModel': []
          ,'CommunityRoot': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'Man': [( 'directLink_T', self.createNewdirectLink_T)] }
    self.ConnectivityMap['backward_link']={
           'directLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'apply_contains': []
          ,'Woman': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Person': []
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': [( 'MetaModelElement_S', self.createNewMetaModelElement_S), ( 'HouseholdRoot', self.createNewHouseholdRoot), ( 'Family', self.createNewFamily), ( 'Member', self.createNewMember)]
          ,'Member': []
          ,'MetaModelElement_T': []
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': []
          ,'ApplyModel': []
          ,'CommunityRoot': []
          ,'backward_link': []
          ,'Man': [] }
    self.ConnectivityMap['Man']={
           'directLink_S': []
          ,'apply_contains': []
          ,'Woman': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'HouseholdRoot': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Family': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'Person': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'MatchModel': []
          ,'directLink_T': []
          ,'indirectLink_S': []
          ,'Member': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'MetaModelElement_T': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'match_contains': []
          ,'trace_link': []
          ,'paired_with': []
          ,'MetaModelElement_S': [( 'backward_link', self.createNewbackward_link), ( 'trace_link', self.createNewtrace_link)]
          ,'ApplyModel': []
          ,'CommunityRoot': [( 'directLink_T', self.createNewdirectLink_T)]
          ,'backward_link': []
          ,'Man': [( 'directLink_T', self.createNewdirectLink_T)] }
    
    self.CardinalityTable['MetaModelElement_S']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['HouseholdRoot']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Family']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['Member']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': [('0', 'N', 'Destination')]
          ,'apply_contains': []
          ,'backward_link': [('0', 'N', 'Destination')]
          ,'indirectLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_T': []
          ,'directLink_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Destination')] }
    self.CardinalityTable['MatchModel']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': [('0', 'N', 'Source')]
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': [('1', '1', 'Source')]
          ,'trace_link': [] }
    self.CardinalityTable['ApplyModel']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Source')]
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': [('1', '1', 'Destination')]
          ,'trace_link': [] }
    self.CardinalityTable['MetaModelElement_T']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['CommunityRoot']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['Person']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['Man']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['Woman']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': [('0', 'N', 'Destination')]
          ,'backward_link': [('0', 'N', 'Source')]
          ,'indirectLink_S': []
          ,'directLink_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [('0', 'N', 'Source')] }
    self.CardinalityTable['match_contains']={
          'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'HouseholdRoot': [('0', 'N', 'Source')]
          ,'Family': [('0', 'N', 'Source')]
          ,'Member': [('0', 'N', 'Source')]
          ,'MatchModel': [('0', 'N', 'Destination')]
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['apply_contains']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': [('0', 'N', 'Destination')]
          ,'MetaModelElement_T': [('0', 'N', 'Source')]
          ,'CommunityRoot': [('0', 'N', 'Source')]
          ,'Person': [('0', 'N', 'Source')]
          ,'Man': [('0', 'N', 'Source')]
          ,'Woman': [('0', 'N', 'Source')]
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['backward_link']={
          'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'HouseholdRoot': [('0', 'N', 'Source')]
          ,'Family': [('0', 'N', 'Source')]
          ,'Member': [('0', 'N', 'Source')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'CommunityRoot': [('0', 'N', 'Destination')]
          ,'Person': [('0', 'N', 'Destination')]
          ,'Man': [('0', 'N', 'Destination')]
          ,'Woman': [('0', 'N', 'Destination')]
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['indirectLink_S']={
          'MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'HouseholdRoot': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Family': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Member': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['directLink_T']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'CommunityRoot': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Person': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Man': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Woman': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['directLink_S']={
          'MetaModelElement_S': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'HouseholdRoot': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Family': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'Member': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['paired_with']={
          'MetaModelElement_S': []
          ,'HouseholdRoot': []
          ,'Family': []
          ,'Member': []
          ,'MatchModel': [('1', '1', 'Destination')]
          ,'ApplyModel': [('1', '1', 'Source')]
          ,'MetaModelElement_T': []
          ,'CommunityRoot': []
          ,'Person': []
          ,'Man': []
          ,'Woman': []
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    self.CardinalityTable['trace_link']={
          'MetaModelElement_S': [('0', 'N', 'Source')]
          ,'HouseholdRoot': [('0', 'N', 'Source')]
          ,'Family': [('0', 'N', 'Source')]
          ,'Member': [('0', 'N', 'Source')]
          ,'MatchModel': []
          ,'ApplyModel': []
          ,'MetaModelElement_T': [('0', 'N', 'Destination')]
          ,'CommunityRoot': [('0', 'N', 'Destination')]
          ,'Person': [('0', 'N', 'Destination')]
          ,'Man': [('0', 'N', 'Destination')]
          ,'Woman': [('0', 'N', 'Destination')]
          ,'match_contains': []
          ,'apply_contains': []
          ,'backward_link': []
          ,'indirectLink_S': []
          ,'directLink_T': []
          ,'directLink_S': []
          ,'paired_with': []
          ,'trace_link': [] }
    
    self.entitiesInMetaModel['FamiliesToPersonsMM']=["MetaModelElement_S", "HouseholdRoot", "Family", "Member", "MatchModel", "ApplyModel", "MetaModelElement_T", "CommunityRoot", "Person", "Man", "Woman", "match_contains", "apply_contains", "backward_link", "indirectLink_S", "directLink_T", "directLink_S", "paired_with", "trace_link"]

    
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
def createNewHouseholdRoot(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = HouseholdRoot(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["HouseholdRoot"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_HouseholdRoot(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_HouseholdRoot(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("HouseholdRoot", new_obj.tag)
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
def createNewFamily(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Family(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Family"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Family(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Family(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Family", new_obj.tag)
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
def createNewMember(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Member(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Member"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Member(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Member(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Member", new_obj.tag)
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
def createNewCommunityRoot(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = CommunityRoot(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["CommunityRoot"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_CommunityRoot(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_CommunityRoot(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("CommunityRoot", new_obj.tag)
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
def createNewPerson(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Person(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Person"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Person(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Person(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Person", new_obj.tag)
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
def createNewMan(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Man(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Man"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Man(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Man(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Man", new_obj.tag)
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
def createNewWoman(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Woman(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Woman"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Woman(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Woman(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Woman", new_obj.tag)
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
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_FamiliesToPersonsMM(self)
   ne = len(self.ASGroot.listNodes["ASG_FamiliesToPersonsMM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_FamiliesToPersonsMM", new_obj.tag)
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

