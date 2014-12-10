"""
__graph_String.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_String(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 123.0, 63
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
        h = drawing.create_oval(self.translate([142.0, 48.0, 142.0, 48.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([20.0, 18.0, 141.0, 79.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'gray')
        self.gf139 = GraphicalForm(drawing, h, "gf139")
        self.graphForms.append(self.gf139)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([62.0, 32.0, 62.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'String', width = '0', justify= 'left', stipple='' )
        self.gf145 = GraphicalForm(drawing, h, 'gf145', fontObject=font)
        self.graphForms.append(self.gf145)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([72.0, 52.0, 72.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf148 = GraphicalForm(drawing, h, 'gf148', fontObject=font)
        self.graphForms.append(self.gf148)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_String
