"""
__graph_MT_pre__apply_contains.py___________________________________________________________

Automatically generated LINK for entity MT_pre__apply_contains
DO NOT MODIFY DIRECTLY
____________________________________________________________________________________
"""
from graphLink import *
from stickylink import *
from widthXfillXdecoration import *
class graph_MT_pre__apply_contains(graphLink):

   def __init__(self, xc, yc, semObject = None ):
      self.semObject = semObject
      self.semanticObject = semObject
      from linkEditor import *
      self.le=linkEditor(self,self.semObject, "MT_pre__apply_contains")
      self.le.FirstLink= stickylink()
      self.le.FirstLink.arrow=ATOM3Boolean()
      self.le.FirstLink.arrow.setValue((' ', 0))
      self.le.FirstLink.arrow.config = 0
      self.le.FirstLink.arrowShape1=ATOM3Integer(8)
      self.le.FirstLink.arrowShape2=ATOM3Integer(10)
      self.le.FirstLink.arrowShape3=ATOM3Integer(3)
      self.le.FirstLink.decoration=ATOM3Appearance()
      self.le.FirstLink.decoration.setValue( ('MT_pre__apply_contains_1stLink', self.le.FirstLink))
      self.le.FirstSegment= widthXfillXdecoration()
      self.le.FirstSegment.width=ATOM3Integer(2)
      self.le.FirstSegment.fill=ATOM3String('black', 20)
      self.le.FirstSegment.stipple=ATOM3String('', 20)
      self.le.FirstSegment.arrow=ATOM3Boolean()
      self.le.FirstSegment.arrow.setValue((' ', 0))
      self.le.FirstSegment.arrow.config = 0
      self.le.FirstSegment.arrowShape1=ATOM3Integer(8)
      self.le.FirstSegment.arrowShape2=ATOM3Integer(10)
      self.le.FirstSegment.arrowShape3=ATOM3Integer(3)
      self.le.FirstSegment.decoration=ATOM3Appearance()
      self.le.FirstSegment.decoration.setValue( ('MT_pre__apply_contains_1stSegment', self.le.FirstSegment))
      self.le.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.le.Center=ATOM3Appearance()
      self.le.Center.setValue( ('MT_pre__apply_contains_Center', self.le))
      self.le.SecondSegment= widthXfillXdecoration()
      self.le.SecondSegment.width=ATOM3Integer(2)
      self.le.SecondSegment.fill=ATOM3String('black', 20)
      self.le.SecondSegment.stipple=ATOM3String('', 20)
      self.le.SecondSegment.arrow=ATOM3Boolean()
      self.le.SecondSegment.arrow.setValue((' ', 0))
      self.le.SecondSegment.arrow.config = 0
      self.le.SecondSegment.arrowShape1=ATOM3Integer(8)
      self.le.SecondSegment.arrowShape2=ATOM3Integer(10)
      self.le.SecondSegment.arrowShape3=ATOM3Integer(3)
      self.le.SecondSegment.decoration=ATOM3Appearance()
      self.le.SecondSegment.decoration.setValue( ('MT_pre__apply_contains_2ndSegment', self.le.SecondSegment))
      self.le.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.le.SecondLink= stickylink()
      self.le.SecondLink.arrow=ATOM3Boolean()
      self.le.SecondLink.arrow.setValue((' ', 1))
      self.le.SecondLink.arrow.config = 0
      self.le.SecondLink.arrowShape1=ATOM3Integer(8)
      self.le.SecondLink.arrowShape2=ATOM3Integer(10)
      self.le.SecondLink.arrowShape3=ATOM3Integer(3)
      self.le.SecondLink.decoration=ATOM3Appearance()
      self.le.SecondLink.decoration.setValue( ('MT_pre__apply_contains_2ndLink', self.le.SecondLink))
      self.le.FirstLink.decoration.semObject=self.semObject
      self.le.FirstSegment.decoration.semObject=self.semObject
      self.le.Center.semObject=self.semObject
      self.le.SecondSegment.decoration.semObject=self.semObject
        helv12 = tkFont.Font ( family="Helvetica", size=12, weight="bold" )
        h = drawing.create_text(self.translate([-3, -3]), font=helv12,
                                tags = (self.tag, self.semanticObject.getClass()), 
                                fill = "black", 
                                text=self.semanticObject.MT_label__.toString())
        self.attr_display["MT_label__"] = h
        self.gf_label = GraphicalForm(drawing, h, 'gf_label', fontObject=helv12)
        self.graphForms.append(self.gf_label)
              self.le.SecondLink.decoration.semObject=self.semObject
      graphLink.__init__(self, xc, yc, self.le,semObject)
