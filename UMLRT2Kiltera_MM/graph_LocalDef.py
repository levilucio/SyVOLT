"""
__graph_LocalDef.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_LocalDef(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 173, 91
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
        h = drawing.create_oval(self.translate([209.0, 88.0, 209.0, 88.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([38.0, 38.0, 209.0, 127.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'cyan')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([115.0, 63.0, 115.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'LocalDef', width = '0', justify= 'left', stipple='' )
        self.gf84 = GraphicalForm(drawing, h, 'gf84', fontObject=font)
        self.graphForms.append(self.gf84)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([120.0, 100.0, 120.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf85 = GraphicalForm(drawing, h, 'gf85', fontObject=font)
        self.graphForms.append(self.gf85)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_LocalDef
