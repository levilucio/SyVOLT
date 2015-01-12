"""
__graph_MatchModel.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_MatchModel(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 119, 61
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([138.0, 52.0, 138.0, 52.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([21.0, 22.0, 138.0, 81.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'gray')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([69.0, 52.0, 69.0, 12.0])[:2], tags = self.tag, font=font, fill = 'gray', anchor = 'center', text = '', width = '0', justify= 'left', stipple='' )
        self.gf3 = GraphicalForm(drawing, h, 'gf3', fontObject=font)
        self.graphForms.append(self.gf3)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([82.0, 52.0, 82.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'MatchModel', width = '0', justify= 'left', stipple='' )
        self.gf4 = GraphicalForm(drawing, h, 'gf4', fontObject=font)
        self.graphForms.append(self.gf4)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_MatchModel
