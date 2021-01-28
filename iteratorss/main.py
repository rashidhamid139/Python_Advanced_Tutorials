"""
Iterable objects: Type of object which can be used with for loop.


"""

x = ",".join(['a', 'b', 'c'])
print(x)
"""
iter takes an iterable object as input, and returns an iterator.
"""
class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            return StopIteration()



y = yrange(5)
z = list(y)
print(z)
