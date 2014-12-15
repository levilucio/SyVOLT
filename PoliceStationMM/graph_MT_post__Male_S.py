"""
__graph_MT_post__Male_S.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_MT_post__Male_S(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 120, 78
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
        h = drawing.create_rectangle(self.translate([-59.0, -38.0, 59.0, 38.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'orange')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_oval(self.translate([1.0, 2.0, 1.0, 2.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-30.0, -18.0, -30.0, -300.0])[:2], tags = self.tag, font=font, fill = 'grey45', anchor = 'center', text = 'Male', width = '0', justify= 'left', stipple='' )
        self.gf8 = GraphicalForm(drawing, h, 'gf8', fontObject=font)
        self.graphForms.append(self.gf8)



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

new_class = graph_MT_post__Male_S
