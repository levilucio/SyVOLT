"""
__graph_Subtract.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Subtract(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 135, 65
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
        h = drawing.create_oval(self.translate([152.0, 52.0, 152.0, 52.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([19.0, 19.0, 152.0, 82.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'gray')
        self.gf129 = GraphicalForm(drawing, h, "gf129")
        self.graphForms.append(self.gf129)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([67.0, 36.0, 67.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Subtract', width = '0', justify= 'left', stipple='' )
        self.gf166 = GraphicalForm(drawing, h, 'gf166', fontObject=font)
        self.graphForms.append(self.gf166)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([80.0, 60.0, 80.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf167 = GraphicalForm(drawing, h, 'gf167', fontObject=font)
        self.graphForms.append(self.gf167)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Subtract
