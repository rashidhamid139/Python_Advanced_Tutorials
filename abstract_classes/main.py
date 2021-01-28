"""
Descriptors are classes which, when accessed through either getting, setting, or deleting, can also alter other objects. Descriptor's aren't meant 
to stand alone; rather they're meant to be held by an owner class.

To be a descriptor a class must have atleast one of __get__, __Set__, __delete__ implemented.


__get__(self, instance, owner):


"""

class Meter(object):

    """Descriptor for a meter"""
    def __init__(self, value=0.0):
        self.value  = float(value)

    def __get__(self, instance, owner ):
        return self.value

    def __set__(self, instance, value ):
        self.value = value

    
class Foot:
    """Descripptor for a Foot."""
    def __get__(self, instance, owner ):
        return instance.meter * 3.2808

    def __set__(self, instance, value ):
        instance.meter  = float(value)/3.2808



class Distance:
    meter   = Meter()
    foot    = Foot()
    