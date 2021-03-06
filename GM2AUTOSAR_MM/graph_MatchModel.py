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
        self.sizeX, self.sizeY = 133.0, 83
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
        h = drawing.create_oval(self.translate([151.0, 60.0, 151.0, 60.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([19.0, 18.0, 150.0, 99.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'gray')
        self.gf68 = GraphicalForm(drawing, h, "gf68")
        self.graphForms.append(self.gf68)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([73.0, 50.0, 73.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'MatchModel', width = '0', justify= 'left', stipple='' )
        self.gf1 = GraphicalForm(drawing, h, 'gf1', fontObject=font)
        self.graphForms.append(self.gf1)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_MatchModel
