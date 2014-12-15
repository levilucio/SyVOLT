"""
__graph_MT_pre__Expression.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_MT_pre__Expression(graphEntity):

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


        helv12 = tkFont.Font ( family="Helvetica", size=12, weight="bold" )
        h = drawing.create_text(self.translate([-3, -3]), font=helv12,
                                tags = (self.tag, self.semanticObject.getClass()), 
                                fill = "black", 
                                text=self.semanticObject.MT_label__.toString())
        self.attr_display["MT_label__"] = h
        self.gf_label = GraphicalForm(drawing, h, 'gf_label', fontObject=helv12)
        self.graphForms.append(self.gf_label)
        
    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_MT_pre__Expression
