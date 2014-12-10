"""
__graph_Action.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Action(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 172, 82
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
        h = drawing.create_oval(self.translate([189.0, 62.0, 189.0, 62.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([20.0, 20.0, 190.0, 100.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'moccasin')
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([30.0, 31.0, 30.0, 12.0])[:2], tags = self.tag, font=font, fill = 'grey45', anchor = 'center', text = '', width = '0', justify= 'left', stipple='' )
        self.gf7 = GraphicalForm(drawing, h, 'gf7', fontObject=font)
        self.graphForms.append(self.gf7)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([100.0, 40.0, 100.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Action', width = '0', justify= 'left', stipple='' )
        self.gf8 = GraphicalForm(drawing, h, 'gf8', fontObject=font)
        self.graphForms.append(self.gf8)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([82.0, 69.0, 82.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf161 = GraphicalForm(drawing, h, 'gf161', fontObject=font)
        self.graphForms.append(self.gf161)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Action
