"""
__graph_EntryPoint.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_EntryPoint(graphEntity):

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
        h = drawing.create_text(self.translate([100.0, 33.0, 100.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'EntryPoint', width = '0', justify= 'left', stipple='' )
        self.gf45 = GraphicalForm(drawing, h, 'gf45', fontObject=font)
        self.graphForms.append(self.gf45)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([95.0, 62.0, 95.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf46 = GraphicalForm(drawing, h, 'gf46', fontObject=font)
        self.graphForms.append(self.gf46)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_EntryPoint
