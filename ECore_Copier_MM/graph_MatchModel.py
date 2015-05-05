"""
__graph_MatchModel.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_MatchModel(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 132, 83
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
        h = drawing.create_rectangle(self.translate([-65.0, -40.0, 65.0, 41.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'grey45')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_oval(self.translate([-5.0, 0.0, -5.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-5.0, 0.0, -5.0, 8.0])[:2], tags = self.tag, font=font, fill = 'white', anchor = 'center', text = 'MatchModel', width = '0', justify= 'left', stipple='' )
        self.gf4 = GraphicalForm(drawing, h, 'gf4', fontObject=font)
        self.graphForms.append(self.gf4)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_MatchModel
