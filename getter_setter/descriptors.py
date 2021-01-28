"""
Descriptors are python objects that implement a method of the descriptor protocol.
Which gives you the ability to create objects that have special behaviour when they 
are accessed as attributes of objects.
__get__( self, obj, type=None ) -> object
__set__( self, obj, value ) -> None
__delete__( self, obj ) -> None
__set_name__( self, owner, name )
"""


class verbose_attribue:
    def __get__( self, obj, type=None )-> object:
        print("accessing the attribute to get the value ")
        return 42

    def __set__(self, obj, value ) -> None:
        print( "accessing the attribute to set the value" )
        raise AttributeError("Cannot change tthe value")

class Foo:
    attribute1  = verbose_attribue()


my_foo_object   =   Foo()
x   =   my_foo_object.attribute1
print(x)