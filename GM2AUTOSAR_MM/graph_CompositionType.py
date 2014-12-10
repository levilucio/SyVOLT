"""
__graph_CompositionType.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_CompositionType(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 145, 80
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
        h = drawing.create_oval(self.translate([160.0, 60.0, 160.0, 60.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([21.0, 19.0, 164.0, 97.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'skyblue1')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([96.0, 38.0, 96.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'CompositionType', width = '0', justify= 'left', stipple='' )
        self.gf55 = GraphicalForm(drawing, h, 'gf55', fontObject=font)
        self.graphForms.append(self.gf55)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([70.0, 75.0, 70.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf56 = GraphicalForm(drawing, h, 'gf56', fontObject=font)
        self.graphForms.append(self.gf56)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_CompositionType
