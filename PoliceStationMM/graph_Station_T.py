"""
__graph_Station_T.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Station_T(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 120, 79
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
        h = drawing.create_rectangle(self.translate([-59.0, -38.0, 59.0, 39.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'skyblue3')
        self.gf13 = GraphicalForm(drawing, h, "gf13")
        self.graphForms.append(self.gf13)

        h = drawing.create_oval(self.translate([1.0, 2.0, 1.0, 2.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-19.0, -18.0, -19.0, -249.0])[:2], tags = self.tag, font=font, fill = 'grey45', anchor = 'center', text = 'Station', width = '0', justify= 'left', stipple='' )
        self.gf15 = GraphicalForm(drawing, h, 'gf15', fontObject=font)
        self.graphForms.append(self.gf15)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([21.0, 22.0, 21.0, -252.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf16 = GraphicalForm(drawing, h, 'gf16', fontObject=font)
        self.graphForms.append(self.gf16)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Station_T
