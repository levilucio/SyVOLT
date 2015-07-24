
from .rule_primitive import RulePrimitive
from .messages import TransformationException
from core.himesis import Himesis
from core.himesis_utils import update_equations

import traceback

import re
def sort_nicely( l ):
    """ Sort the given list in the way that humans expect.
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )
    return l

class Rewriter(RulePrimitive):
    '''
        Transforms the matched source model elements according to the specified post-condition pattern.
    '''
    def __init__(self, condition):
        '''
            Transforms the bound graph of the source graph into what the specification of the post-condition pattern.
            @param condition: The the post-condition pattern.
        '''
        super(Rewriter, self).__init__()
        self.condition = condition
    
    def __str__(self):
        s = super(Rewriter, self).__str__()
        s = s.split(' ')
        s.insert(1, '[%s]' % self.condition.name)
        return reduce(lambda x, y: x + ' ' + y, s)



    def packet_in(self, packet, verbosity = 0):
        self.exception = None
        self.is_success = False
        if self.condition.pre[Himesis.Constants.GUID] not in packet.match_sets:
            self.is_success = False
            # TODO: This should be a TransformationLanguageSpecificException 
            self.exception = TransformationException()
            self.exception.packet = packet
            return packet
        else:
            match = packet.match_sets[self.condition.pre[Himesis.Constants.GUID]].match2rewrite
            try:
                mapping = match.to_label_mapping(packet.graph)
                # Apply the transformation on the match

                if verbosity > 0:
                    print("Rewriter mapping: " + str(mapping))

                graph_eqs = packet.graph["equations"]
                cond_eqs = self.condition["equations"]



                if cond_eqs and graph_eqs != cond_eqs:



                    #get dict from label to node num
                    RHS_labels = {}
                    for n in range(self.condition.vcount()):
                        node = self.condition.vs[n]
                        RHS_labels[node["MT_label__"]] = n

                    new_mapping = {}
                    j=0
                    vcount = packet.graph.vcount()

                    #make sure to iterate in natural order
                    for label in sort_nicely(list(RHS_labels.keys())):

                        #use mapping if possible
                        if label in mapping:
                            new_mapping[int(label)] = mapping[label]

                        #assume nodes will be added in this order
                        #TODO: Handle deleted nodes
                        else:
                            new_mapping[int(label)] = vcount + j
                            j += 1


                    new_cond_eqs = update_equations(cond_eqs, new_mapping)
                    packet.graph["equations"] += new_cond_eqs
                self.condition.execute(packet, mapping)     # Sets dirty nodes as well
            except Exception as e:

                tb = traceback.format_exc()
                print("Rewriter Error: " + str(e))
                print(tb)
                print("packet.graph: " + packet.graph.name)
                print("self.condition: " + self.condition.name)
                raise
                self.is_success = False
                self.exception = TransformationException(e)
                self.exception.packet = packet
                self.exception.transformation_unit = self
                return packet
            
            # Remove the match
            packet.match_sets[self.condition.pre[Himesis.Constants.GUID]].match2rewrite = None
            if  len(packet.match_sets[self.condition.pre[Himesis.Constants.GUID]].matches) == 0:
                del packet.match_sets[self.condition.pre[Himesis.Constants.GUID]]
            
            #print self.condition
            
            self.is_success = True
            return packet


class Rewriter_Equation(Rewriter):

    def __init__(self, condition):
        super(Rewriter_Equation, self).__init__(condition)


    def packet_in(self, packet, verbosity = 0):

        packet = super(Rewriter_Equation, self).packet_in(packet, verbosity)

        if self.is_success:
            solver.combine_equations(packet.graph, self.condition)

        return packet
