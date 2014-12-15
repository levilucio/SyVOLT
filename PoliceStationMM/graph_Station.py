"""
__graph_Station.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Station(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 111, 76
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
        h = drawing.create_oval(self.translate([6.0, 3.0, 6.0, 3.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([-54.0, -37.0, 55.0, 37.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'orange')
        self.gf11 = GraphicalForm(drawing, h, "gf11")
        self.graphForms.append(self.gf11)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([6.0, 3.0, 6.0, 12.0])[:2], tags = self.tag, font=font, fill = 'grey45', anchor = 'center', text = 'Station', width = '0', justify= 'left', stipple='' )
        self.gf13 = GraphicalForm(drawing, h, 'gf13', fontObject=font)
        self.graphForms.append(self.gf13)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([20.0, 20.0, 20.0, -95.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf14 = GraphicalForm(drawing, h, 'gf14', fontObject=font)
        self.graphForms.append(self.gf14)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Station
