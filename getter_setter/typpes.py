import types

class Function:
    def __get__(self, obj, objtype=None ):
        if obj is None:
            return self
        return types.MethodType(self, obj )