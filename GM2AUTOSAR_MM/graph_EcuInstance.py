"""
__graph_EcuInstance.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_EcuInstance(graphEntity):

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
        h = drawing.create_text(self.translate([97.0, 30.0, 97.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'EcuInstance', width = '0', justify= 'left', stipple='' )
        self.gf42 = GraphicalForm(drawing, h, 'gf42', fontObject=font)
        self.graphForms.append(self.gf42)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([60.0, 60.0, 60.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf43 = GraphicalForm(drawing, h, 'gf43', fontObject=font)
        self.graphForms.append(self.gf43)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_EcuInstance
