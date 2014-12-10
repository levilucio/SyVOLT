"""
__graph_Module.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Module(graphEntity):

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
        h = drawing.create_text(self.translate([104.0, 61.0, 104.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Module', width = '0', justify= 'left', stipple='' )
        self.gf14 = GraphicalForm(drawing, h, 'gf14', fontObject=font)
        self.graphForms.append(self.gf14)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([100.0, 100.0, 100.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf15 = GraphicalForm(drawing, h, 'gf15', fontObject=font)
        self.graphForms.append(self.gf15)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Module
