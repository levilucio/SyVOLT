"""
__graph_ApplyModel.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ApplyModel(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 135, 84
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
        h = drawing.create_rectangle(self.translate([-66.0, -41.0, 67.0, 41.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'grey45')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)

        h = drawing.create_oval(self.translate([-1.0, -1.0, -1.0, -1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-6.0, -1.0, -6.0, -227.0])[:2], tags = self.tag, font=font, fill = 'white', anchor = 'center', text = 'ApplyModel', width = '0', justify= 'left', stipple='' )
        self.gf9 = GraphicalForm(drawing, h, 'gf9', fontObject=font)
        self.graphForms.append(self.gf9)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_ApplyModel
