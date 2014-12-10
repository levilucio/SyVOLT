"""
__graph_Signal.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Signal(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 143, 82
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
        h = drawing.create_oval(self.translate([162.0, 61.0, 162.0, 61.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([21.0, 18.0, 162.0, 98.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'moccasin')
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([77.0, 35.0, 77.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Signal', width = '0', justify= 'left', stipple='' )
        self.gf24 = GraphicalForm(drawing, h, 'gf24', fontObject=font)
        self.graphForms.append(self.gf24)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([80.0, 80.0, 80.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf25 = GraphicalForm(drawing, h, 'gf25', fontObject=font)
        self.graphForms.append(self.gf25)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Signal
