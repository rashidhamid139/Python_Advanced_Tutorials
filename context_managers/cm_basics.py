"""
The primary motivation behind context managers is resource management.
The basic methods a low level context manager implements is __enter__ and __exit__

__enter__ is the method that gets called when we open the resource.


"""

#Implement Custom File class which will imitate open method
class FileManager:
    def __init__(self, filename ):
        self.filename   = filename

    def __enter__(self):
        self.opened_file    = open(self.filename)
        return self.opened_file

    def __exit__(self, *exc):
        self.opened_file.close()
        

with FileManager( "readme.txt") as file:
    text    = file.read()

print( text )